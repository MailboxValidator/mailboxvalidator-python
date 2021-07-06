# -*- coding: utf-8 -*-

import pytest
import json

import MailboxValidator

def test_invalid_api_key(global_data):
    mbv = MailboxValidator.EmailValidation(global_data["apikey"])
    results = mbv.ValidateEmail('example@example.com')
    assert results['error_message'] == 'API key not found.'

def test_api_key_exist(global_data, capsys):
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        with capsys.disabled():
            print ("You could enter a MailboxValidator API Key in tests/conftest.py for real web service calling test.")
            print ("You could sign up for a free API key at https://www.mailboxvalidator.com/plans#api if you do not have one.")
        assert global_data["apikey"] == "YOUR_API_KEY"
    else:
        assert global_data["apikey"] != "YOUR_API_KEY"

def test_function_exist(global_data):
    mbv = MailboxValidator.EmailValidation(global_data["apikey"])
    errors = []
    functions_list = ['validate_email', 'is_disposable_email', 'is_free_email']
    for x in range(len(functions_list)): 
        # assert hasattr(mbv, functions_list[x]) == True, "Function did not exist."
        if (hasattr(mbv, functions_list[x]) is False):
            errors.append("Function " + functions_list[x] + " did not exist.")
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_validate_email(global_data):
    mbv = MailboxValidator.EmailValidation(global_data["apikey"])
    results = mbv.validate_email('example@example.com')
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error_code'] == "101"
    else:
        assert results['status'] == "False"

def test_disposable_email(global_data):
    mbv = MailboxValidator.EmailValidation(global_data["apikey"])
    results = mbv.is_disposable_email('example@example.com')
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error_code'] == "101"
    else:
        assert results['is_disposable'] == "True"

def test_free_email(global_data):
    mbv = MailboxValidator.EmailValidation(global_data["apikey"])
    results = mbv.is_free_email('example@example.com')
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error_code'] == "101"
    else:
        assert results['is_free'] == "False"