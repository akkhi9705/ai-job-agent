def calculate_score(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = sorted(list(resume_set & jd_set))

    missing = sorted(list(jd_set - resume_set))

    if len(jd_set) == 0:
        score = 0
    else:
        score = round(
            (len(matched) / len(jd_set)) * 100,
            2
        )

    return {

        "score": score,

        "matched": matched,

        "missing": missing

    }