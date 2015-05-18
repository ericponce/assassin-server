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
