CREATE TABLE userdetails(
    Id int AUTO_INCREMENT,
    firstName VARCHAR(10),
    lastName VARCHAR(10),
    email VARCHAR(30),
    password VARCHAR(30),
    PRIMARY KEY(Id)
);

SELECT * FROM userdetails 
WHERE id = id;

INSERT INTO userdetails(firstName, lastName, email, password)
VALUES("Rakib","Ayon","ayonrakib@gmail.com","*****");

SELECT email, Id FROM userdetails;

SELECT * FROM userdetails WHERE
email = %s;

UPDATE userdetails
SET firstName = "rakib"
WHERE
email = 'ayonrakib@gmail.com';
