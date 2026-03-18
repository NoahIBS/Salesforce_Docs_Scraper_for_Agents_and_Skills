<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_distributed_marketing.htm&language=en_US&type=5 -->

# Set Up Distributed Marketing and Alerts

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Distributed Marketing and Alerts

With Distributed Marketing and Alerts, marketers can help ensure quality content and consistent branding by sharing approved email templates with non-marketing users. To make Distributed Marketing and Alerts available to marketers and other platform users, an admin must turn on the feature, assign permissions, and add the Distributed Marketing and Alerts components to campaign, lead, contact, and prospect account records.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To enable Distributed Marketing and Alerts: | Modify All Data OR Marketing Cloud Admin permission set  
To assign content workspace and builder permissions: | Content Admin role  
  
  1. From Setup, in the Quick Find box, enter `Distributed`, and then select **Distributed Marketing & Alerts**.
  2. Turn on the feature.
  3. [Assign Content Workspace and Builder permissions](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_contributors_workspace.htm&language=en_US&type=5) to marketers who create email templates.
  4. In Setup, , assign the Marketing Cloud Manager permission set and the Send Distributed Messages permission set to users who send templated emails. See [Assign Permission Sets for Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_perms_assign.htm&language=en_US&type=5). 
  5. From Setup, in the Quick Find box, enter `Lightning App`, and then select **Lightning App Builder**.
  6. Add components to record pages.
     1. To add the email composer to a lead, contact, or prospect record, insert the **Distributed Messages** component.
     2. To add a performance dashboard of aggregate email data to the campaign record, create a tab, and then insert the **Total Email Performance** component.
     3. To add the **Send Distributed Message** button to the Campaign Members related list on the campaign record, insert the button from the Related List section of the campaign page layout.
     4. To add the **Send Distributed Message** button to lead, contact, and prospect list views, insert the button on each page layout.
     5. Verify that the components appear on records as expected.



After the feature is set up, a marketer can create a template and configure a flow to make the template available to non-marketing users.

#### See Also

  * [Distributed Marketing and Alerts](https://help.salesforce.com/s/articleView?id=mktg.mktg_dm_overview.htm&language=en_US&type=5 "To increase productivity and maintain brand consistency, marketers can share approved email templates with sales reps and other Salesforce users. Distributed Marketing and Alerts makes it easier for non-marketing users to send email content that’s on brand and approved by marketing.")


