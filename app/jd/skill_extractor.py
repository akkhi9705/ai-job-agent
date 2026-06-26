import re


def extract_jd_skills(jd_text):

    skills = [

        "java",
        "python",
        "sql",
        "spring boot",
        "spring",
        "react",
        "angular",
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "jenkins",
        "terraform",
        "ansible",
        "git",
        "github",
        "linux",
        "unix",
        "kafka",
        "spark",
        "hadoop",
        "oracle",
        "mysql",
        "mongodb",
        "postgresql",
        "redis",
        "microservices",
        "rest",
        "graphql",
        "typescript",
        "javascript",
        "node",
        "c++",
        "c",
        "go",
        "scala"

    ]

    found = []

    jd_text = jd_text.lower()

    for skill in skills:

        if skill in jd_text:

            found.append(skill)

    return sorted(list(set(found)))