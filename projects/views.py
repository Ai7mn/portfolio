from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from projects.forms import ContactUsForm
from projects.models import CV, Project, ProjectImage


def home(request):
    mycv = CV.objects.filter(active=True).first()
    cv_link = mycv.file.url
    projects = Project.objects.filter(visible=True).order_by("display_order")
    context = {"cv_link": cv_link, "projects": projects}
    template = "home.html"
    return render(request, template, context)


def single_project(request, slug):
    project = Project.objects.get(slug=slug)
    project_pages = ProjectImage.objects.filter(project=project)
    context = {'project': project, 'project_pages': project_pages, }
    template = 'single_project.html'
    return render(request, template, context)


def contact_us(request):
    contact_form = ContactUsForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        previous_page = request.META.get('HTTP_REFERER')
        if contact_form.is_valid():
            new_form = contact_form.save(commit=False)
            new_form.save()
            try:
                return HttpResponseRedirect(reverse(previous_page))
            except:
                return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('home'))
    return render(request, "contact.html", context)
