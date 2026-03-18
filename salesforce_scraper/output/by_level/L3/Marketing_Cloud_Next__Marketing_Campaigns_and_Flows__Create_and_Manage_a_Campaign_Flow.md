<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_working.htm&language=en_US&type=5 -->

# Create and Manage a Campaign Flow in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage a Campaign Flow in Marketing Cloud Next

You can create a campaign flow from any campaign Quick Start or from a blank template, and then add flow elements that listen for activities and trigger actions.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
User Permissions Needed  
---  
To create and manage a campaign: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissions AND Permissions to all elements in the flow  
To create and edit flows: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissionsANDPermissions to all elements in the flow  
To share flows and view shared flows: | See [other permissions](https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing.htm&language=en_US&type=5 "In Marketing Cloud Next, campaign flow sharing is set to private by default. However, associated records, sharing rules, and manual sharing can also affect the flow’s visibility.").  
  
In this topic: 

[](https://help.salesforce.com/s?language=en_US)

  * [Quick Start a Campaign Flow](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_working.htm&language=en_US&type=5#quick "The fastest way to create a campaign flow is to use a Quick Start option to send a message, build a form, or trigger an action from an event.")
  * [Edit a Flow](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_working.htm&language=en_US&type=5#edit "You can only directly edit a flow before it has been activated. When you make changes to an active flow, the flow opens in draft status on the Flow Builder canvas, and must be saved as a new version. To customize a campaign flow, open it from the campaign record or the Flows tab.")



Note

Although it's possible to create a flow before the campaign, we typically don't recommend it. If you must create a flow first, verify that the flow type is compatible with Marketing Cloud Next, and add a related campaign the Associated Record field. Skipping these steps can break relationships, personalization, and reporting.

[](https://help.salesforce.com/s?language=en_US)

## Quick Start a Campaign Flow

The fastest way to create a campaign flow is to use a Quick Start option to send a message, build a form, or trigger an action from an event.

[](https://help.salesforce.com/s?language=en_US)

[](https://help.salesforce.com/s?language=en_US) [](https://help.salesforce.com/s?language=en_US)

Check out these resources for creating common campaign flows: 

[](https://help.salesforce.com/s?language=en_US)

  * [Send a Message](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_send_message.htm&language=en_US&type=5 "A message campaign in Marketing Cloud Next includes a segment-triggered flow with one message element, but you can add more messages as needed.")
  * [Generate Leads](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_generate_leads.htm&language=en_US&type=5 "Use a Signup Form campaign to automate lead generation and fuel your pipeline. A Signup Form campaign in Marketing Cloud Next includes a signup form and landing page that you can customize for your business.")
  * [Trigger by Event](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_event.htm&language=en_US&type=5 "Let Marketing Cloud Next take on some of your team’s manual tasks. To automate common tasks, message sends, and actions based on customer events, create a blank event campaign. For example, send an SMS message when someone signs up for an event, or send an email when someone subscribes to your email list.")



[](https://help.salesforce.com/s?language=en_US)

## Edit a Campaign

You can only directly edit a flow before it has been activated. When you make changes to an active flow, the flow opens in draft status on the Flow Builder canvas, and must be saved as a new version. To customize a campaign flow, open it from the campaign record or the Flows tab.

[](https://help.salesforce.com/s?language=en_US)

  1. Open a flow for editing.
     * From any campaign, click **Open Flow**.
     * From the Flows tab, click a row's action menu, and then select **Open Flow**.
  2. [Add structure and logic to your campaign flow](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_add_move.htm&language=en_US&type=5 "A campaign flow contains elements that represent certain actions along a customer's journey. To create the structure, add, remove, and move elements around the flow canvas. You can also add logic, such as branching paths and exit rule filters, to further customize the customer experiences.").
  3. Save your work.
     * Click **Save**.
     * Click **Save As New Version** , and confirm the name, data space, and data graph.


