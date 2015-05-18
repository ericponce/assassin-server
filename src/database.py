#!/bin/bash

import sqlite3

def init_table(database):
	conn = sqlite3.connect(database)
	c = conn.cursor()

	c.execute('''CREATE TABLE if not exists users
					(name, email, status, target, assassin)''')

	conn.commit()
	conn.close()

def add_user(name, email, database):
	conn = sqlite3.connect(database)

	c = conn.cursor()

	c.execute('''select ? from users''',(email,))
	res = c.fetchone()
	if res == None:
		c.execute('''insert into users values(?,?,"alive",null,null)''', (name, email))
		print "Inserted new user " + email + "."
	else:
		print "Tried to insert duplicate email."
	conn.commit()
	conn.close()


def remove_user(email, database):
	conn = sqlite3.connect(database)

	c = conn.cursor()

	c.execute('''select ? from users''',(email,))
	res = c.fetchone()
	if res == None:
		print "Tried to delete non-existant user."
	else:
		c.execute('''delete from users where email=?''', (email,))
		print "Deleted user " + email + "."
	conn.commit()
	conn.close()