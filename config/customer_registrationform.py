from atexit import register
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

register = Blueprint('register', __name__)

@register.route(path.register,methods=['POST'])#route function
def create_ps():
    req_data=request.get_json()
    sql="SELECT * FROM customer_registration WHERE email=%s "
    val=(req_data['email'],)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult)==1 :
        sql="UPDATE customer_registration SET home_address=%s,work_address=%s,aadhar_id=%s,phone=%s,gender=%s WHERE email=%s" 
        val=(req_data['home_address'],req_data['work_address'],req_data['aadhar_id'],req_data['phone'],req_data['gender'],req_data['email'],)
        mycursor.execute(sql,val)
        mydb.commit()
        sql="SELECT * FROM customer_registration WHERE email=%s "
        val=(req_data['email'],)
        mycursor.execute(sql,val)
        myresult1 = mycursor.fetchall()
        return jsonify(myresult1,{'message':'the registration form has been filled'})
    return jsonify(myresult,{'message':'please sign up first if yes contact authority'})