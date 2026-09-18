from django.db import migrations

SERVICES = [
    {
        "title": "Graphic Design",
        "description": "Logos, brand identity, and social media creative that keeps your brand consistent everywhere.",
        "icon": "design",
        "order": 1,
    },
    {
        "title": "UI Design",
        "description": "Clean, usable interfaces for web apps, portfolios, and community platforms.",
        "icon": "ui",
        "order": 2,
    },
    {
        "title": "Web Development",
        "description": "Business sites, landing pages, and SEO-ready builds that load fast and convert.",
        "icon": "web",
        "order": 3,
    },
    {
        "title": "Digital Marketing",
        "description": "SEO, Google Ads, and Meta Ads campaigns built around real growth targets.",
        "icon": "marketing",
        "order": 4,
    },
    {
        "title": "Video Editing",
        "description": "Reels, YouTube edits, and motion graphics that keep viewers watching.",
        "icon": "video",
        "order": 5,
    },
    {
        "title": "Freelancer Community",
        "description": "Networking, collaboration, and learning support for the VSR freelancer network.",
        "icon": "community",
        "order": 6,
    },
]


def seed_services(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    for entry in SERVICES:
        Service.objects.get_or_create(title=entry["title"], defaults=entry)


def remove_services(apps, schema_editor):
    Service = apps.get_model("core", "Service")
    Service.objects.filter(title__in=[s["title"] for s in SERVICES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_services, remove_services),
    ]
