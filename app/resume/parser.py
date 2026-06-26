import pdfplumber
import re


def extract_resume_text(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


def parse_resume_sections(text):

    headings = [

        "PROFESSIONAL SUMMARY",
        "SUMMARY",

        "TECHNICAL SKILLS",
        "SKILLS",

        "PROFESSIONAL EXPERIENCE",
        "WORK EXPERIENCE",
        "EXPERIENCE",

        "PROJECTS",

        "EDUCATION",

        "CERTIFICATIONS"

    ]

    sections = {}

    current_heading = "HEADER"

    sections[current_heading] = ""

    for line in text.splitlines():

        line = line.strip()

        if not line:

            continue

        upper_line = line.upper()

        if upper_line in headings:

            current_heading = upper_line

            sections[current_heading] = ""

        else:

            sections[current_heading] += line + "\n"

    return sections