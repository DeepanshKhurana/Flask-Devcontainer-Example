from flask import Flask, render_template

app = Flask(__name__)

@app.route('/tasks')
def tasks():
    task_list = ["Task 1", "Task 2", "Task 3"]
    return render_template('3.2-tasks.html', tasks=task_list)