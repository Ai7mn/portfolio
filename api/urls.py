from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectImageViewSet, CVViewSet, ContactUsViewSet, ChatbotView, GitHubMetricsView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'project-images', ProjectImageViewSet)
router.register(r'cvs', CVViewSet)
router.register(r'contact-us', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    path('github-stats/', GitHubMetricsView.as_view(), name='github_stats'),
]
