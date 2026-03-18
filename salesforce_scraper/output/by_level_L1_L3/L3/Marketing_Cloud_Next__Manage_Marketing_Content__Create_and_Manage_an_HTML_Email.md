<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_html_create.htm&language=en_US&type=5 -->

# Create an HTML Email in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create an HTML Email in Marketing Cloud Next

Use code view to preview and edit the HTML and CSS of an email. Convert an existing email to HTML or copy HTML from another source and build customized emails based on your own designs. Preview and test the email and publish it for use with a campaign. To change a published email or prevent it from sending in a campaign, you can unpublish it. 

### Required Editions

[](https://help.salesforce.com/s?language=en_US)Note

Currently, plain text versions of emails aren’t supported. Emails can appear blank for recipients whose email clients don't render HTML.

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
[](https://help.salesforce.com/s?language=en_US)

## Create an HTML Email

To ensure your customers get the best experience from your content, preview and test your email. Before you can preview and test, publish at least one segment. You can preview and test an email in any status. Test sends count toward message credits.

The email functionality in Marketing Cloud Next is also available in Salesforce Starter and Pro Suite. For more information, see [Salesforce Starter and Pro Suite Help](https://help.salesforce.com/s/articleView?id=xcloud.easy_help.htm&language=en_US&type=5).

Not sure where to start? Check out these [basics for creating content in ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create.htm&language=en_US&type=5 "The content editing experience in Marketing Cloud Next uses a single design framework so that building marketing content is familiar no matter what you’re creating. The layout and functionality are the same, but after you choose the content type, a curated selection of components appears for you to choose from.")Marketing Cloud Next.

  1. Create or open an email for editing.
     * From the Campaigns tab, open a campaign or create one. Then, on the campaign record, next to the email that you want to work with, click **Edit**.
     * From the Content tab, open your preferred marketing workspace. Select **Add** | **Content** | **Email**.
     * From a flow, open a Send Email Message element, and edit the related email.
  2. In the editor, select an optional brand.
  3. Add or move components to create the layout that you want.
  4. Give your email a title for internal use and write a subject line.
  5. Set the Message Purpose to **Promotional** or **Transactional** depending on your needs.
  6. Click the Code View toggle at the top of the builder. The **Code View** tab shows a preview of the HTML.
  7. Click **Convert to HTML**. 

After you convert an email to HTML, you can’t use drag-and-drop components or apply styling from the Style tab. The conversion also removes dynamic content, including repeaters, conditional logic, and content variants from an email. You can’t undo this action.

  8. To personalize the email, click **Add Merge Field**.
     * To insert a value from the recipient’s unified profile, select **Unified Individual**.

     * To select event data, such as a subscription confirmation or a product from a confirmed order, click **Select Event**. 

     * To select from a curated list of values, such as products purchased, select **Data Graph Attribute**.

     * If saved expressions are available, select a saved expression, which includes pre-saved criteria for selecting a data graph attribute.

  9. In promotional emails, to comply with consent and privacy regulations [include your organization’s address and an opt-out link](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_canspam.htm&language=en_US&type=5 "To comply with privacy and consent laws and regulations, including the U.S. CAN-SPAM Act, add an opt-out link and a physical mailing address to emails. Use the corresponding merge fields in text-based components in the email body.").
  10. Save your work.



To make an email available to send in a campaign, you must publish it. You can’t activate a campaign flow that contains an email until the email is published.

[](https://help.salesforce.com/s?language=en_US)

## Preview and Test an Email

To ensure your customers get the best experience from your content, preview and test your email. Before you can preview and test, publish at least one segment. You can preview and test an email in any status. Test sends count toward message credits.

  1. Open the preview window.
     * When editing your email, in the main toolbar, click **Preview**.
     * From the email content detail page, click **Preview**.
  2. Select a segment and a sample recipient.

  3. To configure a test send, open the **Test** tab.
  4. In the Test Send Email Address field, enter up to five email addresses that you can easily access, separated by a comma.
  5. To change the email address that sends the test, update the From Name and Address field with a From name from an authenticated domain.
  6. To send a test email, click **Send Test**.
  7. Check the inbox and verify that the test email appears as expected.
     1. Ensure that merge fields display properly.
     2. Test any links and buttons, especially the opt-out links.
  8. When you’re ready to use an email with a campaign, publish it.



[](https://help.salesforce.com/s?language=en_US)

## Unpublish an Email

To change your email back to draft status and prevent it from sending in an email campaign, unpublish your email.

  1. From your marketing workspace, open the email that you want to unpublish.
     * From the content detail page, click **Unpublish**.
     * When you’re editing your email, from the main toolbar, click **Unpublish**.
  2. Review the list of related flows and content and determine if any other changes are needed.
  3. To unpublish the email immediately, click **Unpublish Now**.
  4. To unpublish the email at a later date, click **Schedule Unpublish** , and schedule a date and time to unpublish it.


