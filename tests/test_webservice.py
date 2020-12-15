# -*- coding: utf-8 -*-

import pytest
import json

import MailboxValidator

def testinvalidapikey(global_data):
    mbv = MailboxValidator.SingleValidation(global_data["apikey"])
    results = mbv.ValidateEmail('example@example.com')
    assert results['error_message'] == 'API key not found.'

def testapikeyexist(global_data, capsys):
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        with capsys.disabled():
            print ("You could enter a MailboxValidator API Key in tests/conftest.py for real web service calling test.")
            print ("You could sign up for a free API key at https://www.mailboxvalidator.com/plans#api if you do not have one.")
        assert global_data["apikey"] == "YOUR_API_KEY"
    else:
        assert global_data["apikey"] != "YOUR_API_KEY"

def testvalidateemail(global_data):
    mbv = MailboxValidator.SingleValidation(global_data["apikey"])
    results = mbv.ValidateEmail('example@example.com')
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error_code'] == "101"
    else:
        assert results['status'] == "False"

def testdisposableemail(global_data):
    mbv = MailboxValidator.SingleValidation(global_data["apikey"])
    results = mbv.DisposableEmail('example@example.com')
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error_code'] == "101"
    else:
        assert results['is_disposable'] == "True"

def testfreeemail(global_data):
    mbv = MailboxValidator.SingleValidation(global_data["apikey"])
    results = mbv.FreeEmail('example@example.com')
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error_code'] == "101"
    else:
        assert results['is_free'] == "False"