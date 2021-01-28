CREATE DATABASE imageupload;
USE imageupload;
CREATE TABLE imageTracking
(
	id int NOT NULL auto_increment,
    userId int NOT NULL auto_increment,
    userName varchar(50) NOT NULL,
    imageId int NOT NULL auto_increment,
    imageName varchar(255) NOT NULL,
    email varchar(30) NOT NULL,
    password varchar(255) NOT NULL,
    primary key (userId)
);
