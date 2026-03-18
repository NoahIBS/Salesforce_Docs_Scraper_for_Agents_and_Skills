<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_email_quick_start.htm&language=en_US&type=5 -->

# Quick Start: Set Up Email Sending

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Quick Start: Set Up Email Sending

This Quick Start guide covers the steps that are required to send email with Marketing Cloud Next. It outlines the simplest implementation, so that your team can get up and running. For in-depth information, special features, or customization options, we provide additional resources along the way.

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
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
  * Configure Identity Resolution
  * Set Up Email
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

## Set Up Reporting

After you finish setting up your email channel, your last task is to configure your reporting tools. First, install Marketing Performance to get insights and dashboards powered by Tableau. Then, install the marketing analytics packages that include additional pre-configured dashboards and folders with reporting data about your marketing efforts. Finally, make sure users can access analytics folders.

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

     2. For each report or dashboard folder, click [](https://help.salesforce.com/s?language=en_US) and select **Share**.
     3. For Entire Organization, set the access to **Viewer**.
     4. To add other users or groups, such as Editors or Managers, search for them in the Name field, and then apply the correct role.
     5. Save your changes.



[](https://help.salesforce.com/s?language=en_US)

To learn more about reporting and dashboards, see [Measure Success](https://help.salesforce.com/s/articleView?id=mktg.mktg_reporting.htm&language=en_US&type=5 "Monitoring performance and reporting on your successes are a significant part of a marketer’s job. Marketing Cloud Next includes reporting options powered by Data 360 and Tableau Next.").

[](https://help.salesforce.com/s?language=en_US)Note To avoid data processing issues, preserve field visibility for the Data Cloud Salesforce Connector permission set. Visibility can change when you delete a field, change the permissions on a field, or change the API name for a custom field.

[](https://help.salesforce.com/s?language=en_US)

## Next Steps: Optional Features, Channels, and Customization

Here are some features and common enhancements that you can implement alongside the streamlined recommendations in this Quick Start guide.

Enhancement | Admin needed | Description  
---|---|---  
Enable AI features | Salesforce Admin | Salesforce Admin Use generative AI and predictive AI to save time and improve your KPIs. See [Enable AI Features](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_einstein.htm&language=en_US&type=5 "Marketing Cloud Next includes features that use generative AI and predictive AI to save time and improve your key performance indicators \(KPIs\). These features aren’t dependent on each other, so you can choose the features that best fit the needs of your business.").  
Set up personalization | Data Cloud Architect | Let users personalize their email with dynamic content blocks and cross-object merge fields. See [Enable Personalization Features](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5 "When you personalize marketing messages using merge fields or dynamic content, you can improve the customer experience and increase engagement. Before you can start personalizing content, set up Personalization and configure a data graph based on the Unified Individual object. A data graph is also necessary for personalizing flow decisions.").  
Manage reply emails | Salesforce Admin | Plan how to respond when email recipients reply to marketing messages. See [Configure Reply Mail Management](https://help.salesforce.com/s/articleView?id=mktg.um_channel_email_rmm.htm&language=en_US&type=5).  
Add channels | Salesforce Admin | You can also send SMS and WhatsApp messages, publish landing pages, and embed forms on landing pages or your external site. See[ Manage Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content.htm&language=en_US&type=5 "Marketing Cloud Next provides the tools you need to create and store a variety of content to support your marketing efforts. The Content tab, powered by Salesforce CMS, is where you can organize your content in workspaces and folders. When you’re ready to create something new, create or clone and then edit a variety of marketing-specific content types in a consistent editing environment.").
