<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_create.htm&language=en_US&type=5 -->

# Create an Email in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create an Email in Marketing Cloud Next

The content editing experience in Marketing Cloud Next provides tools to build an email, preview and test it, and publish it for use with a campaign. To make major changes to a published email or to prevent it from sending in a campaign, you can unpublish it.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
  * **[Add Required Consent Details to Promotional Emails](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_canspam.htm&language=en_US&type=5)**  
To comply with privacy and consent laws and regulations, including the U.S. CAN-SPAM Act, add an opt-out link and a physical mailing address to emails. Use the corresponding merge fields in text-based components in the email body.
  * **[Create an Email Template in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create_email_template.htm&language=en_US&type=5)**  
To keep your marketing campaigns consistent with brand guidelines and save time, create reusable standard and custom email templates. 



[](https://help.salesforce.com/s?language=en_US)

## Create an Email

To make sure that your customers get the best experience from your content, preview and test your email. Before you can preview and test, publish at least one segment. You can preview and test an email in any status. Test sends count toward message credits.

The email functionality in Marketing Cloud Next is also available in Salesforce Starter and Pro Suite. For more information, see [Salesforce Starter and Pro Suite Help](https://help.salesforce.com/s/articleView?id=xcloud.easy_help.htm&language=en_US&type=5).

Not sure where to start? Check out these [basics for creating content in ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create.htm&language=en_US&type=5 "The content editing experience in Marketing Cloud Next uses a single design framework so that building marketing content is familiar no matter what you’re creating. The layout and functionality are the same, but after you choose the content type, a curated selection of components appears for you to choose from.")Marketing Cloud Next.

  1. Create or open content for editing.
     * From the Campaigns tab, open a campaign or create one. Then, on the campaign record, next to the email that you want to work with, click **Edit**.
     * From the Content tab in a marketing workspace, click **Create** and select **Email**. In the **Select an email creation method** window, select **Create with Drag and Drop**.
     * From a flow, open a Send Email Message element, and edit the related email.
  2. In the editor, select an optional brand.
  3. Add or move components to create the layout that you want.
  4. Give your email a title for internal use and write a subject line.
  5. Set the Message Purpose to **Promotional** or **Transactional** depending on your needs.
  6. To personalize the email, click **Add Merge Field**.
     * To insert a value from the recipient’s unified profile, select **Unified Individual**.

     * To select event data, such as a subscription confirmation or a product from a confirmed order, click **Select Event**. 

     * To select from a curated list of values, such as products purchased, select **Data Graph Attribute**.

     * If saved expressions are available, select a saved expression, which includes pre-saved criteria for selecting a data graph attribute.

  7. To comply with consent and privacy regulations for a promotional email, or if you enabled consent validation for a transactional email, [include your organization’s address and an opt-out link](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_canspam.htm&language=en_US&type=5 "To comply with privacy and consent laws and regulations, including the U.S. CAN-SPAM Act, add an opt-out link and a physical mailing address to emails. Use the corresponding merge fields in text-based components in the email body.").
  8. Save your work.



To make an email available to send in a campaign, publish it. You can’t activate a campaign flow that contains an email that’s unpublished.

[](https://help.salesforce.com/s?language=en_US)

## Use an Email Template to Create an Email

Admins or authors can use a template to create an email that’s consistent with brand guidelines.

[](https://help.salesforce.com/s?language=en_US)

  1. From the Content tab in a marketing workspace, click **Create** and select **Email**.
  2. In the **Select an email creation method** window, select **Select a Template**.
  3. Select the template and start adding your content.
  4. Save your work.

If you can't modify settings or text, it’s possible that your admin locked specific parts of the template. 

[](https://help.salesforce.com/s?language=en_US)
     * Email Settings: Global styles, layouts, or personalization data sources can be locked. 
     * Property Settings: The **Subject Line** or **Preheader** can be set for you. 
     * Components: Specific content blocks, like a legal footer or header logo, can be pre-configured so that they aren’t changed or deleted. 

To change a locked item, contact your Salesforce marketing admin.




[](https://help.salesforce.com/s?language=en_US)

## Preview and Test an Email

To make sure that your customers get the best experience from your content, preview and test your email. Before you can preview and test, publish at least one segment. You can preview and test an email in any status. Test sends count toward message credits.

  1. Open the preview window.
     * When editing your email, in the main toolbar, click **Preview**.
     * From the email content detail page, click **Preview**.
  2. Select a segment and a sample recipient.

  3. To configure a test send, open the **Test** tab.
  4. In the Test Send Email Address field, enter up to five email addresses that you can easily access, separated by a comma.
  5. To change the email address that sends the test, update the From Name and Address field with a From name from an authenticated domain.
  6. To send a test email, click **Send Test**.
  7. Check the inbox and verify that the test email appears as expected.
     1. Make sure that merge fields appear properly.
     2. Test any links and buttons, especially the opt-out links.
  8. When you’re ready to use an email with a campaign, publish it.



A complete physical address, including an alphanumeric value in the State field, must be included in every marketing email that you send. If your business address doesn't use a state, region, or province name, insert a placeholder. For orgs that use a region picklist, add a placeholder to the picklist first, and then select the placeholder from the dropdown menu.

[](https://help.salesforce.com/s?language=en_US)

## Unpublish an Email

To change your email back to draft status and prevent it from sending in an email campaign, unpublish your email.

  1. From your marketing workspace, open the email that you want to unpublish.
     * From the content detail page, click **Unpublish**.
     * When you’re editing your email, from the main toolbar, click **Unpublish**.
  2. Review the list of related flows and content to determine whether other changes are required.
  3. To unpublish the email immediately, click **Unpublish Now**.
  4. To unpublish the email at a later date, click **Schedule Unpublish** , and schedule a date and time to unpublish it.



#### See Also

  * [Manually Create a Segment in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_audiences_segment_create_manual.htm&language=en_US&type=5 "To create a segment, you drag in attributes that describe your target audience. When you build segment rules, make sure that you select objects and fields that align with your data model.")
  * [Create and Manage Variations in Marketing Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_create_variations.htm&language=en_US&type=5 "Personalize emails or landing pages with dynamic content. Create a single variation and configure a targeting rule to determine when that variation appears. Or create variations that use existing personalization settings and targeting rules by cloning a personalization point. Prioritize the most relevant content if someone qualifies for more than one variation.")
  * [Personalizing Content with Merge Fields in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_merge_fields.htm&language=en_US&type=5 "Use merge fields to personalize and enhance your marketing content. For example, personalize an email with your customer's name or customize a landing page with products you know they're interested in. Merge fields are available for any attribute related to a customer's unified profile, including account information and recent engagement activity.")


