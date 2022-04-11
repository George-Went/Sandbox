from flask import Blueprint, render_template
from flask import current_app as app


# Blueprint Configuration
home = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home.route('/', methods=['GET'])
def home():
    return "<p>Hello, This is the home blueprint </p>"