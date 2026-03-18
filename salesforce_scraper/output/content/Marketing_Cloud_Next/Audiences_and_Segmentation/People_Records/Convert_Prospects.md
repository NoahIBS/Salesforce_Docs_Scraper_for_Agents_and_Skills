<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_prospects_conversion.htm&language=en_US&type=5 -->

# Convert Prospects in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Convert Prospects in Marketing Cloud Next

After a prospect meets the required engagement score, convert them to leads or contacts manually or set up an automated flow to convert them.

[](https://help.salesforce.com/s?language=en_US)

## Convert a Prospect to a Lead Manually

Identify prospects who’ve met the engagement score criteria and convert them into leads.

[](https://help.salesforce.com/s?language=en_US)

  1. From the **Prospects** tab, select a prospect and click **Convert**.
  2. Enter the name of the lead or select an existing lead.
  3. Enter all the necessary information, such as record owner and company.
  4. Click **Convert**.



[](https://help.salesforce.com/s?language=en_US)

All the information that you’ve provided for the prospect is now mapped to the lead record. 

[](https://help.salesforce.com/s?language=en_US)

## Convert Prospects to Leads Using a Flow

Create an automated flow to convert multiple prospects into leads after they meet the engagement score criteria.

[](https://help.salesforce.com/s?language=en_US)

  1. Open Flow Builder.
  2. Click **New Flow** and select **Data 360-Triggered Flow**.
  3. Click **Create**.
  4. For the Start element, select engagement score as the Data 360 object.
  5. Set the conditions so that when the engagement score is more than a certain value, the prospect is converted to a lead.
  6. Save and test the flow.



[](https://help.salesforce.com/s?language=en_US)

## Convert a Prospect to a Contact Manually

Look for a qualified prospect and convert it into a contact for targeted engagement. You can also relate the contact to a new or an existing account.

  1. From the Prospects tab, select a prospect and click **Convert**.
  2. On the**Convert Prospect** window, click **Contact**.
  3. Enter or select a contact and account.

Creating a new account is disabled if you choose an existing contact.

  4. (Optional) Link the contact to a new opportunity or an existing one. If you don’t want to create a new opportunity, select **Don’t create an opportunity on conversion**.
  5. Enter the contact record owner, select the converted status, and then click **Convert**.



[](https://help.salesforce.com/s?language=en_US)

## Convert Prospects to Contacts Using a Flow

To convert multiple prospects at one time or as they become marketing qualified, use a record-triggered flow. Data 360-triggered flows and form-triggered flows can also convert prospects. However, these instructions refer only to the record-triggered flow method.

[](https://help.salesforce.com/s?language=en_US)

  1. Open Flow Builder and ​​click **New Flow**.
  2. Select Start From Scratch, click Record-Triggered Flow, and then click Create. 
  3. From the **Object** dropdown, select **Prospect**.
  4. For the trigger, select **A record that is created or updated**.
  5. From the **Condition Requirements** dropdown, select **All Conditions Are Met (AND)**.
  6. Set the condition that if the Prospect field matches the specified value, the prospect is converted to an existing or new contact. 

For example, if `ProspectStatus` equals `Qualified`, then the prospects are converted to contacts.

  7. Select **Actions and Related Records**.
  8. Click the plus icon, and then select **Action**.
  9. Search for and select the **Convert Prospect** action.
  10. Set input values for the selected action.
     1. Give the action a label and API name.
     2. Enter the **Prospect ID**.
     3. Enter the **Converted Status**. The status must be a valid picklist option for **Prospect Status** field in Prospect Object and the **Converted** check box must be selected.
     4. Select **Existing Contact ID** or **New Contact Record** to convert to a new or existing contact.
     5. Select **Existing Account Record** or **New Account Record** to link to a contact. Existing contacts are already associated with an account.
     6. (Optional) Select **Existing Opportunity ID** or **New Opportunity Record** to add to the contact.
  11. Save your changes and click **Activate**.


