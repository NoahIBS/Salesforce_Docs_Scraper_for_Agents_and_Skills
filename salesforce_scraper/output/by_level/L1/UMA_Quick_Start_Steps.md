<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.resource_nextgen_quick_start_steps.htm&language=en_US&type=5 -->

# UMA Quick Start Steps

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# UMA Quick Start Steps

Step blocks with task IDs that can be used to conref common tasks into new Quick Start guides. Use the resource_nextgen_quick_start_template_admin file in the Resource folder to get started with a Quick Start guide. 

### Required Editions

User permissions needed  
---  
To manage settings in Salesforce Setup: | System Administrator profile AND Marketing Cloud Admin permission set  
To manage settings in Data 360: | Data Cloud Architect permission set  
  
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

## Configure Identity Resolution

You’re almost done setting up your marketing data environment. The next step is to tell Salesforce how you want to unify your customer data by creating an identity resolution ruleset. Quickly generate a default ruleset that uses Normalized Email as a match rule, or configure a custom ruleset.

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

## Set Up Email

To send emails with Marketing Cloud Next, you must authenticate a domain for sending, verify at least one sender email address, and provide a physical address to include in your email.

  1. Work with your IT team to authenticate a domain for sending.
     1. From Setup, in the Quick Find box, enter `Authenticated Domains`, and then select **Email Authenticated Domains**. 
     2. Click **Add Domain**.
     3. Review the confirmation modal and click **Continue**. 
     4. Enter the subdomain information that you want to use for sending, and then click **Submit**.
     5. (Optional) To customize the email address for sending, click **Create New** and edit the Display Name and Username fields.
     6. Configure your DNS records with your domain registrar.
     7. After you complete the configuration process, verify that you completed the DNS record upload and click **Verify Domain**.
  2. Add or update the physical address. This is the address that's populated in your emails by the Physical Address merge field.

To maintain regulatory compliance, all marketing and transactional emails must include a physical address.

     1. From Setup, in the Quick Find box, enter `Company`, and then select **Company Information**.
     2. In the Organization Detail section, review or edit the Address details.
     3. Save your changes.



To add more From addresses, check out [Authenticate a From Address for Unified Messaging](https://help.salesforce.com/s/articleView?id=mktg.um_channel_email_from_address.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Import Leads and Contacts

To get started, add the leads and contacts you want to market to. If you already have all your leads and contacts in Salesforce, skip this step.

  1. From the Leads or Contacts tabs, click **Import**.
  2. Follow the steps to upload a CSV file. If you don’t have a CSV file yet, download the sample file from the import window and add your data.




After an import is complete, we send a notification email to the user who imported the file.

[](https://help.salesforce.com/s?language=en_US)

## Add a Segment to a Campaign

To create a recipient list, you use Data 360 segments. The easiest way to create a segment is by working from the campaign record and using quick filters.

  1. From the campaign record, click **Select Segment** , and then select **Use Quick Filters**.
  2. Select one or more filters.

  3. If you’re using multiple filters, select filtering logic for your segment, and then click **Create**.

AND returns results that match all of the filters together. OR returns results that match any of the filters.

  4. From the campaign record, click **Publish**. A segment must be published for people to receive your messages.
  5. Allow some time for the segment to publish and then refresh the page.
  6. After the segment is published, click **Preview** to review a sample of the people in your segment.



