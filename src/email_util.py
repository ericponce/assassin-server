#!/bin/python


import smtplib
import imaplib

def send_email(to_addr, contents, username, password):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(username,to_addr,contents)
	server.quit()

def receive_email(from_addr, username, password):
	server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	server.login(username, password)

	server.select()
	typ, data = server.search(None, 'FROM', from_addr)
	nums = data[0].split()
	if (nums):
		num = nums[0]
		typ, data = server.fetch(num, '(BODY.PEEK[TEXT])')
		data = data[0][1]
	else:
		num = -1
	   	typ, data = 0, 0

	# print('Message %s\n%s\n' % (num, data[0][1]))
	server.close()
	server.logout()

	return num, data

def delete_email(num, username, password):
	server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	server.login(username, password)

	server.select()
	server.store(num, "+FLAGS", "\\Deleted");
	server.expunge()
	server.close()
	server.logout()