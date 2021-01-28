UPDATE message
SET isDeleted = 1
WHERE id = messageNumber;

UPDATE message
SET message = newMessage
WHERE id = id;