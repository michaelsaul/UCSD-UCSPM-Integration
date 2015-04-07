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
workflowName = config.get("Workflow", "workflowName")

#Set Authentication Header
authHeader = "X-Cloupia-Request-Key"

#Construct the URL
url = "http://" + ip + "/app/api/rest?"

values = {"formatType" : "json",
          "opName" : "version:userAPIGetWorkflowVersions",
          "opData" : {"param0" : workflowName}
          }
data = urllib.urlencode(values)
headers = {authHeader : authKey,
           }

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

json_object = json.load(response)

for results in json_object["serviceResult"]:
    print results["version"]

