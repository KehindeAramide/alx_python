import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Print employee TODO list progress
    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
    for task in todo_data:
        if task['completed']:
            print(f'\t{task["title"]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print('Error: Employee ID must be an integer.')
