import http.client
import urllib
import hashlib
import json

class SingleValidation:
    def __init__(self, apikey):
        self.apikey = apikey

    def ValidateEmail(self, email):
        p = { 'key': self.apikey, 'format': 'json', 'email': email }

        try:
            conn = http.client.HTTPConnection("api.mailboxvalidator.com")
            conn.request("GET", "/v1/validation/single?" + urllib.parse.urlencode(p))
            res = conn.getresponse()
            # print res.read()
            return json.loads(res.read())
        except:
            return None
