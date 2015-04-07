#!/usr/bin/python

import argparse
import ConfigParser
import urllib
import urllib2
import json

#Get SR ID from arguments
parser = argparse.ArgumentParser(description='Roll back a Service Request')
parser.add_argument('SR', metavar="SR", type=int, nargs=1, help="A service request ID.")

args = parser.parse_args()

serviceRequestID = args.SR

#Get configuration from file site.cfg
config = ConfigParser.RawConfigParser()
config.read("site.cfg")
authKey = config.get("UCSD", "authKey")
ip = config.get("UCSD", "ip")

#Set Authentication Header
authHeader = "X-Cloupia-Request-Key"

#Construct the URL
url = "http://" + ip + "/app/api/rest?"

values = {"formatType" : "json",
          "opName" : "userAPIRollbackWorkflow",
          "opData" : {"param0" : serviceRequestID}
          }
data = urllib.urlencode(values)
headers = {authHeader : authKey}

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

json_object = json.load(response)
serviceRequest = json_object['serviceResult']
print("Your rollback request has been assigned SR: " + str(serviceRequest));