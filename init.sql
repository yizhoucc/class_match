
CREATE DATABASE IF NOT EXISTS class_match;
use class_match;


CREATE or REPLACE TABLE user_login(
    user_id int UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    login_name varchar(20) NOT NULL,
    login_pass char(32) NOT NULL,
    login_status TINYINT NOT NULL default 0,
    modify_time TIMESTAMP not NULL DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);

CREATE or REPLACE TABLE userinfo(
    user_info_id int UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    user_id int UNSIGNED NOT NULL ,
    last_name varchar(16),
    first_name varchar(32),
    edu_addr varchar(32)  NOT NULL,
    interests ENUM('card_game','party','music'),
    bio text,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);


CREATE or REPLACE TABLE class_info(
    entry_id int UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    class_id varchar(32) NOT NULL, 
    class_session int not null default 0,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE or REPLACE TABLE class_students(
    class_student_id int UNSIGNED NOT NULL AUTO_INCREMENT primary key,
    entry_id int UNSIGNED NOT NULL,
    user_id int UNSIGNED NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
);