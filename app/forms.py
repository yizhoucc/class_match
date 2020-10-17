from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional, Length

class RegisterForm(FlaskForm):
    login_name=StringField('class_id', validators=[DataRequired()])
    login_pass=StringField('class_id', validators=[DataRequired()])

    class_id=StringField('class_id', validators=[DataRequired()])
    class_session =StringField('class_session')
    last_name =StringField('last_name', validators=[DataRequired()])
    first_name =StringField('first_name', validators=[DataRequired()])
    edu_addr =StringField('edu_addr', validators=[DataRequired()])
    interests=StringField('interests')
    bio =StringField('bio')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('submit')


class RegForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    eduaddr = StringField('eduaddr', validators=[DataRequired()])
    submit = SubmitField('submit')


class ProfileForm(FlaskForm):
    first_name=StringField("firstname df: ", validators=[Optional(), Length(0, 255)])
    last_name=StringField("lastname df: ", validators=[Optional(), Length(0, 255)])
    bio=StringField("bio df: ", validators=[Optional(), Length(0, 255)])
    submit = SubmitField('submit')



class ClassForm(FlaskForm):
    class1=StringField("class1: ", validators=[Optional(), Length(0, 255)])
    class2=StringField("class2: ", validators=[Optional(), Length(0, 255)])
    class3=StringField("class3: ", validators=[Optional(), Length(0, 255)])
    submit = SubmitField('submit')




#     wxid = StringField('Enter his/her Wechat ID', validators=[DataRequired()])
#     lastname = StringField('Enter his/her Last Name in English', validators=[DataRequired()])
#     submit = SubmitField('search now')

# class InputForm(FlaskForm):

#     # 2nd part
#     mywxid=StringField('Enter your Wechat ID', validators=[DataRequired()])
#     mylname= StringField('Enter your Last Name in English', validators=[DataRequired()])
#     app1=StringField('App name', validators=[DataRequired()])
#     id1=StringField('id number friend code', validators=[DataRequired()])
#     app2=StringField('App name')
#     id2=StringField('id number friend code')
#     app3=StringField('App name')
#     id3=StringField('id number friend code')
#     submit2 = SubmitField('build your record now')


