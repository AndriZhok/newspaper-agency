from django.urls import path, include

from catalog.views import (
    index,
    NewspaperListView,
    logout,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("logout/", logout, name="logout"),
    path("newspaper-list/", NewspaperListView.as_view(), name="newspaper-list"),
    path(
        "newspaper-list-detail/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-list-detail",
    ),
    path(
        "newspaper-list-create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "newspaper-list-update/<int:pk>/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspaper-list-delete/<int:pk>/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
]

app_name = "catalog"
