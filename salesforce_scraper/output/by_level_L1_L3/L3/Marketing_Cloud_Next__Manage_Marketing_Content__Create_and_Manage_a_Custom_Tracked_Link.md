<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_custom_link_create.htm&language=en_US&type=5 -->

# Create and Manage a Custom Tracked Link

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage a Custom Tracked Link

A custom tracked link reports clicks from content that you manage outside of Marketing Cloud Next, such as an ad, that points to a connected external website.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create a tracked link: | Marketing Cloud Manager permission set ANDAny CMS workspace contributor role  
  
[](https://help.salesforce.com/s?language=en_US)

## Create a Tracked Link

Tracked links collect data from site visitors. You’re responsible for complying with privacy laws and regulations applicable to your business. To protect the privacy of your site visitors, use the default consent banner on your external website to collect consent to track. You can have up to 50 tracked links.

  1. Verify that [web tracking is configured](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_external.htm&language=en_US&type=5) for the external site that your link will point to.
  2. From your marketing workspace, click Add, and then select **Content**.
  3. Select **Tracked Link** as the content type and then click **Create**.
  4. Select a campaign to attribute click activity to.
  5. Enter a destination URL.

This URL must point to a page on an external website that’s configured to track activity back to Marketing Cloud Next.

  6. Enter any applicable UTM parameters for your tracked link.
  7. Save your work, and then publish the tracked link.



After you create and publish a tracked link, copy the URL from the content detail page. You can use the link in any piece of content.

[](https://help.salesforce.com/s?language=en_US)

## Unpublish a Tracked Link

To disable a tracked link and stop collecting data from it, unpublish the link. Before you unpublish a link, remove it from any content or set up a redirect URL

  1. From your marketing workspace, open a tracked link, and then click **Unpublish**.
  2. Review the warnings, and determine if any other changes are needed, and then click **Next**.
  3. Decide when to publish the link.
     * To unpublish the link immediately, click **Unpublish Now**.
     * To unpublish the link at a later date, click **Schedule Unpublish** , and enter a date and time. Then, click **Schedule**.


