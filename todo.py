def add_task(tasks, title):
    tasks.append({"title": title, "done": False})

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def edit_task(tasks, index, new_title):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title