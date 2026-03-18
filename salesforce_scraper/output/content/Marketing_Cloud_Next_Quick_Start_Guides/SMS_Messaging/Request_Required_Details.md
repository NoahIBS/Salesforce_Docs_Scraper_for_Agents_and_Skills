<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start_request_assets.htm&language=en_US&type=5 -->

# Quick Start: Request an SMS Brand, Campaign, and 10DLC

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Quick Start: Request an SMS Brand, Campaign, and 10DLC

Now that you’ve completed the prerequisites, it’s time to request a brand, campaign, and code to send SMS messages in the United States and Canada. Every SMS send from a 10DLC in the United States and Canada requires an approved brand, campaign, and code. 

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and Salesforce Message Credits - SMS add-on  
---  
User permissions needed  
---  
To manage settings in Salesforce Setup: | System Administrator profile AND Marketing Cloud Admin permission set  
To manage settings in Data 360: | Data Cloud Architect permission set  
  
Every country has specific sending requirements. These instructions are for the United States and Canada. To find out more about requesting codes in other countries, check out [_Request Location-Specific Sending Code_](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_request_location_specific_code.htm&language=en_US&type=5).

Included in this guide: 

[](https://help.salesforce.com/s?language=en_US)

  * Request an SMS Brand
  * Request an SMS Campaign
  * Request an SMS Code
  * Activate an SMS Code



[](https://help.salesforce.com/s?language=en_US)

## Request an SMS Brand

Register your company as a brand once within Salesforce. This registered brand can then be associated with multiple 10-digit long codes and campaigns. Your brand request can take up to 5 business days to process, due to the time it takes our third-party vetting partner to approve your request. 

Before you begin, make sure that your Marketing Cloud Admin has completed the required setup steps to send SMS messages in Marketing Cloud Next. See [Quick Start: Set Up SMS Prerequisites](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start.htm&language=en_US&type=5 "This Quick Start guide covers the preliminary steps that are required to send SMS messages with Marketing Cloud Next using United States and Canada 10-digit long codes \(10DLC\). It outlines the simplest implementation, so that your team can get up and running. For in-depth information, special features, or customization options, we provide additional resources along the way.").

Before you start your brand request, [collect this information](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_samples.htm&language=en_US&type=5).

  1. In Setup, in the Quick Find box, enter `Regulatory Compliance`, and then select **Regulatory Compliance**.
  2. On the 10DLC Brands tab, click **Register Brand**.
  3. Enter the details, and then click **Next**.
  4. Enter the company information for the brand, and then click **Submit**.



You can review the progress of your request via status messages on the Regulatory Compliance page.

  * Requested—Your request was submitted and is awaiting review.
  * Pending—Your request is received, but not yet reviewed
  * Verified—Your request is approved.
  * Unverified—Your request isn’t approved.
  * Under Verification—Your brand purchase request is being reviewed.
  * Declined—Your request wasn’t approved. Purchase a brand and try again.



You can save a draft of your request and return to it at a later time. Save up to 10 drafts of each type of request, including brands, campaigns, and codes.

You can also review the reasons for rejection. If the review process requires corrections, you can edit the request by clicking the arrow next to the request and selecting **Edit and Resubmit Request**. 

If the request is rejected two times, Salesforce emails your support contact to address the issue.

[](https://help.salesforce.com/s?language=en_US)

## Request an SMS Campaign

After you get your brand, you can request a campaign. You can request one campaign per purchased 10-digit long code, and we recommend using only one code per campaign. Processing your campaign request can take up to 10 business days, depending on the time needed for carriers and aggregators to provide approval.

Before you start your campaign request, [collect this information](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_samples.htm&language=en_US&type=5).

  1. In Setup, in the Quick Find box, enter `Regulatory Compliance`, and then select **Regulatory Compliance**.
  2. On the 10DLC Brands tab, click **Register Campaign**.
  3. Enter the information for the campaign, and then click **Next**.
  4. Enter the attributes, including keywords and regulatory content, and then click **Next**.
  5. Enter the opt-in information, and then click **Next**.
  6. Enter the opt-out information, and click **Submit**.

This information defines how subscribers can stop receiving marketing SMS messages or get additional assistance.




[](https://help.salesforce.com/s?language=en_US)

## Request an SMS Code

Now that you have a brand and campaign, you’re ready to request your 10-digit long code. Processing your code request can take up to 2 business days, depending on the time needed for carriers and aggregators to provide approval. 

Every country has specific sending requirements. These instructions are for the United States and Canada. To find out more about requesting codes in other countries, check out [Request Location-Specific Sending Code](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_request_location_specific_code.htm&language=en_US&type=5).

Important SMS Messaging in the United States and Canada is highly regulated by US and CA carriers and applicable laws. Salesforce supports the use of sanctioned, carrier-approved sender codes only for US and CA SMS messaging. Review these guidelines and restrictions for using sender codes for SMS sending in the United States and Canada. The information provided doesn’t, and isn’t intended to, constitute legal advice. All information is only for general informational purposes. Consult your own legal counsel for guidance on use cases and applicable legal and industry requirements. The overall registration process can take several weeks, so make sure to plan ahead. Unified Messaging doesn’t support MMS messaging.

  1. In Setup, in the Quick Find box, enter `SMS Codes`, and then select **SMS Codes**.
  2. Click **Request Code**.
  3. Select **United States** as the county that you want to associate the code with. 
  4. For Code Type, select **10-digit Long Code,** and then click **Next**.
  5. Review the regulatory compliance notices, and then click **Next**.
  6. Select the brand and campaign from your registered options.
  7. Enter the number of codes that you want. If you request more than one code, enter the reason for that quantity.
  8. Click **Submit**.



You can track the process of your code request in the Open Requests tab of the SMS Codes page.

  * Inactive—This default status indicates a code is available. Complete the mandatory consent and keyword information before you activate the code. You can’t use an inactive code to send SMS messages.
  * Active—You can use this code to send SMS messages.
  * Blocked—This code is blocked due to an expired contract or compliance violations. You can’t use this code to send SMS messages. 
  * Disabled—You can’t renew this code or use it to send SMS messages.



[](https://help.salesforce.com/s?language=en_US)

## Activate an SMS Code

After your SMS code request is approved, your code appears in the SMS Codes section of Setup with an Inactive status. You must activate your SMS code to use it. 

  1. In Setup, in the Quick Find box, enter `SMS Codes`, and then select **SMS Codes**.
  2. Click the code you want to activate.
  3. On the Consent tab, set your consent opt-in status to **Explicit** or **Double Opt-in**. 
  4. Enter your opt-in and keyword information.
  5. Save your changes.
  6. Activate the capabilities that you want to add to the code. These capabilities can require additional steps depending on how you configure your Salesforce org. To send and receive SMS messages using Flow, in the Activate Send and Receive Messages via Flow section, click **Activate**.
  7. To support agent and bot conversation via Service Cloud, in the Activate Access to Agent and Bot Conversational Support section, click Configure and complete these steps.
     1. On the Messaging Settings page, in the Omni-Channel Routing section, click Edit and set the Omni-Channel Routing configuration to route service messages to queues, flows, or agents depending on your business needs.
     1. Save your configuration. 
     1. Go to your SMS code details page and in the Activate Access to Agent and Bot Conversational Support section, click **Activate**.



Now that you've requested your necessary assets, it's time to [manage audiences and consent](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_sms_quick_start_manage_audience.htm&language=en_US&type=5). 
