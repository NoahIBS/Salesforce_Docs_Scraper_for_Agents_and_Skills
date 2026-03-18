<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_reporting_formula_reference.htm&language=en_US&type=5 -->

# Metrics Formulas for Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Metrics Formulas for Marketing Cloud Next

Reports and dashboards in Marketing Cloud Next contain a combination of direct and calculated values. The available metrics vary by channel and report location.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
Metric tables cover these channels and engagement types:

  * Email
  * Landing pages
  * Mobile in-app
  * Mobile push
  * SMS
  * Tracked external sites
  * WhatsApp



[](https://help.salesforce.com/s?language=en_US)

## Aggregate Metrics

Metric | Location | Description | Formula  
---|---|---|---  
Total Activities | Marketing Performance reports and dashboards | The total number of clicks, opens, reads, and replies across various marketing channels. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(Email Clicks, Email Opens, SMS Clicks, WhatsApp Reads, SMS Route, SMS Unknown, WhatsApp Inbound, WhatsApp Others)  
  
[](https://help.salesforce.com/s?language=en_US)

## Email Metrics

Metric | Location | Description | Formula  
---|---|---|---  
Email Bounce Rate  | Analytics and Marketing Performance reports and dashboards  |  The percentage of sent emails that result in a bounce.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL") / SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL")

Analytics reports count all bounces regardless of whether they’re unique.  
Email Bounces  | Marketing Performance reports and dashboards  | The total number of hard and soft bounces related to an email. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL")  
  
Email Clicks | Marketing Performance reports and dashboards  | The total number of times a link was clicked in an email.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "EMAIL")  
  
Email Click Rate | Marketing Performance reports and dashboards  |  The percentage of sent emails that result in a click.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE EmailEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "EMAIL") / (SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL") - SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL"))  
  
Email Click-Through Rate  | Analytics and Marketing Performance reports and dashboards  | The percentage of opened emails that result in a click.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE EmailEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "EMAIL") / SUM(All UNIQUE EmailEngagement Records with ChannelAction = "OPEN" AND EngagementChannelType = "EMAIL") 

Data 360 reports count all clicks, regardless of whether they’re unique.  
Email Deliveries  | Marketing Performance reports and dashboards  | The total number of successfully delivered emails.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL") - SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL")  
  
Email Delivery Rate  | Marketing Performance reports and dashboards  |  The percentage of sent emails that result in a successful delivery. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)(SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL") - SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL")) / SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL")  
  
Email Opens  | Marketing Performance reports and dashboards  | The total number of times an email was opened.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "OPEN" AND EngagementChannelType = "EMAIL")  
  
Email Open Rate  | Analytics and Marketing Performance reports and dashboards  | The percentage of sent emails that result in an open.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE EmailEngagement Records with ChannelAction = "OPEN" AND EngagementChannelType = "EMAIL") / (SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL") - SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL"))

Data 360 reports count all opens regardless of whether they’re unique.  
Email Opt-Out Rate | Analytics and Marketing Performance reports and dashboards  | The percentage of sent emails that result in an unsubscribe.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE EmailEngagement Records with ChannelAction = "UNSUBSCRIBE" AND EngagementChannelType = "EMAIL") / (SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL") - SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND EngagementChannelType = "EMAIL"))

Analytics reports count all opt-out actions regardless of whether they’re unique.  
Email Sends | Analytics and Marketing Performance reports and dashboards  | The total number of emails sent. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL")  
  
Email Failed to Send | Analytics and Marketing Performance reports and dashboards  | The total number of emails that failed to send.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "NOT_SENT" AND EngagementChannelType = "EMAIL")  
  
Email Unsubscribes | Marketing Performance reports and dashboards  | The total number of unsubscribes related to an email. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All EmailEngagement Records with ChannelAction = "UNSUBSCRIBE" AND EngagementChannelType = "EMAIL")  
  
Email Hard Bounce Rate | Marketing Performance reports and dashboards  | The percentage of sent emails that are classified as a hard bounce. | 
    
    
    SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND BounceType ="HARD" AND EngagementChannelType = "EMAIL") / SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL")  
  
Email Soft Bounce Rate | Marketing Performance reports and dashboards  | The percentage of sent emails that are classified as a soft bounce. | 
    
    
    SUM(All EmailEngagement Records with ChannelAction = "BOUNCE" AND BounceType ="SOFT" AND EngagementChannelType = "EMAIL") / SUM(All EmailEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "EMAIL")  
  
Email Variation Unique Clicks  | Content Performance dashboard | The total number of unique clicks for dynamic content in campaign emails.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE EmailEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "EMAIL") GROUPED by PersonalizationContentId and PersonalizationDecisionId  
  
Email Total Failed Activities | Marketing Performance reports and dashboards  | The total number of emails that failed, bounced, or resulted in opt-outs. | 
    
    
    SUM(Email Failed To Send, Email Bounces, Email Unsubscribes)  
  
[](https://help.salesforce.com/s?language=en_US)

## Landing Page Metrics

Metric | Location | Description | Formula  
---|---|---|---  
Form Submissions | Marketing Performance reports and dashboards | The total number of submissions related to a form on a landing page. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All WebsiteEngagement Records with ChannelAction = “form-submit" AND EngagementChannelType = "Web")  
  
Form Submission Rate | Marketing Performance reports and dashboards | The percentage of landing page views that result in a form submission. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All WebsiteEngagement Records with ChannelAction = “form-submit" AND EngagementChannelType = "Web") / SUM(All WebsiteEngagement Records with ChannelAction = “page-view" AND EngagementChannelType = "Web")  
  
Page Click Rate | Marketing Performance reports and dashboards | The percentage of landing page views that result in a click engagement. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All WebsiteEngagement Records with ChannelAction = "anchor-click" OR ChannelAction = "button-click" AND EngagementChannelType = "Web") / (SUM(All UNIQUE WebsiteEngagement Records with ChannelAction = "page-view" AND EngagementChannelType = "Web")  
  
Page Clicks  | Marketing Performance reports and dashboards | The total number of clicks on a landing page. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All WebsiteEngagement Records with ChannelAction = “anchor-click" OR ChannelAction = "button-click" AND EngagementChannelType = "Web")  
  
Page Views | Marketing Performance reports and dashboards | The total number of page views for a landing page. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All WebsiteEngagement Records with ChannelAction = “page-view" AND EngagementChannelType = "Web")  
  
[](https://help.salesforce.com/s?language=en_US)

## Mobile In-App Metrics 

Metric | Location | Description | Formula  
---|---|---|---  
In-App Sends | Marketing Performance reports and dashboards | The total number of in-app messages sent. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “IN APP NOTIFICATION” 
    EngagementChannelAction=”SEND_STATUS” AND SendStatus = “SENT” group by IndividualId, BulkMessageId)
    
      
  
In-App Displays | Marketing Performance reports and dashboards | The total number of in-app messages displayed. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “IN APP NOTIFICATION” 
    EngagementChannelAction=”DISPLAY” group by IndividualId, BulkMessageId)
    
      
  
In-App Dismissals | Marketing Performance reports and dashboards | The total number of in-app messages that were dismissed. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “IN APP NOTIFICATION” 
    EngagementChannelAction=”DISMISS” group by IndividualId, BulkMessageId)
    
      
  
In-App CTA (Call to Action) Button Clicks | Marketing Performance reports and dashboards | The number of times users selected a specific call-to-action button in an in-app message. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “IN APP NOTIFICATION” 
    EngagementChannelAction=”BUTTON_CLICK” group by IndividualId, BulkMessageId)
    
      
  
In-App Downloads | Marketing Performance reports and dashboards | The total number of in-app messages that resulted in a successful download. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “IN APP NOTIFICATION” 
    EngagementChannelAction=”RECEIVED” group by IndividualId, BulkMessageId)
    
      
  
[](https://help.salesforce.com/s?language=en_US)

## Mobile Push Metrics

Metric | Location | Description | Formula  
---|---|---|---  
Push Deliverability Rate | Marketing Performance reports and dashboards | The percentage of attempted push notifications that result in a successful delivery. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction=”DELIVERED”) / UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction=”SEND_STATUS” AND MessageRecipientSendStatus in(”SENT”, “NOT_SENT”))  
  
Push Sends | Marketing Performance reports and dashboards | The total number of push notifications sent. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction = “SEND_STATUS” 
    AND MessageRecipientSendStatus = “SENT”)  
  
Push Deliveries  | Marketing Performance reports and dashboards | The total number of push notifications that were delivered. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction= “DELIVERED”)
      
  
Push Not Sent | Marketing Performance reports and dashboards | The total number of push notifications that were not sent | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction= “SEND_STATUS” AND MessageRecipientSendStatus = “NOT_SENT”)
      
  
Push Bounces | Marketing Performance reports and dashboards | The total number of push notifications that resulted in a bounce. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction= “SEND_STATUS” AND MessageRecipientSendStatus = “BOUNCE”)
      
  
Push Bounce Rate | Marketing Performance reports and dashboards | The percentage of push notifications that resulted in a bounce. | 
    
    
    (Push Bounces) / (Push Sends)  
  
Push Opens | Marketing Performance reports and dashboards | The total number of notifications that user opened. | 
    
    
    UNIQUE COUNT (All EngagementId where EngagementChannelType = “PUSH NOTIFICATION” 
    EngagementChannelAction= “SEND_STATUS” AND MessageRecipientSendStatus = “OPEN”)
      
  
Push Open Rate | Marketing Performance reports and dashboards | The percentage of delivered push notifications that result in an open. | 
    
    
    (Push Opened) / (Push Delivered)   
  
[](https://help.salesforce.com/s?language=en_US)

## SMS Metrics

Metric | Location | Description | Formula  
---|---|---|---  
SMS Clicks | Marketing Performance reports and dashboards  |  The total number of clicks related to an SMS message. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "SMS")  
  
SMS Click Rate  | Marketing Performance reports and dashboards  | The percentage of delivered SMS messages that result in a click. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All Unique MessageEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "SMS") / SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "DELIVERED" AND EngagementChannelType = "SMS")  
  
SMS Conversation Forwards | Marketing Performance reports and dashboards  | The total number of SMS messages that are transferred to a conversation.SMS Conversation Forwards work only when Service Cloud is set up. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "ROUTE" AND SendClassification = "TRANSFER" AND EngagementChannelType = "SMS")  
  
SMS Deliveries | Marketing Performance reports and dashboards  | The total number of delivered SMS messages. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "DELIVERED" AND EngagementChannelType = "SMS")  
  
SMS Delivery Rate  | Marketing Performance reports and dashboards  | The percentage of sent SMS messages that are successfully delivered. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)UNIQUE COUNT(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "DELIVERED" AND EngagementChannelType = "SMS") / SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "SMS")  
  
SMS Failed Deliveries | Marketing Performance reports and dashboards  | The total number of SMS messages that failed to send. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "UNDELIVERED" AND EngagementChannelType = "SMS")  
  
SMS Failure Rate  | Marketing Performance reports and dashboards  | The percentage of sent SMS messages that result in a failed delivery. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "UNDELIVERED" AND EngagementChannelType = "SMS") / SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "SMS")  
  
SMS Inbound Replies  | Marketing Performance reports and dashboards | The total number of replies to an SMS message, excluding unsubscribes.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records where ChannelAction = "ROUTE" AND SendClassification != "TRANSFER" AND EngagementChannelType = "SMS") + SUM(All MessageEngagement Records where ChannelAction = "UNKNOWN_KEYWORD" AND EngagementChannelType = "SMS")  
  
SMS Opt-Out Rate  | Analytics and Marketing Performance reports and dashboards  | The percentage of delivered SMS messages that result in an unsubscribe.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)UNIQUE COUNT(All MessageEngagement Records with ChannelAction = "UNSUBSCRIBE" AND EngagementChannelType = "SMS")/ UNIQUE COUNT(All MessageEngagement Records with ChannelAction = "DELIVERED" AND EngagementChannelType = "SMS")

Analytics reports count all opt-outs regardless of whether they’re unique.   
SMS Response Rate  | Analytics and Marketing Performance reports and dashboards | The percentage of delivered SMS messages that result in a reply. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SMS Inbound Replies/UNIQUE COUNT(All MessageEngagement Records with ChannelAction = "DELIVERED" AND EngagementChannelType = "SMS")

In Analytics reports, this metric is called Inbound Rate.  
SMS Sends | Analytics and Marketing Performance reports and dashboards  | The total number of SMS messages sent.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "SMS")  
  
SMS Unsubscribes | Marketing Performance reports and dashboards | The total number of unsubscribes related to an SMS message.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "UNSUBSCRIBE" AND EngagementChannelType = "SMS")  
  
## Tracked External Website Metrics

Metric | Location | Description | Formula  
---|---|---|---  
Page Click Rate | Marketing Performance reports and dashboards | The percentage of landing page views that result in a click engagement. | 
    
    
    SUM(All WebsiteEngagement Records with ChannelAction = "anchor-click" OR ChannelAction = "button-click" AND EngagementChannelType = "Web") / (SUM(All UNIQUE WebsiteEngagement Recrods with ChannelAction = "page-view" AND EngagementChannelType = "Web")  
  
Page Clicks  | Marketing Performance reports and dashboards | The total number of clicks on a landing page. | 
    
    
    SUM(All WebsiteEngagement Records with ChannelAction = “anchor-click" OR ChannelAction = "button-click" AND EngagementChannelType = "Web")  
  
Page Views | Marketing Performance reports and dashboards | The total number of page views for a landing page. | 
    
    
    SUM(All WebsiteEngagement Records with ChannelAction = “page-view" AND EngagementChannelType = "Web")  
  
Tracked Link Click | Tracked link content record | The total number of tracked link clicks. | 
    
    
    SUM(All WebsiteEngagement Records with EngagementChannelAction = “tracked-link-click" AND EngagementChannelType = "Web")  
  
[](https://help.salesforce.com/s?language=en_US)

## WhatsApp Metrics

Metric | Location | Description | Formula  
---|---|---|---  
WhatsApp Conversation Forwards | Marketing Performance reports and dashboards | The total number of WhatsApp messages transferred to a conversation.WhatsApp Conversation Forwards work only when Service Cloud is set up. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "ROUTE" AND SendClassification = "TRANSFER" AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT"))  
  
WhatsApp Click Rate | Marketing Performance reports and dashboards | The percentage of delivered messages that result in the recipient clicking on a link within the message. | 
    
    
    SUM(All Unique MessageEngagement Records with ChannelAction = "CLICK" AND EngagementChannelType = "WHATSAPP") / UNIQUE COUNT((All MessageEngagementRecords with ChannelAction = "DR" AND (SendStatus="SENT" OR SendStatus="DELIVERED" OR SendStatus="READ")) AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT"))  
  
WhatsApp Deliveries | Marketing Performance reports and dashboards | The total number of WhatsApp messages delivered. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "DR" AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT") AND (SendStatus="SENT" OR SendStatus="DELIVERED" OR SendStatus="READ"))
    
    
    [](https://help.salesforce.com/s?language=en_US)Total WhatsApp Deliveries = Total Whatsapp marked as sent + Total WhatsApp marked as Delivered (without a matching sent record) + Total WhatsApp marked as Read (without a matching Delivered/sent record)
      
  
WhatsApp Delivery Rate | Marketing Performance reports and dashboards | The percentage of sent WhatsApp messages that result in a successful delivery.  | 
    
    
    [](https://help.salesforce.com/s?language=en_US)(SUM(All MessageEngagement Records with ChannelAction = "DELIVERED" AND EngagementChannelType = "WHATSAPP") + SUM(All MessageEngagement Records with ChannelAction = "READ" without a Matching MessageEngagement Record on MessageID with ChannelAction = "DELIVERED" AND EngagementChannelType = "WHATSAPP")) / SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND EngagementChannelType = "WHATSAPP")  
  
WhatsApp Failed Deliveries  | Marketing Performance reports and dashboards | The total number of failed deliveries related to a WhatsApp message. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with (SendStatus="FAILED" and ChannelAction="DR") or (SendStatus="NOT_SENT" and ChannelAction="SEND_STATUS") AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT"))  
  
WhatsApp Failure Rate | Marketing Performance reports and dashboards | The percentage of sent WhatsApp messages that result in a failed delivery. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)WhatsApp Failed Deliveries / SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND ( SendStatus = "SENT" or SendStatus = "NOT_SENT") AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT"))  
  
WhatsApp Inbound Replies | Marketing Performance reports and dashboards | The total number of recipient replies related to a WhatsApp message. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "INBOUND" AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT")) + SUM(All MessageEngagement Records with (ChannelAction = "UNSUBSCRIBE" OR ChannelAction="SUBSCRIBE" OR ChannelAction=" HELP") AND EngagementChannelType = "WHATSAPP")  
  
WhatsApp Open Rate | Marketing Performance reports and dashboards |   | 
    
    
    SUM(All MessageEngagement Records with ChannelAction = "DR" AND SendStatus="READ" AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT")) / UNIQUE COUNT((All MessageEnagementRecords with ChannelAction = "DR" AND (SendStatus="SENT" OR SendStatus="DELIVERED" OR SendStatus="READ")) AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT"))  
  
WhatsApp Opt-Out Rate | Marketing Performance reports and dashboards | The percentage of delivered WhatsApp messages that result in an unsubscribe. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE MessageEngagement Records with ChannelAction = "UNSUBSCRIBE" AND EngagementChannelType = "WHATSAPP")/ UNIQUE COUNT((All MessageEngagementRecords with ChannelAction = "DR" AND (SendStatus="SENT" OR SendStatus="DELIVERED" OR SendStatus="READ")) AND EngagementChannelType = "WHATSAPP" by IndividualId and BulkMessageId)  
  
WhatsApp Reads | Marketing Performance reports and dashboards | The total number of WhatsApp messages that result in a read. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "DR" AND SendStatus="READ" AND EngagementChannelType = "WHATSAPP" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT"))  
  
WhatsApp Response Rate | Marketing Performance reports and dashboards | The percentage of delivered WhatsApp messages that result in a reply. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All UNIQUE MessageEngagement Records with ChannelAction = "INBOUND" AND EngagementChannelType = "WHATSAPP" AND EngagementNotes = "EINSTEIN1_MARKETING") + SUM(All UNIQUE MessageEngagement Records with (ChannelAction = "UNSUBSCRIBE" OR ChannelAction="SUBSCRIBE" OR ChannelAction = "HELP") AND EngagementChannelType = "WHATSAPP") / Total Whatsapp Deliveries  
  
WhatsApp Sends | Marketing Performance reports and dashboards | The total number of WhatsApp messages sent. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "SEND_STATUS" AND SendStatus = "SENT" AND (EngagementNotes = "EINSTEIN1_MARKETING" OR EngagementNotes = "MARKETING_CLOUD_ENGAGEMENT") AND EngagementChannelType = "WHATSAPP")  
  
WhatsApp Unsubscribes | Marketing Performance reports and dashboards | The total number of unsubscribes related to a WhatsApp message. | 
    
    
    [](https://help.salesforce.com/s?language=en_US)SUM(All MessageEngagement Records with ChannelAction = "UNSUBSCRIBE" AND EngagementChannelType = "WHATSAPP")
