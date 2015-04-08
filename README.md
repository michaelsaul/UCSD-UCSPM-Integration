# UCSD-UCSPM-Integration
My first attempt at playing with UCS Director REST API.

These scripts can be used by UCS Performance Manager to launch custom workflows in UCS Director. In this example, we are using a workflow that can will provision a new datastore. By attaching this command to a trigger that monitors datastore capacity, we can automatically grow our storage environment to match demand.  

The custom workflow that we are using takes 3 arguments:

-   Datastore Name
-   Datastore Size
-   Volume Size

##Configuration File
Running the scripts requires a configuration file in the following format. Be sure to include the API access key. The API 

	[UCSD]
	ip = a.b.c.d
	authKey = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
	[Workflow]
	workflowName = A Workflow Name
	workflowVersion = 0
	dataStoreName = A Datastore Name
	dataStoreSize = 5
	volumeSize = 10
	parentSRID = -1
	srStartTime = 0
	srDurationHours = 1
	groupID = 0

##ToDo
- Add error handling
    - HTTP Status codes
    - Check for any errors returned from the API and display/log if not availeble
- Clean up code to resue funtions
- Create and add command line options for workflow names, inputs for workflows

##More Information
[Cisco UCS Performance Manager](http://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-performance-manager/index.html)

[Cisco UCS Director](http://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-director/index.html)

[UCS Director REST API Guide on Cisco DevNet](https://developer.cisco.com/site/ucs-director/rest-api-guide/)

