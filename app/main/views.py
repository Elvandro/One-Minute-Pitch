from flask import render_template
from . import main
from flask_login import login_required

@main.route('/')
def index():
    """
    Function that returns the index page
    """
    return render_template('index.html')

@main.route('/pitch')
def pitch():
    '''
    Function that returns the pitch page
    '''
    return render_template('pitch.html')

@main.route('/general')
def general():
    '''
    Function that returns the general category page
    '''
    return render_template('general.html')

@main.route('/career')
def career():
    '''
    Function that returns the career category page
    '''
    return render_template('career.html')

@main.route('/business')
def business():
    '''
    Function that returns the business category page
    '''
    return render_template('business.html')

@main.route('/technology')
def technology():
    '''
    Function that returns the technology category page
    '''
    return render_template('technology.html')

@main.route('/science')
def science():
    '''
    Function that returns the science category page
    '''
    return render_template('science.html')

@main.route('/sports')
def sports():
    '''
    Function that returns the sports category page
    '''
    return render_template('sports.html')

@main.route('/entertainment')
def entertainment():
    '''
    Function that returns the entertainment category page
    '''
    return render_template('entertainment.html')
