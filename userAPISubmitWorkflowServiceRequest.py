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
workflowVersion = config.get("Workflow", "workflowVersion")
dataStoreName = config.get("Workflow", "dataStoreName")
dataStoreSize = config.get("Workflow", "dataStoreSize")
volumeSize = config.get("Workflow", "volumeSize")
parentSRID = config.get("Workflow", "parentSRID")

#Not sure why I need to define these here, it won't complete without it.
param0 = "param0"
param1 = "param1"
param2 = "param2"

#Set Authentication Header
authHeader = "X-Cloupia-Request-Key"

#Construct the URL
url = "http://" + ip + "/app/api/rest?"

values = {"formatType" : "json",
          "opName" : "userAPISubmitWorkflowServiceRequest",
          "opData" : {param0 : workflowName,
                      param1 : {"list":[
                                 {"name":"Data Store name","value":dataStoreName},
                                 {"name":"Data Store Size","value":dataStoreSize},
                                 {"name":"Volume Size","value":volumeSize}
                                 ]
                                },
                      param2 : parentSRID}
          }

data = urllib.urlencode(values)
headers = {authHeader : authKey}

#print(data)

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

json_object = json.load(response)
serviceRequest = json_object['serviceResult']
print(serviceRequest)