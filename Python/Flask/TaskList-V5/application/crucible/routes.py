from distutils.log import error
from http import client
from urllib import response
from charset_normalizer import detect
from flask import Blueprint, render_template, request, redirect, flash, url_for, abort, jsonify
from httplib2 import Response
from application.extensions import db
from application.crucible.models import Container
from application.crucible.forms import ContainerForm

from os import environ, name
import docker
import docker.errors as errors
dockerClient = docker.from_env()


## ------------------------------------------------------------------------------------------- 
## Example Crucible Database
## -------------------------------------------------------------------------------------------

## Initilising the tasks blueprint / Registering the Blueprint
crucible = Blueprint('crucible', __name__ ,
    template_folder='templates',
    static_folder='static',
    url_prefix='crucible')


## List of containers in database ---------------------------------------------------
@crucible.route('/', methods=['GET'])
def crucibleIndex():
    # Get existing container database entries 
    db_container_list = Container.query.all()

    container = []
    for db_container in db_container_list:
        try:
            client_container = dockerClient.containers.get(db_container.name)
            container.append(
                {
                    "id": db_container.id,
                    "name": db_container.name,
                    "image": db_container.image,
                    "ports": db_container.ports,
                    "status": client_container.status
                }
            )
        except:
            # if container is not in docker
            container.append(
                {
                    "id": db_container.id,
                    "name": db_container.name,
                    "image": db_container.image,
                    "ports": db_container.ports,
                    "status": "not in docker"
                }
            )
            print(container)
    return render_template('crucible/index.html', containers=container)

## List all docker containers on client system --------------------------------------------------------------------------
@crucible.route('/all', methods=['GET'])
def crucibleIndexAll():
    # Get existing container database entries 
    db_container_list = Container.query.all()
    docker_container_list = dockerClient.containers.list(all=True)
    container = []
    for db_container in docker_container_list:
        try:
            client_container = dockerClient.containers.get(db_container.name)
            container.append(
                {
                    "id": db_container.short_id,
                    "name": db_container.name,
                    "image": db_container.image,
                    "ports": db_container.ports,
                    "status": client_container.status
                }
            )
        except:
            # if container is not in docker
            container.append(
                {
                    "id": db_container.id,
                    "name": db_container.name,
                    "image": db_container.image,
                    "ports": db_container.ports,
                    "status": "not in docker"
                }
            )
            print(container)
    return render_template('crucible/index.html', containers=container)


## List all docker images --------------------------------------------------------------------------
@crucible.route('/images', methods=['GET'])
def crucibleImagesAll():
    # Get existing container database entries 
    docker_image_list = dockerClient.images.list(all=True)
    images = []
    print(docker_image_list)
    for image in docker_image_list:
        images.append(
            {
                "id": image.id,
                "tags": image.tags
            }
        )
    print(images)
    return render_template('crucible/images.html', images=images)


<<<<<<< HEAD
    return render_template('crucible/index.html', containers=containers)
=======
## List Induvidual containers -------------------------------------------------
## Gets a containers infomation based on database not docker infomation 
# if the contianer is in docker 
@crucible.route('/<int:id>', methods=['GET'])
def singleContainer(id):

    db_container = Container.query.get_or_404(id)
    print(db_container)

    container = []
    try:
        client_container = dockerClient.containers.get(db_container.name)
        container.append(
            {
                "id": db_container.id,
                "name": db_container.name,
                "image": db_container.image,
                "ports": db_container.ports,
                "entrypoint": db_container.entrypoint,
                "environment": db_container.environment,
                "network": db_container.network,
                "network_mode": db_container.network_mode,
                "restart_policy": db_container.restart_policy,
                "volumes": db_container.volumes,
                "status": client_container.status
            }
        )
    except errors.APIError as error: 
        print(error)
        container.append(
            {
                "id": db_container.id,
                "name": db_container.name,
                "image": db_container.image,
                "ports": db_container.ports,
                "entrypoint": db_container.entrypoint,
                "environment": db_container.environment,
                "network": db_container.network,
                "network_mode": db_container.network_mode,
                "restart_policy": db_container.restart_policy,
                "volumes": db_container.volumes,
                "status": "not in docker"
            }
        )
        print(container)
    except: 
        # if container is not in docker
        container.append(
            {
                "id": db_container.id,
                "name": db_container.name,
                "image": db_container.image,
                "ports": db_container.ports,
                "entrypoint": db_container.entrypoint,
                "environment": db_container.environment,
                "network": db_container.network,
                "network_mode": db_container.network_mode,
                "restart_policy": db_container.restart_policy,
                "volumes": db_container.volumes,
                "status": "not in docker"
            }
        )
        print(container)
    
    return render_template('crucible/singleContainer.html', containers=container)

>>>>>>> c3a9b7e7f2114831e82d8097b14df802eb28d807


## ----------------------------------------------------------------------
## Creating Stuff
## ----------------------------------------------------------------------

## Add Container to Database -----------------------------------------------
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
        
        flash('Container added {}'.format(form.name.data))
        return redirect('/crucible/') 

    # Get existing tasks 
    return render_template('crucible/add.html', form=form) 


# Create Container in docker client
@crucible.route('/create/<int:id>')
def createContainer(id):

    db_container = Container.query.get_or_404(id)
    print(db_container)
    containerObject = {
        "image": db_container.image,
        "name": db_container.name,
        "command": db_container.command,
        "detach" : True
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
        containerObject['ports'] = db_container.ports
    if db_container.volumes: 
        containerObject['volumes'] = db_container.volumes

    try:
        dockerClient.containers.create(**containerObject)
        flash("creating container: " + db_container.name)
    except Exception as error:     
        flash("Failed to create " + str(db_container.name) + "Error: " + str(error))
        
    return redirect('/crucible')




# Start Container 
@crucible.route('/start/<int:id>')
def startContainer(id):

    db_container = Container.query.get_or_404(id)
    print(db_container)

    try:
        container = dockerClient.containers.get(db_container.name)
        container.start()
        flash("starting container: " + db_container.name)
    except Exception as error:     
        flash("Failed to start " + str(db_container.name) + "Error: " + str(error))
        
    return redirect('/crucible')


# Stop Container 
@crucible.route('/stop/<int:id>')
def stopContainer(id):
    db_container = Container.query.get_or_404(id)

<<<<<<< HEAD
    flash("stopping container: " + db_container.name)
    print(db_container)
    containers = Container.query.all()

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
=======
    try:
        container = dockerClient.containers.get(db_container.name)
        container.stop()
        flash("stopping container: " + db_container.name)
    except Exception as error:     
        flash("Failed to stop " + str(db_container.name) + "Error: " + str(error))
        
    return redirect('/crucible')
>>>>>>> c3a9b7e7f2114831e82d8097b14df802eb28d807



## Remove Container 
@crucible.route('/delete/<int:id>')
def deleteContainer(id):
    container_to_delete = Container.query.get_or_404(id) # sqlalchemy query

    try:
        db.session.delete(container_to_delete)
        db.session.commit()
        return redirect('/crucible')
    except Exception as error:     
        flash("Failed to stop " + str(container_to_delete) + "Error: " + str(error))

    return redirect('/crucible')


