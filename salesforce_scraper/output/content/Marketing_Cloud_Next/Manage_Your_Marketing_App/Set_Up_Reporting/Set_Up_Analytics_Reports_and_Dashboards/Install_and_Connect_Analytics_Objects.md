<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_install_analytics.htm&language=en_US&type=5 -->

# Install and Connect Analytics Objects

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Install and Connect Analytics Objects

Install the analytics packages and add users to analytics folders. Then, head to Digital Experiences to finalize the data connection.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To install data kits and packages: | View Setup and Configuration ORSystem Administrator profileORMarketing Cloud Admin permission set  
To deploy data streams: | Data Cloud Architect permission set  
To add Digital Experiences integrations: | Content Admin role  
To customize the Analytics tab: | Marketing Cloud Admin permission setORMarketing Cloud Manager permission set  
  
Before you install the analytics packages, make sure to [install and deploy the required marketing data kits](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.").

[](https://help.salesforce.com/s?language=en_US)

  1. From Setup, in the Quick Find box, enter `Marketing Cloud`. Under Reporting and Optimization, select **Analytics**.
  2. From the Analytics Packages section, install the Marketing Engagement Analytics package for all users.
  3. (Optional) If you’re using the SMS add-on, repeat these steps for the SMS Analytics package.
  4. (Optional) Configure tracking and analytics for the default Marketing Landing Pages site. [](https://help.salesforce.com/s?language=en_US)
     1. From Setup, in the Quick Find box, enter `All Sites`. Under Digital Experiences, click **All Sites**.
     2. Next to Marketing Landing Pages, select **Builder**.

Landing pages in Marketing Cloud Next are served using the Data 360 Sites framework. This site operates behind the scenes—don’t add content to it.

     3. Click **Settings** and select **Integrations**.

[](https://help.salesforce.com/s?language=en_US)

     4. On the Data Cloud tile, click **Add to Site**.
     5. (Optional) To collect engagement metrics and consent for tracking on landing pages, add the Data 360 Web Tracking Consent Banner integration. Then, in the site toolbar, click **Publish**.

If you don’t need to track consent, skip this step and see [Activity Tracking for Landing Pages](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_parent.htm&language=en_US&type=5 "Track visitor activities and engagement across your marketing web pages. Use the data to create more targeted segments and inform your marketing strategy. You can track activity on landing pages hosted by Marketing Cloud Next and on external websites.").

     6. From Setup, in the Quick Find box, enter `Marketing Cloud`. Under Reporting and Optimization, select **Analytics**.
     7. Install the [Landing Pages and Forms Analytics package](https://login.salesforce.com/packaging/installPackage.apexp?p0=04t1Q000001MpYO) for all users.
  5. From the Marketing app, make folders available to users. [](https://help.salesforce.com/s?language=en_US)
     1. On the Analytics tab, click **Browse** (1), and select **Folders** (2).

[](https://help.salesforce.com/s?language=en_US)

     2. For each report or dashboard folder, click [](https://help.salesforce.com/s?language=en_US) and select **Share**.
     3. For Entire Organization, set the access to Viewer.
     4. To add other users or groups, such as Editors or Managers, search for them in the Name field, and then apply the correct role.
     5. Save the changes.



[](https://help.salesforce.com/s?language=en_US)

To avoid data processing issues, preserve field visibility for the Data 360 Salesforce Connector permission set. Visibility can change when you delete a field, change the permissions on a field, or change the API name for a custom field.
