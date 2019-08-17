from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from config import Config


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Beni'}
    return render_template("index.html",title="Home Page",user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/blog')
def blog():
    user = {'username': 'Beni'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('blog.html', title='Home', user=user, posts=posts)