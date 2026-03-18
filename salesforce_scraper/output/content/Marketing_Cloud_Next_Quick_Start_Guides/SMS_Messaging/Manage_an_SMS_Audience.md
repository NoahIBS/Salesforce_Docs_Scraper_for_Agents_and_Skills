<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start_manage_audience.htm&language=en_US&type=5 -->

# Quick Start: Manage Your SMS Audience

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Quick Start: Manage Your SMS Audience

After you’ve completed the setup prerequisites for SMS and requested your brand, campaign, and code, it’s time to create subscriptions to manage audiences and consent for your SMS messages.

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and Salesforce Message Credits - SMS add-on  
---  
User permissions needed  
---  
To manage settings in Salesforce Setup: | System Administrator profile AND Marketing Cloud Admin permission set  
To manage settings in Data 360: | Data Cloud Architect permission set  
  
Included in this guide: 

[](https://help.salesforce.com/s?language=en_US)

  * Update Subscriptions
  * Import Consent Data
  * Add Consent to Lead and Contact Pages



[](https://help.salesforce.com/s?language=en_US)

## Update a Communication Subscription 

We preconfigured a standard communication subscription called Marketing and added it to your SMS Preference Center page by default. To add a new SMS code, you can edit this subscription or create a custom one.

Before you begin, make sure that your Marketing Cloud Admin has completed the required setup steps to send SMS messages in Marketing Cloud Next. See [Quick Start: Set Up SMS Prerequisites](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start.htm&language=en_US&type=5 "This Quick Start guide covers the preliminary steps that are required to send SMS messages with Marketing Cloud Next using United States and Canada 10-digit long codes \(10DLC\). It outlines the simplest implementation, so that your team can get up and running. For in-depth information, special features, or customization options, we provide additional resources along the way.") and [Quick Start: Request an SMS Brand, Campaign, and Code](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start_request_assets.htm&language=en_US&type=5 "Now that you’ve completed the prerequisites, it’s time to request a brand, campaign, and code to send SMS messages in the United States and Canada. Every SMS send from a 10DLC in the United States and Canada requires an approved brand, campaign, and code.").

  1. In Setup, in the Quick Find box, enter `Consent`.
  2. Under **Preference Pages and Subscriptions** , select a subscription from the dropdown, and then click **Edit**.
  3. Select a SMS Sender Code to relate to the selected subscription, and save your work.
  4. Click **Update**.



If you wish to create an SMS-specific subscription, see [Create a Communication Subscription](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_comm_sub_create.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Import Consent Data

Unified Messaging manages SMS consent via communication subscriptions. An SMS code can be mapped to one or more communication subscriptions. 

Before you import consent data, make sure the contact points exist in Marketing Cloud Next.

  1. [Prepare in import CSV](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_import_format.htm&language=en_US&type=5).
     * The file must include a column for phone numbers and a separate column for recording the date of consent.
     * For each entry, you must include a country code and the complete phone number. Phone numbers are validated based on [ITU E.164 standards](https://www.itu.int/rec/T-REC-E.164/en), such as +1-555-555-5555. 
     * Spaces, dashes, underscores, and parentheses are automatically removed from phone numbers.
     * Phone numbers can’t include letters or special characters. 
  2. From Setup, in the Quick Find box, enter `Consent`. 
  3. Under Unified Messaging, select **Consent Imports**. 
  4. Click **Import**.
  5. Select the SMS channel, a communication subscription, and a sender code.
  6. Select a consent status to apply to all of the imported contacts, and then click **Next**. 
  7. Upload your CSV, and then click **Next**. 
  8. Preview the import fields, and then click **Import**.



[](https://help.salesforce.com/s?language=en_US)

## Add Consent to Lead and Contact Pages

To review the consent data, add the consent component to lead and contact page layouts. 

  1. Open a Contact or Lead page.
  2. To open the Lightning App Builder, click the profile icon in the toolbar, and then select **Edit Page**.
  3. Drag the Privacy Consent Status component to the related list tab on the page layout. [](https://help.salesforce.com/s?language=en_US)
  4. Save your work.



Here are some features and common enhancements that you can implement alongside the recommendations in this Quick Start guide.

Customization enhancement | Admin Needed | description  
---|---|---  
Set up a URL-shortening domain | Salesforce Admin | Enhance your brand recognition by using a custom domain for links shortened with the Marketing Cloud Engagement shortener. See [_Create a Branded Domain for Unified Messaging_](https://help.salesforce.com/s/articleView?id=mktg.um_set_up_branded_domain.htm&language=en_US&type=5).  
Manage reply SMS messages | Salesforce Admin | Plan how to respond when recipients reply to marketing messages. See [_Set Up an SMS Conversation in Unified Messaging_](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_conversation.htm&language=en_US&type=5).
