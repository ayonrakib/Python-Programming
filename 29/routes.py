from flask import Flask, request, render_template, make_response, redirect, url_for, Response
import hashlib, binascii, peewee, mysql.connector as mysql
from library.DatabaseConnection import DatabaseConnection
from model.User import User
from controller.UserController import UserController

app = Flask("twentynine",template_folder='templates', static_folder='',static_url_path='/')
userController = UserController()

@app.route('/')
def welcomeScreen():
    return render_template('welcomeScreen.html')


# eikhane, duita different route er jonno eki function execute hocche.
# /login, /login/... eirokom duita pailei ei login function execute kore
# /login/... eikhane jai thakbe, loginfailed er moddhe save korbe.
@app.route('/login')
@app.route('/login/<loginfailed>')
def login(loginfailed = ""):
    currentSessionCookie = request.cookies.get('currentSessionCookie')
    if currentSessionCookie is not None:
        return redirect(url_for('homePage'))
    loginForm = render_template('loginForm.html',
                                action = "authenticate",
                                loginfailed = loginfailed,
                                pageHeader = "Log In",
                                buttonValue = "Log In")
    return loginForm


@app.route('/authenticate', methods = ['POST','GET'])
def authenticateUser():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if userController.authenticate(email, password):
            homePage = make_response(redirect(url_for('homePage',
                                     action = "playgame",
                                     pageHeader = "Click button to start game",
                                     buttonValue = "Start Game")))
            homePage.set_cookie('currentSessionCookie', userController.createCurrentUserSessionCookie(email))
            homePage.set_cookie('email', email)
            return homePage
        return redirect(url_for('login', loginfailed = "login failed"))
        

@app.route('/userregistration')
@app.route('/userregistration/<userFound>')
def newUserRegistration(userFound = ""):
    return render_template('userRegistration.html',
                            action = "validateregistration",
                            pageHeader = "Register",
                            buttonValue = "Register",
                            userFound = userFound)


@app.route('/validateregistration', methods = ['POST','GET'])
def validateRegistration():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        try:
            if userController.getUserWithEmail(email):
                return redirect(url_for('newUserRegistration',userFound = "User Found"))
        except peewee.DoesNotExist:
            homePage = make_response(redirect(url_for('homePage',
                                     action = "playgame",
                                     pageHeader = "Click button to start game",
                                     buttonValue = "Start Game")))
            homePage.set_cookie('currentSessionCookie', userController.createCurrentUserSessionCookie(email))
            homePage.set_cookie('email', email)
            return homePage


@app.route('/homepage')
def homePage():
    currentSessionCookie = request.cookies.get('currentSessionCookie')
    email = request.cookies.get('email')
    # print(userController.getUserId(email))
    if currentSessionCookie is not None:
        return render_template('homePage.html',
                                action = "playgame",
                                pageHeader = "Click button to start game",
                                buttonValue = "Start Game")
    return redirect(url_for('login'))


@app.route('/playgame', methods = ['POST', 'GET'])
def playGame():
    currentSessionCookie = request.cookies.get('currentSessionCookie')
    if currentSessionCookie is None:
        return redirect(url_for('login'))
    if request.method == 'POST':
        return render_template('29.html',
                                playerId = userController.getUserId(request.cookies.get('email')))


@app.route('/logout')
def logout():
    email = request.cookies.get('email')
    userController.updateCurrentUserSessionCookie(email, "")
    loginForm = make_response(redirect(url_for('login')))
    loginForm.set_cookie('currentSessionCookie', expires = 0)
    return loginForm


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)