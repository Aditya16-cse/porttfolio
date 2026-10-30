from django.db import models


class Project(models.Model):
    class ProjectType(models.TextChoices):
        GRAPHIC_DESIGN = "graphic-design", "Graphic Design"
        WEB_DEVELOPMENT = "web-development", "Web Development"

    class CardStyle(models.TextChoices):
        DEFAULT = "", "Default"
        PRODUCT = "product", "Product"
        MONO = "mono", "Monochrome"

    title = models.CharField(max_length=120)
    project_type = models.CharField(max_length=30, choices=ProjectType.choices)
    category = models.CharField(
        max_length=180,
        help_text="Short details shown below the title, e.g. tools or project type.",
    )
    image_url = models.URLField(max_length=500)
    image_alt = models.CharField(max_length=180)
    project_url = models.URLField(max_length=500, blank=True)
    card_style = models.CharField(
        max_length=20,
        choices=CardStyle.choices,
        blank=True,
        default="",
    )
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.title
