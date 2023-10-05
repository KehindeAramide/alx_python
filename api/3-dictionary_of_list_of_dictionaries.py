import json
import requests

users_url = "https://jsonplaceholder.typicode.com/users"

def user_info():
    with open('todo_all_employees.json', 'r') as f:
        student_json = json.load(f)

    correct_json = requests.get(users_url).json()

    correct_ids = [entry['id'] for entry in correct_json]  # Extract IDs from correct_json

    for student_entry in student_json:
        if int(student_entry) not in correct_ids:
            print("User ID {} Found: Incorrect".format(student_entry))
            return
    
    print("All users found: OK")

if __name__ == "__main__":
    user_info()
