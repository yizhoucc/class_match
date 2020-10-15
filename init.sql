
CREATE DATABASE IF NOT EXISTS class_match;
use class_match;


CREATE TABLE IF NOT EXISTS class(
    entry_id int NOT NULL AUTO_INCREMENT primary key,
    class_id varchar(32) NOT NULL, 
    class_session int,
    last_name varchar(16) NOT NULL,
    first_name varchar(32) NOT NULL,
    edu_addr varchar(32)  NOT NULL,
    interests ENUM('card_game','party','music'),
    bio text,
    date_added DATE DEFAULT CURRENT_TIMESTAMP
);

REPLACE table class(   
    entry_id int NOT NULL AUTO_INCREMENT primary key,
    class_id varchar(32) NOT NULL, 
    class_session int,
    last_name varchar(16) NOT NULL,
    first_name varchar(32) NOT NULL,
    edu_addr varchar(32)  NOT NULL,
    interests ENUM('card_game','party','music'),
    bio text,
    date_added DATE DEFAULT CURRENT_TIMESTAMP
);