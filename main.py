import json
from datetime import datetime


def load_file():
    """Initializing JSON file"""
    try:
        with open('task.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_file(tasks):
    """Saving JSON file"""
    with open('task.json', 'w', encoding='utf-8') as file:
        return json.dump(obj=tasks, fp=file, ensure_ascii=False, indent=4)


def add_task(parts):
    """Adding new tasks"""
    tasks = load_file()
    task_list = {}
    if parts[0] == 'add':
        with open('task.json', 'w', encoding='utf-8') as file:
            if not tasks:
                task_list['id'] = 1
            else:
                task_list['id'] = tasks[-1]['id'] + 1
            task_list['description'] = ' '.join(parts[1:])
            task_list['status'] = 'todo'
            task_list['created_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            task_list['updated_at'] = '-'
            tasks.append(task_list)
            save_file(tasks)

            print(f'\nTask was successfully created! (ID: {task_list['id']})')
    else:
        print('\nAn error occurred! Try again.')


def update_task(parts):
    """Updating task by ID"""
    tasks = load_file()
    check = False

    if parts[0] == 'update' and parts[1].isdigit():
        for task in tasks:
            if task['id'] == int(parts[1]):
                task['description'] = ' '.join(parts[2:])
                task['updated_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                check = True

        # Checking for potential errors
        if check:
            save_file(tasks)
            print(f'\nTask ID: {parts[1]} updated successfully!')
        else:
            print('\nTask ID was not found.')
    else:
        print('\nAn error occurred! Try again.')


def delete_task(parts):
    """Deleting task ID"""
    tasks = load_file()
    check = False
    if len(parts) == 2 and parts[0] == 'delete' and parts[1].isdigit():
        for i, task in enumerate(tasks):
            if task['id'] == int(parts[1]):
                del tasks[i]  # Удаляем по индексу из enumerate
                print('\nThe task was deleted successfully!')
                check = True

        if check:
            save_file(tasks)
            print(f'\nTask with (ID {parts[1]}) was deleted successfully!')
        else:
            print('\nTask ID was not found.')
    else:
        print('\nAn error occurred! Try again.')


def marking_task_status(parts):
    """Changing status of task by ID"""
    tasks = load_file()
    check = False

    if len(parts) == 3 and parts[0] == 'mark' and parts[1].isdigit() and (
            parts[2] == 'done' or parts[2] == 'todo' or parts[2] == 'in-progress'):
        for task in tasks:
            if task['id'] == int(parts[1]):
                task['status'] = parts[2]
                task['updated_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                check = True

        if check:
            save_file(tasks)
            print(f'\nStatus with (ID: {parts[1]}) updated successfully!')
        else:
            print('\nTask ID was not found.')

    else:
        print('\nAn error occurred! Try again.')


def show_task(parts):
    """Listing all tasks with filters"""
    tasks = load_file()
    if len(parts) == 1 and parts[0] == 'list':
        for task in tasks:
            print(f'''            Task ID: {task['id']}
            Task: {task['description']}
            Status: {task['status']}
            Creating date: {task['created_at']}\n''')

    # Отображаем задачи todo
    elif len(parts) == 2 and (parts[1] == 'todo' or parts[1] == 'done' or parts[1] == 'in-progress'):
        for task in tasks:
            if task['status'] == 'todo':
                print(f'''            Task ID: {task['id']}
                            Task: {task['description']}
                            Status: {task['status']}
                            Creating date: {task['created_at']}\n''')
    else:
        print('\nStatus was invalid! Try again.')


while True:
    prompt = input('''\nType the command:
    
    Adding new task: add <text>
    Updating current task: update <task id> <text>
    Deleting task: delete <id>
    Changing status of task: mark <id> <status: todo, done, in-progress>
    Show tasks: list <type: todo, done, in-progress>
    === Type 'exit' to close the program. ===
    
    Type command: ''')

    # 'exit' to close the program
    if prompt == 'exit':
        break

    parts = prompt.split()  # Dividing user input

    if parts[0] == 'add':
        add_task(parts)
    elif parts[0] == 'update':
        update_task(parts)
    elif parts[0] == 'delete':
        delete_task(parts)
    elif parts[0] == 'mark':
        marking_task_status(parts)
    elif parts[0] == 'list':
        show_task(parts)
    else:
        print('Unknown command! Try again.')
