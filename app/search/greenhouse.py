import requests

def search_jobs(board):

    url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

    response = requests.get(url)

    return response.json()