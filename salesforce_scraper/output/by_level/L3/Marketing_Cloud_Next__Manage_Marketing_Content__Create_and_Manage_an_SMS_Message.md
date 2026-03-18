<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_sms_create.htm&language=en_US&type=5 -->

# Create and Manage an SMS Message in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage an SMS Message in Marketing Cloud Next

Create an SMS message for your marketing campaigns and reach your customers directly on their mobile devices. For example, use SMS messaging to promote something new or follow up on an ongoing transaction.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and the Salesforce Message Credits - SMS add-on  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
Before you begin, review information about message length and required opt-out keywords. See [SMS Message Length](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_sms_message_length.htm&language=en_US&type=5 "To avoid sending multiple messages and using extra message credits, be mindful of the length of your SMS message. When you exceed the character limit for a single message, the message count increases. Using non-GSM characters, links, or merge fields increases message length.") and [Opt-Out Keywords](https://help.salesforce.com/s/articleView?id=mktg.mcu_content_sms_keywords_optout.htm&language=en_US&type=5 "To meet consent and privacy regulations, your recipients must know how to opt-out of SMS messages. In your messages, provide specific opt-out keywords and clear instructions for using them. Include keywords in promotional or transactional messages every time you send.").

[](https://help.salesforce.com/s?language=en_US)

## Create an SMS Message

The SMS preview updates on the canvas while you're working. If you exceed the maximum length for a single message, the number of messages increases. Many carriers support concatentation, which combines multiple messages into a single message. Other carriers send the messages separately.

  1. From your marketing workspace, create or open an SMS message.
  2. Give your message a title for internal use.
  3. Set the Message Purpose to **Promotional** for marketing content.

The transactional message purpose is intended for one-to-one messages, such as password resets and order confirmations.

  4. In the Message field, enter your message content.
  5. To personalize your message, click **Add Merge Field**.
     * To insert a value from the recipient’s unified profile, select **Unified Individual**.

     * To select event data, such as a subscription confirmation or a product from a confirmed order, click **Select Event**. 

     * To select from a curated list of values, such as products purchased, select **Data Graph Attribute**.

     * If saved expressions are available, select a saved expression, which includes pre-saved criteria for selecting a data graph attribute.

  6. To build a URL with UTM and custom tracking parameters, click **Add UTM Link**. [](https://help.salesforce.com/s?language=en_US)
     1. Enter a destination URL that begins with http:// or https://.
     2. Turn on **UTM Parameters** , and then select the [UTM parameters](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_sms_utm_parameters.htm&language=en_US&type=5) that you want to add to the URL.
     3. Enter the values for the selected parameters or select merge fields.
     4. To append custom parameters to your URL, click **Add Row** , and then enter the custom parameter details.
     5. Preview the final URL and click **Add**.
  7. In the message body, add clear opt-out instructions and an opt-out keyword.
  8. Save your work.



Now you can preview and test your SMS message.

[](https://help.salesforce.com/s?language=en_US)

## Preview and Test an SMS Message

Before you can preview or test, you must publish at least one segment and make sure you that have a sender code available in Salesforce Setup. You can preview and test an SMS message in any status. Test sends count toward message credits.

To test personalization fields, send a test message. When you receive the message, test links and make sure that merge fields and shortened links display properly.

  1. Open the preview window. [](https://help.salesforce.com/s?language=en_US)
     * When editing your message, in the main toolbar, click **Preview**.
     * From the content detail page, click **Preview**.
  2. Select a segment and a sample recipient.

[](https://help.salesforce.com/s?language=en_US)

  3. To configure a test send, open the **Test** tab.
  4. Select a sender code to send the message from.
  5. In the Test Send Mobile Number fields, enter up to five numbers for devices that you can easily access.
  6. Send the test message.



[](https://help.salesforce.com/s?language=en_US)

## Unpublish an SMS Message

To prevent a message from sending in a campaign, unpublish the SMS message.

  1. From your marketing workspace, open the SMS message that you want to unpublish.
     * When you’re editing your message, from the main toolbar, click **Unpublish**.
     * From the content detail page, click **Unpublish**.
  2. Review the list of related flows and content and determine if any other changes are needed.
  3. Unpublish the message.
     * To unpublish the message immediately, click **Unpublish Now**.
     * To unpublish the message at a later date, click **Schedule Unpublish** , and schedule a date and time to unpublish it.



After you unpublish, the SMS message is no longer available to campaign flows and can't be sent. You can make any necessary edits and republish it, or delete it.

#### See Also

  * [Personalizing Content with Merge Fields in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_merge_fields.htm&language=en_US&type=5 "Use merge fields to personalize and enhance your marketing content. For example, personalize an email with your customer's name or customize a landing page with products you know they're interested in. Merge fields are available for any attribute related to a customer's unified profile, including account information and recent engagement activity.")


