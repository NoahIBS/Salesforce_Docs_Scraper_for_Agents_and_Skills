<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mcu_content_sms_keywords_optout.htm&language=en_US&type=5 -->

# Opt-Out Keywords for SMS Messages in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Opt-Out Keywords for SMS Messages in Marketing Cloud Next

To meet consent and privacy regulations, your recipients must know how to opt-out of SMS messages. In your messages, provide specific opt-out keywords and clear instructions for using them. Include keywords in promotional or transactional messages every time you send.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and the Salesforce Message Credits - SMS add-on  
---  
  
Every SMS sender code reserves keywords that recipients use to opt out of receiving messages. These keywords are always reserved.

  * STOP
  * QUIT
  * CANCEL
  * END
  * UNSUBSCRIBE



A marketing admin can assign custom opt-out keywords to sender codes in Salesforce Setup. In the body of your SMS message, include one of these keywords and brief opt-out instructions.

To opt out, a recipient must reply to the sender code with an opt-out keyword appearing before the first space in their message. Salesforce immediately unsubscribes the recipient from all messages from that sender code.

Example

Try one of these SMS opt-out instructions that are fewer than 25 characters:

  * Text STOP to opt out.
  * Reply QUIT to end.



#### See Also

  * [Request a Campaign for a United States 10-digit Long Code](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_campaign_request.htm&language=en_US&type=5)


