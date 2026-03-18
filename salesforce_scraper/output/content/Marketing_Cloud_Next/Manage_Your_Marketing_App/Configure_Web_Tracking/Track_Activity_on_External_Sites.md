<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_external.htm&language=en_US&type=5 -->

# Track Activity on External Sites

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Track Activity on External Sites

Track visitor activities on web pages hosted outside of Salesforce, such as your company website. To protect the privacy of your site visitors, use the default consent banner to collect consent to track. You’re responsible for complying with privacy laws and regulations applicable to your business.

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To configure external tracking: | Marketing Cloud Admin permission set  
  
  * If you’re setting up external tracking for the first time, create a website connector, and then create embed code that you add to your external site.
  * If you've set up external tracking before Winter ‘26, update your external tracking configuration.
  * Apply and customize a consent banner for activity tracking on your website.



#### See Also

  * [ _Knowledge Article:_ Data Cloud: Salesforce CRM Data Stream Refresh Errors due to Missing Field or Object](https://help.salesforce.com/s/articleView?id=000395797&language=en_US&type=1)



[](https://help.salesforce.com/s?language=en_US)

## Create External Tracking Configuration

First, create a website connector that collects activity data from your external site. Then, create the embed code to add to your external site, and associate it with your website connector and a campaign. 

Important In most cases, you can reuse the same website connector for multiple embed codes. However, if you’re a Data Cloud One user, create and use a unique website connector for each org that has web tracking enabled.

[](https://help.salesforce.com/s?language=en_US)

  1. Create a website connector.
     1. From Setup, in the Quick Find box, enter `Web Tracking`, and then select **Website Connectors**.
     2. Click **New**.
     3. Name the website connector and click **Create**.
  2. Create the embed code.
     1. From Setup, in the Quick Find box, enter `Web Tracking`, and then select **Webpage Embed Codes**. 
     2. Click **New**. 
     3. Name the embed code and select a website connector.
     4. In the Configure Tracking Settings section, choose whether to require consent to track external pages that include the embed code. This setting is on by default. You're responsible for complying with privacy laws and regulations applicable to your business.
     5. Select a campaign to associate with the engagement data.
     6. Click **Create**.
  3. To turn on data collection on your website, copy the embed code and add it to your website’s head tag.



[](https://help.salesforce.com/s?language=en_US)

## Update External Tracking Configuration

If you set up external tracking before Winter ‘26, update your external tracking configuration to access the latest feature updates. Copy the web tracking script, and replace the existing script on your website.

  1. From the Website Connectors page, configure your web tracking connector.

Important If you don't see your connectors and you created them before Summer ’25, contact Salesforce Customer Support to regain access to your website connectors with required updates.

  2. Copy the embed code and replace the existing code in your webpage's head tag.

Note For accurate reporting of your website data, replace the script on your website. 

  3. Save your changes.


