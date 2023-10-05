import csv
import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    username = employee_data['username']

    # Get employee's TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()

    # Write tasks to CSV file
    filename = f'{employee_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todo_data:
            task_completed_status = str(task['completed'])
            task_title = task['title']
            csvwriter.writerow([employee_id, username, task_completed_status, task_title])

    print(f'Tasks exported to {filename}')

def user_info(id):
    # Get employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    employee_data = employee_response.json()
    username = employee_data['username']

    try:
        with open(str(id) + ".csv", 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # skip header row
            for row in reader:
                user_id, csv_username, _, _ = row
                if user_id == str(id) and csv_username == username:
                    print("User ID and Username: OK")
                    return
        print("User ID or Username: Incorrect")
    except FileNotFoundError:
        print(f"File '{id}.csv' not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
            user_info(employee_id)
        except ValueError:
            print('Error: Employee ID must be an integer.')