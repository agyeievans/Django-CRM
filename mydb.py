import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE django_CRM")

print("Database created successfully........")