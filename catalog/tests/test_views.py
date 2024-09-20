from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Newspaper, Redactor, Topic


class TestIndexView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)


class TestNewspaperListView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:newspaper-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_retrieve_newspaper_list(self):
        topic = Topic.objects.create(name="Test Topic")
        Newspaper.objects.create(title="Test Newspaper", content="Content", topic=topic)
        response = self.client.get(reverse("catalog:newspaper-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/newspaper_list.html")
        self.assertContains(response, "Test Newspaper")


class TestNewspaperDetailView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(name="Test Topic")
        self.newspaper = Newspaper.objects.create(title="Test Newspaper", content="Content", topic=self.topic)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:newspaper-detail", args=[self.newspaper.id]))
        self.assertNotEqual(response.status_code, 200)

    def test_retrieve_newspaper_detail(self):
        response = self.client.get(reverse("catalog:newspaper-detail", args=[self.newspaper.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/newspaper_detail.html")
        self.assertContains(response, "Test Newspaper")


class TestNewspaperCreateView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)
        self.topic = Topic.objects.create(name="Test Topic")

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:newspaper-create"))
        self.assertNotEqual(response.status_code, 200)


class TestRedactorListView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:redactor-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_retrieve_redactor_list(self):
        Redactor.objects.create(username="test_redactor", password="test_password", email="test@example.com")
        response = self.client.get(reverse("catalog:redactor-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/redactor_list.html")
        self.assertContains(response, "test_redactor")


class TestRedactorDetailView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)
        self.redactor = Redactor.objects.create(username="test_redactor", password="test_password",
                                                email="test@example.com")

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:redactor-detail", args=[self.redactor.id]))
        self.assertNotEqual(response.status_code, 200)


class TestTopicListView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:topic-list"))
        self.assertNotEqual(response.status_code, 200)

    def test_retrieve_topic_list(self):
        Topic.objects.create(name="Test Topic")
        response = self.client.get(reverse("catalog:topic-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalog/topic_list.html")
        self.assertContains(response, "Test Topic")


class TestTopicCreateView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse("catalog:topic-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_create_topic(self):
        response = self.client.post(reverse("catalog:topic-create"), {
            'name': 'New Topic'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(name='New Topic').exists())
