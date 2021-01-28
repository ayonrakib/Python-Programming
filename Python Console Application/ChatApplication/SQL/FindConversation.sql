SELECT message 
FROM message 
WHERE (receiverId = 7 AND senderId = 5) 
OR (receiverId = 5 AND senderId = 7);

SELECT * FROM message 
WHERE id = %s 
and 
isDeleted = 0