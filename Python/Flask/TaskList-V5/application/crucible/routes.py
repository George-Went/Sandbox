from distutils.log import error
from http import client
from urllib import response
from charset_normalizer import detect
from flask import Blueprint, render_template, request, redirect, flash, url_for, abort, jsonify
from httplib2 import Response
from application.extensions import db
from application.crucible.models import Container
from application.crucible.forms import ContainerForm, ContainerFormPorts

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

## test to see if i can have external and interal port settings on the form
@crucible.route('/add2', methods=['GET','POST'])
def crucibleAdd2():
    form = ContainerFormPorts() # pass in our WTForm
       
    if form.validate_on_submit():
        # bind form results to the database model
        # database entry = Model(varaible = form data)
        # Example Port: [{"54332/tcp":"5432"}]
        internal_port = form.internal_port.data
        external_port = form.external_port.data
        ports = '[{"' + external_port + '/tcp":"' + internal_port + '"}]'
        print(internal_port)
        print(external_port)
        print(ports)
        # new_container = Container(
        #     name = form.name.data,
        #     image = form.image.data,
        #     command = form.command.data,
        #     entrypoint = form.entrypoint.data,
        #     environment = form.environment.data,
        #     network = form.network.data,
        #     network_mode = form.network_mode.data,
        #     ports = 
        #     restart_policy = form.restart_policy.data,
        #     volumes = form.volumes.data
        # ) 
    
        # print(new_container)
        
        # add the "new_container" object to the database 
        # db.session.add(new_container) 
        # db.session.commit() # commit the changes made to thze database 
        
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

    try:
        container = dockerClient.containers.get(db_container.name)
        container.stop()
        flash("stopping container: " + db_container.name)
    except Exception as error:     
        flash("Failed to stop " + str(db_container.name) + "Error: " + str(error))
        
    return redirect('/crucible')

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



## ----------------------------------------------------------------------
## Dumping data into the system on startup 
## ----------------------------------------------------------------------
@crucible.route('/dump',methods=['GET'])
def dumpData():
    
    database = Container(
        name = "hive_metrics_db",
        image = 'post',
        command = "hive_metrics_db psql -U postgres -c 'CREATE DATABASE cervus_hive'",
        entrypoint = "entrypoint.sh",
        environment = "POSTGRES_PASSWORD=hivedemo",
        network = "hive",
        network_mode = "form.network_mode.data",
        ports = "[{'54332/tcp':'5432'}]",
        restart_policy = "Always",
        volumes = "hive_metrics_db_13:/var/lib/postgresql/data",
    ) 
    db.session.add(database)
    db.session.commit()


# homer = User(name="Homer")
# marge = User(name="Marge")

# netflix = Channel(name="Netflix")
# appleTV = Channel(name="AppleTV")

# ## add an example post 
# db.session.add_all([homer, marge, netflix, appleTV])

# # commit to the database


# ## linking the many to many relationship 
# ## we can append a database - to "add onto the end" of the user
# homer.following.append(netflix)
# homer.following.append(netflix)
# homer.following.append(netflix)
# db.session.commit()