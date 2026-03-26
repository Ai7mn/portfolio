from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core.forms import ContactUsForm
from core.models import CV
from portfolio_app.models import Project


def home(request):
    mycv = CV.objects.filter(active=True).first()
    cv_link = mycv.file.url if mycv else ""
    projects = Project.objects.filter(visible=True).order_by("display_order")
    context = {"cv_link": cv_link, "projects": projects}
    template = "home.html"
    return render(request, template, context)


def contact_us(request):
    contact_form = ContactUsForm(request.POST or None)
    context = {}
    if request.method == "POST":
        previous_page = request.META.get("HTTP_REFERER")
        if contact_form.is_valid():
            new_form = contact_form.save(commit=False)
            new_form.save()
            try:
                return HttpResponseRedirect(previous_page or reverse("home"))
            except Exception:
                return HttpResponseRedirect(reverse("home"))
        else:
            return HttpResponseRedirect(reverse("home"))
    return render(request, "contact.html", context)
