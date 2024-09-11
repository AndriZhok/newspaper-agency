from django.urls import path, include

from catalog.views import index, NewspaperListView

urlpatterns = [
    path('', index, name='index'),

    path('newspaper-list/', NewspaperListView.as_view(), name='newspaper-list'),
]

app_name = "catalog"
