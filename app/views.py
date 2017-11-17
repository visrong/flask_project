from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'zyt'}
    posts = [
        {
            'author': {'name': 'John'},
            'body': 'Beautiful day'
        },
        {
            'author': {'name': 'Susan'},
            'body': 'The Avengers movie'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
