<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_flows_concepts.htm&language=en_US&type=5 -->

# Understanding Campaigns and Flows in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Understanding Campaigns and Flows in Marketing Cloud Next

Campaigns and flows are two distinct objects, but they work together to organize and execute your marketing work in Marketing Cloud Next. The campaign record aims to simplify how you connect the assets and metadata that comprise a marketing effort. A flow is the engine that prepares and executes the campaign.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
  
## Definitions

Campaigns and flows work together to organize and execute your marketing efforts, but they’re two distinct objects in Salesforce.

Campaign | An object that organizes the assets and metadata comprising a marketing effort. | Performance metrics for related assets roll up to a campaign.  
---|---|---  
Flow | A series of automated actions represented like a flow chart on an interactive canvas. | For marketers, a flow can automate message sends and follow-up tasks, such as record creation or lead routing.  
Campaign Flow | A flow that is related to a campaign record. | A new campaign includes a related flow; if you create a flow first, you must manually relate its campaign. We use this term in Salesforce Help to differentiate a marketing-related flow from the traditional Salesforce flows that admins create.  
  
## Relationships

A single campaign can contain multiple flows, but each flow can relate to only one campaign.

Changing these relationships can impact sharing settings and marketing performance metrics. When a flow is active, you can't remove its related campaign or relate it to a different campaign. If you must change a flow's campaign, update the Associated Record field on the flow record.

## Pausing, Sharing, and Deleting

When a flow is related to a campaign, they share information. Keep these considerations in mind before you make changes.

  * A single flow supports multiple versions, but only one version can be active. A paused flow is considered active.
  * The linked flow that appears on the campaign record is the most recent _activated_ campaign. If an old flow version appears on your campaign, activate the latest version, and then check the campaign again.
  * Access to a campaign flow is based on the campaign’s sharing settings. When you delete a campaign, its flows' sharing settings revert to the defined sharing rules for each flow. If no sharing rules are defined, the flow becomes private and is accessible only to the owner, Salesforce admins, and anyone with View All Non-Setup Flows or Manage Flow permissions.
  * When you delete a campaign or flow, its counterpart isn't deleted but the relationship is removed.



The linked flow that appears on the campaign record is the most recent _activated_ campaign. If an old flow version appears on your campaign, activate the latest version, and then check the campaign again.

  * **[Campaign Record vs. Flow Canvas](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_ref.htm&language=en_US&type=5)**  
A campaign record shows information about each flow in the campaign, and it's designed to reflect certain elements from the Flow Builder canvas. Note, however, that some features and settings appear in Flow Builder that aren't available on the campaign record, and vice versa.
  * **[Flow Status Reference](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_monitoring_your_flow_status.htm&language=en_US&type=5)**  
The tasks that are available or restricted on a flow at a particular time are defined by its status. Individual flow occurrences generate their own statuses, which can help you understand why something didn't occur as expected.
  * **[Tools for Tracking and Reporting on Campaigns](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_reporting_ref.htm&language=en_US&type=5)**  
Marketing Cloud Next offers tools to help you monitor and track campaign success over time.
  * **[Flow Builder Features and Elements for Marketers](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_reference.htm&language=en_US&type=5)**  
Flow Builder is a robust tool for creating automation solutions to business challenges faced by a variety of industries and roles. Marketers have access to portions of Flow Builder that are helpful for accomplishing marketing jobs.
  * **[Campaign Flow Sharing Settings](https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing.htm&language=en_US&type=5)**  
In Marketing Cloud Next, campaign flow sharing is set to private by default. However, associated records, sharing rules, and manual sharing can also affect the flow’s visibility.


