"""Writing a script that fetches the below url"""

import requests
"""importing requests"""
req = requests.get("https://alu-intranet.hbtn.io/status")
"""this fetches the above url"""
if response.status_code == 200:
    print(response.text)

