<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_send_message.htm&language=en_US&type=5 -->

# Send a Message with a Marketing Campaign

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Send a Message with a Marketing Campaign

A message campaign in Marketing Cloud Next includes a segment-triggered flow with one message element, but you can add more messages as needed.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create and manage a campaign: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissions AND Permissions to all elements in the flow  
  
In this topic:

  * [Start from a Campaign](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_send_message.htm&language=en_US&type=5#mktg-send-from-campaign "Start with a campaign and a flow to send messages to an audience segment. Message-based campaigns can be a simple email or you can use them to design a highly curated customer journey.")
  * [Start from a List](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_send_message.htm&language=en_US&type=5#mktg-send-to-list "Quickly send a marketing email from a Lead or Contact list view. We take care of creating the campaign, flow, and audience segment for you.")



[](https://help.salesforce.com/s?language=en_US)

## Start From a Campaign

Start with a campaign and a flow to send messages to an audience segment. Message-based campaigns can be a simple email or you can use them to design a highly curated customer journey.

  1. From the Campaigns tab, create a campaign.
  2. Name your campaign, enter the details that you need, and then click **Save**.
  3. Select a message-based campaign option, or select **Build Your Own**.

When you build your own, add a segment-triggered flow in the Start section and save.

  4. Set a schedule for your flow. To begin sending immediately, finish configuring your campaign, and then select **Send Now** in the Schedule section.

Messages aren't sent until you activate the campaign.

  5. In the Start Trigger section, click **Select Segment**.
  6. Create a segment, or select an existing one.
  7. To publish your segment, click **Publish** in the Start Trigger section.

To send messages and preview segment membership, publish the segment first. If your segment hasn’t been published recently, we recommend that you publish it again so your segment is up to date.

  8. Allow time for the segment to publish, and then refresh the page.
  9. To preview who’s in the segment, click **Preview**.

[](https://help.salesforce.com/s?language=en_US) [](https://help.salesforce.com/s?language=en_US)

  10. Add message elements, and select or create content as needed.
  11. For each message in your flow, complete these steps.
     1. Edit and customize the content.
     2. Preview and test the content.
     3. Publish the message.
     4. Configure required message details, such as sender and communication subscription.
  12. To reorder a message element or to view it in the flow, click the message’s action menu, and then select **View in Flow**.
  13. If needed, add and configure a time-based wait element in your flow.

To add or remove other elements, open Flow Builder.

  14. When you’re done, activate the campaign flow.
  15. Decide when to republish your segment, and then finish activating the campaign.

Flow Builder uses the segment’s publish schedule. For the most up-to-date data, select the option to republish the segment immediately before running the flow.




After you activate a segment-triggered flow, it begins sending messages at the scheduled time. To change a scheduled flow, deactivate it first.

[](https://help.salesforce.com/s?language=en_US)

## Start From a List

Quickly send a marketing email from a Lead or Contact list view. We take care of creating the campaign, flow, and audience segment for you.

  1. Filter a Lead or Contact list view to show the people you want to email.
  2. From the filtered list view, click **Send List Email**.
  3. Select **Marketing List Email** , and then click **Next**.
  4. Review the filters for your segment, and then click **Next**.
  5. If needed, [draft a new email to send](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_create.htm&language=en_US&type=5). When know which email you want to use, click **Next**
  6. Select an email to send, and then click **Next**.
  7. Select a communication subscription and a sender for your email.
  8. Send your email.


