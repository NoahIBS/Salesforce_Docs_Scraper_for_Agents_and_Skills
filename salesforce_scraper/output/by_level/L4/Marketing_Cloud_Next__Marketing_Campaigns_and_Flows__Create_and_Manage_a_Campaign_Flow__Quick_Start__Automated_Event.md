<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_event.htm&language=en_US&type=5 -->

# Automate Event-Based Tasks with a Campaign

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Automate Event-Based Tasks with a Campaign

Let Marketing Cloud Next take on some of your team’s manual tasks. To automate common tasks, message sends, and actions based on customer events, create a blank event campaign. For example, send an SMS message when someone signs up for an event, or send an email when someone subscribes to your email list.

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create and manage a campaign: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissions AND Permissions to all elements in the flow  
  
The event options that you have depend on the features enabled in your org. To review the full list of supported events, see [Event Library](https://help.salesforce.com/s/articleView?id=platform.automate_flow_ref_event_library.htm&language=en_US&type=5).

  1. From the Campaigns tab, create a campaign.
  2. Name your campaign, enter the campaign details that you need, and click **Save**.
  3. From the campaign options, select **Blank Event**.
  4. In the Start Trigger section, click **Configure Event**.
  5. In Flow Builder, click **Select Event**.
  6. From the Event Library, select an event to trigger your flow. 

For example, to send a welcome email when someone signs up for your email list, select **Email Subscription**.

  7. Complete the required fields for your event, and then save your flow.
  8. (Optional) Add elements to your flow, such as a Send Email Message element or flow action.
     * On the flow canvas, click , and then select any element.
     * From the campaign record, add a message element or time-based wait element.
  9. When you’re done, activate the flow.



To make changes to an active flow, pause it first.
