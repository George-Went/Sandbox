from flask import Blueprint, render_template, request, redirect
from application.extensions import db

## Initilising the tasks blueprint / Registering the Blueprint
main = Blueprint('main', __name__ ,
    template_folder='templates',
    static_folder='static')

## READ / CREATE TASK
@main.route('/', methods=['POST', 'GET'])
def index():
    return render_template('main/index.html')

