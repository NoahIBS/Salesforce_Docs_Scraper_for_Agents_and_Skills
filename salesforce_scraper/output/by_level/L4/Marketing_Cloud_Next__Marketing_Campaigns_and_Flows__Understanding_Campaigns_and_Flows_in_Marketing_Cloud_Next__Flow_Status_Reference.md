<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_monitoring_your_flow_status.htm&language=en_US&type=5 -->

# Flow Status Reference

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Flow Status Reference

The tasks that are available or restricted on a flow at a particular time are defined by its status. Individual flow occurrences generate their own statuses, which can help you understand why something didn't occur as expected.

### Required Editions

Available in: Lightning Experience Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Flow Statuses

A flow status provides information about what's going on behind the scenes, and what tasks you can complete at a given time.

Flow Status | Details | Available Actions  
---|---|---  
Preparing | The flow is preparing resources, but hasn’t started processing data yet. | 

  * Edit
  * Pause
  * Save as a new version

  
Activated | The flow is running. | 

  * Edit
  * Pause
  * Save as a new version

  
Finishing | The flow is continuing to process people or data that were in the flow when it was canceled. It doesn’t accept anything new. | 

  * Edit
  * Pause
  * Save as a new version

  
Completed | The flow finished running. | 

  * Save as a new version

  
Scheduled | The flow hasn’t started running. | 

  * Deactivate
  * Edit
  * Save
  * Save as a new version

  
Canceled | The flow was paused and deactivated. | 

  * Save as a new version

  
Draft | The flow hasn’t been activated yet | 

  * Activate
  * Edit
  * Save
  * Save as a new version

  
Error | The flow was stopped due to a problem. | 

  * Save as a new version

  
  
## Versions and Occurrences

A flow version is a named iteration that's created when you modify a flow and save it as a new version. Because flows are updated over time, it's common to save multiple versions.

Each time a flow version runs, it creates a flow version occurrence. To monitor the progress of flow version occurrences and view error details in case of failures, look for the Flows Version Occurrence related list on the flow record.

Here's what's included in the related list.

Column Name | Indicates  
---|---  
Progress Status | Running status of a flow version occurrence  
Error Details | Reason for a failed flow version occurrence   
Entries | Number of times a flow version was started or triggered  
Exits | Number of times the flow version completed successfully  
Errors | Number of times the flow encountered errors during its execution
