from app.forms import LoginForm
from app import app
from flask import render_template, request, redirect, url_for, flash

from flask import Flask, render_template, redirect
from .forms import LoginForm
 
app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    form = LoginForm()
    title = 'Register'
    return render_template('signup.html', title=title, form=form)

@app.route("/phonebook")
def phonebook():
    title = "Phonebook"
    return render_template("phonebook.html", title=title)