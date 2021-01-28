from flask import Flask, request
from flask import make_response
from User import User
from UserController import UserController
import mysql.connector as mysql
import hashlib, binascii


connection = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hahaha01670",
    auth_plugin='mysql_native_password',
    database = "userregistration"
)

userController = UserController(connection)

# static_url_path = jodi base url er pore /static paay, taile oi url kono function process/handle/execute korbe na,
# oi static_folder e jabe and file er naam match kore file pathabe
 
app = Flask("userRegistration",
            static_url_path='/static',  
            static_folder='static')


def buttonHTML(redirectHTML, buttonString):
    return f"""
    	<input type="button" value="{buttonString}" 
    onclick="window.location='{redirectHTML}';" />
    """


# header html
# input: string
# return: string
# method:
#   start from <!DOCTYPE HTML> to </head>
#   input as parameter
#   send formatted string
def headHTML(headCodeBlock, bodyClass=""):
    return f"""
        <!DOCTYPE html>
            <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="/static/designFile.css">
                    {headCodeBlock}
                </head>
            <body class = {bodyClass}>
    """


# nav html
# input: string
# return: string
# method:
#   start from <body> to </body>
#   input as parameter
#   send formatted string
def navHTML(bodyCodeBlock, bodyClass=""):
    return f"""
                    {bodyCodeBlock}
    """


# footer html
# input: none
# return: string
# method:
#   start from </body> to </html>
#   return string
def footerHTML():
    return """
            </body>
            </html>
    """


def getLoginForm(userNotAuthenticatedError = "", emailError="", passwordError="", storedEmail = ""):
    headCodeBlock = headHTML("","LoginForm") 
    bodyCodeBlock = navHTML(f"""
                <div>
                    {userNotAuthenticatedError}
                </div>
                <div>
                    <form action="/authenticate" method="POST">
                        Please insert the email and password:<br> <br>
                        <label for="email">Email:</label> <br>
                        <input type="text" id="email" name="email" value="{storedEmail}"> {emailError} <br>
                        <label for="pwd">Password:</label><br>
                        <input type="password" id="pwd" name="pwd" minlength="6"> {passwordError} <br><br>
                        <input type="submit" value="Submit">
                    </form>
                </div>
    ""","LoginForm")  
    return headCodeBlock + bodyCodeBlock + footerHTML()


def getRedirectHTML(redirectString):
    headCodeBlock = headHTML(f"""
            <title>
                Html Meta tag
            </title>
            <meta http-equiv="refresh" content="0;url={redirectString}" />
    ""","") 
    bodyCodeBlock = navHTML("","") 
    HTMLCodeForRedirect = headCodeBlock + bodyCodeBlock + footerHTML()
    return HTMLCodeForRedirect


@app.route('/modelApplication')
def modelApplication():
    htmlForModelApplicationURL = headHTML("","") + navHTML(f"""
            <div>
                Hello. This is the default home page for everyone to see.
            </div>
            <br> <br>
            <div>
                <ul class = "modelApplicationUl">
                    <li class = "modelApplicationLi"><a class="modelApplicationLiA" href="/modelApplication">Home</a></li>
                    <li class = "modelApplicationLi"><a class="modelApplicationLiA" href="/aboutus">About Us</a></li>
                    <li class = "modelApplicationLi"><a class="modelApplicationLiA" href="/login">Log in</a></li>
                </ul>
            </div>
    ""","")+footerHTML()
    return htmlForModelApplicationURL


@app.route('/aboutus')
def aboutUs():
    htmlForAboutUs = headHTML("","") + navHTML("Hello! This is a model application.","")+footerHTML()
    return htmlForAboutUs


@app.route('/login')
def loginPage():
    HTMLCodeForLoginForm = getLoginForm()
    return HTMLCodeForLoginForm


@app.route('/authenticate', methods = ['POST','GET'])
def authenticate():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        if email == "" and password == "":
            emailError = "*Please insert valid email."
            passwordError= "*Please insert valid password."
            loginForm = getLoginForm("", emailError, passwordError)
            return loginForm


        if email == "":
            emailError = "*Please insert valid email."
            loginForm = getLoginForm("", emailError)
            return loginForm


        if password == "":
            passwordError= "*Please insert valid password."
            loginForm = getLoginForm("", "", passwordError, email)
            return loginForm
            

        isUserAuthenticated = userController.authenticateUser(email, password)
        if isUserAuthenticated:
            successfulAuthenticationURL = "http://127.0.0.1:5000/authenticationsuccessful"
            response = make_response(getRedirectHTML(successfulAuthenticationURL))
            response.set_cookie('email',email)
            response.set_cookie('password',password)
            return response


        failedAuthenticationURL = "http://127.0.0.1:5000/authenticationfailed"
        authenticationFailed = getRedirectHTML(failedAuthenticationURL)
        return authenticationFailed
        

@app.route('/authenticationfailed')
def authenticationFailed():
    userNotAuthenticatedError = "The email or password does not match."
    loginForm = getLoginForm(userNotAuthenticatedError, "", "")
    return loginForm


@app.route('/authenticationsuccessful')
def authenticationSuccessful():
    # cookieEmail = request.cookies.get('email')
    # cookiePassword = request.cookies.get('password')
    homePageURL = "http://127.0.0.1:5000/homePage"
    homePage = getRedirectHTML(homePageURL)
    return homePage


@app.route('/homePage', methods = ['POST','GET'])
def homePage():
    cookiePassword = request.cookies.get('password')
    cookieEmail = request.cookies.get('email')
    homePageData = headHTML("","") + navHTML(f"""
        <div>
                    Hello. This is the home page.
                </div>
                <br> <br>
                <div>
                    <form action="/editprofile">
                        <input type="submit" value="Edit Profile">
                    </form> <br> <br>
                    <form action="/logout">
                        <input type="submit" value="Logout">
                    </form> 

                </div>
        """) + footerHTML()
    if cookieEmail is None or cookiePassword is None:
        return getRedirectHTML("http://127.0.0.1:5000/login")
    return homePageData


@app.route('/profile')
def profile():
    resultSetForAllUserId = userController.getAllUserId()
    resultString = "<br>"
    for result in resultSetForAllUserId:
        resultString += str(result[0]) + ": " + str(result[1]) + "<br>"
    publicProfilePageHTML = headHTML("",f"profilePage") + navHTML(f"""
            """) + footerHTML()
    return publicProfilePageHTML


# get user data from user controller
# show all data
# present a form to edit data
# all form is not required, if empty, dont update
@app.route('/editprofile')
def editProfile():
    email = request.cookies.get('email')
    if email is None:
        return getRedirectHTML("http://127.0.0.1:5000/login")
    authenticatedUserDataInTuple = userController.getAllUserData(email)
    id = authenticatedUserDataInTuple[0]
    firstName = authenticatedUserDataInTuple[1]
    lastName =  authenticatedUserDataInTuple[2]
    email = authenticatedUserDataInTuple[3]
    userDescription = userController.getDescription(email)
    buttonHTMLforCancellingInput = buttonHTML("http://127.0.0.1:5000/homePage","Cancel")
    editProfilePageHTML = headHTML("","profilePageBackground") + navHTML(f"""
            <div>
                <ul class = "profilePageUl">
                    <li class = "profilePageLi"><a class="profilePageLiA" href="/modelApplication">Model Application</a></li>
                    <li class = "profilePageLi"><a class="profilePageLiA" href="/modelApplication">Home</a></li>
                    <li class = "profilePageLi"><a class="profilePageLiA" href="/aboutus">About Us</a></li>
                    <li class = "profilePageLi"><a class="profilePageLiA" href="/login">Log in</a></li>
                </ul>
            </div>
            <br> <br>

    <br> <br>
    <div class="row">
        <div class="column" >
            <img class="profilePicture" src="/static/profilePicture.png">
        </div>
        <div class="column">
            <div>
                Please edit the name you want to modify. Keep it unchanged if you want to keep it fixed:
                <form action="/datachanged" method="POST">
                    <br> <br>
                    <label for="firstName">First Name:</label> <br>
                    <input type="text" id="firstName" name="firstName" value = "{firstName}"><br><br>
                    <label for="lastName">Last Name:</label> <br>
                    <input type="text" id="lastName" name="lastName" value="{lastName}"><br><br>
                    <textarea rows="3" cols="25">{userDescription}
                    </textarea>
                    <div class= "logoRow">
                        <img class="logo logoColumn", src="/static/ping.png">
                        <div class = "logoColumnWithPadding">
                            Location:    <input type="text" id="location" name="location" value="{lastName}">
                        </div>
                    </div>
                    <div class= "logoRow">
                        <img class="logo logoColumn", src="/static/linkedin.png">
                        <div class = "logoColumnWithPadding">
                            LinkedIn:    <input type="text" id="linkedin" name="linkedin" value="{lastName}">
                        </div>
                    </div>
                    <div class= "logoRow">
                        <img class="logo logoColumn", src="/static/website.png">
                        <div class = "logoColumnWithPadding">
                            LinkedIn:    <input type="text" id="website" name="website" value="{lastName}">
                        </div>
                    </div>
                    <input type="submit" value="Submit">
                    {buttonHTMLforCancellingInput}
                </form>
                
            </div>
        </div>
    </div>

    """) + footerHTML()
    return editProfilePageHTML


@app.route('/datachanged', methods = ['POST','GET'])
def dataChanged():
    if request.method == 'POST':
        email = request.cookies.get('email')
        if email is None:
            return getRedirectHTML("http://127.0.0.1:5000/login")
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userController.changeUserName(firstName, lastName, email)
        userData = userController.getAllUserData(email)
        return str(userData)



@app.route('/logout')
def logOut():
    successfulLogoutURL = "http://127.0.0.1:5000/login"
    response = make_response(getRedirectHTML(successfulLogoutURL))
    response.set_cookie('email','',0)
    response.set_cookie('password','',0)
    return response


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug = True)



# html e newline bole kisu nai. string return korsi dekhe notun notun line hoy nai.
# sob page e menu bar thakbe. emon ki public profile page eo menu bar thakbe.
# footer e copyright, private eisob dibo.
# head er moddhe div thakbe na.