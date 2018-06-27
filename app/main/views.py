from flask import render_template
from . import main

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    return render_template('index.html')

@main.route('/signup')
def signup():
    """
    Function that returns the sign up page
    """
    return render_template('signup.html')
