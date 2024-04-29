from flask import render_template, url_for, flash, redirect, request
from . import create_app, db
from .forms import UserForm
from .models import User

app = create_app()

@app.route("/", methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, segment_id=form.segment_id.data)
        db.session.add(user)
        db.session.commit()
        flash('User added to segment!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route("/add_user", methods=['POST'])
def add_user():
    # Additional functionality if needed
    return redirect(url_for('index'))
