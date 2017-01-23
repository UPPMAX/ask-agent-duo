#!/usr/bin/env python

import duo_config
import duo_client
import sys
import os

import requests
import urllib


question = "Nothing to ask about."

if len(sys.argv) == 2:
    question = sys.argv[1]


authclient = duo_client.Auth(duo_config.ikey, 
                       duo_config.skey, 
                       duo_config.api_hostname)

push=urllib.urlencode({'Question':question})


response =  authclient.auth(username = os.getlogin(),
                            factor = 'push',
                            async = False,
                            device = 'auto',
                            type = 'ssh key usage', 
                            pushinfo = push) 

if response.has_key('status') and response['status'] == 'allow':
    sys.exit(0)

sys.exit(1)
