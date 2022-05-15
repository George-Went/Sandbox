import os # allows picture saving
import secrets
from PIL import Image
from flask import render_template, flash, redirect, url_for, flash, redirect, request
from wtforms.validators import Email
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm,  PostForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")  # Root page of the website
def root():
    return "<a href='http://localhost:5000/home'>Go to Home Page</a>"


@app.route("/home")  # Root page of the website
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts)


@app.route("/about")  # About page
def about():
    return render_template("about.html", title="about")


@app.route("/register", methods=["GET", "POST"])
def register():
    ## Returns user to home page if they are already logged in 
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm() # use the registration form from 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")  # Create Hashed Password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)  # define a user as a object consisting of the form entries and our newely generated hashed password
        db.session.add(user)  # adding our newely created user
        db.session.commit()  # Commit the above changes to the database
        flash("Your account has been created, you can now log in", "success")  # pop up message saying that an acount has been created
        return redirect(url_for("login"))  # Return user to the login page
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # check if a user == User in our database by checking emails
        if user and bcrypt.check_password_hash(user.password, form.password.data): # if user exists + password they entered into form is valid
            login_user(user, remember=form.remember.data) # login user and adds checkbox asking if they want to be remembered
            flash("you have logged in: " + form.email.data)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger") ## red box that appears up top 
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# route inside /account for saving a picture
def save_picture(form_picture):
    # we can save the picture as a random file name rather than the file name the user wants 
    print("saving picture")
    random_hex = secrets.token_hex(8)
    filename, filename_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + filename_ext
    print(picture_filename)
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_filename) # create the file location for the picture to be stored in
    ## form_picture.save(picture_path)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename
    ## We can also resize the images using pillow https://youtu.be/803Ei2Sq-Zs?t=2208


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        # Commit new username + email to database
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success') # green box with text
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file = image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post has been created", 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',form=form)

@app.route("/post/<int:post_id>")
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', title='post.title', post=post)



