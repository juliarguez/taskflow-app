##VERSIÓN CLI

from todo import add_task, delete_task, complete_task, edit_task
from storage import load_tasks, save_tasks

tasks = load_tasks()


def show_tasks():
    if not tasks:
        print("\nNo hay tareas\n")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. [{status}] {t['title']}")


while True:
    print("""
=== TO-DO APP ===
1. Ver tareas
2. Añadir tarea
3. Eliminar tarea
4. Completar tarea
5. Editar tarea
6. Salir
""")

    option = input("Opción: ")

    if option == "1":
        show_tasks()

    elif option == "2":
        title = input("Nueva tarea: ")
        add_task(tasks, title)
        save_tasks(tasks)

    elif option == "3":
        show_tasks()
        index = int(input("Número de tarea a eliminar: ")) - 1
        delete_task(tasks, index)
        save_tasks(tasks)

    elif option == "4":
        show_tasks()
        index = int(input("Número de tarea a completar: ")) - 1
        complete_task(tasks, index)
        save_tasks(tasks)
    
    elif option == "5":
        show_tasks()
        index = int(input("Número de tarea a editar: ")) - 1
        new_title = input("Nuevo nombre de la tarea: ")
        edit_task(tasks, index, new_title)
        save_tasks(tasks)
    
    if option == "6":
        break
