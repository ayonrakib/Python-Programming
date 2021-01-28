CREATE TABLE Message(
    id INT NOT NULL AUTO_INCREMENT,
    receiverId INT NOT NULL,
    senderId INT NOT NULL,
    message VARCHAR(50),
    PRIMARY KEY(id),
    FOREIGN KEY(receiverId) REFERENCES User(id),
    FOREIGN KEY(senderId) REFERENCES User(id)
);