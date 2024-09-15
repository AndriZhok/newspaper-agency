from django.test import TestCase
from django.core.exceptions import ValidationError
from catalog.models import Redactor, Topic
from catalog.forms import (
    NewspaperForm,
    TopicForm,
    validate_years_of_experience
)


class FormsTestCase(TestCase):
    @staticmethod
    def __newspaper_form_data(title: str, content: str, topic: Topic, publishers: list) -> dict:
        return {
            "title": title,
            "content": content,
            "topic": topic.id if topic else None,
            "publishers": publishers,
        }

    @staticmethod
    def __redactor_form_data(username: str, first_name: str, last_name: str, email: str, years_of_experience: int,
                             password: str) -> dict:
        return {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "years_of_experience": years_of_experience,
            "password": password,
        }

    @staticmethod
    def __topic_form_data(name: str) -> dict:
        return {
            "name": name,
        }

    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")
        self.redactor = Redactor.objects.create(username="test_redactor", first_name="Test", last_name="Redactor",
                                                email="test@example.com")

    def test_valid_newspaper_form(self):
        form = NewspaperForm(data=self.__newspaper_form_data(
            title="Test Newspaper",
            content="Test Content",
            topic=self.topic,
            publishers=[self.redactor.id]
        ))
        self.assertTrue(form.is_valid())

    def test_missing_newspaper_title(self):
        form = NewspaperForm(data=self.__newspaper_form_data(
            title="",
            content="Test Content",
            topic=self.topic,
            publishers=[self.redactor.id]
        ))
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["title"], ["This field is required."])

    def test_missing_newspaper_content(self):
        form = NewspaperForm(data=self.__newspaper_form_data(
            title="Test Newspaper",
            content="",
            topic=self.topic,
            publishers=[self.redactor.id]
        ))
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["content"], ["This field is required."])

    def test_invalid_years_of_experience(self):
        invalid_years = [-1, 101]
        for years in invalid_years:
            with self.assertRaises(ValidationError):
                validate_years_of_experience(years)

    def test_valid_topic_form(self):
        form = TopicForm(data=self.__topic_form_data(name="Test Topic"))
        self.assertTrue(form.is_valid())

    def test_missing_topic_name(self):
        form = TopicForm(data=self.__topic_form_data(name=""))
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["name"], ["This field is required."])
