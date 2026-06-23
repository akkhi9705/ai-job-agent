def detect_sponsorship(jd):

    jd = jd.lower()

    sponsor_words = [

        "visa sponsorship",
        "h1b sponsorship",
        "work visa sponsorship",
        "employment sponsorship",
        "offer sponsorship",
        "provide sponsorship",
        "sponsorship available"

    ]

    no_sponsor_words = [

        "will not sponsor",
        "unable to sponsor",
        "no sponsorship",
        "without future sponsorship",
        "must not require sponsorship",
        "cannot sponsor",
        "do not sponsor",
        "authorized to work without sponsorship",
        "without employer sponsorship",
        "future sponsorship"

    ]

    for phrase in no_sponsor_words:

        if phrase in jd:
            return "NO_SPONSORSHIP"

    for phrase in sponsor_words:

        if phrase in jd:
            return "SPONSORS"

    return "UNKNOWN"