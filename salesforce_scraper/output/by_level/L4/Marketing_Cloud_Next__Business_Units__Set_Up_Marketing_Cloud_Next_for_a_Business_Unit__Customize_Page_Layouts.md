<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_customize_page_layouts.htm&language=en_US&type=5 -->

# Customize Page Layouts

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Customize Page Layouts

To display Data 360 Lightning components, such as Profile Engagement and Profile Insights, in the context of a business unit on a record page, use the Business Unit Container component. This container component contains a business-unit dropdown and is available in the Lightning App Builder for the Contact, Lead, and Prospect records. 

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
  
A Salesforce or marketing admin can access the Lightning App Builder from the Object Manager or the Setup menu on the Campaign record page.

The Business Unit Container renders child components based on the selected business unit at run time, updating all data to reflect the associated data space. This single component simplifies the admin setup and ensures that users only see relevant, partitioned marketing data. The component is only visible in orgs with more than one business unit and to members of business units.

## Business Unit Container Settings

Configure sections that appear on a record page based on the user's selected business unit. You can configure these sections by selecting one of these business unit scopes:

  * Specific Business Unit: Define settings for each business unit.

  * Default Settings: Define settings for a fallback section, which is used for any business unit that doesn’t have its own specific configuration.




To configure fields for Data 360 Profile Engagement and Profile Insights, see [_Recommended Page Customization_](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_page_layouts_ref.htm&language=en_US&type=5).

To learn more about customizing pages in Marketing Cloud Next, see [Create and Configure Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&language=en_US&type=5).
