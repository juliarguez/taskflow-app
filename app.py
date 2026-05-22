##VERSION WEB

from flask import Flask, render_template, request, redirect
from storage import load_tasks, save_tasks
from todo import add_task, delete_task, complete_task, edit_task

app = Flask(__name__)

@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"]
    tasks = load_tasks()
    add_task(tasks, title)
    save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    tasks = load_tasks()
    delete_task(tasks, index)
    save_tasks(tasks)
    return redirect("/")

@app.route("/complete/<int:index>")
def complete(index):
    tasks = load_tasks()
    complete_task(tasks, index)
    save_tasks(tasks)
    return redirect("/")

@app.route("/edit/<int:index>")
def edit(index):
    tasks = load_tasks()
    task = tasks[index]

    return render_template(
        "edit.html",
        task = task,
        index = index
    )

@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    tasks = load_tasks()


    new_title = request.form["title"]
    edit_task(tasks, index, new_title)
    save_tasks(tasks)

    return redirect("/")

@app.route("/clear", methods=["POST"])
def clear():
    tasks = []
    save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)