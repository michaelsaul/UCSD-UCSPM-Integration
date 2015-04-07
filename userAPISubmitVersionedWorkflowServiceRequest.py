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
srStartTime = config.get("Workflow", "srStartTime")
srDurationHours = config.get("Workflow", "srDurationHours")
groupID = config.get("Workflow", "groupID")

#Set Authentication Header
authHeader = "X-Cloupia-Request-Key"

#Construct the URL
url = "http://" + ip + "/app/api/rest?"

values = {"formatType" : "json",
          "opName" : "version:userAPISubmitVersionedWorkflowServiceRequest",
          "opData" : {param0:{"workflowName" : workflowName, 
                              "versionLabel" : workflowVersion,
                              "list":{
                              "list":[
                                  {"name" : "Data Store name", "value" : dataStoreName},
                                  {"name" : "Data Store Size", "value" : dataStoreSize},
                                  {"name" : "Volume Size", "value" : volumeSize}
                                     ]
                                     },
                              "parentSRID" : arentSRID,
                              "srStartTime" : srStartTime,
                              "srDurationHours" : srDurationHours,
                              "groupId" : groupID
                              }
                      }
          }

data = urllib.urlencode(values)
headers = {authHeader : authKey}

req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)

json_object = json.load(response)