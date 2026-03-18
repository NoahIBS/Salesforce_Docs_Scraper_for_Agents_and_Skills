<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_reporting_ref.htm&language=en_US&type=5 -->

# Tools for Tracking and Reporting on Campaigns

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Tools for Tracking and Reporting on Campaigns

Marketing Cloud Next offers tools to help you monitor and track campaign success over time.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
  
In this topic:

  * Marketing Performance
  * Flow Analytics reporting
  * Campaign Stage field
  * Opportunity Influence
  * Marketing Calendar
  * Email: Not Sent Reasons table
  * Related Landing Pages related list



## Marketing Performance

For comprehensive campaign analytics, admins can configure Marketing Performance dashboards for marketers. Aggregate analytics are available on the Performance tab and individual campaign insights are available on the sidebar of campaign records under **Performance > Insights**. The campaign-specific email deliverability dashboard is available under **Performance > Deliverability**.

See [Set Up Marketing Performance](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_marketing_performance.htm&language=en_US&type=5). 

[](https://help.salesforce.com/s?language=en_US)

## Flow Analytics Reporting

When you have Marketing Cloud Next Advanced edition, certain flow types support on-canvas analytics and other contextual insights. To view insights for messaging elements, such as Send Email Message, make sure that you have the Tableau Next Included App Business User permission set.

See [View Embedded Element Analytics and Detailed Insights](https://help.salesforce.com/s/articleView?id=platform.flow_monitor_on_canvas_insights.htm&language=en_US&type=5) for more details about permissions and setup.

[](https://help.salesforce.com/s?language=en_US)

## Campaign Stage

Each campaign can be related to multiple flows. The Campaign Stage field on the campaign record shows which stage the campaign is in based on all the flows in the campaign. To make this field available, an admin must add it to the campaign page layout and set the field-level security for each profile that needs access to the field.

Campaign Stage | Campaign Flow Status Scenarios  
---|---  
In Planning | Scenario 1:[](https://help.salesforce.com/s?language=en_US)

  * At least one flow with a status of Scheduled or Preparing Data
  * No flows with a status of In Progress or Finishing

Scenario 2:[](https://help.salesforce.com/s?language=en_US)

  * At least one flow with a status of Draft
  * No flows with a status of Scheduled, Preparing Data, In Progress, or Finishing

  
In Progress | At least one flow with a status of In Progress or Finishing  
Completed | [](https://help.salesforce.com/s?language=en_US)

  * At least one flow with a status of Completed
  * No flows with a status of Draft, Scheduled, Preparing Data, In Progress, Finishing, or Error

  
Error | [](https://help.salesforce.com/s?language=en_US)

  * At least one flow with a status of Error
  * No flows with a status of Draft, Scheduled, Preparing Data, In Progress, or Finishing

  
Canceled | [](https://help.salesforce.com/s?language=en_US)

  * At least one flow with a status of Canceled
  * No flows with other statuses

  
Paused | [](https://help.salesforce.com/s?language=en_US)

  * At least one flow with a status of Paused
  * No flows with a status of Scheduled, Preparing Data, In Progress, or Finishing

  
  
[](https://help.salesforce.com/s?language=en_US)

## Opportunity Influence

Opportunity Influence uses engagement data from contacts related to Closed/Won opportunities to attribute revenue to specific campaigns. To make this feature available to marketers, an admin must enable Opportunity Influence in Salesforce Setup. After setup is complete, Influenced Opportunities appears on the campaign sidebar under Performance. 

See [Enable Opportunity Influence](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_opp_influence_enable.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Marketing Calendar

Stay aligned with Sales and track current and upcoming marketing efforts with the Marketing Calendar. Add and remove individual calendar views as needed. Here are the available calendars.

[](https://help.salesforce.com/s?language=en_US)

  * Campaigns
  * Campaign Segment Flows
  * Segment Flows



See [Manage Your Campaigns and Flows with Marketing Calendar](https://help.salesforce.com/s/articleView?id=mktg.mktg_track_campaigns_with_calendar.htm&language=en_US&type=5).

Value | Resolution  
---|---  
Message didn't send because internal error occurred while trying to send message | Try again later.  
Can't verify recipient consent |  Make sure the recipient provided consent to receive your email messages and try again.  
Tried to send promotional email to recipient without opt-in |  Try the send again after the recipient provides opt-in consent.  
Reached or exceeded sending allowance |  Work with your Salesforce account executive to purchase more entitlements and try the send again.  
Data graph doesn't contain valid personalization information | Review your data and try again.  
From address not authorized to send email  |  Make sure the From address is valid, then try the send again.  
Invalid number of data graphs | Review the data graphs and try again.  
Message was missing a recipient email address. | Add at least one recipient email address to your send and try again.  
Message wasn't sent because it included an unsupported preference center merge field | We can't send a message with an unsupported preference center merge field. Review the merge field and try again.  
Can't retrieve profile attributes | We can't retrieve profile attributes for this send.  
Recipient address returned hard bounce in previous send attempt |  Removed address from send and try again  
Failed to render because of syntax errors |  Make sure you’re using a valid message, then try the send again.  
Message wasn't sent because the time-to-live (TTL) value was exceeded  |  Try again later.  
  
[](https://help.salesforce.com/s?language=en_US)

## Email: Not Sent Reasons

This table lists the possible values for the NotSentReason field, and the steps that you can take to resolve each issue.

The NotSentReason field maps to the Engagement Action Reason field of the Email Engagement DMO. To identify recent reasons, open that object in the Data Explorer. If the field doesn't appear, click **Edit Columns** to add it.

For more information about available engagement DMO data, see [Email Engagement Data in Unified Messaging](https://help.salesforce.com/s/articleView?id=mktg.um_channel_email_engagement.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Related Landing Pages

To relate reporting metrics for a landing page to a campaign, manually add the URL alias for the page to the Related Landing Pages related list on the campaign record. To make the Related Landing Pages related list available to marketers, an admin must add it to the campaign page layout.
