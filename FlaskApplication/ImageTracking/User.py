class User():
    def __init__(self, name, email, password):
        self.name = name
        self. email = email
        self.password = password


    def __str__(self):
        return f"The name of the user is {self.name} and the email is {self.email}"


    def getName(self):
        return self.name

    
    def getEmail(self):
        return self.email


    def setEmail(self, email):
        self.email = email


    def setPassword(self, password):
        self.password = password