import requests

"""Send a GET request to the specified URL"""
response = requests.get("https://intranet.hbtn.io/status")

"""Check if the request was successful (status code 200)""""
if response.status_code == 200:
    """Print the response body with its type and content"""
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
else:
    """Print an error message with the status code"""
    print(f"Request failed with status code {response.status_code}")







#"""Writing a script that fetches the below url"""

#import requests
#"""importing requests"""
#req = requests.get("https://alu-intranet.hbtn.io/status")
#"""this fetches the above url"""