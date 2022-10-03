import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Task@111999",
  database="ola"
)
#connection helps to talk to server whether it is in same machine or not