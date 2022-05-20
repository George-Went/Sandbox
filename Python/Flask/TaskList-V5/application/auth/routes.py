
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, logout_user, current_user, login_user
from application.auth.forms import SignupForm, LoginForm
from application.auth.models import User
from application.extensions import db, login_manager
from application import login_manager



auth = Blueprint('auth', __name__ ,
    template_folder='templates',
    static_folder='static',
    url_prefix='auth')



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    print("CHECK 1")
    if form.validate_on_submit():
        print("CHECK 2")
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            #login_user(user)  # Log in as newly created user

            flash('User added {}'.format(form.name.data))
            return redirect(url_for('auth.login'))
        flash('A user already exists with that email address.')

    return render_template(
        'auth/signup.html',
        title='Create an Account.',
        form=form
    )


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # # Bypass if user is logged in
    # if current_user.is_authenticated:
    #     return "ur logged in"

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            # If the user successfully logs in
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('auth.check'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth.login'))
    return render_template(
        'auth/login.html',
        form=form,
        title='Log in.',
        template='login-page',
        body="Log in with your User account."
    )

# Page that logs the user out 
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# Page that only shows if a user is logged in
@auth.route('/check')
@login_required
def check():
    print(current_user)
    print(current_user.name)
    return render_template('auth/check.html', current_user = current_user)



# Method uesd to check if a user is logged in
@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

# Redirect Users if they are no logged in
@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))