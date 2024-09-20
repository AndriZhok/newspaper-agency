from django.urls import path, include

from catalog.views import (
    index,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("newspaper-list/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspaper-detail/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail",
    ),
    path(
        "newspaper-create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "newspaper-update/<int:pk>/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspaper-delete/<int:pk>/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("redactor-list/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactor-detail/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail",
    ),
    path(
        "redactor-create/",
        RedactorCreateView.as_view(),
        name="redactor-create",
    ),
    path(
        "redactor-update/<int:pk>/",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactor-delete/<int:pk>/",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path("topic-list/", TopicListView.as_view(), name="topic-list"),
    path(
        "topic-create/",
        TopicCreateView.as_view(),
        name="topic-create",
    ),
    path(
        "topic-update/<int:pk>/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topic-delete/<int:pk>/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
]

app_name = "catalog"
