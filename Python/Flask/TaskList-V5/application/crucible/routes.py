from urllib import response
from charset_normalizer import detect
from flask import Blueprint, render_template, request, redirect, flash
from httplib2 import Response
from application.extensions import db
from application.crucible.models import Container
from application.crucible.forms import ContainerForm

from os import name
import docker
dockerClient = docker.from_env()


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
    return render_template('crucible/index.html', containers=containers)

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
    return render_template('crucible/add.html', form=form)


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

# Start Container
@crucible.route('/start/<int:id>')
def startContainer(id):
    # get container
    print("CHECK")
    containers = Container.query.all()
    db_container = Container.query.get_or_404(id)

    
    print(db_container)

    try:
        # If the container exists in the client 
        container = dockerClient.containers.get(db_container.name)
        container.start()
        flash("starting container: " + db_container.name)
    except:
        flash("Creating a lcoal container called: " + db_container.name)

        containerObject = {                    
            "image": db_container.image,
            "name": db_container.name,
            "detach": True
        }
        if db_container.command: 
            containerObject['command'] = db_container.command
        if db_container.entrypoint: 
            containerObject['entrypoint'] = db_container.entrypoint  
        if db_container.environment: 
            containerObject['environment'] = db_container.environment
        if db_container.network: 
            containerObject['network'] = db_container.network
        if db_container.ports: 
            containerObject['ports'] = {'8080/tcp': 8080, '8443/tcp':8443}
        if db_container.volumes: 
            containerObject['volumes'] = db_container.volumes


        print(containerObject)
        ## create the container 
        dockerClient.containers.create(**containerObject) # needs "**" to start keyword arguments
        ## get (select) the new container
        new_container = dockerClient.containers.get(containerObject['name'])
        ## run the selected container
        new_container.start()

    return render_template('crucible/index.html', containers=containers)



# Stop Container
@crucible.route('/stop/<int:id>')
def stopContainer(id):
    # get container
    print("CHECK")
    containers = Container.query.all()
    db_container = Container.query.get_or_404(id)

    flash("stopping container: " + db_container.name)
    print(db_container)

    return render_template('crucible/index.html', containers=containers)









## ------------------------------------------------------------------------------------------- 
## Docker API Interaction
## -------------------------------------------------------------------------------------------


# List Local Containers
@crucible.route('/api/list', methods=['GET','POST'])
def listContainers():
    print("Container List")
  
    result = []
    for container in dockerClient.containers.list(all=True):
        result.append(
            {
                "id": container.id,
                "name": container.name,
                "image": container.image,
                "status": container.status
            }
        )
    return render_template('crucible/api.html', result = result)

## Test Functions

# Create Local Container
@crucible.route('/api/create', methods=['GET','POST'])
def createContainer():
    
    containerObject = {
        "image": "bfirsh/reticulate-splines",
        "name": "docker_from_object",
        "ports": {'8080/tcp': 8080, '8443/tcp':8443},
        "detach": True
    }
    print(containerObject)
    dockerClient.containers.create(**containerObject) # needs "**" to start keyword arguments
    # container = client.containers.run("bfirsh/reticulate-splines",name='docker_from_run', ports={'8080/tcp': 8080}, detach=True)
    # container = client.containers.run(**containerObject)

    text = "creating contianer: " + containerObject["name"]
    return render_template('crucible/api.html', result = text)

# Create local container from API payload 
@crucible.route('/api/create/<int:id>', methods=['GET','POST'])
def createContainer2(id):
    payload = request.json
    print(payload)



    containerObject = {
        "image": payload["image"],
        "name": payload["name"],
        "command": payload["command"],
        "detach": True
    }
    dockerClient.containers.create(**containerObject)


    response = containerObject
    
    return response

# Start Local Container
@crucible.route('/api/start', methods=['GET','POST'])
def startContainerAPI():
    containerObject = {
        "image": "bfirsh/reticulate-splines",
        "name": "docker_from_object",
        "ports": {'8080/tcp': 8080, '8443/tcp':8443},
        "detach": True
    }

    container = dockerClient.containers.get(containerObject['name'])
    container.start()

    text = "starting container: " + containerObject["name"]

    return render_template('crucible/api.html', result = text)

# Stop Local Container 
@crucible.route('/api/stop', methods=['GET','POST'])
def stopContainerAPI():

    containerObject = {
        "image": "bfirsh/reticulate-splines",
        "name": "docker_from_object",
        "ports": {'8080/tcp': 8080, '8443/tcp':8443},
        "detach": True
    }

    container = dockerClient.containers.get(containerObject['name'])
    container.stop()

    text = "stopping contianer: " + containerObject["name"]
    # client.containers.run(**containerObject)
    # for container in client.containers.list():
    #     if container.name == name:
    #         container.stop()

    return render_template('crucible/api.html', result = text)

# Stop container based on payload
