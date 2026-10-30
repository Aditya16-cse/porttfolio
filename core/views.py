from pathlib import Path

from django.conf import settings
from django.shortcuts import render

from .models import Project


def home(request):
    services = [
        {
            "number": "01",
            "title": "Graphic design",
            "description": "Logos, posters and visual identities that make a lasting impression.",
            "image": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=900&q=85",
            "alt": "Printed graphic design samples on a desk",
        },
        {
            "number": "02",
            "title": "Web development",
            "description": "Fast, responsive websites built to work beautifully on every screen.",
            "image": "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?auto=format&fit=crop&w=900&q=85",
            "alt": "Website displayed on a desktop screen",
        },
    ]
    projects = Project.objects.all()
    process = [
        ("01", "Discover", "Understanding your goals, audience and requirements."),
        ("02", "Strategize", "Planning the structure, features and a clear roadmap."),
        ("03", "Design", "Building thoughtful, responsive solutions with care."),
        ("04", "Deliver", "Testing, launching and supporting your finished product."),
    ]
    skill_groups = [
        {
            "title": "Graphic Design",
            "skills": ["Social Media Design & Marketing Creatives", "Logo Design & Brand Identity", "Typography", "Color Theory", "Photo Editing & Image Manipulation", "AI-Assisted Design & Ideation"],
            "software": ["Adobe Photoshop", "Canva", "Figma", "CorelDRAW", "Inkscape"],
        },
        {
            "title": "Web Development",
            "skills": [
                "HTML",
                "CSS",
                "JavaScript",
                "Python",
                "Django",
                "Bootstrap"
            ],
            "software": ["Visual Studio Code", "Django Admin"],
        },
    ]
    certifications = [
        "Python — Techpile Technology Pvt. Ltd.",
        "AI Skills — EY & Microsoft",
    ]
    education = [
        {
            "title": "High School (10th)",
            "institution": "Janak Dulare Vidya Mandir Inter College, Osiyan Unnao",
            "years": "Apr 2019 – Jun 2020",
        },
        {
            "title": "Intermediate (10+2)",
            "institution": "Janak Dulare Vidya Mandir Inter College, Osiyan Unnao",
            "years": "Apr 2021 – Jun 2022",
        },
        {
            "title": "Certificate in Computer Operator & Programming Assistant (COPA)",
            "institution": "Government Industrial Training Institute Bighapur, Unnao",
            "years": "Aug 2022 – Jul 2023",
        },
        {
            "title": "Diploma in Computer Science & Engineering",
            "institution": "Government Polytechnic Bighapur, Unnao",
            "years": "Aug 2023 – Jul 2026",
        },   
    ]
    return render(
        request,
        "core/home.html",
        {
            "services": services,
            "graphic_design_projects": [
                project for project in projects
                if project.project_type == Project.ProjectType.GRAPHIC_DESIGN
            ],
            "web_development_projects": [
                project for project in projects
                if project.project_type == Project.ProjectType.WEB_DEVELOPMENT
            ],
            "process": process,
            "skill_groups": skill_groups,
            "certifications": certifications,
            "education": education,
            "phone": "+91 8081146683",
            "email": "adityapatelcse16@gmail.com",
            "location": "Lucknow, Uttar Pradesh, India",
            "resume_available": (
                Path(settings.BASE_DIR) / "static" / "files" / "resume.pdf"
            ).is_file(),
        },
    )
