from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField, HiddenField, IntegerField, FloatField
from wtforms.validators import DataRequired

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