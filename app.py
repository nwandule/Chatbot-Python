import os
from flask import Flask
from flask import request
from twilio.rest import Client
app = Flask(__name__)

ACCOUNT_ID = "ACad38eb6b75499e30797a8206d29144a7"
TWILIO_TOKEN = "9ff6123ded636809ca0b2ef52ab6e2a0"
TWILIO_NUMBER = 'whatsapp:+14155238886'
client = Client(ACCOUNT_ID,TWILIO_TOKEN)
def send_msg(msg, recipient):
   client.messages.create(
       from_=TWILIO_NUMBER,
       body=msg,
       to=recipient
   )
   

def process_msg(msg):
    response= ""
    if msg== "hi":
        response= "Hello, Welcome to Bidbot"
    else:
        response= "Please type hi"
    return response

@app.route("/webhook",methods=["POST"])
def webhook():
    f=request.form
    msg=f['Body']
    sender=f['From'] 
    response=process_msg(msg)
    send_msg(response,sender)
    print(response)
    return "OK", 200