from flask import render_template, redirect, url_for, flash
from . import main
from flask_login import login_required
from .forms import PitchForm, CommentForm
from ..models import User, Category, Pitch, Comment
from ..import db

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
    form = PitchForm()
    return render_template('general.html', pitch_form=form)

@main.route('/career')
def career():
    '''
    Function that returns the career category page
    '''
    form = PitchForm()
    return render_template('career.html', pitch_form=form)

@main.route('/business')
def business():
    '''
    Function that returns the business category page
    '''
    form = PitchForm()
    return render_template('business.html', pitch_form=form)

@main.route('/technology')
def technology():
    '''
    Function that returns the technology category page
    '''
    form = PitchForm()
    return render_template('technology.html', pitch_form=form)

@main.route('/science')
def science():
    '''
    Function that returns the science category page
    '''
    form = PitchForm()
    return render_template('science.html', pitch_form=form)


@main.route('/write_pitch',methods = ["GET", "POST"])
@login_required
def write_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        new_pitch = Pitch(title=title,body=body)
        new_pitch.save_pitch()
        return redirect(url_for('main.pitch'))
    title = "Create a Pitch"
    return render_template('main/pitch.html', title=title, pitch_form=form)

@main.route('/write_comment', methods = ["GET", "POST"])
@login_required
def write_comment():
    comment_form = CommentForm()
    pitch = Pitch.query.filter_by(id=id).first()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(pitch_id=pithc_id, comment=comment)
        new_comment.save_comment()
        return redirect(url_for('main.pitch'))

    return render_template('main/pitch.html', comment_form=comment_form)
