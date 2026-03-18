<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_email_verify_sender.htm&language=en_US&type=5 -->

# Configure Required Email Settings

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure Required Email Settings

To send emails, you must authenticate a domain for sending, verify at least one sender email address, and provide a physical address to include in your email. In some cases, such as upgrading from Starter or Pro Suite, you can transfer email sending capabilities to Marketing Cloud Next. 

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User permissions needed  
---  
To modify organization-wide addresses: | Modify All Data ORMarketing Cloud Admin permission set  
  
We recommend using a subdomain of your root domain for marketing sends. This best practice improves the deliverability of your sends and protects the reputation of your domain. Make sure that your subdomain has an inbox available to receive the authentication verification email for the subdomain.

  1. Work with your IT administrator to [configure DKIM settings](https://help.salesforce.com/s/articleView?id=mktg.um_channel_email_domain.htm&language=en_US&type=5) that add a recognized digital signature to your emails and can improve your deliverability.

Note In some cases, such as upgrading from Starter or Pro Suite, the email authenticated domains page guides you through the process of transferring your sending activities to Marketing Cloud Next. Before you complete the transfer, [pause your active campaigns](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_pause.htm&language=en_US&type=5 "Although it’s rare, sometimes you need to stop a campaign’s flow from running. To fix an issue or make other changes, pause the flow."). After you complete the transfer, resume the paused campaigns that you want to continue.

  2. Verify an email address for the From field.

Verified sender email addresses are listed in the From field selector of an email campaign. Marketers can select the email address that they want to use for each email that they create. See [Authenticate a From Address for Unified Messaging](https://help.salesforce.com/s/articleView?id=mktg.um_channel_email_from_address.htm&language=en_US&type=5).

  3. Add or update the physical address inserted by the Physical Address merge tag. 

To maintain regulatory compliance, all marketing and transactional emails must include a physical address. 

[](https://help.salesforce.com/s?language=en_US)
     1. From Setup, in the Quick Find box, enter `Company`, and then select **Company Information**.
     2. In the Organization Detail section, review or edit the Address details.
     3. Save your changes.



A complete physical address, including an alphanumeric value in the State field, must be included in every marketing email that you send. If your business address doesn't use a state, region, or province name, insert a placeholder. For orgs that use a region picklist, add a placeholder to the picklist first, and then select the placeholder from the dropdown menu.

#### See Also

  * [ _Knowledge Article:_ DNS Configuration Tips for Marketing Cloud](https://help.salesforce.com/s/articleView?id=001533984&language=en_US&type=1)


