from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "static" / "files" / "resume.pdf"
BURGUNDY = colors.HexColor("#260d10")
ACCENT = colors.HexColor("#b76e45")
INK = colors.HexColor("#241817")
MUTED = colors.HexColor("#665753")
RULE = colors.HexColor("#dfd3ce")
PAPER = colors.HexColor("#faf7f3")
PALE_ROSE = colors.HexColor("#f2e8e2")

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "ResumeName",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=27,
        textColor=colors.white,
        spaceAfter=5,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeRole",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#e8ad85"),
    )
)
styles.add(
    ParagraphStyle(
        "ResumeContact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#f9eee8"),
        alignment=TA_RIGHT,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeSection",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=BURGUNDY,
        spaceBefore=5,
        spaceAfter=0,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=INK,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeSmall",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=7.5,
        leading=9,
        textColor=MUTED,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeItem",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=10,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeDate",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=8.5,
        textColor=ACCENT,
        alignment=TA_RIGHT,
    )
)
styles.add(
    ParagraphStyle(
        "ResumeSkillTitle",
        parent=styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=9,
        textColor=BURGUNDY,
        spaceAfter=3,
    )
)


def paragraph(text, style="ResumeBody"):
    return Paragraph(escape(text), styles[style])


def add_section(story, title):
    heading = Table(
        [["", Paragraph(escape(title.upper()), styles["ResumeSection"])]],
        colWidths=[2.2 * mm, 165.8 * mm],
        hAlign="LEFT",
    )
    heading.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), ACCENT),
                ("BACKGROUND", (1, 0), (1, 0), PALE_ROSE),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 0),
                ("LEFTPADDING", (1, 0), (1, 0), 7),
                ("RIGHTPADDING", (1, 0), (1, 0), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    story.extend([heading, Spacer(1, 3)])


def add_entry(story, title, date, detail):
    row = Table(
        [["", paragraph(title, "ResumeItem"), paragraph(date, "ResumeDate")]],
        colWidths=[1.3 * mm, 124.7 * mm, 42 * mm],
        hAlign="LEFT",
    )
    row.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), ACCENT),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 0),
                ("LEFTPADDING", (1, 0), (-1, -1), 5),
                ("RIGHTPADDING", (1, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    story.extend(
        [
            row,
            Table(
                [["", paragraph(detail, "ResumeSmall")]],
                colWidths=[1.3 * mm, 166.7 * mm],
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (0, 0), ACCENT),
                        ("LEFTPADDING", (0, 0), (0, 0), 0),
                        ("RIGHTPADDING", (0, 0), (0, 0), 0),
                        ("LEFTPADDING", (1, 0), (1, 0), 5),
                        ("RIGHTPADDING", (1, 0), (1, 0), 0),
                        ("TOPPADDING", (0, 0), (-1, -1), 1),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                    ]
                ),
            ),
            Spacer(1, 2),
        ]
    )


def draw_footer(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(BURGUNDY)
    canvas.rect(0, height - 3 * mm, width, 3 * mm, stroke=0, fill=1)
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.6)
    canvas.line(21 * mm, 16 * mm, width - 21 * mm, 16 * mm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(21 * mm, 11 * mm, "ADITYA PATEL - RESUME")
    canvas.drawRightString(width - 21 * mm, 11 * mm, f"PAGE {doc.page}")
    canvas.restoreState()


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        rightMargin=21 * mm,
        leftMargin=21 * mm,
        topMargin=12 * mm,
        bottomMargin=20 * mm,
        title="Aditya Patel - Resume",
        author="Aditya Patel",
        subject="Graphic Design and Web Development",
    )
    story = []

    portrait = Image(
        str(ROOT / "static" / "images" / "aditya-patel.png"),
        width=16 * mm,
        height=21.3 * mm,
    )
    header = Table(
        [
            [
                portrait,
                [
                    paragraph("ADITYA PATEL", "ResumeName"),
                    paragraph("GRAPHIC DESIGNER  |  WEB DEVELOPER", "ResumeRole"),
                ],
                Paragraph(
                    "Unnao, Uttar Pradesh, India<br/>"
                    "adityapatelcse16@gmail.com<br/>"
                    "+91 8081146683",
                    styles["ResumeContact"],
                ),
            ]
        ],
        colWidths=[18 * mm, 92 * mm, 58 * mm],
        hAlign="LEFT",
    )
    header.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BURGUNDY),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.extend([header, Spacer(1, 5)])

    add_section(story, "Professional Summary")
    story.append(
        paragraph(
            "Creative and detail-oriented aspiring professional with a Diploma in "
            "Computer Science and Engineering and practical experience in graphic "
            "design and web development. Completed Python with Django internship "
            "training and built responsive projects using modern web technologies. "
            "A fast learner with strong communication and problem-solving skills, "
            "able to work independently and collaboratively."
        )
    )

    add_section(story, "Skills")
    skill_rows = [
        [
            [
                paragraph("GRAPHIC DESIGN", "ResumeSkillTitle"),
                paragraph(
                    "Social media and marketing creatives, logo design and brand "
                    "identity, typography, color theory, photo editing and image "
                    "manipulation, AI-assisted design and ideation.",
                    "ResumeSmall",
                ),
                paragraph("SOFTWARE", "ResumeSkillTitle"),
                paragraph(
                    "Adobe Photoshop, Canva, Figma, CorelDRAW, Inkscape.",
                    "ResumeSmall",
                ),
            ],
            [
                paragraph("WEB DEVELOPMENT", "ResumeSkillTitle"),
                paragraph(
                    "HTML, CSS, JavaScript, Python, Django, Bootstrap.",
                    "ResumeSmall",
                ),
                paragraph("TOOLS", "ResumeSkillTitle"),
                paragraph("Visual Studio Code, Django Admin.", "ResumeSmall"),
            ],
        ]
    ]
    skill_table = Table(skill_rows, colWidths=[84 * mm, 84 * mm], hAlign="LEFT")
    skill_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), PAPER),
                ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#f6f0eb")),
                ("BOX", (0, 0), (-1, -1), 0.6, RULE),
                ("INNERGRID", (0, 0), (-1, -1), 0.6, colors.white),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 9),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(skill_table)

    add_section(story, "Professional Experience")
    add_entry(
        story,
        "Python with Django Intern - Techpile Technology Pvt. Ltd.",
        "JUN 2025 - JUL 2025",
        "Lucknow, Uttar Pradesh. Completed structured on-the-job training in "
        "frontend and backend development, database design, and application "
        "frameworks. Contributed to real application modules, met timelines, "
        "and collaborated with mentors and teammates.",
    )

    add_section(story, "Selected Projects")
    add_entry(
        story,
        "Job Portal",
        "JUL 2025",
        "Developed a responsive job portal where users can browse and apply for "
        "listings. Built with HTML, CSS, JavaScript, Bootstrap, Python, and Django.",
    )
    add_entry(
        story,
        "Timetable Management System",
        "DEC 2025",
        "Built a system to create and manage class and exam timetables, streamlining "
        "scheduling and reducing manual effort with HTML, CSS, and JavaScript.",
    )
    add_entry(
        story,
        "Real-Time Price Tracking System",
        "MAR 2026",
        "Designed a price tracking and comparison application to monitor and "
        "compare product prices across sources using HTML, CSS, JavaScript, "
        "Python, and Django.",
    )

    add_section(story, "Education")
    add_entry(
        story,
        "Diploma in Computer Science and Engineering",
        "AUG 2023 - JUL 2026",
        "Government Polytechnic Bighapur, Unnao.",
    )
    add_entry(
        story,
        "Certificate in Computer Operator and Programming Assistant (COPA)",
        "AUG 2022 - JUL 2023",
        "Government Industrial Training Institute Bighapur, Unnao.",
    )
    add_entry(
        story,
        "Intermediate (10+2)",
        "APR 2021 - JUN 2022",
        "Janak Dulare Vidya Mandir Inter College, Osiyan, Unnao.",
    )
    add_entry(
        story,
        "High School (10th)",
        "APR 2019 - JUN 2020",
        "Janak Dulare Vidya Mandir Inter College, Osiyan, Unnao.",
    )

    add_section(story, "Certifications")
    story.append(paragraph("Python - Techpile Technology Pvt. Ltd.", "ResumeSmall"))
    story.append(paragraph("AI Skills - EY and Microsoft.", "ResumeSmall"))

    add_section(story, "Core Strengths")
    story.append(
        paragraph(
            "Communication and interpersonal skills, team collaboration, "
            "problem-solving, time management, adaptability, attention to detail, "
            "fast learning, MS Office, typing, internet research, and email handling."
        )
    )

    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
