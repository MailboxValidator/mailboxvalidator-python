# MailboxValidator Python API

## EmailValidation Class
```{py:class} EmailValidation(api_key)
Configure MailboxValidator API key.

:param str api_key: (Required) MailboxValidator API key.
```

```{py:function} validate_email(email)
Validate whether an email address is a valid email or not.

:param str email: (Required) The email address.

:return: Returns the validation result in JSON object.
:rtype: Object

**Successful Response Parameters**
| Field Name | Description |
|-----------|------------|
| email_address | The input email address. |
| base_email_address | The input email address after sanitizing the username of the dots (only Gmail) and [subaddressing](https://en.wikipedia.org/wiki/Email_address#Sub-addressing). |
| domain | The domain of the email address. |
| is_free | Whether the email address is from a free email provider like Gmail or Hotmail. Return values: true, false, null  (null means not applicable) |
| is_syntax | Whether the email address is syntactically correct. Return values: true, false |
| is_domain | Whether the email address has a valid MX record in its DNS entries. Return values: true, false, null  (null means not applicable) |
| is_smtp | Whether the mail servers specified in the MX records are responding to connections. Return values: true, false, null  (null means not applicable) |
| is_verified | Whether the mail server confirms that the email address actually exist. Return values: true, false, null  (null means not applicable) |
| is_server_down | Whether the mail server is currently down or unresponsive. Return values: true, false, null  (null means not applicable) |
| is_greylisted | Whether the mail server employs greylisting where an email has to be sent a second time at a later time. Return values: true, false, null  (null means not applicable) |
| is_disposable | Whether the email address is a temporary one from a disposable email provider. Return values: true, false, null  (null means not applicable) |
| is_suppressed | Whether the email address is in our blacklist. Return values: true, false, null  (null means not applicable) |
| is_role | Whether the email address is a role-based email address like admin@example.net or webmaster@example.net. Return values: true, false, null  (null means not applicable) |
| is_high_risk | Whether the email address contains high risk keywords. Return values: true, false, null  (null means not applicable) |
| is_catchall | Whether the email address is a catch-all address. Return values: true, false, null  (null means not applicable) |
| is_dmarc_enforced | Whether the email domain is enforcing DMARC. Return values: true, false |
| is_strict_spf | Whether the email domain is using strict SPF. Return values: true, false |
| website_exist | Whether the email domain is a reachable website. Return values: true, false |
| mailboxvalidator_score | Email address reputation score. Score > 0.70 means good; score > 0.40 means fair; score <= 0.40 means poor. |
| time_taken | The time taken to get the results in seconds. |
| status | Whether our system think the email address is valid based on all the previous fields. Return values: True, False |
| credits_available | The number of credits left to perform validations. |

**Error Response Parameters**
| Field Name | Description |
|-----------|------------|
| error.error_code | The error code if there is any error. See error table in the [Error Codes](reference.md) section. |
| error.error_message | The error message if there is any error. See error table in the [Error Codes](reference.md) section. |

```

```{py:function} is_disposable_email(email)
Validate whether an email address is a disposable email or not.

:param str email: (Required) The email address.

:return: Returns the validation result in JSON object.
:rtype: Object

**Successful Response Parameters**
| Field Name | Description |
|-----------|------------|
| email_address | The input email address. |
| is_disposable | Whether the email address is a temporary one from a disposable email provider. Return values: True, False |
| credits_available | The number of credits left to perform validations. |


**Error Response Parameters**
| Field Name | Description |
|-----------|------------|
| error.error_code | The error code if there is any error. See error table in the [Error Codes](reference.md) section. |
| error.error_message | The error message if there is any error. See error table in the [Error Codes](reference.md) section. |

```

```{py:function} is_free_email(email)
Validate whether an email address is a free email or not.

:param str email: (Required) The email address.

:return: Returns the validation result in JSON object.
:rtype: Object

**Successful Response Parameters**
| Field Name | Description |
|-----------|------------|
| email_address | The input email address. |
| is_free | Whether the email address is from a free email provider like Gmail or Hotmail. Return values: True, False |
| credits_available | The number of credits left to perform validations. |


**Error Response Parameters**
| Field Name | Description |
|-----------|------------|
| error.error_code | The error code if there is any error. See error table in the [Error Codes](reference.md) section. |
| error.error_message | The error message if there is any error. See error table in the [Error Codes](reference.md) section. |

```

