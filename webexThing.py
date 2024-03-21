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
#cert = x509.load_pem_x509_certificate(pem_data, default_backend())
#cert.serial_number

#and now, it's time to start reading some files
databaseLocation = os.listdir() #check if that's allowed
for file in databaseLocation:
	checkCert(file)

#this function opens a file and parses the text therein to look for expiry date
def checkCert(file):
	datetime weekAfterToday = datetime.today().date() + timedelta(days=7)
	string bufferString
	datetime expiryDate
	
	#load the file
	#debug command, for unencrypted files
	file1 = open(file, "r")
	#real command. not correct, still researching
	#file1 = x509.load_pem_x509_certificate(file)
	#certString = X509.load_cert_string(file1)
	
	#parse the file line by line
	Lines = file1.readlines()
	for line in Lines:
		if "Serial Number" in line:
			bufferString = line
		if "notAfter" in line:
			expiryDate = dateStripper(line)
	file1.close()
	#this function assumes only one instance of "Serial Number" and "notAfter"
	#so it only looks at the last instance of each
	
	#now compare the expiry date with today's date
	if (expiryDate) and (bufferString) and (expiryDate < weekAfterToday):
		#messageText = "some stuff"
		#jsonStruct = {roomId: roomId, text: messageText}
		#responseCode = requests.post(requestAPI, json = jsonStruct)
		#print responseCode
		#clear messageText if needed
	
#this function takes a string and turns it into a datetime object
def dateStripper(dateString):
	#function assumes this format:
	#'notAfter': 'Jan 24 14:24:11 2025 GMT',
	string bufferString = dateString
	bufferString.strip("'notAfter': '")
	bufferString.strip("GMT ',")
	return datetime.strptime(bufferString, '%m %d %H:%M:%S %y')

#send a message with this code:
#jsonStruct = {roomId: roomId, text: messageText}
#responseCode = requests.post(requestAPI, json = jsonStruct)
#print responseCode

#This might make everything easier
#certObject = x509.load_pem_x509_certificate(file1.read())
#if certObject.not_valid_after_utc < weekAfterToday:

#https://pyjwt.readthedocs.io/en/stable/faq.html
#https://stackoverflow.com/questions/57877935/how-to-convert-an-x509name-object-to-a-string-in-python
#https://cryptography.io/en/latest/x509/reference/