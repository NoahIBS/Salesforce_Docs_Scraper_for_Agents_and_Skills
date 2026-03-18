<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_configure_web_tracking_for_a_business_unit.htm&language=en_US&type=5 -->

# Configure Web Tracking for a Business Unit

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure Web Tracking for a Business Unit

To track visitor activities for your campaign on external web pages, create a website connector that collects activity data from your external site. Then, create the embed code to add to your external site, and associate it with your website connector, business unit, and a campaign. You can then copy the embed code to your website. 

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To configure web tracking: | Marketing Cloud Admin permission set  
  
For more information about considerations and compliance details with activity tracking, see [Considerations for Activity Tracking](https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_considerations.htm&language=en_US&type=5).

  1. Create a website connector.
     1. From Setup, in the Quick Find box, enter `Web Tracking`, and then select **Website Connectors**.
     2. Click **New**.
     3. Name the website connector and click **Create**.
  2. Create the embed code.
     1. From Setup, in the Quick Find box, enter `Web Tracking`, and then select **Webpage Embed Codes**. 
     2. Click **New**. 
     3. Name the embed code and select a website connector.
     4. Select a business unit to associate with the embed code.
     5. In the Configure Tracking Settings section, select whether to require consent to track external pages that include the embed code. This setting is on by default. You're responsible for complying with privacy laws and regulations applicable to your business.
     6. Select a campaign to associate with the engagement data. 
     7. Click **Create**.
  3. To enable data collection on your website, copy the embed code and add it to your website’s head tag.
  4. If necessary, configure and apply the web consent banner.

For more information, see [Customize the Consent Banner](https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_consent_banner.htm&language=en_US&type=5)



