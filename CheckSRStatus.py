#!/usr/bin/python

import argparse
import ConfigParser
import urllib
import urllib2
import json

#Get SR ID from arguments
parser = argparse.ArgumentParser(description='Check ST status.')
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
          "opName" : "userAPIGetWorkflowStatus",
          "opData" : {"param0" : serviceRequestID}
          }
data = urllib.urlencode(values)
headers = {authHeader : authKey}

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
json_object = json.load(response)

status = json_object["serviceResult"]

if status == 1:
    print "Workflow SR " + str(serviceRequestID) + " is in progress."
elif status == 3:
    print "Workflow SR " + str(serviceRequestID) + " is complete."
elif status == 2:
    print "Workflow SR " + str(serviceRequestID) + " failed."