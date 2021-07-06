import http.client
import urllib
import hashlib
import json

class EmailValidation:
    def __init__(self, apikey):
        self.apikey = apikey

    def validate_email(self, email):
        p = { 'key': self.apikey, 'format': 'json', 'email': email }

        try:
            conn = http.client.HTTPConnection("api.mailboxvalidator.com")
            conn.request("GET", "/v1/validation/single?" + urllib.parse.urlencode(p))
            res = conn.getresponse()
            # print res.read()
            return json.loads(res.read())
        except:
            return None

    def is_disposable_email(self, email):
        p = { 'key': self.apikey, 'format': 'json', 'email': email }

        try:
            conn = http.client.HTTPConnection("api.mailboxvalidator.com")
            conn.request("GET", "/v1/email/disposable?" + urllib.parse.urlencode(p))
            res = conn.getresponse()
            # print res.read()
            return json.loads(res.read())
        except:
            return None

    def is_free_email(self, email):
        p = { 'key': self.apikey, 'format': 'json', 'email': email }

        try:
            conn = http.client.HTTPConnection("api.mailboxvalidator.com")
            conn.request("GET", "/v1/email/free?" + urllib.parse.urlencode(p))
            res = conn.getresponse()
            # print res.read()
            return json.loads(res.read())
        except:
            return None
