<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_set_up_marketing_channels.htm&language=en_US&type=5 -->

# Manage Marketing Channels for Business Units

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Manage Marketing Channels for Business Units

You can assign channels to all business units or a single business unit. Channels include email, SMS, WhatsApp, and Mobile App Messaging. Assign channels to all business units for a single sender address, such as an SMS code or email domain, to be used across the entire organization. Alternatively, assign channels to a single business unit so that individual divisions can use dedicated sender addresses. You can also unassign channels from business units.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To assign or unassign channels to business units: | Marketing Cloud Admin permission set  
  
Before you begin, set up the required channels for your marketing communications. For more information, see these resources: 

Channel | Resources  
---|---  
Email | [Configure Required Email Settings](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_email_verify_sender.htm&language=en_US&type=5)  
SMS | [Set Up SMS Messaging](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_sms.htm&language=en_US&type=5)  
WhatsApp | [Set Up WhatsApp](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_whatsapp.htm&language=en_US&type=5)  
All channels | [Domain Settings in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_domains_ref.htm&language=en_US&type=5)  
All channels | [Ensure Compliance with Consent Settings](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_consent.htm&language=en_US&type=5)  
  
[](https://help.salesforce.com/s?language=en_US)

## Assign Channels to All Business Units

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. Select a channel type and click **Assign**.
  3. Select the channels that you want to assign to all business units and click **Done**.

Changing a channel's assignment from a single business unit to all business units automatically removes its previous assignment and makes it available across the entire organization.




[](https://help.salesforce.com/s?language=en_US)

## Assign Channels to a Single Business Unit

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units list page, select a business unit.
  3. In the Channels section, select a channel type and click **Assign**.
  4. Select the channels that you want to assign and click **Assign**.

Channels assigned to all business units aren’t available for selection. To change the assignment of a channel that’s assigned to all business units, you must first unassign it and then remove any dependencies of the channel on flows and subscription.




[](https://help.salesforce.com/s?language=en_US)

## Unassign a Channel from All Business Units

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. Select a channel type.
  3. Make sure that the channel that you want to unassign isn’t in use in any flows or subscriptions.
  4. In the row of the channel that you want to unassign, click  and select **View Dependencies**.
  5. Remove the channel from all the dependent flows and subscriptions.
  6. In the row of the channel that you want to unassign, click and select **Unassign**.



[](https://help.salesforce.com/s?language=en_US)

## Unassign a Channel from a Business Unit

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units list page, select a business unit.
  3. In the Channels section, select a channel type.
  4. Make sure that no flows or subscriptions are by using the channel that you want to unassign.
  5. In the row of the channel that you want to unassign, click  and select **View Dependencies**.
  6. Remove the channel from all the dependent flows and subscriptions.
  7. In the row of the channel that you want to unassign, click  and select **Unassign**.


