import json

# Your existing data
data = {
    "1": [{"username": "Bret", "task": "delectus aut autem", "completed": False},
          {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": False},
          # ... other tasks for user 1 ...
          ],
    "2": [{"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
          {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": True},
          # ... other tasks for user 2 ...
          ],
    # ... other users ...
}

# Convert data to JSON format
json_data = json.dumps(data, indent=4)

# Write JSON data to a file
with open("todo_all_employees.json", "w") as json_file:
    json_file.write(json_data)
