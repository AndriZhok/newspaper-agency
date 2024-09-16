from django.contrib import admin
from .models import Topic, Redactor, Newspaper


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "years_of_experience")
    search_fields = ("username", "email")
    list_filter = ("years_of_experience",)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "topic")
    search_fields = ("title", "content")
    list_filter = ("published_date", "topic")
    filter_horizontal = ("publishers",)
