from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Config
from forms import EventForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            event_type=form.event_type.data,
            description=form.description.data,
            date=form.date.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Wydarzenie dodane!')
        return redirect(url_for('index'))
    return render_template('add_event.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Utworzenie tabeli w bazie danych
    app.run(debug=True)
