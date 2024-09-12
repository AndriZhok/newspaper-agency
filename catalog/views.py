from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import NewspaperSearchForm, NewspaperForm, RedactorForm, RedactorSearchForm
from catalog.models import Newspaper, Redactor, Topic


@login_required
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


def logout(request):
    return render(request, "registration/logged_out.html")


class NewspaperListView(LoginRequiredMixin, ListView):
    model = Newspaper
    template_name = "catalog/newspaper_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        title = self.request.GET.get("title", None)
        newspapers = Newspaper.objects.all()
        if title:
            return newspapers.filter(title__icontains=title)

        return newspapers


class NewspaperDetailView(LoginRequiredMixin, DetailView):
    model = Newspaper
    template_name = "catalog/newspaper_detail.html"


class NewspaperCreateView(LoginRequiredMixin, CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperUpdateView(LoginRequiredMixin, UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperDeleteView(LoginRequiredMixin, DeleteView):
    model = Newspaper
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form_confirm_delete.html"


class RedactorListView(LoginRequiredMixin, ListView):
    model = Redactor
    template_name = "catalog/redactor_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("title", "")
        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        username = self.request.GET.get("username", None)
        redactors = Redactor.objects.all()
        if username:
            return redactors.filter(username__icontains=username)

        return redactors


class RedactorDetailView(LoginRequiredMixin, DetailView):
    model = Redactor
    template_name = "catalog/redactor_detail.html"


class RedactorCreateView(LoginRequiredMixin, CreateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_form.html"


class RedactorUpdateView(LoginRequiredMixin, UpdateView):
    model = Redactor
    form_class = RedactorForm
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_form.html"


class RedactorDeleteView(LoginRequiredMixin, DeleteView):
    model = Redactor
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_confirm_delete.html"
