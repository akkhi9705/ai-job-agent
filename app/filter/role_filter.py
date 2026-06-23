def is_cs_role(title):

    title = title.lower()

    keywords = [

         # Engineering
        "engineer",
        "developer",

        # Software
        "software",
        "backend",
        "frontend",
        "full stack",
        "fullstack",

        # Data
        "data engineer",
        "data analyst",
        "analytics engineer",
        "business intelligence",
        "bi developer",
        "data scientist",

        # AI / ML
        "machine learning",
        "ml engineer",
        "ai engineer",
        "artificial intelligence",

        # Cloud / Platform
        "cloud engineer",
        "platform engineer",
        "infrastructure engineer",
        "site reliability",
        "sre",
        "devops",

        # Mobile
        "android",
        "ios",
        "mobile engineer",

        # QA
        "qa engineer",
        "quality engineer",
        "sdet",

        # Security
        "security engineer",
        "cybersecurity",

        # Technical Analyst
        "systems analyst",
        "application engineer",
        "solutions engineer"
    ]

    for keyword in keywords:

        if keyword in title:
            return True

    return False