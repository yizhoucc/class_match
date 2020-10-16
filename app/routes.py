from flask import render_template, flash, redirect, url_for
from app import app
# from app.forms import InputForm
from app.db import *

# cp
from app.forms import LoginForm
from flask_wtf.csrf import CsrfProtect
from flask import Flask
# from model import User
from flask_login import login_user, login_required
from flask_login import LoginManager, current_user
from flask_login import logout_user
# config
import configparser
config = configparser.ConfigParser()
config.read(r'/home/maliao/.dbconfig')
dbconf=dict(config.items('secret_key'))


app = Flask(__name__)

app.secret_key = dbconf['key']

# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)

# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# csrf protection
csrf = CsrfProtect()
csrf.init_app(app)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_name = request.form.get('username', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        # user = User(user_name, password)
        # if user.verify_password(password):
        #     login_user(user)
        if valid_pass({'login_name':user_name,'login_pass':password}):
            login_user(user)

            return redirect(request.args.get('next') or url_for('main'))
    return render
    

# @app.route('/',methods=['GET', 'POST'])
# def index():
#     form=InputForm()
#     if form.validate_on_submit():




# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))




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