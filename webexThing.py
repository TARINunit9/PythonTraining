#imports
import os
import requests
import datetime
import cryptography
from cryptography import x509
from cryptography.hazmat.backends import default_backend

#some variables to let requests and cryptography work
requestAPI = "https://webexapis.com/v1/messages"
roomId = "This is a room ID."
messageText = "This is a string I will use for the message."

#and now, it's time to start reading some files
databaseLocation = os.listdir() #check if that's allowed
for file in databaseLocation:
	checkCert(file)
#for file in os.listdir(os.getcwd()):
#	if file.endswith(".pem"):
#		checkCert(file)

#this function opens a file and parses the SSL to look for expiry date
def checkCert(file):
	datetime weekAfterToday = datetime.today().date() + timedelta(days=7)
	
	#load the file
	file1 = open(file, "r")
	certObject = x509.load_pem_x509_certificate(file.read())
	if certObject.not_valid_after_utc < weekAfterToday:
		messageText = "Alert! " + certObject.subject + "is aboout to expire!"
		jsonStruct = {roomId: roomId, text: messageText}
		responseCode = requests.post(requestAPI, json = jsonStruct)
		print responseCode
		#print messageText
	file1.close()
