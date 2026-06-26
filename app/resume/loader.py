import os

RESUME_FOLDER = "resumes"

def load_resumes():

    resumes = []

    for file in os.listdir(RESUME_FOLDER):

        if file.endswith(".pdf"):

            resumes.append(
                os.path.join(
                    RESUME_FOLDER,
                    file
                )
            )

    return resumes