"""Writing a script that fetches the below url"""

import requests
import sys

"""Check if a URL is provided as a command-line argument"""
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

"""Get the URL from the command-line argument"""
url = sys.argv[1]

"""Send a GET request to the specified URL"""
response = requests.get(url)

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:
    """Check if the 'X-Request-Id' header is present in the response"""
    if 'X-Request-Id' in response.headers:
        """Print the value of the 'X-Request-Id' header"""
        print(response.headers['X-Request-Id'])
    else:
        """Print a message when the header is not found"""
        print("X-Request-Id header not found in the response.")
else:
    """Print an error message with the status code if the request fails"""
    print(f"Request failed with status code {response.status_code}")
