#!/bin/python

import email_util
import database
import sqlite3

if __name__ == "__main__":
	f = open('email_config.cfg', 'r')
	username = f.readline().strip()
	password = f.readline().strip()
	dbase = f.readline().strip()
	f.close()

	database.init_table(dbase);

	while(1):
		num, sender, body = email_util.receive_email_subj("add", username, password)
		if (num != -1):
			print "Received new user email requesting add!"
			sender = sender[sender.index("<") + 1:-1]
			body = body.split();
			if not body:
				database.add_user(sender, sender, dbase)
			else:
				database.add_user(body[0], sender, dbase)
			email_util.delete_email(num, username, password)
		num, sender, body = email_util.receive_email_subj("quit", username, password)
		if (num != -1):
			print "Received new user email requesting removal!"
			sender = sender[sender.index("<") + 1:-1]
			body = body.split();
			database.remove_user(sender, dbase)
			email_util.delete_email(num, username, password)

