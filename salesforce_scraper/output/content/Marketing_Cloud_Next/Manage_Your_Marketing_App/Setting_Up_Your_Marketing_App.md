<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_overview.htm&language=en_US&type=5 -->

# Getting Started with Marketing Cloud Next Setup

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Getting Started with Marketing Cloud Next Setup

To get started with Marketing Cloud Next, complete some basic settings, then continue through the required and recommended steps. The time it takes to complete setup depends on the features that you want to use.

### Required Editions

Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
Note If you want to set up Marketing Cloud Next only for sending email, check out the [Quick Start Guides](https://help.salesforce.com/s/articleView?id=mktg.mktg_quick_start_parent.htm&language=en_US&type=5 "If you're new to Marketing Cloud Next, get up and running with a quick start guide. Quick start guides focus on a single marketing channel and walk you through the simplest, most direct path to accomplish your goals."). 

[](https://help.salesforce.com/s?language=en_US)

## Prepare for Setup

Before you start, make sure that you have the necessary roles and permissions. Most tasks require a Salesforce admin (System Administrator profile) with the Marketing Cloud Admin permission set and Data Cloud Architect permission set. See [Manage Permission Set Assignments](https://help.salesforce.com/s/articleView?id=platform.perm_sets_manage_assignments.htm&language=en_US&type=5) and [User Permissions in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_permissions_ref.htm&language=en_US&type=5 "Marketing Cloud Next comes with two permission sets: Marketing Cloud Admin and Marketing Cloud Manager. Many individual permissions are available for managing access more granularly throughout the app. The permissions list can help you build a custom permission set or troubleshoot access issues.").

Salesforce admin (System Administrator profile)
    A Salesforce admin has permissions to complete tasks in Salesforce Setup, which you can access by clicking [](https://help.salesforce.com/s?language=en_US) on any page.
Data Cloud Architect
    A Data Cloud Architect has permissions in Data 360 Setup and on other data modeling objects. To add this critical infrastructure to your org, a Marketing Cloud Next admin must install data kits and deploy data streams. These admins also configure identity resolution and people scoring rules.
Marketing admin
    A marketing admin is any user with the Marketing Cloud Admin permission set. Users with this permission can configure most settings on Salesforce Setup pages and publish and activate campaigns and segments.

[](https://help.salesforce.com/s?language=en_US)

## Access the Setup Assistant

The Marketing Cloud Next setup assistant guides you through the required and recommended tasks. To access the setup assistant page, click . From the Quick Find box, enter `Marketing Cloud`. Then, under Assisted Setup, select **Assistant Home**. 

The setup assistant home page includes three sections: Basic Settings, Required Setup, and Additional Settings. Each section shows you how many steps are left based on the checkboxes that you select as you complete the tasks on each page.

You can also track your progress with the [Setup checklist](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/mktg_setup_checklist_sp25.pdf). 

Before you can access all the required and additional settings, you must first go to Basic Settings and enable Marketing Cloud Next.

[](https://help.salesforce.com/s?language=en_US)

## Enable Marketing Cloud Next

Estimated time: Up to 15 minutes

On the Basic Settings page, review the list of required tasks. Most of these tasks begin automatically when Salesforce adds functionality to your org. After each task is complete, click to enable Marketing Cloud Next, and then start the automated process of connecting the necessary content and privacy tools.

To successfully complete all of the prerequisites, you must first enable Data 360. If you run into issues, here are some troubleshooting notes for each task.

Step | Troubleshooting notes  
---|---  
Enable Data 360 | In the App Launcher, search for and select **Data 360**. Click  to access Data 360 Setup and enable it. A Data Cloud Architect is required to complete this process.  
Create a Salesforce CRM connector | In Data 360 Setup, open the Connectors page, and click **New**. Select Salesforce CRM and follow the prompts. A Data Cloud Architect is required to complete this process.  
Add a default email channel | The default email channel in Salesforce CMS is where marketing emails are stored. An admin can’t create this channel. Contact Salesforce Customer Support for help.  
Add data protection details to records | From Setup, in the Quick Find box, enter `Data Protection and Privacy`, and then select **Data Protection and Privacy**. Select the option to make data privacy data protection details available in records.  
Select a data space | Every active data space that’s configured in Data 360 appears in the dropdown, including the default data space. To learn more about data spaces, including how to create a new data space, see [Manage Data Spaces](https://help.salesforce.com/s/articleView?id=data.c360_a_data_spaces.htm&language=en_US&type=5).  
Other | If the content management or privacy tools aren’t created, contact Salesforce Customer Support.  
  
Note To use these content tools with Government Cloud, manually enable the content delivery network. See [Marketing Cloud Next in Government Cloud](https://help.salesforce.com/s/articleView?id=ind.government_cloud_marketing_cloud.htm&language=en_US&type=5).

## Complete the Basic Settings and Continue Setup

Estimated time: Variable

Next, [install the data kits](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.") and [configure your identity resolution rulesets](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_identity_resolution.htm&language=en_US&type=5 "Identity resolution is a critical step to organizing and unifying your data. Usually, when your data originates from many systems, it’s modeled and labeled differently in each place. Identity resolution rulesets define the relationships among data model objects \(DMOs\) and their fields. After you configure these rules, Data 360 can organize related and duplicate data into unified individual records that marketers can use to target audiences."). These tasks are on the same Basic Settings page where you enabled Marketing Cloud Next.

The remaining pages of setup provide you with shortcuts to other required tasks, such as authenticating an email domain for sending and setting up reporting features.

Setup also includes recommended tasks to help you make the most of Marketing Cloud Next, like activating AI features or customizing your domain.

#### See Also

  * [ _Implementation Guide:_ Marketing Cloud](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/mktg_implementation_guide.pdf)


