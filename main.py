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

    command = prompt.split()[0]
    description = ' '.join(prompt.split()[1:])

    # Загружаем файл
    try:
        with open('task.json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    # Добавляем файл
    if command.lower() == 'add':
        with open('task.json', 'w', encoding='utf-8') as file:
            if task_list['id'] == 0:
                task_list['id'] = 1
            else:
                task_list['id'] = tasks[-1]['id'] + 1
            task_list['description'] = description
            task_list['status'] = 'todo'
            task_list['created_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            task_list['updated_at'] = '-'
            tasks.append(task_list)
            json.dump(obj=tasks, fp=file, ensure_ascii=False, indent=4)

