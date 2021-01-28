# User
# constructor: firstName, lastName, email, password
# method: getname, setname
class User():
    def __init__(self,firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password


    def __str__(self):
        return f"The first name of the user is {self.firstName}, last name is {self.lastName}, email is {self.email}."


    def getFirstName(self):
        return self.firstName


    def getlastName(self):
        return self.lastName

    
    def getEmail(self):
        return self.email


    # def getPassword(self):
    #     return self.password

        
    def setFirstName(self, firstName):
        self.firstName = firstName


    def setLastName(self, lastName):
        self.lastName = lastName


    def setEmail(self, email):
        self.email = email


    def setPassword(self, password):
        self.password = password

    