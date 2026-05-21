##VERSION WEB

from flask import Flask, render_template, request, redirect
from storage import load_tasks, save_tasks
from todo import add_task

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
    tasks.pop(index)
    save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)