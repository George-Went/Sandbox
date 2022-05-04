from importlib.resources import contents
from flask import render_template, request, redirect, flash, url_for
from app import app, db
from app.models import Task
from app.forms import TaskForm


## READ / CREATE TASK
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Task(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Task.query.order_by(Task.date_created).all()
        return render_template('index.html', tasks=tasks)

## DELETE TASK
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id) # sqlalchemy query

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

## UPDATE TASK
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', task=task)


## -------------------------------------------------------------------------------------------
## USING WTFORMS 
## -------------------------------------------------------------------------------------------

## READ / CREATE TASK (WITH WTF FORMS)
@app.route('/form', methods=['POST', 'GET'])
def exampleForm():
    taskForm = TaskForm() # pass in our WTForm
       
    if taskForm.validate_on_submit():
        new_task = Task(content = taskForm.content.data) # new_entry == Model(model.field = WTForm.field)
        db.session.add(new_task) # add the object to the database 
        db.session.commit() # commit the changes made to the database 
        
        flash('Task added {}'.format(taskForm.content.data))
        return redirect(url_for('exampleForm'))

    # Get existing tasks 
    tasks = Task.query.order_by(Task.date_created).all()
    return render_template('wtforms/indexWTF.html', tasks=tasks, form=taskForm)


## UPDATE TASK (WITH WTF FROMS)
@app.route('/form/update/<int:id>', methods=['GET', 'POST'])
def formUpdate(id):
    task = Task.query.get_or_404(id) # get existing task from database - means we dont need model schema 
    taskForm = TaskForm() # refer to instance of WTForm form

    if taskForm.validate_on_submit():
        # We dont need the model as our task already has a pre-existing schema
        task.content = taskForm.content.data #  existing_task(content) = WTForm.content.data
        db.session.commit()                  # commit the changes made to the database 
        
        flash('Task updated {}'.format(taskForm.content.data))
        return redirect('/form')
        
    return render_template('wtforms/updateWTF.html', task=task, form=taskForm)

## CREATE TASK (Not Showing exisitng tasks)
@app.route('/form/add', methods=['GET', 'POST'])
def formCreate():
    taskForm = TaskForm() # 

    if taskForm.validate_on_submit():
        new_task = Task(content = taskForm.content.data) # new_entry == Model(model.field = WTForm.field)
        db.session.add(new_task) # add the object to the database 
        db.session.commit() # commit the changes made to the database 
        
        flash('Task added {}'.format(taskForm.content.data))
        return redirect(url_for('exampleForm'))

    return render_template('wtforms/addWTF.html', form = taskForm)

if __name__ == "__main__":
    app.run(debug=True)