"""Writing a script that fetches the below url"""

import requests
import sys

"""Get the URL from the command-line arguments"""
url = sys.argv[1]

"""Send a GET request to the specified URL"""
response = requests.get(url)

"""Check if the 'X-Request-Id' header is present in the response"""
if 'X-Request-Id' in response.headers:
    """Print the value of the 'X-Request-Id' header"""
    print(response.headers['X-Request-Id'])
else:
    """Print "None" when the header is not found"""
    print("None")
