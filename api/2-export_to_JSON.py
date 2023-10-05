import json
import requests
import sys

def get_employee_info(employee_id):
    # Getting employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    username = employee_data['username']

    # Getting employee's TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()

    # Preparing tasks in JSON format
    tasks_json = []
    for task in todo_data:
        task_json = {
            'task': task['title'],
            'completed': task['completed'],
            'username': username
        }
        tasks_json.append(task_json)

    # Writing tasks to JSON file
    filename = f'{employee_id}.json'
    with open(filename, 'w') as jsonfile:
        json.dump({str(employee_id): tasks_json}, jsonfile)

    print(f'Tasks exported to {filename}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print('Error: Employee ID must be an integer.')
