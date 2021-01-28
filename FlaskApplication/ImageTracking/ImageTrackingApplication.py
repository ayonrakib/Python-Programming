from flask import Flask, request, make_response
import mysql.connector as mysql
import hashlib, binascii
import peewee

userDatabaseConnection = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Hahaha01670",
    auth_plugin = "mysql_native_password",
    database = ""
)

imageDatabaseConnection = mysql.connect(
    host = "locahost",
    user = "root",
    passwd = "Hahaha01670",
    auth_plugin = "mysql_native_password",
    database = ""
)


