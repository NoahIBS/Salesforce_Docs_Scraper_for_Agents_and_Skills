<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_dma_create_message.htm&language=en_US&type=5 -->

# Configure an Approved Email Template for Non-Marketing Users

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure an Approved Email Template for Non-Marketing Users

After an admin enables Distributed Marketing and Alerts, designate a marketing-approved email template for non-marketing users to use to send email. First, create the template in Salesforce CMS. Then, create an event-triggered campaign and select the template in the flow.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create and manage a campaign: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissions AND Permissions to all elements in the flow  
To create and edit flows: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissionsANDPermissions to all elements in the flow  
To share flows and view shared flows: | See [other permissions](https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing.htm&language=en_US&type=5 "In Marketing Cloud Next, campaign flow sharing is set to private by default. However, associated records, sharing rules, and manual sharing can also affect the flow’s visibility.").  
  
  1. [Create an email template to use for Distributed Marketing and Alerts](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create_email_template.htm&language=en_US&type=5).
  2. Create a Blank Event campaign.
  3. From the campaign record, click **Configure Event**.
  4. In the Start element, select the **Distributed Marketing and Alerts Message** event type.
  5. On the flow canvas, add the **Send Email Message** element and select the template you want to make available to non-marketing users.
  6. In the Select Email Template section, click the dropdown menu and select **Edit**.
  7. From the template editor, open the Component Tree. To lock or unlock a component, click the component and use the toggle. Non-marketing users can edit only unlocked components.
  8. Select a From address and a communication subscription.
  9. To make the template available to non-marketing users, publish it and activate the flow.



After you activate the flow, non-marketing users can send a Distributed Marketing and Alerts message using the designated email template.
