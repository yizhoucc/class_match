from flask import render_template, flash, redirect, url_for, request, Response
from app import app
# from app.forms import InputForm
from app.db import *
# import requests
from werkzeug.datastructures import MultiDict
# # cp
from app.forms import *
from flask_wtf.csrf import CsrfProtect
# from flask import Flask

from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user
# # config
import configparser
config = configparser.ConfigParser()
config.read(r'/home/maliao/.dbconfig')
dbconf=dict(config.items('secret_key'))


# app = Flask(__name__)

app.secret_key = dbconf['key']

# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

# reload User object
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# # csrf protection
csrf = CsrfProtect()
csrf.init_app(app)

# # @app.route('/')
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user_name = request.form.get('username', None)
#         password = request.form.get('password', None)
#         remember_me = request.form.get('remember_me', False)
#         # user = User(user_name, password)
#         # if user.verify_password(password):
#         #     login_user(user)
#         if valid_pass({'login_name':user_name,'login_pass':password}):
#             login_user(user)

#             return redirect(request.args.get('next') or url_for('main'))
#     return render_template('base.html',  title='Sign In', form=form)
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if valid_pass({'login_name':form.username.data,'login_pass':form.password.data}):
            user = User(form.username.data)
            login_user(user)
            flash('your name：{}，login sucess'.format(form.username.data))
        else:
            flash('!!! wrong pass')
        # return redirect(request.args.get('misc'))
        return redirect(url_for('misc'))
    return render_template('login.html',  title='Sign In', form=form)



@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('!!! loged out')
    return redirect(url_for('login'))


@app.route('/')
# @app.route('/index')
@login_required
def index():
    user = {'username': current_user.username}
    return render_template('index.html', title='Home', user=user)

@app.route('/my_class')
@login_required
def userclass():    
    flash('!!!my_class')
    user = {'username': current_user.username}
    infodict=get_class(current_user.id)
    num_class=len(infodict)
    flash(infodict)

    if request.method == 'GET':
        form=ProfileForm(formdata=MultiDict(infodict))   
    else:
        form = ProfileForm()

    if form.validate_on_submit():
        if is_new_class(form.class_id.data):
            new_class(form.class_id.data) # record new class to db
        total=3
        i=0
        while i < (num_class):
            result=update_info(form,current_user.id)
            flash('updated, current profile:')
            flash(result)
            i+=1
        while i < total:
            enroll_class(class_code[i],current_user.id)
            i+=1
    return render_template('userclass.html', title='my info',form=form)



@app.route('/my_profile',methods=['GET', 'POST'])
@login_required
def userinfo():    
    flash('!!!my_profile')
    user = {'username': current_user.username}
    infodict=get_info(current_user.id)
    # flash(infodict)

    if request.method == 'GET':
        form=ProfileForm(formdata=MultiDict(infodict))   
    else:
        form = ProfileForm()

    if form.validate_on_submit():
        result=update_info(form,current_user.id)
        flash('updated, current profile:')
        flash(result)
    return render_template('userinfo.html', title='my info',form=form)


@app.route('/my_classmates')
@login_required
def class_match():    
    flash('!!!my_classmates')
    user = {'username': current_user.username}
    return render_template('base.html', title='secrete')


@app.route('/misc')
@login_required
def misc():  
    user = {'username': current_user.username}
    flash('!!!adfasdf')
    flash('!!!adfasdf')
    flash('!!!adfasdf')
    flash('!!!adfasdf')
    return render_template('base.html', title='secrete')


@app.route('/register',methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        # send link to addr.
        infodict={'login_name':form.username.data,'login_pass':form.password.data, 'edu_addr':form.eduaddr.data}
        if check_email(infodict):
            if check_name(infodict):
                register_user(infodict)
                flash('registered')
            else:
                flash('name taken')
        else:
            flash('email already registered')
    return render_template('reg.html',  title='Register', form=form)








# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     # flash('search')
#     form = SearchForm()
#     if form.validate_on_submit():
#         # do xx xhere to sql
#         data=db.searchdb(form, mydb)
#         flash('Only [Wechat ID] and [Last Name] BOTH match our records, you can get what you want:')
#         for  i in (data):

#                 for index, j in enumerate(i):
#                     if index>2:
#                         if j !='':
#                             flash(j)

#     return render_template('search.html',  title='2 In', form=form)

# @app.route('/input', methods=['GET', 'POST'])
# def inputdata():
#     # flash('input')
#     form = InputForm()
#     if form.validate_on_submit():
#         # do xx xhere to sql
#         data=db.insertion(form, mydb)
#         flash('SUCCESS! We recorded following infomation:')
#         for i in (data):
#             if i !='':
#                 flash(i)


#     return render_template('input.html',  title='3 In', form=form)

# @app.route('/',methods=['GET', 'POST'])
# def index():
#         # flash('input')
#     form = InputForm()
#     if form.validate_on_submit():
#         # do xx xhere to sql
#         data=db.insertion(form, mydb)
#         flash('SUCCESS! We recorded following infomation:')
#         for i in (data):
#             if i !='':
#                 flash(i)
#     return render_template('input.html',  title='3 In', form=form)