
import pymysql
import configparser
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