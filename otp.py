from flask import Blueprint,jsonify,request
import sys
sys.path.insert(0, 'ola\config')
from database import mydb
from flask_mysqldb import MySQL
import path
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import os
import math
import random
import smtplib
from jinja2 import Environment, FileSystemLoader
import json



mycursor=mydb.cursor(buffered=True , dictionary=True)


#app routing @app.route('url') - maps specific url to the specific function that handles the logic for that url

create = Blueprint('create', __name__)

@create.route(path.create,methods=['POST'])#route function
def create_ps():
   digits="123456789"
   OTP=""
   for i in range(4):
    OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
   req_data=request.get_json()
   sql="SELECT * FROM customer_registration WHERE email=%s and authentication=1"
   val=(req_data['email'],)
   mycursor.execute(sql,val)
   myresult = mycursor.fetchall()
   if len(myresult)!=0 :
    return jsonify(myresult,{'message':'already registered fill the registration form'})

  
   sql = "DELETE FROM customer_registration WHERE email = %s"
   val=(req_data['email'],)
   mycursor.execute(sql,val)
   sql = "INSERT INTO customer_registration(email, created_time, otp,authentication) VALUES (%s, current_timestamp,%s,0)"
   val=(req_data['email'],OTP)
   mycursor.execute(sql, val)
   mydb.commit()
   sender_email = "abishek@twilightsoftwares.com"
   receiver_email =  req_data['email']
   password = "task111999"
   msg = MIMEMultipart("alternative")
   msg["Subject"] = "OTP for OLA customer registration"
   msg["From"] = sender_email
   msg["To"] = receiver_email
   filename = "document.pdf"
   HTMLFile = open("ola/config/email.html", "r")
   index = HTMLFile.read()
   part = MIMEText(index, "html")
   msg.attach(part)
   x=msg.as_string()
   y=Template(x)
   z=y.substitute({'content':OTP})
   context = ssl.create_default_context()
   
   with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email,z
    )
   sql="SELECT * FROM customer_registration WHERE email=%s "
   val=(req_data['email'],)
   mycursor.execute(sql,val)
   mydb.commit()
   myresult = mycursor.fetchall()
   return jsonify(myresult,{'message':'Password has sent to your mail id'})
