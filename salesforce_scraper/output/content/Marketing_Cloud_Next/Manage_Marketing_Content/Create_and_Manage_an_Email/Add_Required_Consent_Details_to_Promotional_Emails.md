<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_canspam.htm&language=en_US&type=5 -->

# Add Required Consent Details to Promotional Emails

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Add Required Consent Details to Promotional Emails

To comply with privacy and consent laws and regulations, including the U.S. CAN-SPAM Act, add an opt-out link and a physical mailing address to emails. Use the corresponding merge fields in text-based components in the email body.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
Merge fields easily populate the required information into your email. You can insert the merge fields anywhere in your email, but they commonly appear at the end in a footer. At send time, the Physical Address merge field inserts your organization’s address from Salesforce Setup, and the opt-out merge fields resolve to URLs.

Certain merge field links, such as the Preference Manager and Unsubscribe links, aren’t functional when you preview an email, SMS, or WhatsApp message. You can review default preference pages on the Consent tab.

  1. From your marketing workspace, create or open a promotional email.
  2. On the canvas, click a text-based component, such as a paragraph or a heading.
  3. To add your organization’s address, click  in the component toolbar.
  4. Select **Organization** | **Physical Address**.
  5. To add an opt-out link in the same text-based component, click , and enter descriptive, accessible link text in the Link Text field.
  6. For the URL field, click **Add Merge Field** | **Link**.
     * To give the recipient a way to unsubscribe only from the communication subscription related to the email, select **Unsubscribe**. When the recipient clicks this link, Salesforce immediately unsubscribes them and shows a confirmation page.
     * To link to a page where the recipient can manage individual email preferences, select **Preference Manager**.
     * To link to a custom preference page, add your URL instead of using a merge field.
  7. Save your work.


