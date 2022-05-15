from importlib.resources import contents

from flask import render_template, request, redirect, flash, url_for
from app import app, db
from app.models import Container, Task, Sock
from app.forms import TaskForm, AddRecord, DeleteForm, ContainerForm

from datetime import date


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















## ------------------------------------------------------------------------------------------- 
## Example Crucible Database???
## -------------------------------------------------------------------------------------------


## List of containers  (WITH WTF FORMS)
@app.route('/crucible/', methods=['GET'])
def crucibleIndex():
    # Get existing tasks 
    containers = Container.query.all()
    return render_template('crucible/index.html', containers=containers)

## Add Container 
@app.route('/crucible/add', methods=['GET','POST'])
def crucibleAdd():
    form = ContainerForm() # pass in our WTForm
       
    if form.validate_on_submit():
        # bind form results to the database model
        # database entry = Model(varaible = form data)
        new_container = Container(
            name = form.name.data,
            image = form.image.data,
            command = form.command.data,
            entrypoint = form.entrypoint.data,
            environment = form.environment.data,
            network = form.network.data,
            network_mode = form.network_mode.data,
            ports = form.ports.data,
            restart_policy = form.restart_policy.data,
            volumes = form.volumes.data
        ) 
    
        print(new_container)
        
        # add the "new_container" object to the database 
        db.session.add(new_container) 
        db.session.commit() # commit the changes made to thze database 
        
        flash('Task added {}'.format(form.name.data))
        return redirect('/crucible/') 

    # Get existing tasks 
    return render_template('crucible/add.html', form=form)


## Remove Container 
@app.route('/crucible/delete/<int:id>')
def deleteContainer(id):
    container_to_delete = Container.query.get_or_404(id) # sqlalchemy query

    try:
        db.session.delete(container_to_delete)
        db.session.commit()
        return redirect('/crucible/')
    except:
        return 'There was a problem deleting that task'


@app.route('/crucible/update/<int:id>', methods=['GET', 'POST'])
def crucibleUpdate(id):
    task = Task.query.get_or_404(id) # get existing task from database - means we dont need model schema 
    taskForm = TaskForm() # refer to instance of WTForm form

    if taskForm.validate_on_submit():
        # We dont need the model as our task already has a pre-existing schema
        task.content = taskForm.content.data #  existing_task(content) = WTForm.content.data
        db.session.commit()                  # commit the changes made to the database 
        
        
        return redirect('/form')
        
    return render_template('wtforms/updateWTF.html', task=task, form=taskForm)










## ------------------------------------------------------------------------------------------- 
## Example Database "Socks" - https://python-adv-web-apps.readthedocs.io/en/latest/flask_db3.html#
## -------------------------------------------------------------------------------------------

## Getting the curretn date and returnign it in a dd-mm-yyyyy format 
def stringdate():
    today = date.today()
    date_list = str(today).split('-')
    # build string in format 01-01-2000
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
    return date_string


@app.route('/socks')
def socksIndex():
    # get a list of unique values in the style column
    styles = Sock.query.with_entities(Sock.style).distinct()
    return render_template('/socks/index.html', styles=styles)

@app.route('/socks/inventory/')
def inventorySocks():
    socks = Sock.query.all()
    return render_template('socks/list.html', socks=socks)

@app.route('/socks/inventory/<style>')
def inventorySocksStyle(style):
    socks = Sock.query.filter_by(style=style).order_by(Sock.name).all()
    return render_template('socks/list.html', socks=socks, style=style)

# add a new sock to the database
@app.route('/socks/add_record', methods=['GET', 'POST'])
def add_record():
    form1 = AddRecord()
    if form1.validate_on_submit():
        name = request.form['name']
        style = request.form['style']
        color = request.form['color']
        quantity = request.form['quantity']
        price = request.form['price']
        # get today's date from function, above all the routes
        updated = stringdate()
        # the data to be inserted into Sock model - the table, socks
        record = Sock(name, style, color, quantity, price, updated)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for sock {name} has been submitted."
        return render_template('socks/add_record.html', message=message)
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('socks/add_record.html', form1=form1)

# select a record to edit or delete
@app.route('/socks/select_record/<letters>')
def select_record(letters):
    # alphabetical lists by sock name, chunked by letters between _ and _
    # .between() evaluates first letter of a string
    a, b = list(letters)
    socks = Sock.query.filter(Sock.name.between(a, b)).order_by(Sock.name).all()
    return render_template('/socks/select_record.html', socks=socks)

# edit or delete - come here from form in /select_record
@app.route('/socks/edit_or_delete', methods=['POST'])
def edit_or_delete():
    id = request.form['id']
    choice = request.form['choice']
    sock = Sock.query.filter(Sock.id == id).first()
    # two forms in this template
    form1 = AddRecord()
    form2 = DeleteForm()
    return render_template('socks/edit_or_delete.html', sock=sock, form1=form1, form2=form2, choice=choice)

# result of delete - this function deletes the record
@app.route('/socks/delete_result', methods=['POST'])
def delete_result():
    id = request.form['id_field']
    purpose = request.form['purpose']
    sock = Sock.query.filter(Sock.id == id).first()
    if purpose == 'delete':
        db.session.delete(sock)
        db.session.commit()
        message = f"The sock {sock.name} has been deleted from the database."
        return render_template('socks/result.html', message=message)
    else:
        # this calls an error handler
        abort(405)

# result of edit - this function updates the record
@app.route('/socks/edit_result', methods=['POST'])
def edit_result():
    id = request.form['id_field']
    # call up the record from the database
    sock = Sock.query.filter(Sock.id == id).first()
    # update all values
    sock.name = request.form['name']
    sock.style = request.form['style']
    sock.color = request.form['color']
    sock.quantity = request.form['quantity']
    sock.price = request.form['price']
    # get today's date from function, above all the routes
    sock.updated = stringdate()

    form1 = AddRecord()
    if form1.validate_on_submit():
        # update database record
        db.session.commit()
        # create a message to send to the template
        message = f"The data for sock {sock.name} has been updated."
        return render_template('socks/result.html', message=message)
    else:
        # show validaton errors
        sock.id = id
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('socks/edit_or_delete.html', form1=form1, sock=sock, choice='edit')


# +++++++++++++++++++++++
# error routes
# https://flask.palletsprojects.com/en/1.1.x/patterns/apierrors/#registering-an-error-handler

@app.errorhandler(404)
def page_not_found(e):
    return render_template('socks/error.html', pagetitle="404 Error - Page Not Found", pageheading="Page not found (Error 404)", error=e), 404

@app.errorhandler(405)
def form_not_posted(e):
    return render_template('socks/error.html', pagetitle="405 Error - Form Not Submitted", pageheading="The form was not submitted (Error 405)", error=e), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('socks/error.html', pagetitle="500 Error - Internal Server Error", pageheading="Internal server error (500)", error=e), 500

# +++++++++++++++++++++++








if __name__ == "__main__":
    app.run(debug=True)