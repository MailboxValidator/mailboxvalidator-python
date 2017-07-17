MailboxValidator Python Module
==============================

This Python module provides an easy way to call the MailboxValidator API which validates if an email address is a valid one.

This module can be used in many types of projects such as:

 - validating a user's email during sign up
 - cleaning your mailing list prior to an email marketing campaign
 - a form of fraud check

Installation
============

To install this module type the following:

::

	pip install MailboxValidator

Dependencies
============

An API key is required for this module to function.

Go to `<http://www.mailboxvalidator.com/plans#api>`_ to sign up for a FREE API plan and you'll be given an API key.

Sample Usage
============

::

	import MailboxValidator
	
	mbv = MailboxValidator.SingleValidation('PASTE_API_KEY_HERE')
	results = mbv.ValidateEmail('example@example.com')
	
	if results is None:
		print("Error connecting to API.\n")
	elif results['error_code'] == '':
		print('email_address = ' + results['email_address'] + "\n")
		print('domain = ' + results['domain'] + "\n")
		print('is_free = ' + results['is_free'] + "\n")
		print('is_syntax = ' + results['is_syntax'] + "\n")
		print('is_domain = ' + results['is_domain'] + "\n")
		print('is_smtp = ' + results['is_smtp'] + "\n")
		print('is_verified = ' + results['is_verified'] + "\n")
		print('is_server_down = ' + results['is_server_down'] + "\n")
		print('is_greylisted = ' + results['is_greylisted'] + "\n")
		print('is_disposable = ' + results['is_disposable'] + "\n")
		print('is_suppressed = ' + results['is_suppressed'] + "\n")
		print('is_role = ' + results['is_role'] + "\n")
		print('is_high_risk = ' + results['is_high_risk'] + "\n")
		print('is_catchall = ' + results['is_catchall'] + "\n")
		print('mailboxvalidator_score = ' + str(results['mailboxvalidator_score']) + "\n")
		print('time_taken = ' + str(results['time_taken']) + "\n")
		print('status = ' + results['status'] + "\n")
		print('credits_available = ' + str(results['credits_available']) + "\n")
	else:
		print('error_code = ' + results['error_code'] + "\n")
		print('error_message = ' + results['error_message'] + "\n")

Copyright
=========

Copyright (C) 2017 by MailboxValidator.com, support@mailboxvalidator.com
