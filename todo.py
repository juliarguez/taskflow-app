def add_task(data, title):
    data["pending"].append({"title": title})

def delete_task(data, index):
    if 0 <= index < len(data["pending"]):
        data["pending"].pop(index)

def complete_task(data, index):
    if 0 <= index < len(data["pending"]):
        task = data["pending"].pop(index)
        data["completed"].append(task)

def edit_task(data, index, new_title):
    if 0 <= index < len(data["pending"]):
        data["pending"][index]["title"] = new_title