from django.shortcuts import render
from portfolio_app.models import Project, ProjectImage

def single_project(request, slug):
    project = Project.objects.get(slug=slug)
    project_pages = ProjectImage.objects.filter(project=project)
    context = {'project': project, 'project_pages': project_pages, }
    template = 'single_project.html'
    return render(request, template, context)
