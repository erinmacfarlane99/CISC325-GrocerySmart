"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from test import app

@app.route('/')
@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
    )

@app.route('/fridge')
def fridge():
    """Renders the about page."""
    return render_template(
        'fridge.html',
        title='Your Fridge',
        year=datetime.now().year,
    )

@app.route('/consumption')
def consumption():
    """Renders the about page."""
    return render_template(
        'consumption.html',
        title='Your Weekly Consumption',
        year=datetime.now().year,
    )

@app.route('/notifications')
def notifications():
    """Renders the about page."""
    return render_template(
        'notifications.html',
        title='Notifications',
        year=datetime.now().year,
    )

@app.route('/scan')
def scan():
    """Renders the about page."""
    return render_template(
        'scan.html',
        title='Upload Your Groceries',
        year=datetime.now().year,
    )