#!/bin/python

import sendemail

if __name__ == "__main__":
	f = open('email_config.cfg', 'r')
	username = f.readline().strip()
	password = f.readline().strip()
	f.close()

	