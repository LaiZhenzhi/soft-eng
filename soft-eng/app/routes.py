from flask import render_template,flash,redirect,url_for,session,request,g
from app import app,db,admin
from flask_admin.contrib.sqla import ModelView
from app.forms import AccountForm,DataForm,RegisterForm
from app.models import Account,Data
import datetime
from sqlalchemy import or_
from flask_login import current_user,login_user,logout_user,login_required

@app.route('/',methods=['GET','POST'])

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('data',username=current_user.username))

    form = AccountForm()

    if request.method == 'POST' and form.validate_on_submit():
        account = Account.query.filter_by(username=form.username.data).first()
        if account is None or not account.check_password(form.password.data):
            flash('no such user or wrong password')
            return redirect(url_for('login'))
        login_user(account,remember=form.remember_me.data)
        return redirect(url_for('data',username=account.username))
    return render_template('login.html',title='login',form=form)

@app.route('/a')
def a():
    return render_template('1.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logout successfully!')
    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('data'))

    form = RegisterForm()

    if form.validate_on_submit():
        account = Account(username=form.username.data)
        account.set_password(form.password.data)
        db.session.add(account)
        db.session.commit()
        flash('Welcome! You have been the new user!')
        return redirect(url_for('login'))
    return render_template('register.html',title='register a new account',form=form)

@app.route('/data/<username>',methods=['GET','POST'])
@login_required
def data(username):
    all_data = Data.query.all()
    return render_template('data.html',title='data',all_data=all_data)

@app.route('/data/<username>/add',methods=['GET','POST'])
@login_required
def add(username):
    form = DataForm()
    if form.validate_on_submit():
        new = Data(content=form.content.data)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('data',username=username))
    return render_template('add.html',title='add',form=form)

@app.route('/data/<username>/delete/<id>',methods=['GET','POST'])
@login_required
def delete(username,id):
    dele = Data.query.get(id)
    db.session.delete(dele)
    db.session.commit()
    return redirect(url_for('data', username=username))