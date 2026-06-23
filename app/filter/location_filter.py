def is_us_job(location):

    location = location.lower()

    us_keywords = [

        # Generic
        "us",
        "usa",
        "united states",
        "remote",

        # States
        "alabama", "alaska", "arizona", "arkansas",
        "california", "colorado", "connecticut",
        "delaware", "florida", "georgia",
        "hawaii", "idaho", "illinois", "indiana",
        "iowa", "kansas", "kentucky", "louisiana",
        "maine", "maryland", "massachusetts",
        "michigan", "minnesota", "mississippi",
        "missouri", "montana", "nebraska",
        "nevada", "new hampshire", "new jersey",
        "new mexico", "new york", "north carolina",
        "north dakota", "ohio", "oklahoma",
        "oregon", "pennsylvania", "rhode island",
        "south carolina", "south dakota",
        "tennessee", "texas", "utah",
        "vermont", "virginia", "washington",
        "west virginia", "wisconsin", "wyoming",

         "AL","AK","AZ","AR","CA","CO","CT","DE",
        "FL","GA","HI","ID","IL","IN","IA","KS",
        "KY","LA","ME","MD","MA","MI","MN","MS",
        "MO","MT","NE","NV","NH","NJ","NM","NY",
        "NC","ND","OH","OK","OR","PA","RI","SC",
        "SD","TN","TX","UT","VT","VA","WA","WV",
        "WI","WY"

        # Common city names
        "san francisco",
        "los angeles",
        "san diego",
        "seattle",
        "boston",
        "chicago",
        "atlanta",
        "charlotte",
        "austin",
        "dallas",
        "houston",
        "miami",
        "orlando",
        "denver",
        "phoenix",
        "detroit",
        "philadelphia",
        "washington dc",
        "new york city"
    ]

    for keyword in us_keywords:

        if keyword in location:
            return True

    return False