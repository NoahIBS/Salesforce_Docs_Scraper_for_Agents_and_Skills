<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing.htm&language=en_US&type=5 -->

# Campaign Flow Sharing Settings

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Campaign Flow Sharing Settings

In Marketing Cloud Next, campaign flow sharing is set to private by default. However, associated records, sharing rules, and manual sharing can also affect the flow’s visibility.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To view all flows in the Flows Lightning app regardless of sharing settings: | Manage Flow or View Flows and View All Non-Admin Flows  
To view flows owned by or shared with you in the Flows Lightning app: | View Flows  
To create and edit all flows in the Flows Lightning app, regardless of sharing settings: | Manage Flow or Create or Edit Flows, View Flows and View All Non-Admin Flow  
To create and edit flows owned by or shared with you with Read/Write access in the Flows Lightning app: | Create or Edit Flows and View Flows  
  
Important

If you’re familiar with creating flows in Flow Builder from Setup, be aware that campaign flow sharing settings are different. Flows created in Setup remain visible to everyone who has View Setup and Manage Flow permissions, and you can’t share flows or associate records.

## Who Can See a Campaign Flow on the Flows Page?

In Marketing Cloud Next, a campaign flow without sharing rules is private and visible only to its owner, Salesforce admins, and users with View All Non-Setup Flows or Manage Flow permissions. However, when you add an associated record to a campaign flow, the flow inherits that record’s sharing settings. If you remove or delete the record in the campaign flow’s Associated Record field, the flow’s sharing settings revert to the sharing rule defined for that flow. If the campaign flow doesn’t have any defined sharing rules, it reverts to private.

Relationship | Sharing Outcome  
---|---  
A campaign is available in a flow’s Associated Record field. | The flow inherits the campaign’s sharing settings.  
A campaign is removed from a flow’s Associated Record field. | The flow reverts to previously defined sharing rules. When there aren’t any rules, it becomes private to its owner, Salesforce admins, and users with View All Non-Setup Flows or Manage Flow permissions.  
A campaign that’s used in a flow’s Associated Record field is deleted. | The flow reverts to previously defined sharing rules. When there aren’t any rules, it becomes private to its owner, Salesforce admins, and users with View All Non-Setup Flows or Manage Flow permissions.  
A previously deleted campaign is restored from the Recycle Bin. | The flow inherits the campaign’s sharing settings.  
  
## How Do You Share a Campaign Flow?

An admin can group campaign flows into categories and subcategories and create sharing rules in Sharing Settings. After an admin creates the sharing rules in Sharing Settings, users add the category and subcategory to the flow record’s detail page to apply them.

Alternatively, users can use manual sharing to share an individual campaign flow from the flow’s record detail page. After they click **Sharing** , users can choose whether to share the flow with other users, public groups, roles, or roles and subordinates.

  * **[Share Campaign Flows](https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing_categorize.htm&language=en_US&type=5)**  
To plan for long-term, dynamic sharing, create categories and sharing rules for campaign flows. If you need to share a single campaign flow at any time, share a campaign flow manually.


