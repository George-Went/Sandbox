from flask import Blueprint, render_template, request, redirect
from application.database import db
from application.tasks.models import Task

## -----------------------------------------------------------
## TASKS Blueprint : Found under "/tasks"
## -----------------------------------------------------------


## Initilising the tasks blueprint / Registering the Blueprint
tasks = Blueprint('tasks_bp', __name__ ,
    template_folder='templates',
    static_folder='static',
    url_prefix='tasks')

## READ / CREATE TASK
@tasks.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print("post request recived")
        task_content = request.form['content']
        new_task = Task(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/tasks/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Task.query.order_by(Task.date_created).all()
        return render_template('index.html', tasks=tasks)

## DELETE TASK
@tasks.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    print("Delete Request Recived")
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/tasks')
    except:
        return 'There was a problem deleting that task'

## UPDATE TASK
@tasks.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/tasks/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)

## Create example data
@tasks.route('/example/<content>')
def example(content):
    exampleData = Task(content=content)
    db.session.add(exampleData)
    db.session.commit()

    return "created example task"

@tasks.route('/hello', methods=['GET'])
def hello():
    return "hello world"

