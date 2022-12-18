from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, Regexp


class DataForm(FlaskForm):

    age = StringField(label='Age')
    Gender = StringField(label='Gender')
    ChestPain = StringField(label='Chest Pain')
    cholestrol = StringField(label='Cholestrol')
    restecg = StringField(label='resting ectocardiograph results')
    exng = StringField(label='excersize induced angina')
    thall = StringField(label='thalassemia')
    oldpeak = StringField(label='oldpeak')
    submit = SubmitField(label='Create Account')
