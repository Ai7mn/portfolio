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
import google.generativeai as genai
import os
import requests


class ChatbotView(APIView):
    def post(self, request):
        user_message = request.data.get("message")
        if not user_message:
            return Response(
                {"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")

        prompt = (
            "You are AI Aiman, an AI assistant for Aiman Daba's portfolio website. "
            "Answer questions about my skills, projects, and professional background. "
            f"Question: {user_message}"
        )

        try:
            response = model.generate_content(prompt)
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
                "https://api.github.com/graphql", json={"query": query}, headers=headers
            )
            response.raise_for_status()
            data = response.json()

            contributions = data["data"]["viewer"]["contributionsCollection"][
                "contributionCalendar"
            ]["totalContributions"]
            repos = data["data"]["viewer"]["repositories"]["nodes"]

            language_stats = {}
            for repo in repos:
                for edge in repo.get("languages", {}).get("edges", []):
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
