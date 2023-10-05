import json
import requests

users_url = "https://jsonplaceholder.typicode.com/users"

def user_info():
    with open('todo_all_employees.json', 'r') as f:
        student_json = json.load(f)

    correct_json = requests.get(users_url).json()

    student_json = {int(key): value for key, value in student_json.items()}  # Convert keys to integers

    for correct_entry in correct_json:
        if correct_entry not in student_json:
            print("User ID {} Found: Incorrect".format(correct_entry))
            return
    
    print("All users found: OK")

if __name__ == "__main__":
    user_info()
