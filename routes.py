from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import User, Post
from collection import app, db, bcrypt

SECRET_KEY = '12345'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jjcuumbp:0ZzI8WrcGBRkUtNlmM8-ml4CkFWGB1KZ@salt.db.elephantsql.com/jjcuumbp'

posts = [
    {
        'author': 'Sam Collins',
        'car_title': 'Honda CRV',
        'car_description': "2013 grey",
        'date_posted': 'January 29, 2024' 
    },
    {
        'author': 'John Doe',
        'car_title': 'Ford',
        'car_description': "2011 red",
        'date_posted': 'January 20, 2022' 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/profile")
def profile():
    return render_template('profile.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        print("success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for ('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/getdata')
def getdata():
    return {'yee': 'haw'}

if __name__ == '__main__':
    app.run(debug=True)