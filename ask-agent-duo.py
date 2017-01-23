#!/usr/bin/env python
#
# For use as appointed as SSH_ASKPASS when starting ssh-agent, call
# on the user seconds factor instead.
#
# Needs https://github.com/duosecurity/duo_client_python installed
# or cloned and this script copied to the cloned directory.
#
# duo_config should define ikey, skey and api_hostname per your 
# configuration (see duosecurity.com).
#

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
