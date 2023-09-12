"""Writing a script that fetches the below url"""

import requests

"""Define the URL to fetch"""
url = "https://intranet.hbtn.io/status"

"""Send a GET request to the URL"""
response = requests.get(url)

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:

    content_type = type(response.text).__name__
    content = response.text
    print(f"Body response:\n\t- type: {content_type}\n\t- content: {content}")
else:
    print(f"Request failed with status code {response.status_code}")