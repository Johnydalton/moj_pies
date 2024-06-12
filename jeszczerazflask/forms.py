from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SubmitField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    event_type = StringField('Typ wydarzenia', validators=[DataRequired()])
    description = TextAreaField('Opis')
    date = DateTimeField('Data', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    submit = SubmitField('Dodaj wydarzenie')
