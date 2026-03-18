<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_consent.htm&language=en_US&type=5 -->

# Ensure Compliance with Consent Settings

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Ensure Compliance with Consent Settings

Marketing Cloud Next can help you stay in compliance with regulatory bodies and provide your customers with their preferred experience. These tools help you organize contact details, communication subscriptions, and preference forms.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User permissions needed  
---  
To manage settings in Salesforce Setup: | View Setup and Configuration ORSystem Administrator profileORMarketing Cloud Admin permission set  
To manage consent: | Marketing Cloud Admin ORMarketing Cloud Manager permission set  
  
A default Marketing communication subscription is available. To organize consent records by channel or content types, create at least one communication subscription.

If you manage consent in another platform, you can disable consent checks in Marketing Cloud Next, but you must affirm responsibility for any compliance-related issues that arise.

  1. Verify your physical address.

This physical address is the primary address that’s used in other parts of Salesforce. If you edit it, those changes appear in other locations.

     1. From Setup, in the Quick Find box, enter `Company`, and then select **Company Information**.
     2. Review or edit the address field.
  2. Set consent validation preferences for email.
     1. From Setup, in the Quick Find box, enter `Channels`, and then select **Email**.
     2. Review the consent validation settings for promotional and transactional email messages.
  3. To use custom communication subscriptions for your marketing channels, see [Create a Communication Subscription](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_comm_sub_create.htm&language=en_US&type=5 "Create a communication subscription for each category of marketing content that you send, such as product updates. For each subscription that you create, add marketing channels, such as email and SMS. Subscribers must give consent to receive promotional messages from each channel type.").
  4. To create a consent import, see [Import Consent Data](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_import_create.htm&language=en_US&type=5 "If you collect consent data outside of Marketing Cloud Next, import it as a CSV. Each import corresponds to a single marketing channel, communication subscription, and consent status.").
  5. To customize the banner that asks page visitors for consent to track web activity, see [ Activity Tracking](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_parent.htm&language=en_US&type=5 "Track visitor activities and engagement across your marketing web pages. Use the data to create more targeted segments and inform your marketing strategy. You can track activity on landing pages hosted by Marketing Cloud Next and on external websites.").



By default, the email preference page includes the default marketing communication subscription. To add or remove subscriptions, see [Edit the Email Preference Page](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_pref_page_create.htm&language=en_US&type=5 "Marketing Cloud Next comes with default preference pages for email, SMS, and WhatsApp. Preference pages are visible to subscribers when they click the Preference Manager link in a marketing message. The default marketing communication subscription is included on the page, but you can add or remove subscriptions as needed. Preference pages are customized for each recipient.").
