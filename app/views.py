"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.security import generate_password_hash, check_password_hash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/secure-page')
def secure_page():
    return render_template('secure_page.html')

@app.route('/profile', methods=['GET','POST'])
def add_profile():
    """Either (GET) provide profile form or (POST) create the profile"""
    form = ProfileForm()
    if form.validate_on_submit():
        # Get values from form
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        email = request.form['email']
        location = request.form['location']
        bio = request.form['bio']
        prof_pic = request.form['photo']
        pp_filename = secure_filename(prof_pic.filename)
        try:
            """Idea for now: need to save the picture, and save the filename. Store items to database"""
            flash('User successfully created', 'success')
            return redirect(url_for('view_profiles'))
        except:
            flash("User could not be created", 'danger')
    return render_template('add_profile.html', form = form)

@app.route('/profiles')
def view_profiles():
    """Retrieve all profiles from the database, then display them"""
    return render_template("view_profiles.html")

@app.route('/profile/<userid>')
def view_profile(userid):
    """Query database for complete user info for id, then pass to a template to render the info"""
    return "in progress fam"

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
