#!/bin/python

import email_util

if __name__ == "__main__":
	f = open('email_config.cfg', 'r')
	username = f.readline().strip()
	password = f.readline().strip()
	f.close()
