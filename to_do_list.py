tasks = []

def add_task(task):
    if task and isinstance(task, str):
        tasks.append(task)
        return True
    return False

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return True
    return False

def list_tasks():
    return tasks
