from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Newspaper, Redactor, Topic


def index(request: HttpRequest) -> HttpResponse:
    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
    }
    return render(request, "catalog/index.html", context=context)


class NewspaperListView(ListView):
    model = Newspaper
    template_name = "catalog/newspaper_list.html"


def logout(request):
    return render(request, "registration/logged_out.html")
