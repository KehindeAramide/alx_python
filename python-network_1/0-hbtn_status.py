"""Writing a script that fetches the below url"""

import requests

"""Define the URL to fetch"""
url = 'https://alu-intranet.hbtn.io/status'

"""Send a GET request to the URL"""
response = requests.get(url)

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:
    """Print the response content"""
    print("\t" + response.text)
else:
    """Print an error message with the status code if the request fails"""
    print(f"Request failed with status code {response.status_code}")
