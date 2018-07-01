from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from ..models import Pitch, Comment

class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    body = TextAreaField('Enter your Pitch here')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment here')
    submit = SubmitField('Submit')    
