import requests
import sys

"""Check if both URL and email are provided as command-line arguments"""
if len(sys.argv) < 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

"""Get the URL and email from the command-line arguments"""
url = sys.argv[1]
email = sys.argv[2]

"""Define the data to send in the POST request"""
data = {'email': email}

"""Send a POST request to the specified URL with the email as a parameter"""
response = requests.post(url, data=data)

"""Check if the request was successful (status code 200)""""
if response.status_code == 200:
    """Print the response content"""
    print(response.text)
else:
    """Print an error message with the status code if the request fails"""
    print(f"Request failed with status code {response.status_code}")
