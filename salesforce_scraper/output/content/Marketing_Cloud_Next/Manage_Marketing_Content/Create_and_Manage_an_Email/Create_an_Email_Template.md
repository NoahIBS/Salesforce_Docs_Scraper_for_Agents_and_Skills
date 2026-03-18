<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create_email_template.htm&language=en_US&type=5 -->

# Create an Email Template in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create an Email Template in Marketing Cloud Next

To keep your marketing campaigns consistent with brand guidelines and save time, create reusable standard and custom email templates. 

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission setANDAny CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDA CMS workspace contributor role of contentAdmin or content manager  
  
[](https://help.salesforce.com/s?language=en_US)

## Create an Email Template

To create reusable email templates that match your branding, select a prebuilt standard layout or design a custom template.

[](https://help.salesforce.com/s?language=en_US)

  1. On the Content tab in a marketing workspace, select **Add** | **Content** | **Email Template**. Click **Create**.
  2. Select a creation method.
     1. Use standard template: Click **Select a Template** | **Select**. Select a layout from the Standard Templates tab, and then click **Select**. 
     2. Build custom template: Click **Use Components** , and then click **Select**.
  3. In Experience Builder, click the Settings tab and configure the properties. [](https://help.salesforce.com/s?language=en_US)
     1. Give your email template a title for internal use and write a subject line.
     2. Enter a preheader summary that appears next to the subject line in the recipient's inbox.
     3. Set the Message Purpose to **Promotional** or **Transactional** depending on your needs.
  4. Add or move components to create the layout that you want.

If you’re using a standard template, to change the layout without losing your content, click Template Switcher in the properties panel.

  5. Save your work.
  6. To preview the template or send a test message, click **Preview**.
  7. To make the template available for authors to use, click **Publish Now**.



Whether you started with a standard layout or a custom design, the published template is available in the template library under Custom Templates. 

[](https://help.salesforce.com/s?language=en_US)

## Edit an Email Template

You can modify an email template at any time.

[](https://help.salesforce.com/s?language=en_US)

  1. From the Content tab in a marketing workspace, open the email template that you want to use.
  2. On the content details page, click **Edit**.
  3. Edit the template, and then save it.
  4. To make the changes available to authors, click **Publish**.



[](https://help.salesforce.com/s?language=en_US)

## Manage Template Content

By default, template-wide settings and individual content components are locked. You can adjust these settings to grant or restrict access as needed.

The state of nested components in the email template mirrors that of the parent component:

[](https://help.salesforce.com/s?language=en_US)

  * Unlocking the parent component automatically unlocks all nested components.
  * Locking the parent component locks all nested components.



[](https://help.salesforce.com/s?language=en_US)

  1. To configure template-wide settings, on the Settings tab, select or deselect **Allow users to modify template settings for an individual email.**

When you enable this setting, users can change styles, layouts, settings, and any unlocked components in the email. 

  2. To control editing subject lines and preheaders, on the Settings tab, use the lock icons next to Subject Line and Preheader.

If editing template-wide settings is disabled, you can still enable editing for subject lines and preheaders.

  3. To let users modify data sources, on the Data Sources tab, select **Allow users to modify data sources**. 
  4. To let users edit individual components, select a component, column, or section on the canvas. On the Settings tab, select **Allow users to modify this component**.

Users can edit the selected component and all its nested components. 

  5. Save your work.



[](https://help.salesforce.com/s?language=en_US)

## Unpublish an Email Template

To hide a template from other users so that it can't be used anymore, unpublish it.

[](https://help.salesforce.com/s?language=en_US)

  1. From the Content tab, find the template that you want to hide. 
  2. Open the content detail page, and then select **Unpublish**.
  3. Choose whether to unpublish the template now or later.
     * To unpublish immediately, select **Unpublish Now**.
     * To unpublish later, select **Schedule Unpublish** , and set the date and time.


