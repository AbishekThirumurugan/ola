from flask import Flask, jsonify,request
from flask_mysqldb import MySQL #importing necessary file
import sys
sys.path.insert(0, 'ola\config') # to get path of the config folder
from home import home
#from read import read
from otp import create
from otp_verification import verify
from customer_registrationform import register
#from delete import delete


app=Flask(__name__) #constructor in flask - object is our application

app.register_blueprint(home)#blueprint object get registered in application - it extends content of the application with blueprint
app.register_blueprint(create)
app.register_blueprint(verify)
app.register_blueprint(register)
#app.register_blueprint(update)
#app.register_blueprint(delete)
app.run(port=8000,debug=True) #run() method of flask class runs the application