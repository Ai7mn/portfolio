from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from portfolio_app.models import Project, ProjectImage
from core.models import CV, ContactUs
from .serializers import (
    ProjectSerializer,
    ProjectImageSerializer,
    CVSerializer,
    ContactUsSerializer,
)
from google import genai
import os
import requests
import PyPDF2
from io import BytesIO


class ChatbotView(APIView):
    def _get_context(self):
        # 1. Gather Projects Context
        projects = Project.objects.filter(visible=True).order_by("display_order")
        projects_text = "PORTFOLIO PROJECTS:\n"
        for p in projects:
            projects_text += f"- {p.name} ({p.category}): {p.content}\n"

        # 2. Gather CV Context
        cv_text = "\nPROFESSIONAL CV CONTENT:\n"
        active_cv = CV.objects.filter(active=True).first()
        if active_cv and active_cv.file:
            try:
                file_ext = os.path.splitext(active_cv.file.name)[1].lower()
                if file_ext == ".pdf":
                    try:
                        active_cv.file.open()
                        reader = PyPDF2.PdfReader(active_cv.file)
                        for page in reader.pages:
                            cv_text += page.extract_text() + "\n"
                    finally:
                        active_cv.file.close()
                else:
                    try:
                        active_cv.file.open()
                        cv_text += active_cv.file.read().decode("utf-8")
                    finally:
                        active_cv.file.close()
            except Exception as e:
                cv_text += f"(Error reading CV file: {str(e)})"
        else:
            cv_text += "(No active CV found)"

        return f"{projects_text}\n{cv_text}"

    def post(self, request):
        user_message = request.data.get("message")
        if not user_message:
            return Response(
                {"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

            context = self._get_context()
            
            prompt = (
                "You are AI Aiman, an elite AI assistant for Aiman Daba's professional portfolio. "
                "Your goal is to answer questions about Aiman's skills, experience, and projects using the context provided below. "
                "Be professional, encouraging, and accurate based ONLY on the provided context. "
                "If the context doesn't contain the answer, say you're not sure but offer to let the user contact Aiman directly.\n\n"
                f"CONTEXT:\n{context}\n\n"
                f"USER QUESTION: {user_message}"
            )

            # Note: Public Gemini models are gemini-2.5-flash or gemini-2.5-pro
            # Using flash for faster responses if not specified
            model_name = os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")

            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
            )
            return Response({"response": response.text})
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class GitHubMetricsView(APIView):
    def get(self, request):
        github_token = os.environ.get("GITHUB_TOKEN")
        if not github_token:
            return Response(
                {"error": "GitHub token not configured"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # FIX 1: Added a space after 'Bearer'
        # FIX 2: GitHub GraphQL endpoint is /graphql, not the base URL
        url = "https://api.github.com/graphql"
        headers = {
            "Authorization": f"Bearer {github_token}",
            "Content-Type": "application/json",
        }

        query = """
        {
          viewer {
            login
            contributionsCollection {
              contributionCalendar {
                totalContributions
              }
            }
            repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
              nodes {
                languages(first: 10) {
                  edges {
                    size
                    node {
                      name
                    }
                  }
                }
              }
            }
          }
        }
        """

        try:
            response = requests.post(
                url, json={"query": query}, headers=headers
            )
            response.raise_for_status()
            data = response.json()

            # FIX 3: GraphQL can return 200 OK even if there are query errors
            if "errors" in data:
                return Response(data["errors"], status=status.HTTP_400_BAD_REQUEST)

            viewer_data = data["data"]["viewer"]
            contributions = viewer_data["contributionsCollection"]["contributionCalendar"]["totalContributions"]
            repos = viewer_data["repositories"]["nodes"]

            language_stats = {}
            for repo in repos:
                # Use .get() to avoid KeyErrors if languages are empty
                langs = repo.get("languages", {})
                for edge in langs.get("edges", []):
                    lang = edge["node"]["name"]
                    size = edge["size"]
                    language_stats[lang] = language_stats.get(lang, 0) + size

            return Response(
                {"total_contributions": contributions, "language_stats": language_stats}
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
