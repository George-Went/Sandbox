from flask import Blueprint, render_template, request, redirect, flash
from application.database import db
from application.crucible.models import Container
from application.crucible.forms import ContainerForm


## ------------------------------------------------------------------------------------------- 
## Example Crucible Database
## -------------------------------------------------------------------------------------------

## Initilising the tasks blueprint / Registering the Blueprint
crucible = Blueprint('crucible', __name__ ,
    template_folder='templates',
    static_folder='static',
    url_prefix='crucible')

## List of containers  (WITH WTF FORMS)
@crucible.route('/', methods=['GET'])
def crucibleIndex():
    # Get existing tasks 
    containers = Container.query.all()
    return render_template('index.html', containers=containers)

## Add Container 
@crucible.route('/add', methods=['GET','POST'])
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
        return redirect('/') 

    # Get existing tasks 
    return render_template('add.html', form=form)


## Remove Container 
@crucible.route('/delete/<int:id>')
def deleteContainer(id):
    container_to_delete = Container.query.get_or_404(id) # sqlalchemy query

    try:
        db.session.delete(container_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


# @crucible.route('/crucible/update/<int:id>', methods=['GET', 'POST'])
# def crucibleUpdate(id):
#     task = Task.query.get_or_404(id) # get existing task from database - means we dont need model schema 
#     taskForm = TaskForm() # refer to instance of WTForm form

#     if taskForm.validate_on_submit():
#         # We dont need the model as our task already has a pre-existing schema
#         task.content = taskForm.content.data #  existing_task(content) = WTForm.content.data
#         db.session.commit()                  # commit the changes made to the database 
        
        
#         return redirect('/form')
        
#     return render_template('wtforms/updateWTF.html', task=task, form=taskForm)






