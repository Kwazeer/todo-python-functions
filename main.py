import json
from datetime import datetime

task_list = {
    'id': 0,
    'description': 'description',
    'status': 'status',
    'created_at': 'created_at',
    'updated_at': 'updated_at'
}


while True:
    prompt = input('''Что вы хотите сделать?
    
    add <наименование задачи>
    update <обновление задачи>
    delete <удаление задачи>
    
    Введите команду: ''')

    parts = prompt.split()

    # Загружаем файл
    try:
        with open('task.json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    # Добавляем файл
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
            json.dump(obj=tasks, fp=file, ensure_ascii=False, indent=4)

            print(f'Задача успешно добавлена! (ID: {task_list['id']})')

    # Отображаем все задачи
    if len(parts) == 1 and parts[0] == 'list':
        for task in tasks:
            print(f'''            ID задачи: {task['id']}
            Задача: {task['description']}
            Статус: {task['status']}
            Дата создания: {task['created_at']}\n''')

    # Отображаем задачи todo
    if len(parts) == 2 and parts[1] == 'todo':
        for task in tasks:
            if task['status'] == 'todo':
                print(f'''            ID задачи: {task['id']}
                            Задача: {task['description']}
                            Статус: {task['status']}
                            Дата создания: {task['created_at']}\n''')

    # Отображаем задачи done
    if len(parts) == 2 and parts[1] == 'done':
        for task in tasks:
            if task['status'] == 'done':
                print(f'''            ID задачи: {task['id']}
                            Задача: {task['description']}
                            Статус: {task['status']}
                            Дата создания: {task['created_at']}\n''')

    # Отображаем задачи in-progress
    if len(parts) == 2 and parts[1] == 'in-progress':
        for task in tasks:
            if task['status'] == 'in-progress':
                print(f'''            ID задачи: {task['id']}
                            Задача: {task['description']}
                            Статус: {task['status']}
                            Дата создания: {task['created_at']}\n''')

