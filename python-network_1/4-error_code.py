"""Python script that fetches a URL, sends a request, and displays the body of the response. """
import requests
import sys

"""Get the URL from the command-line arguments"""
url = sys.argv[1]

"""Send a GET request to the specified URL"""
response = requests.get(url)

"""Print the body of the response"""
print(response.text)

"""Check if the status code is greater than or equal to 400"""
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
