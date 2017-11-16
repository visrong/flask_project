from app import app
from flask import render_template


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
