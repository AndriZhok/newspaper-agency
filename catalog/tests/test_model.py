from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.models import Topic, Redactor, Newspaper


class TestTopicModel(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="test_topic")

    def test_topic_str(self):
        self.assertEqual(str(self.topic), self.topic.name)


class TestRedactorModel(TestCase):
    def setUp(self):
        self.redactor = Redactor.objects.create(
            username="test_redactor",
            email="redactor@example.com",
            first_name="Test",
            last_name="Redactor",
            password="test_password",
            years_of_experience=5
        )

    def test_redactor_with_years_of_experience(self):
        self.assertEqual(self.redactor.years_of_experience, 5)


class TestNewspaperModel(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="test_topic")
        self.redactor = Redactor.objects.create(
            username="test_redactor",
            email="redactor@example.com",
            first_name="Test",
            last_name="Redactor",
            password="test_password",
            years_of_experience=5
        )
        self.newspaper = Newspaper.objects.create(
            title="test_title",
            content="test_content",
            topic=self.topic
        )
        self.newspaper.publishers.add(self.redactor)

    def test_newspaper_str(self):
        self.assertEqual(str(self.newspaper), self.newspaper.title)

    def test_newspaper_publishers(self):
        self.assertIn(self.redactor, self.newspaper.publishers.all())
