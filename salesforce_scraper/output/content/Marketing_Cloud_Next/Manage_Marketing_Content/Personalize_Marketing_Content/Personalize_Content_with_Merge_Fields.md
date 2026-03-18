<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_merge_fields.htm&language=en_US&type=5 -->

# Personalizing Content with Merge Fields in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Personalizing Content with Merge Fields in Marketing Cloud Next

Use merge fields to personalize and enhance your marketing content. For example, personalize an email with your customer's name or customize a landing page with products you know they're interested in. Merge fields are available for any attribute related to a customer's unified profile, including account information and recent engagement activity.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
Note Account Engagement merge fields don't work with emails in Marketing Cloud Next campaigns. For more information, review [this Knowledge Article](https://help.salesforce.com/s/articleView?id=004518450&language=en_US&type=1).

## Use Event Data in a Merge Field

To use event data for merge field personalization, first assign an event as a [data source](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.") for your email, SMS, or WhatsApp message. You can then select that event when you configure the merge field and use message in an event-triggered flow. For example, send an order confirmation that includes the order amount and shipping details.

## Personalizing Content with Data from Different Objects

Cross-object merge fields help you personalize messages more precisely with timely and accurate data. For example, use data from a contact record and attributes from related objects, like a recent product purchase or a service case.

To personalize emails, reusable content blocks, or landing pages with data from different objects, make sure that a data graph based on the unified individual object is available as a [data source](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content."). Then, create an expression to find a data attribute for a merge field in associated data objects. In the expression, define criteria across objects to find the right attribute and narrow results.

To help maintain consistency across your marketing content and reduce message design time, you can create and save an expression in your marketing workspace. Then, select the expression in a future message to reuse filter and sort criteria, including the references to data objects.

Note Merge fields in landing pages are available in orgs created in Spring ’25 and later. SMS and WhatsApp messages use the default data graph that's configured in Setup.

This example shows building an expression with filter and sort conditions to find accounts with an annual revenue amount greater than $10,000.

Example

Marketer Erin wants to share recent opportunities with partners in an email. By using a merge field that’s related to both an account and an opportunity, Erin can insert the latest opportunity for a specific account. In the expression, Erin filters accounts by lead type and then sorts the related opportunities in descending date order to get the most recent opportunity. Erin saves the expression to reuse it in next month’s email to partners.

#### See Also

  * [Set Up Personalization Features in Marketing Cloud](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5)
  * [ _Video_ : Marketing Cloud: Cross-Object Merge Fields](https://salesforce.vidyard.com/watch/VrrS2gDQpW48LxffxdumDv)
  * [Create an Expression for a Personalized Merge Field in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_expression_create.htm&language=en_US&type=5 "Get more consistency and control over how data is referenced in your marketing content by saving criteria for personalized merge fields in an expression. Define filter and sort options across related data objects to select the right attribute for the merge field. Save the expression, including the references to those data objects, in Salesforce CMS. You can reuse the expression in email, SMS, and WhatsApp messages.")
  * [Create an Email in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_create.htm&language=en_US&type=5 "The content editing experience in Marketing Cloud Next provides tools to build an email, preview and test it, and publish it for use with a campaign. To make major changes to a published email or to prevent it from sending in a campaign, you can unpublish it.")
  * [Create and Manage an SMS Message in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_sms_create.htm&language=en_US&type=5 "Create an SMS message for your marketing campaigns and reach your customers directly on their mobile devices. For example, use SMS messaging to promote something new or follow up on an ongoing transaction.")


