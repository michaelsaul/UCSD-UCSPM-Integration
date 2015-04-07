#!/usr/bin/python

import ConfigParser
import urllib
import urllib2
import json

#Get configuration from file site.cfg
config = ConfigParser.RawConfigParser()
config.read("site.cfg")
authKey = config.get("UCSD", "authKey")
ip = config.get("UCSD", "ip")

#Set Authentication Header
authHeader = "X-Cloupia-Request-Key"

workflowName = "Randy Create Data Store Fiber Channel"
workflowVersion = 0

#Construct the URL
url = "http://" + ip + "/app/api/rest?"

values = {"formatType" : "json",
          "opName" : "version:version:userAPIGetVersionedWorkflowInputs",
          "opData" : {"param0" : workflowName, "param1" : workflowVersion}
          }
data = urllib.urlencode(values)
headers = {authHeader : authKey,
           }

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

json_object = json.load(response)

for results in json_object["serviceResult"]["0"]:
  print results["name"]
