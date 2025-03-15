import json
from datetime import datetime


def load_file():
    """Инициализация JSON файла"""
    try:
        with open('task.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_file(tasks):
    """Сохранение JSON файла"""
    with open('task.json', 'w', encoding='utf-8') as file:
        return json.dump(obj=tasks, fp=file, ensure_ascii=False, indent=4)


def add_task(parts):
    """Добавление задачи"""
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

            print(f'Задача успешно добавлена! (ID: {task_list['id']})')
    else:
        print('Произошла ошибка! Повторите ещё раз.')


def update_task(parts):
    """Обновление задачи по ID"""
    tasks = load_file()
    if parts[0] == 'update' and parts[1].isdigit():
        for task in tasks:
            if task['id'] == int(parts[1]):
                task['description'] = ' '.join(parts[2:])
                task['updated_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        save_file(tasks)
    else:
        print('Введён неверный ID. Повторите попытку.')


def delete_task(parts):
    """Удаление задачи по ID"""
    tasks = load_file()
    if len(parts) == 2 and parts[0] == 'delete' and parts[1].isdigit():
        for i, task in enumerate(tasks):
            if task['id'] == int(parts[1]):
                del tasks[i]  # Удаляем по индексу из enumerate
                print('\nЗадача успешно удалена!')
        save_file(tasks)
    else:
        print('Произошла ошибка. Повторите ещё раз.')



def marking_task_status(parts):
    """Изменяем статус задачи по ID"""
    tasks = load_file()
    if len(parts) == 3 and parts[0] == 'mark' and parts[1].isdigit() and (
            parts[2] == 'done' or parts[2] == 'todo' or parts[2] == 'in-progress'):
        for task in tasks:
            if task['id'] == int(parts[1]):
                task['status'] = parts[2]
                task['updated_at'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        save_file(tasks)

    else:
        print('Введён неверный статус! Повторите ещё раз.')


def show_task(parts):
    """Отображение списка всех задач"""
    tasks = load_file()
    if len(parts) == 1 and parts[0] == 'list':
        for task in tasks:
            print(f'''            ID задачи: {task['id']}
            Задача: {task['description']}
            Статус: {task['status']}
            Дата создания: {task['created_at']}\n''')
    else:
        print('Введён неверный статус! Повторите ещё раз.')

    # Отображаем задачи todo
    if len(parts) == 2 and (parts[1] == 'todo' or parts[1] == 'done' or parts[1] == 'in-progress'):
        for task in tasks:
            if task['status'] == 'todo':
                print(f'''            ID задачи: {task['id']}
                            Задача: {task['description']}
                            Статус: {task['status']}
                            Дата создания: {task['created_at']}\n''')
            else:
                print('Введён неверный статус! Повторите ещё раз.')


while True:
    prompt = input('''\nЧто вы хотите сделать?
    
    Добавление новой задачи: add <наименование задачи>
    Обновление существующей задачи: update <id задачи> <текст>
    Удаление задачи: delete <id>
    Изменение статуса задачи: mark <id> <статус задачи>
    Вывод списка задач: list <тип задачи>
    Введите 'exit' чтобы закрыть программу
    
    Введите команду: ''')

    # 'exit' для выхода из программы
    if prompt == 'exit':
        break

    parts = prompt.split()  # Деление ввода на части

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
        print('Неизвестная команда! Попробуйте снова.')
