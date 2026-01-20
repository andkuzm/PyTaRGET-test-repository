import requests

def get_status_code(url):
    """
    Return HTTP status code for the given URL.
    """
    response = requests.get(url)
    return response.status_code