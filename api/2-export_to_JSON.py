import json
import requests
import sys

def export_to_json(employee_id, tasks):
    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump({str(employee_id): tasks}, json_file)
    print(f'Tasks exported to {employee_id}.json')

def get_employee_info(employee_id):
    # Get employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    username = employee_data['username']

    # Get employee's TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()

    # Prepare tasks in JSON format
    tasks = []
    for task in todo_data:
        task_json = {
            'task': task['title'],
            'completed': task['completed'],
            'username': username
        }
        tasks.append(task_json)

    # Export tasks to JSON file
    export_to_json(employee_id, tasks)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print('Error: Employee ID must be an integer.')