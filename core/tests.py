from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Project


class ProjectAdminTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="portfolio-admin",
            email="admin@example.com",
            password="test-password",
        )

    def test_admin_requires_login(self):
        response = self.client.get(reverse("admin:core_project_changelist"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("admin:login"), response.url)

    def test_admin_can_add_project_and_show_it_on_homepage(self):
        self.client.force_login(self.admin_user)
        response = self.client.post(
            reverse("admin:core_project_add"),
            {
                "title": "Portfolio admin test",
                "project_type": Project.ProjectType.WEB_DEVELOPMENT,
                "category": "Django · Portfolio",
                "image_url": "https://example.com/project.jpg",
                "image_alt": "A portfolio project preview",
                "project_url": "https://example.com/project",
                "card_style": "",
                "display_order": "4",
                "_save": "Save",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Project.objects.filter(title="Portfolio admin test").exists())

        homepage = self.client.get(reverse("home"))
        self.assertContains(homepage, "Portfolio admin test")
        self.assertContains(homepage, "Visual identity concept")
        self.assertContains(homepage, "https://example.com/project")
