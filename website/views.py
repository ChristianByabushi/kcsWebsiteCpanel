from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import generic
from django.core.paginator import Paginator
from .forms import MessagesForm
from .models import (
    News,
    Services,
    Partners,
    ProjectOnWebsite,
    teamMembers,
    AboutUs,
    Messages,
    backgrounddescription,
    Socialmediaslinks,
)

def home(request):
    projects = Paginator(ProjectOnWebsite.objects.all(), 2)
    page_number_project = request.GET.get("page")
    projects = projects.get_page(page_number_project) 

    news = News.objects.all()
    services = Services.objects.all()
    partners = Partners.objects.all()
    teamMembersInfo = teamMembers.objects.all()
    about = AboutUs.objects.all().first()
    backgrounddescriptionobject = backgrounddescription.objects.all()[1:]
    socialmediaslinks = Socialmediaslinks.objects.all().first()
    context = {
        "projects": projects,
        "News": news,
        "services": services,
        "partners": partners,
        "teamMembersInfo": teamMembersInfo,
        "about": about,
        "socialmediaslinks": socialmediaslinks, 
        "backgrounddescriptionfirst":backgrounddescription.objects.first(),
        "backgrounddescription": backgrounddescriptionobject,
        "homepage": True,
    }
    return render(request, "base.html", context)

def indexNews(request):
    projects = ProjectOnWebsite.objects.all()
    news = News.objects.all()
    context = {"News": news, "projects": projects}
    return render(request, "news.html", context)

def detailsNews(request, pk):
    context = {
        "projects": ProjectOnWebsite.objects.all(),
        "news": News.objects.get(id=pk),
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
    }
    return render(request, "newsitem.html", context)

def indexAboutus(request):
    partners = Partners.objects.all()
    teamMembersInfo = teamMembers.objects.all()
    about = AboutUs.objects.all().first()
    projects = ProjectOnWebsite.objects.all()

    context = {
        "projects": projects,
        "partners": partners,
        "teamMembersInfo": teamMembersInfo,
        "about": about,
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
    }
    return render(request, "about-us.html", context)

def projectsindex(request):
    partners = Partners.objects.all()
    teamMembersInfo = teamMembers.objects.all()

    projects = Paginator(ProjectOnWebsite.objects.all(), 2)
    page_number_project = request.GET.get("page")
    projects = projects.get_page(page_number_project) 

    context = {
        "partners": partners,
        "teamMembersInfo": teamMembersInfo,
        "projects": projects,
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
    }
    return render(request, "projects.html", context)

def servicesindex(request):
    context = {
        "teamMembersInfo": teamMembers.objects.all(),
        "partners": Partners.objects.all(),
        "services": Services.objects.all(),
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
    }
    return render(request, "services.html", context)

def detailsProject(request, pk):
    context = {
        "projectitem": ProjectOnWebsite.objects.get(id=pk),
        "projects": ProjectOnWebsite.objects.all(),
        "partners": Partners.objects.all(),
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
    }
    return render(request, "projectitem.html", context)


def contactus(request):
    teamMembersInfo = teamMembers.objects.all()
    projects = ProjectOnWebsite.objects.all()
    form = MessagesForm()
    context = {
        "projects": projects,
        "teamMembersInfo": teamMembersInfo,
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
        "form": form,
    }
    if request.method == "POST":
        form = MessagesForm(request.POST)
        if form.is_valid():
            msgForm = form.cleaned_data
            dataToStore = Messages(
                name=msgForm["name"],
                subject=msgForm["subject"],
                content=msgForm["content"],
                email=msgForm["email"],
            )
            dataToStore.save()
            return JsonResponse({"message": "success"})
    return render(request, "contact.html", context)

def postmessage(request):
    form = MessagesForm()
    teamMembersInfo = teamMembers.objects.all()
    projects = ProjectOnWebsite.objects.all()
    context = {
        "projects": projects,
        "socialmediaslinks": Socialmediaslinks.objects.all().first(),
        "teamMembersInfo": teamMembersInfo,
    }
    if request.method == "POST":
        form = MessagesForm(request.POST)
        if form.is_valid():
            msgForm = form.cleaned_data
            dataToStore = Messages(
                name=msgForm["name"],
                subject=msgForm["subject"],
                content=msgForm["content"],
                email=msgForm["email"],
            )
            dataToStore.save()
            return JsonResponse({"message": "success"})
    return render(request, "contact.html", context)


class ModelCreateView(generic.CreateView):
    model = Messages
    template_name = ".html"


class AboutView(generic.ListView):
    template_name = "about.html"
    context_object_name = "About"

    def get_queryset(self):
        return AboutUs.objects.all()


class teamMembersView(generic.ListView):
    context_object_name = "About"

    def get_queryset(self):
        return teamMembers.objects.all()
