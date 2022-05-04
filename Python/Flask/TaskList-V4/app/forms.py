from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    content = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')