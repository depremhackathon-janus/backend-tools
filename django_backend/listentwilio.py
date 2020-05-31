from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml


import json 
import os
import sys


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
sys.path.append(dname)

import re

os.environ['DJANGO_SETTINGS_MODULE'] = 'deprem_backend.settings'
import django
django.setup()

from smsget.models import PersonInfo

app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])
def sms():
    print("[Twilio:sms] request, ",request)
    if('From' in request.form):
        number = request.form['From']
        message_body = request.form['Body']

        """
        print("[Twilio:sms]"," number: ",number)
        print("[Twilio:sms]"," message body: ",message_body)

        completebody1 = "'s"+str(message_body)
        print("[Twilio:sms]"," completebody1: ",completebody1)
        
        completebody2 = "{"+str(completebody1)

        print("[Twilio:sms]"," completebody2: ",completebody2)
        
        completebody2 = str(completebody2) + "}}"
        
        print("[Twilio:sms]"," completebody2: ",completebody2)
        
        completebody3 = completebody2.replace("'",'"') 
        
        print("[Twilio:sms]"," completebody3: ",completebody3)
        
        dump_json = json.dumps(completebody3)
        
        print("[Twilio:sms]"," dump_json: ",dump_json)

        """
        #body_json = json.loads(dump_json)
        #body_json = json.dumps(completebody2)
        
        print("[Twilio:sms]"," message json: ",message_body)

        if "num" in message_body and "stat" in message_body and \
            "long" in message_body and "lat" in message_body:
            print("[Twilio:sms]"," ENTERED PARSE: ")
            
            
            num_matches = re.findall(r'"num":(.+?),',message_body)
            if(len(num_matches)>0):
                print("num: ",num_matches[0])
                num = int(num_matches[0])
            num_matches = re.findall(r'"stat":(.+?),',message_body)
            if(len(num_matches)>0):
                print("stat: ",num_matches[0])
                stat = int(num_matches[0])
            num_matches = re.findall(r'"long":(.+?),',message_body)
            if(len(num_matches)>0):
                print("long: ",num_matches[0])
                long = float(num_matches[0])
            num_matches = re.findall(r'"lat":(.+?),',message_body)
            if(len(num_matches)>0):
                print("lat: ",num_matches[0])
                lat = float(num_matches[0])
            num_matches = re.findall(r'"txt":"(.+?)"',message_body)
            if(len(num_matches)>0):
                print("txt: ",num_matches[0])
                txt = str(num_matches[0])


            new_person = PersonInfo(num=num,stat=stat,lat=lat,long=long,txt=txt)
            new_person.save()
            #num = body_json['num']
            #stat = body_json['stat']
            #lat = body_json['lat']
            #long = body_json['long']
            #read_person = PersonInfo(num=num,stat=stat,lat=lat,long=long)
            #read_person.save()

    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    #test_person = PersonInfo(num=5379125656,stat=0,lat=45.46,long=36.54)
    #test_person.save()
    app.run(debug=True)
