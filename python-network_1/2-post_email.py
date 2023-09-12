
import requests
import sys
"""Check if both URL and email are provided as command-line arguments"""
if len(sys.argv) < 3:
    sys.exit("Usage: python script.py <URL> <email>")

url, email = sys.argv[1], sys.argv[2]
data = {'email': email}
"""Get the URL and email from the command-line arguments"""

response = requests.post(url, data=data)
"""Send a POST request to the specified URL with the email as a parameter"""

if response.status_code == 200:
    """Check if the request was successful (status code 200)"""
    print(f"Email: {email}")
    """Print the response content"""
else:
    print(f"Request failed with status code {response.status_code}")
    """Print an error message with the status code if the request fails"""
