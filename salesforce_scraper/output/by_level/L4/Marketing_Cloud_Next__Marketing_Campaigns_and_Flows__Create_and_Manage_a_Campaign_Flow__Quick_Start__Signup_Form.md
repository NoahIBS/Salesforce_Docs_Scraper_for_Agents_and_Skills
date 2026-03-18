<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_generate_leads.htm&language=en_US&type=5 -->

# Generate Leads with a Marketing Cloud Next Campaign

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Generate Leads with a Marketing Cloud Next Campaign

Use a Signup Form campaign to automate lead generation and fuel your pipeline. A Signup Form campaign in Marketing Cloud Next includes a signup form and landing page that you can customize for your business.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create and manage a campaign: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissions AND permissions to all elements in the flow  
  
  1. On the Campaigns tab, create a campaign.
  2. Name your campaign, enter the campaign details that you need, and click **Save**.
  3. From the campaign options, select **Signup Form**.
  4. In the Start Trigger section, edit the signup form. Don’t publish the form yet.

If you’re marketing to your leads, make sure that your form clearly states that they’re opting in to receive messages from you.

  5. In the Related Landing Pages section, click the [](https://help.salesforce.com/s?language=en_US) for the landing page and select **Edit**.
  6. Customize the landing page that hosts the form. Don’t publish the landing page yet.
  7. Configure or remove the Consent Request element in Flow Builder. This element is required to send marketing messages to people who submit your form. [](https://help.salesforce.com/s?language=en_US)
     1. Click **Open Flow**.
     2. In Flow Builder, click the **Consent Request** element, and then click **Edit Element**.
     3. Complete the required fields.
     4. Verify that the contact point, channel, and communication subscription correspond. For example, if an email address is the contact point, select the Email channel and the communication subscription that you use for email marketing.
  8. To send messages to people who submit your form, add messages elements to the flow. For example, add a Send Email Message element to send an email when someone submits the form.
  9. Click the  for the landing page, select **Edit** , and then publish the landing page. This action also publishes the form and activates the flow.



After you publish the landing page, use its URL on the content detail page to live-test your form. If you’re collecting consent, make sure that a consent record is created when you submit the form.

#### See Also

  * [ _Salesforce Help_ : Flow Element: Create Consent](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_consent_request.htm&language=en_US&type=5)


