from flask import Flask, render_template
from storage import load_tasks

app = Flask(__name__)

@app.route("/")
def home():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)