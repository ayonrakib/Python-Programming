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
app = Flask("userRegistration",
            static_url_path='/static', 
            static_folder='static')


# html code
# input: headBlock, bodyBlock
# return: string of html code
# method:
#   headCodeBlock = "" and bodyCodeBlock = "" by default
#   formatted string of default html format
#   {} on head block and body block
#   return formatted string
def getHTMLCodeBlock(headCodeBlock="",bodyCodeBlock="", headClass = "", bodyClass = ""):
    return f"""
    <!DOCTYPE html>
            <html>
                <head class = {headClass}>
                    {headCodeBlock}
                </head>
                <body class = {bodyClass}>
                    {bodyCodeBlock}
                </body>
            </html>
    """ 


# redirection function
# input: string
# return: string
# method:
#   common redirect format with the customized {} format to insert string.
#   all {} will contain the sent string.
#   return the string
def getRedirectHTML(redirectString):
    headCodeBlock = f"""
            <title>
                Html Meta tag
            </title>
            <meta http-equiv="refresh" content="0;url={redirectString}" />
    """
    bodyCodeBlock = ""
    HTMLCodeForRedirect = getHTMLCodeBlock(headCodeBlock, bodyCodeBlock)
    return HTMLCodeForRedirect


# method: get login form
# input: none
# return: multi line string with html
# method:
#   generate formatted multi line string with html code which creates a form
def getLoginForm(userNotAuthenticatedError = "", emailError="", passwordError="", storedEmail = ""):
    headCodeBlock = f"""
                <div>
                    <link rel="stylesheet" type="text/css" href="/static/designFile.css">
                </div>
    """
    bodyCodeBlock = f"""
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
    """
    bodyClass = f"LoginForm"
    HTMLCodeForLoginForm = getHTMLCodeBlock(headCodeBlock, bodyCodeBlock,"",bodyClass)
    return HTMLCodeForLoginForm


# method:
# input: email, password
# return: based on following conditions:
# if email and password both empty string:
#   return multi line string of an html log in form
# if email empty:
#   return multi line string of an html log in form
# if password empty:
#   return multi line string of an html log in form
# if both valid string:
#   return multi line string of an html log in form


# email, password nibe form theke.
# redirect korbe login e jodi button click kori.
@app.route('/modelApplication')
def modelApplication():
    headCodeBlock = f"""
        <link rel="stylesheet" type="text/css" href="/static/designFile.css">
    """
    bodyCodeBlock = f"""
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
    """
    HTMLCodeForModelApplication = getHTMLCodeBlock(headCodeBlock, bodyCodeBlock)
    return HTMLCodeForModelApplication


@app.route('/aboutus')
def aboutUs():
    bodyCodeBlock = "Hello! This is a model application."
    HTMLCodeForAboutUsSection = getHTMLCodeBlock("",bodyCodeBlock)
    return HTMLCodeForAboutUsSection


# email and password cookie get korbe server.
# jodi kono ekta field empty paay, taile oi field ta empty string hishebe cookie boshabo.
# jeivabei entry dik na keno user, ami sob field send korbo authenticate url e.
# jodi submit e click kori, jabe authentication url e.


# task1: getlogin form sob khane use korbo
# task2: email likhe password na likhleo store kore rakhbe email
@app.route('/login')
def loginPage():
    loginHtml = getLoginForm("","","","")
    return loginHtml


# username: ayon@gmail.com, pass: rakibayon
# user name er jaygay email likhte hobe sob jaygay, eita ke bole disinformation. ami use korsi email, username na. DONE
# so, ami username use korte parbo na. email likhte hobe. DONE
# password hashing ta usercontroller er method er vitore hobe, baire na. DONE
# store cookie for empty email and empty password.
# ekta app route e ektai method thakbe, oitai execute hobe.
# oi method execute hoile baki gula hobe na.
# so, one app route e ekta method thakbe.


# pseudocode of authenticate:
# login er porei authenticate e ashbe.
# email and password field form theke nibe.
# jodi duitai empty hoy, redirect kore duitai chabe.
# jodi email empty hoy, redirect kore email chabe.
# credential check korbe.
# jodi authenticated hoy:
#   cookie set korbo.
#   redirect korbo homepage e
# redirect korbo login page e.
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
        

@app.route('/homePage')
def homePage():
    bodyCodeBlock = """
            <div>
                Hello. This is the home page.
            </div>
            <br> <br>
            <div>
                <form action="/logout">
                    <input type="submit" value="Logout">
                </form>
            </div>
    """
    HTMLCodeBlockForSuccessfulAuthentication = getHTMLCodeBlock("", bodyCodeBlock)
    return HTMLCodeBlockForSuccessfulAuthentication


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