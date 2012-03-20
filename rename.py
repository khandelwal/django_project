#!/usr/bin/env python

import sys
import os
from random import choice

#def generate_secret_key():
#	""" Generate a SECRET_KEY for the settings file. This method is apparently from the 
#	Django source. """
#	return ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))

if __name__ == '__main__':
	DEFAULT_PROJECT_NAME = 'myproject'

	if len(sys.argv) < 2:
		print "Usage: ./rename.py <new_django_project_name>"
		sys.exit()


	new_django_name = sys.argv[1]

	#rename the project directory
	os.rename(DEFAULT_PROJECT_NAME, new_django_name)

	#generate a new unique, secret key
	new_secret_key = generate_secret_key()

	f = open(os.path.join(DEFAULT_PROJECT_NAME, 'local_settings.py'), 'a')

	#set the new secret key
	f.write("SECRET_KEY='%s'\n" % new_secret_key)

	#set an appropriate ROOT_URLCONF
	f.write("ROOT_URLCONF='%s.urls'" % new_django_name)

	f.close()

	print "Please new project to INSTALLED APPS"
