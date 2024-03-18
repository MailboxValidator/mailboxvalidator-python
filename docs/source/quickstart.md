# Quickstart

## Dependencies

An API key is required for this module to function.

Go to [https://www.mailboxvalidator.com/plans#api](https://www.mailboxvalidator.com/plans#api) to sign up for FREE API plan and you'll be given an API key.

## Installation

To install this module type the following:

```
    pip install MailboxValidator
```

## Sample Codes

### Validate email

You can validate whether an email address is invalid or not as below:

```python
import MailboxValidator

mbv = MailboxValidator.EmailValidation('PASTE_API_KEY_HERE')
results = mbv.validate_email('example@example.com')

if results is None:
    print("Error connecting to API.\n")
elif 'error' not in results:
    print('email_address = ' + results['email_address'] + "\n")
    print('base_email_address = ' + results['base_email_address'] + "\n")
    print('domain = ' + results['domain'] + "\n")
    print('is_free = ' + str(results['is_free']) + "\n")
    print('is_syntax = ' + str(results['is_syntax']) + "\n")
    print('is_domain = ' + str(results['is_domain']) + "\n")
    print('is_smtp = ' + str(results['is_smtp']) + "\n")
    print('is_verified = ' + str(results['is_verified']) + "\n")
    print('is_server_down = ' + str(results['is_server_down']) + "\n")
    print('is_greylisted = ' + str(results['is_greylisted']) + "\n")
    print('is_disposable = ' + str(results['is_disposable']) + "\n")
    print('is_suppressed = ' + str(results['is_suppressed']) + "\n")
    print('is_role = ' + str(results['is_role']) + "\n")
    print('is_high_risk = ' + str(results['is_high_risk']) + "\n")
    print('is_catchall = ' + str(results['is_catchall']) + "\n")
    print('is_dmarc_enforced = ' + str(results['is_dmarc_enforced']) + "\n")
    print('is_strict_spf = ' + str(results['is_strict_spf']) + "\n")
    print('website_exist = ' + str(results['website_exist']) + "\n")
    print('mailboxvalidator_score = ' + str(results['mailboxvalidator_score']) + "\n")
    print('time_taken = ' + str(results['time_taken']) + "\n")
    print('status = ' + str(results['status']) + "\n")
    print('credits_available = ' + str(results['credits_available']) + "\n")
else:
    print('error_code = ' + str(results['error']['error_code']) + "\n")
    print('error_message = ' + results['error']['error_message'] + "\n")
```

### Check if an email is from a disposable email provider

You can validate whether an email address is disposable email address or not as below:

```python
import MailboxValidator

mbv = MailboxValidator.EmailValidation('PASTE_API_KEY_HERE')
results = mbv.is_disposable_email('example@example.com')

if results is None:
    print("Error connecting to API.\n")
elif 'error' not in results:
    print('email_address = ' + results['email_address'] + "\n")
    print('is_disposable = ' + str(results['is_disposable']) + "\n")
    print('credits_available = ' + str(results['credits_available']) + "\n")
else:
    print('error_code = ' + results['error']['error_code'] + "\n")
    print('error_message = ' + results['error']['error_message'] + "\n")
```

### Check if an email is from a free email provider

You can validate whether an email address is free email address or not as below:

```python
import MailboxValidator

mbv = MailboxValidator.EmailValidation('PASTE_API_KEY_HERE')
results = mbv.is_free_email('example@example.com')

if results is None:
    print("Error connecting to API.\n")
elif 'error' not in results:
    print('email_address = ' + results['email_address'] + "\n")
    print('is_free = ' + str(results['is_free']) + "\n")
    print('credits_available = ' + str(results['credits_available']) + "\n")
else:
    print('error_code = ' + results['error']['error_code'] + "\n")
```
