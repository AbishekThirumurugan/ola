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



mycursor=mydb.cursor(buffered=True , dictionary=True)


#app routing @app.route('url') - maps specific url to the specific function that handles the logic for that url

verify = Blueprint('verify', __name__)

@verify.route(path.verify,methods=['POST'])#route function
def create_ps():
    req_data=request.get_json()
    sql="SELECT * FROM customer_registration WHERE email=%s and otp=%s and TIME_TO_SEC(TIMEDIFF(current_timestamp,created_time))<300"
    val=(req_data['email'],req_data['otp'],)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult)==1 :
        sql="UPDATE customer_registration SET authentication=1 WHERE email=%s" 
        val=(req_data['email'],)
        mycursor.execute(sql,val)
        mydb.commit()
        return jsonify(myresult,{'message':'OTP verified and maqil id registered fill the registration form'})
    return jsonify(myresult,{'message':'try again by generating new otp your otp might be expired if you keep on having this problem contact authority'})