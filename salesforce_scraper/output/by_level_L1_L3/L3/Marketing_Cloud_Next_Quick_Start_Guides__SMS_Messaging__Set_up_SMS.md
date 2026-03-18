<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start.htm&language=en_US&type=5 -->

# Quick Start: Set Up SMS Prerequisites

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Quick Start: Set Up SMS Prerequisites

This Quick Start guide covers the preliminary steps that are required to send SMS messages with Marketing Cloud Next using United States and Canada 10-digit long codes (10DLC). It outlines the simplest implementation, so that your team can get up and running. For in-depth information, special features, or customization options, we provide additional resources along the way. 

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and Salesforce Message Credits - SMS add-on  
---  
User permissions needed  
---  
To manage settings in Salesforce Setup: | System Administrator profile AND Marketing Cloud Admin permission set  
To manage settings in Data 360: | Data Cloud Architect permission set  
  
[](https://help.salesforce.com/s?language=en_US)

Included in this guide: 

[](https://help.salesforce.com/s?language=en_US)

  * Identify Admins and Assign Permissions
  * Enable Marketing Cloud Next
  * Install Data Kits
  * Map an E164 Phone Number
  * Configure Identity Resolution
  * Set Up Reporting 



[](https://help.salesforce.com/s?language=en_US)

## Identify Admins and Assign Permissions

When you configure Marketing Cloud Next, you work in Salesforce Setup, Data 360, and Data Cloud Architect Setup. Before you can begin, make sure you or other admins on your team have the necessary roles and permissions.

  1. From Setup, in the Quick Find box, enter `Users`, and then select **Users**.
  2. Select a user.
  3. In the Permission Set Assignments related list, click **Edit Assignments**.
  4. Under Available Permission Sets, select the permission sets you want to add, and then click **Add**.
     * Marketing Cloud Admin—Users who have this permission set can configure most settings in Salesforce Setup. They can also publish and activate campaigns and segments.
     * Data Cloud Architect—Users who have this permission set can configure settings in Data 360 setup and on other data modeling objects.
  5. To remove a permission set assignment, select it under Enabled Permission Sets, and then click **Remove**.
  6. Save your changes.



To learn more about user access in Marketing Cloud Next, including how to add workspace and site contributors, check out [User Permissions in Marketing Cloud Next ](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_permissions_ref.htm&language=en_US&type=5 "Marketing Cloud Next comes with two permission sets: Marketing Cloud Admin and Marketing Cloud Manager. Many individual permissions are available for managing access more granularly throughout the app. The permissions list can help you build a custom permission set or troubleshoot access issues.") and [Manage User Access](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_user_access.htm&language=en_US&type=5 "Add users and assign roles and permissions to make sure your team can access the necessary tools to complete their work in Marketing Cloud Next."). 

[](https://help.salesforce.com/s?language=en_US)

## Enable Marketing Cloud Next

Next, go to **Setup** | **Marketing Cloud** | **Basic Settings**. In the Enable Marketing Cloud section, confirm that each task is complete. Then, click **Enable** to start the automated process of connecting the necessary content and privacy tools.

To troubleshoot or learn more about the prerequisites, check out [Getting Started with Marketing Cloud Next Setup](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_overview.htm&language=en_US&type=5 "To get started with Marketing Cloud Next, complete some basic settings, then continue through the required and recommended steps. The time it takes to complete setup depends on the features that you want to use.").

[](https://help.salesforce.com/s?language=en_US)

## Install Data Kits

On the Basic Settings page, click **Install** to get data kits that are required to work with marketing data. This process automatically installs each data kit and deploys the related data streams in Data 360.

This process may take a few minutes. Refresh the page to confirm everything installed and deployed successfully. To learn more about the data kit install and deployment process, see [Install and Deploy Data Streams](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.").

Note When one or more of the required marketing data kits needs an update, we’ll let you know so you can return to the setup assistant and get the latest versions.

[](https://help.salesforce.com/s?language=en_US)

## Map an E164 Phone Number 

To include Normalized Phone in an Identity Resolution ruleset, you must manually map an E164 formatted phone number to the contact point phone. 

  1. In the Data 360 Data Streams tab, select the **Contact** data stream. 
  2. Under Data Mapping, click **Review**. 
  3. Map the Business Phone field on the Contact DLO to the Formatted E164 Phone Number field on the Contact Point Phone DMO.
  4. Save your work and repeat these steps on the Lead object.



[](https://help.salesforce.com/s?language=en_US)

## Configure Identity Resolution

You’re almost done setting up your marketing data environment. The next step is to tell Salesforce how you want to unify your customer data by creating an identity resolution ruleset. You can quickly generate a default ruleset that uses Normalized Phone as a match rule, or configure a custom ruleset.

[](https://help.salesforce.com/s?language=en_US)Note Identity resolution rulesets consume Data 360 credits, which impacts billing. We recommend having only one active ruleset for the Individual object, and one ruleset for the Account object. Maintaining two rulesets per object increases the amount that you’re billed for identity resolution. See [Data 360 Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5). 

[](https://help.salesforce.com/s?language=en_US)

  1. On the Basic Settings page, scroll to the Identity Resolution Rulesets section.
  2. In the Unified Individual section, click **Generate Ruleset**.
  3. Review the confirmation details and click **Generate**.
  4. Confirm that your new ruleset is published. [](https://help.salesforce.com/s?language=en_US)
     1. In Data 360, go to **Identity Resolutions**.
     2. Next to the Identity Resolution ruleset that you generated, confirm that the ruleset status is published.



[](https://help.salesforce.com/s?language=en_US)

To learn more, including steps for how to create a custom ruleset for both the Individual and Account objects, see [Configure Identity Resolution Rulesets](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_identity_resolution.htm&language=en_US&type=5 "Identity resolution is a critical step to organizing and unifying your data. Usually, when your data originates from many systems, it’s modeled and labeled differently in each place. Identity resolution rulesets define the relationships among data model objects \(DMOs\) and their fields. After you configure these rules, Data 360 can organize related and duplicate data into unified individual records that marketers can use to target audiences.").

[](https://help.salesforce.com/s?language=en_US)

## Set Up Reporting

After you finish setting up your channel, your last task is to configure your reporting tools. First, install Marketing Performance to get insights and dashboards powered by Tableau. Then, install the marketing analytics packages that include additional preconfigured dashboards and folders with reporting data about your marketing efforts. Finally, make sure users can access analytics folders. 

[](https://help.salesforce.com/s?language=en_US)

  1. Install Marketing Performance.

Using the Marketing Performance feature consumes Data 360 credits, which can increase your bill. Learn more about the billing impact of Data 360-powered features.

[](https://help.salesforce.com/s?language=en_US)
     1. From Setup, in the Quick Find box, enter `Marketing` and click **Marketing Performance**.
     2. In the Install Marketing Performance section, click **Install**.
     3. Assign the Tableau Next Included App Business User permission set to any users who require access to Marketing Performance data.
     4. In the Marketing app, go to the Marketing Performance tab to view the main dashboard and confirm that your install is complete. 
  2. Install the additional analytics packages. [](https://help.salesforce.com/s?language=en_US)
     1. From Setup, in the Quick Find box, enter `Reporting`. Under Marketing Setup, click **Reporting and Optimization**.
     2. From the Analytics Packages section, install the Marketing Engagement Analytics package and Flow Reports Analytics Package for all users. To learn more about these packages, see [Set Up Analytics Reports and Dashboards](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_reports.htm&language=en_US&type=5 "Marketing analytics packages include preconfigured dashboards and folders with reporting data about your marketing efforts.").
  3. From the Marketing app, make folders available to users. [](https://help.salesforce.com/s?language=en_US)
     1. On the Analytics tab, click **Browse** (1), and select **Folders** (2). For each report or dashboard folder, click and select **Share**.

[](https://help.salesforce.com/s?language=en_US)

     2. For each report or dashboard folder, click [](https://help.salesforce.com/s?language=en_US), and then select **Share**.
     3. For Entire Organization, set the access to **Viewer**.
     4. To add other users or groups, such as editors or managers, search for them in the Name field, and then apply the correct role.
     5. Save your changes.



[](https://help.salesforce.com/s?language=en_US)

To learn more about reporting and dashboards, see [Measure Success](https://help.salesforce.com/s/articleView?id=mktg.mktg_reporting.htm&language=en_US&type=5 "Monitoring performance and reporting on your successes are a significant part of a marketer’s job. Marketing Cloud Next includes reporting options powered by Data 360 and Tableau Next."). 

[](https://help.salesforce.com/s?language=en_US)Note To avoid data processing issues, preserve field visibility for the Data 360 Salesforce Connector permission set. Visibility can change when you delete a field, change the permissions on a field, or change the API name for a custom field.

Now that you’ve set up your SMS prerequisites, it’s time to request your brand, campaign, and 10-digit long code (10DLC).
