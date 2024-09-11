from django.urls import path, include

from catalog.views import index, NewspaperListView, logout

urlpatterns = [
    path('', index, name='index'),
    path('newspaper-list/', NewspaperListView.as_view(), name='newspaper-list'),
    path("logout/", logout, name="logout")
]

app_name = "catalog"
