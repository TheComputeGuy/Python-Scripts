# -*- coding: utf-8 -*-
import csv
import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *
from time import sleep

num=[]
slot=[]
s=0;
with open ('num.csv', 'rb') as f:
    numb=csv.reader(f, csv.excel)
    for row in numb:
        num+=row
with open ('slot.csv', 'rb') as f1:
    sl=csv.reader(f1, csv.excel)
    for row1 in sl:
        slot+=row1

## way2sms allows only 140 characters in the message body. Consider that while framing message body and number of messages
message1 = "Greetings from Festember Quality Mangement Team your first phase of induction will take place at "
message2 = " in the Barn Hall on *date*, *day*."
message3 = "Please fill in your responses to the questionnaire prior to the PI. Kindly acknowledge with your name to *someContact* (yourName), and be on time."

username = "yourPhoneNumberHere"
passwd = "yourPassword"

#logging into the sms site
url ='http://site24.way2sms.com/Login1.action?'
data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

#For cookies
cj= cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#Adding header details
opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
try:
    usock =opener.open(url, data)
except IOError:
    print "error"

for e in xrange (len(num)):
    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(num[e])+'&message='+message1+str(slot[e])+message2+'&msgLen=139'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"
    sleep(1)            ##Had to send two messages because of the character limit
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(num[e])+'&message='+message3+'&msgLen=137'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"
    s+=1
    sleep(1)
    print "Sent to "+str(s)    

print "All SMSes sent!"


##ISSUE: For me, the script could send only 30 messages from one account at once, per day. Even varying delay didn't work.
##Keep that in mind while writing scripts
