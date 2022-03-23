from flask import request
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.api import ModelRestApi, BaseApi, expose, rison, safe
from flask_appbuilder.security.decorators import protect
import requests, json
from . import appbuilder, db
import sqlalchemy
from sqlalchemy import func
import docker

client = docker.from_env()

class docker_api(BaseApi):
  @expose("/list_running_containers", methods=["GET"])
  # ! protect() # Include for production to require Auth
  def list_running(self):
    """
    This endpoint accepts get requests only with no args and returns all running containers
    """
    container_list = client.containers.list()
    message = []
    for container in container_list:
      message.append(container.attrs) 
    return self.response(200,message=(message))

  @expose("/list_all_containers", methods=["GET"])
  # ! protect() # Include for production to require Auth
  def list_all(self):
    """
    This endpoint accepts get requests only with no args and returns all containers regardless of state
    """
    container_list = client.containers.list(all)
    message = []
    for container in container_list:
      message.append(container.attrs) 
    return self.response(200,message=(message))

  @expose("/get_container", methods=["GET"])
  # ! protect() # Include for production to require Auth
  def get_container(self):
    """
    This endpoint accepts a container_id or name and returns information about that container
    """
    try:
      container = client.containers.get(request.json['id_name'])
      return self.response(200,message=(container.attrs))
    except:
      return self.response(400)

  @expose("/run_container", methods=["POST"])
  # ! protect() #Include for production to requre auth
  def run_container(self):
    """
    This endpoint accepts arguements about a container and then creates and starts the container with those arguements
    """
    if request.method =='POST':
      # ! This will require more logic later to take the load out of the front end
      json_string = request.json
      container = client.containers.run(json_string['image'],\
        json_string['command'],\
        environment=json_string.get('environment'),\
        ports=json_string.get('ports'),\
        volumes=json_string.get('volumes'),\
        name=json_string.get('name'),\
        network=json_string.get('network'),\
        detach=True,\
        mem_limit=json_string.get('mem_limit'),\ 
        storage_opt=json_string.get('storage_opt'))
      return self.response(200, message=container.attrs)
    else:
      return self.response(400)
    
  @expose("/start_container", methods=['POST'])
  # ! protect() #Include for production to require auth
  def start_container(self):
    """
    This endpoint accepts a container_id or name and returns information about that container
    """
    try:
      container = client.containers.get(request.json['id_name'])
      container.start()
      return self.response(200,message=(container.attrs))
    except:
      return self.response(400)
  
  @expose("/stop_container", methods=['POST'])
  # ! protect() #Include for production to require auth
  def stop_container(self):
    """
    This endpoint accepts a container_id or name and returns information about that container
    """
    try:
      container = client.containers.get(request.json['id_name'])
      container.stop()
      return self.response(200,message=(container.attrs))
    except:
      return self.response(400)

  @expose("/remove_container", methods=['POST'])
  # ! protect() #Include for production to require auth
  def remove_container(self):
    """
    This endpoint accepts a container_id or name and returns information about that container
    """
    try:
      container = client.containers.get(request.json['id_name'])
      container.remove(force=True)
      return self.response(200,message=(container.attrs))
    except:
      return self.response(400)
  
  @expose("/kill_container", methods=['POST'])
  # ! protect() #Include for production to require auth
  def kill_container(self):
    """
    This endpoint accepts a container_id or name and returns information about that container
    """
    try:
      container = client.containers.get(request.json['id_name'])
      container.kill()
      return self.response(200,message=(container.attrs))
    except:
      return self.response(400)


appbuilder.add_api(docker_api)