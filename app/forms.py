from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

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
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')




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


