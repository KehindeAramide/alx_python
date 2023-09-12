"""Write a Python script that takes your GitHub credentials"""
import requests
import sys

"""Replace 'YOUR_USERNAME' with your GitHub username and 'YOUR_TOKEN' with your personal access token"""
username = sys.argv[1]
token = sys.argv[2]

"""Create a Basic Authentication header with your username and token"""
headers = {'Authorization': 'Basic ' + f'{username}:{token}'.encode('utf-8').hex()}

"""Send a GET request to the GitHub API to fetch your user information"""
url = 'https://api.github.com/user'
response = requests.get(url, headers=headers)

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:
    user_data = response.json()
    user_id = user_data['id']
    print(f"Your GitHub user ID is: {user_id}")
else:
    print(f"Failed to fetch user data. Status code: {response.status_code}")
