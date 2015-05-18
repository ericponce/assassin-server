#!/bin/python


import smtplib
import imaplib
import email

def send_email(to_addr, contents, username, password):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(username,to_addr,contents)
	server.quit()

def receive_email_user(from_addr, username, password):
	server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	server.login(username, password)

	server.select()
	typ, data = server.search(None, 'FROM', from_addr)
	nums = data[0].split()
	if (nums):
		num = nums[0]
		typ, data = server.fetch(num, '(RFC822)')
		msg = email.message_from_string(data[0][1])
		subject = msg['Subject']
		body = msg['Body']
	else:
		num = -1
	   	typ, body = 0, 0

	server.close()
	server.logout()

	return num, subject, body

def receive_email_subj(subject, username, password):
	server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	server.login(username, password)

	server.select()
	typ, data = server.search(None, 'SUBJECT', subject)
	nums = data[0].split()
	if (nums):
		num = nums[0]
		typ, data = server.fetch(num, '(RFC822)')
		msg = email.message_from_string(data[0][1])
		sender = msg['From']
		body = msg.get_payload()
	else:
		num = -1
	   	typ, sender, body = 0, 0, 0

	server.close()
	server.logout()

	return num, sender, body

def delete_email(num, username, password):
	server = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	server.login(username, password)

	server.select()
	server.store(num, "+FLAGS", "\\Deleted");
	server.expunge()
	server.close()
	server.logout()