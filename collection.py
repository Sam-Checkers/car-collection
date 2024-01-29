from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET KEY'] = '12345'

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
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)