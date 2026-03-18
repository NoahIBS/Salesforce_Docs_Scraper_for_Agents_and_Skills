<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_permissions_ref.htm&language=en_US&type=5 -->

# User Permissions in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# User Permissions in Marketing Cloud Next

Marketing Cloud Next comes with two permission sets: Marketing Cloud Admin and Marketing Cloud Manager. Many individual permissions are available for managing access more granularly throughout the app. The permissions list can help you build a custom permission set or troubleshoot access issues.

### Required Editions

Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
First, [create your users](https://help.salesforce.com/s/articleView?id=platform.adding_new_users.htm&language=en_US&type=5), and then assign permissions.

## Permission Sets

Assign permission sets on the Permission Sets page in Salesforce Setup. These permission sets are based on a standard user profile.

Name| Description  
---|---  
Marketing Cloud Admin | Access to Salesforce Setup, Agentforce Admin, Prompt Template Manager, and full control on campaigns, segments, and flows.  
Marketing Cloud Manager | Full control to manage campaigns, segments, and campaign (non-admin) flows, and access to use Agentforce and Prompt Templates.  
  
## General Marketing Permissions

These permissions are available in the System Permissions list for a permission set.

Name | Description  
---|---  
Access the Marketing App | Access to the Marketing app in Lightning Experience.  
Allows user access segments | Access to the Segments tab in the Marketing app.  
Configure Marketing Cloud Scoring Rules | Review and publish lead scoring rules.  
Manage Campaigns | Create, edit, and delete permissions on campaigns.  
  
## CMS Content Roles

These roles are assigned on the Administration pages in sites and workspaces.

Name | Description  
---|---  
Viewer | View content published on the Marketing Landing Pages site.  
Content Admin | Full access to all content in a workspace, contributor, and sharing management for a workspace.  
Content Manager | Full access to all content in a workspace.  
Content Author | Create, edit, and view content in a workspace.  
  
## Consent Permissions in Marketing Cloud Next

These permissions are available in the System Permissions list for a permission set.

Name | Description  
---|---  
Edit Marketing Consent Settings | Edit the consent settings in Salesforce Setup.  
Manage Consent Banner Setup | Edit styles for the consent banner used on marketing landing pages.  
Manage Preference Manager | Create, edit, and delete Preference Manager configurations.  
  
## Content and Publishing Permissions

These permissions are available in the System Permissions list for a permission set.

Name | Description  
---|---  
Manage Email Content | View, create, edit, and delete email content. You can also send, preview, and test your email content with this permission.  
Manage Email Messaging Setup | Create, generate, view, edit, and delete email objects in Salesforce Setup.  
Manage SMS Messaging Setup | Create, view, edit, and delete SMS objects in Salesforce Setup.  
Query CMS Email Content | Prepare CMS email content for sending from campaigns and Flow Builder. Email sending also requires Create on Flow object.  
Send Test Email | Send test emails from the preview and test operation via Messaging Service.  
Send Test SMS | Send test SMS messages for the preview and test operation via Messaging Service.  
Send Unified Messaging Email | Send email via Messaging Service.  
Send Unified Messaging SMS | Send SMS via Messaging Service.  
View Email Messaging Setup | View email objects in Salesforce Setup.  
View SMS Messaging Setup | View SMS objects in Salesforce Setup.  
  
## Flow Permissions in Marketing Cloud Next

These permissions are available in the App Permissions list for a permission set.

Name | Description  
---|---  
Activate or Deactivate Flows | Allow users without the Manage Flow user permission to activate and deactivate flows in the Automation or Marketing apps.  
Add Assignment Element to Flows | Allow users without the Manage Flow user permission to add the Assignment element to flows in the Automation or Marketing apps.  
Add Collection Filter Element to Flows | Allow users without the Manage Flow user permission to add the Collection Filter element to flows in the Automation or Marketing apps.  
Add Collection Sort Element to Flows | Allow users without the Manage Flow user permission to add the Collection Sort element to flows in the Automation or Marketing apps.  
Add Create Records Element to Flows | Allow users without the Manage Flow user permission to add the Create Records element to flows in the Automation or Marketing apps.  
Add Decision Element to Flows | Allow users without the Manage Flow user permission to add the Decision element to flows in the Automation or Marketing apps.  
Add Delete Records Element to Flows | Allow users without the Manage Flow user permission to add the Delete Records element to flows in the Automation or Marketing apps.  
Add Get Records Element to Flows | Allow users without the Manage Flow user permission to add the Get Records element to flows in the Automation or Marketing apps.  
Add Loop Element to Flows | Allow users without the Manage Flow user permission to add the Loop element to flows in the Automation or Marketing apps.  
Add Path Experiment Element to Flows | Allow users without the Manage Flow user permission to add the Path Experiment element to flows in the Automation or Marketing apps.  
Add Subflow Element to Flows | Allow users without the Manage Flow user permission to add the Subflow element to flows in the Automation or Marketing apps.  
Add Transform Element to Flows | Allow users without the Manage Flow user permission to add the Transform element to flows in the Automation or Marketing apps.  
Add Update Records Element to Flows | Allow users without the Manage Flow user permission to add the Update Records element to flows in the Automation or Marketing apps.  
Add Wait Element to Flows | Allow users without the Manage Flow user permission to add the Wait for Amount of Time element, the Wait Until Date element, and the Wait for Conditions element to flows in the Automation or Marketing apps.  
Can Marketing User Debug Marketing Flows | Allow Marketing Cloud users to debug flows.  
Create or Edit Flows | Allow users without the Manage Flow user permission to create and edit flows in the Automation or Marketing apps.  
Create or Modify Automation Event-Triggered Flows | Allow users without the Manage Flow user permission to create, edit, and delete automation event-triggered flows in the Automation or Marketing apps.  
Create or Modify Flows with Data Graph Event Triggers | Allow users without the Manage Flow user permission to create, edit, and delete automation event-triggered flows with data graph change triggers in the Automation or Marketing apps.  
Create or Modify Form-Triggered Flows | Allow users without the Manage Flow user permission to create, edit, and delete form-triggered flows in the Automation or Marketing apps.  
Create or Modify Segment-Triggered Flows | Allow users without the Manage Flow user permission to create, edit, and delete segment-triggered flows in the Automation or Marketing apps.  
Delete Flows | Allow users without the Manage Flow user permission to delete flows in the Automation or Marketing apps.  
Run Flows | Allow users in the org to run any active flow. In Experience Builder sites, run any active flow that's distributed with the Flow Lightning component.  
View All Non-Admin Flows | Allow users without the Manage Flow or View All Data user permissions to see all flows with associated flow records in the Automation or Marketing apps, regardless of sharing settings.  
View Flows | Allow users without the Manage Flow user permission to view flows shared with them in the Automation or Marketing apps.  
  
## Objects Access

These permissions are available in the System Permissions list for a permission set.

Name | Related Cloud or Feature  
---|---  
Calculated Insight Fields | Data 360  
Calculated Insight Object | Data 360  
Calculated Insight Object Definitions | Data 360  
Campaigns | Marketing Cloud Next, Sales Cloud  
Communication Subscription Channel Types | Privacy Center, consent settings  
Communication Subscription | Privacy Center, consent settings  
Data Connections | Data 360  
Data Connector Credentials | Data 360  
Data Connectors for GCS | Data 360  
Data Connectors for Interaction Studio | Data 360  
Data Connectors for Marketing Cloud | Data 360  
Data Connectors for S3 | Data 360  
Data Connectors for Sftp | Data 360  
Data Connectors for Upload | Data 360  
Data Lake Fields | Data 360  
Data Lake Object Definitions | Data 360  
Data Model Domain Capability Usage | Data 360  
Data Model Fields | Data 360  
Data Model Objects | Data 360  
Data Model Relation Constraints | Data 360  
Data Model Taxonomies | Data 360  
Data Object Categories | Data 360  
Data Platforms | Data 360  
Data Source Objects | Data 360  
Data Sources | Data 360  
Data Source Tenants | Data 360  
Data Space Definitions | Data 360  
Data Spaces | Data 360  
Data Transport Fields | Data 360  
Data Transport Object | Data 360  
Engagement Channel Types | Privacy Center, consent settings  
External Data Connectors | Data 360  
Field Source Target Relationships | Data 360  
Ingestion API Data Connectors | Data 360  
Internal Data Connectors | Data 360  
Market Segment Definitions | Data 360  
Mobile App Data Connectors | Data 360
