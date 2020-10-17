
import pymysql
import configparser
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import json
import uuid

config = configparser.ConfigParser()
config.read(r'/home/maliao/.dbconfig')
dbconf=dict(config.items('class_match'))


def valid_pass(info_dict,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `login_pass` from user_login where `login_name`=%s; "
            cursor.execute(sql, (info_dict['login_name']))
            result = cursor.fetchone()   
    finally:
        connection.close()
    if info_dict['login_pass']==result['login_pass']:
        return True
    else:
        return False


def get_pass(info_dict,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `login_pass` from user_login where `login_name`=%s; "
            cursor.execute(sql, (info_dict['login_name']))
            result = cursor.fetchone()   
    finally:
        connection.close()
    if result is not None:
        return result['login_pass']
    else:
        return None

def check_email(info_dict,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        # check edu addr
        with connection.cursor() as cursor:
            sql = "select `user_id`, `edu_addr` from `userinfo` where `edu_addr`=%s;"
            cursor.execute(sql, (info_dict['edu_addr']))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is None:
        return True

def check_name(info_dict,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `login_name` from `user_login` where `login_name`=%s;"
            cursor.execute(sql, (info_dict['login_name']))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is None:
        return True





def register_user(info_dict,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `user_login` (`login_name`, `login_pass`) values (%s, %s);"
            cursor.execute(sql, (info_dict['login_name'],info_dict['login_pass']))
        connection.commit()
        with connection.cursor() as cursor:
            sql = "select `user_id`,`login_pass` from `user_login` where `login_name`=%s;"
            cursor.execute(sql, (info_dict['login_name']))
            result = cursor.fetchone()
        if info_dict['login_pass']==result['login_pass']:
            with connection.cursor() as cursor:
                sql="INSERT into `userinfo` (`user_id`, `edu_addr`) values (%s, %s);"
                cursor.execute(sql, (result['user_id'],info_dict['edu_addr']))
                connection.commit()
            with connection.cursor() as cursor:
                sql = "select `edu_addr` from `userinfo` where `user_id`=%s;"
                cursor.execute(sql, (result['user_id']))
                result2 = cursor.fetchone()
    finally:
        connection.close()
    if info_dict['edu_addr']==result2['edu_addr']:
        return True
    else:
        return False



def conn(dbconf):
    connection = pymysql.connect(host='localhost',
                                user=dbconf['user'],
                                password=dbconf['password'],
                                db=dbconf['db'],
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection


def dbinsert(connection,info_dict):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `class` (`class_id`, `last_name`, `first_name`, `edu_addr`, `interests`, `bio`) VALUES (%s, %s,%s,%s,%s,%s)"
            cursor.execute(sql, (info_dict['class_id'],info_dict['last_name'],info_dict['first_name'],info_dict['edu_addr'],info_dict['interests'],info_dict['bio'] ))
        connection.commit()
    finally:
        pass
    #     connection.close()

def dbselect(connection):
    try:
        with connection.cursor() as cursor:
                sql = "SELECT `last_name`, `first_name` FROM `class` WHERE `last_name`=%s"
                cursor.execute(sql, ('last'))
                result = cursor.fetchone()
                print(result)
    finally:
        pass
    #     connection.close()

def get_id(login_name, dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `user_id` from `user_login` where `login_name`=%s;"
            cursor.execute(sql, (login_name))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is not None:
        return result['user_id']
    else:
        return None


def get_name(user_id, dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `login_name` from `user_login` where `user_id`=%s;"
            cursor.execute(sql, (user_id))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is not None:
        return result['login_name']
    else:
        return None

def get_info(user_id, dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select * from userinfo where `user_id`=%s;"
            cursor.execute(sql, (user_id))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is not None:
        return result
    else:
        return None

def update_info(form, user_id, dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "update class_match.userinfo set first_name=%s, last_name=%s, bio=%s where user_id=%s;"
            cursor.execute(sql, (form.first_name.data, form.last_name.data, form.bio.data, user_id))
        connection.commit()
        with connection.cursor() as cursor:
            sql = "select * from userinfo where `user_id`=%s;"
            cursor.execute(sql, (user_id))
            result = cursor.fetchone()
    finally:
        connection.close()
        return result

def get_class(user_id, dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `entry_id` from `class_students` where `user_id`=%s;"
            cursor.execute(sql, (user_id))
            result = cursor.fetchall()
    finally:
        connection.close()
    if result is not None:
        return result
    else:
        return None

def is_new_class(form,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `entry_id` from `class_students` where `class_id`=%s;"
            cursor.execute(sql, (form.class_id.data))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is not None:
        return False
    else:
        return True

def new_class(class_code,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "insert into `class_info` (`class_id`) values (%s);"
            cursor.execute(sql, (class_code))
        connection.commit()
    finally:
        connection.close()
    if result is not None:
        return result
    else:
        return None

def get_class_id(class_code,dbconf=dbconf ):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `entry_id` from `class_info` where `class_id`=%s;"
            cursor.execute(sql, (class_code))
            result = cursor.fetchone()
            entry_id=result['entry_id']
    finally:
        connection.close()
    if entry_id is not None:
        return entry_id

def enroll_class(class_code,user_id,dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "select `entry_id` from `class_info` where `class_id`=%s;"
            cursor.execute(sql, (class_code))
            result = cursor.fetchone()
            entry_id=result['entry_id']
        with connection.cursor() as cursor:
            sql = "insert into `class_students` (`entry_id`, `user_id`) values (%s, %s);"
            cursor.execute(sql, (entry_id,user_id))
        connection.commit()
        with connection.cursor() as cursor:
            sql = "select `entry_id`,`user_id` from `class_students` where `user_id`=%s and entry_id=%s;"
            cursor.execute(sql, ((user_id,entry_id)))
            result = cursor.fetchone()
    finally:
        connection.close()
    if result is not None:
        return result
    else:
        return None


def update_class(old_var, new_var, user_id, dbconf=dbconf):
    connection=conn(dbconf)
    try:
        with connection.cursor() as cursor:
            sql = "update class_students set entry_id=%s where user_id=%s and entry_id=%s;"
            cursor.execute(sql, (new_var, user_id, old_var))
        connection.commit()
        with connection.cursor() as cursor:
            sql = "select entry_id from class_students where user_id=%s and entry_id=%s;"
            cursor.execute(sql, (user_id, new_var))
            result = cursor.fetchone()
    finally:
        connection.close()
        return result

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        # self.password_hash = self.get_password_hash()
        self.id = get_id(username, dbconf=dbconf)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # @password.setter
    # def password(self, password):
    #     """save user name, id and password hash to json file"""
    #     self.password_hash = generate_password_hash(password)
    #     with open(PROFILE_FILE, 'w+') as f:
    #         try:
    #             profiles = json.load(f)
    #         except ValueError:
    #             profiles = {}
    #         profiles[self.username] = [self.password_hash,
    #                                    self.id]
    #         f.write(json.dumps(profiles))

    def verify_password(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_password_hash(self):
        return get_pass({'login_name':self.username},dbconf=dbconf)


    @classmethod
    def get(self,user_id):
        try:
            username=get_name(user_id)
            return User(username)
        except:
            return None

