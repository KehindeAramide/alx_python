import requests

"""end a GET request to the specified URL"""
response = requests.get("https://alu-intranet.hbtn.io/status")

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:
    """Check if the 'X-Request-Id' header is present in the response"""
    if 'X-Request-Id' in response.headers:
        """Print the value of the 'X-Request-Id' header after stripping whitespace"""
        print(response.headers['X-Request-Id'].strip())
    else:
     """Print None when the header is not found"""
    print("None")
else:
    """Print an error message with the status code"""
    print(f"Request failed with status code {response.status_code}")








#"""Writing a script that fetches the below url"""

#import requests
#"""importing requests"""
#req = requests.get("https://alu-intranet.hbtn.io/status")
#"""this fetches the above url"""