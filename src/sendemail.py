#!/bin/python


import smtplib

def send_email(to_addr, contents, username, password):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(username,to_addr,contents)
	server.quit()
