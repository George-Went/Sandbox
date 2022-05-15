from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField, HiddenField, IntegerField, FloatField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    content = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

# For the "socks" table
class AddRecord(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    name = StringField('Sock name')
    style = SelectField('Choose the sock style',
        choices=[ ('', ''), ('ankle', 'Ankle'),
        ('knee-high', 'Knee-high'),
        ('mini', 'Mini'),
        ('other', 'Other') ])
    color = StringField('Color')
    quantity = IntegerField('Quantity in stock')
    price = FloatField('Retail price per pair')
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

class DeleteForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This Sock')


# Containers 
class ContainerForm(FlaskForm):
    id = HiddenField()
    name = StringField() 
    image = StringField()
    command = StringField('Command')
    entrypoint = StringField('Entrypoint')
    environment = StringField()
    network = StringField()
    network_mode = StringField()
    ports = StringField()
    restart_policy = StringField()
    volumes = StringField()
    submit = SubmitField('Add Container')

## Login 
class LoginForm(FlaskForm):
    id_field = HiddenField()
    username = StringField()
    password = StringField()