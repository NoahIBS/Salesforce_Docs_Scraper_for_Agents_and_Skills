<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization.htm&language=en_US&type=5 -->

# Personalize Marketing Content

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Personalize Marketing Content

To increase customer engagement and improve conversations, personalize your marketing content. Create one email with dynamic content variations that appear for different recipients based on targeting rules. Get timely and accurate results for merge fields in marketing messages, landing pages, and reusable content blocks by referencing personalized data. For example, include a name attribute from a customer’s unified individual profile, include product purchase or subscription event data, or reference attributes from across related data objects, such as a contact from an account.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
Before marketers can use cross object merge fields or create dynamic content, set up Salesforce Personalization and configure a data graph. See [Set up Personalization Features](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5).

  * **[Manage Data Sources for Personalizing Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5)**  
To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.
  * **[How Dynamic Content and Salesforce Personalization Work Together](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ep.htm&language=en_US&type=5)**  
Dynamic content in Marketing Cloud Next improves conversations and relationships with customers, and it can lead to more effective campaigns. Personalization points, decisions, and targeting rules from Salesforce Personalization power dynamic content. Dynamic components and fields are associated with personalization points, and variations are associated with decisions and targeting rules.
  * **[Create and Manage Variations in Marketing Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_create_variations.htm&language=en_US&type=5)**  
Personalize emails or landing pages with dynamic content. Create a single variation and configure a targeting rule to determine when that variation appears. Or create variations that use existing personalization settings and targeting rules by cloning a personalization point. Prioritize the most relevant content if someone qualifies for more than one variation.
  * **[Linked Personalization Points in Dynamic Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ppoint_reuse.htm&language=en_US&type=5)**  
To control variations in an email or landing page with the same personalization settings, link multiple components to a personalization point. Any changes that you make to the personalization settings apply to all the linked components. You can also personalize more components in an email without going over the limit of 25 personalization points per content item.
  * **[Link Components to an Existing Personalization Point in Dynamic Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ppoint_link.htm&language=en_US&type=5)**  
To control multiple dynamic components with the same personalization settings and rules, link multiple components or fields to one personalization point. When you add or delete variations, edit targeting rules, or reorder priorities, your changes apply to all the components or fields linked to that personalization point.
  * **[Personalizing Content with Merge Fields in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_merge_fields.htm&language=en_US&type=5)**  
Use merge fields to personalize and enhance your marketing content. For example, personalize an email with your customer's name or customize a landing page with products you know they're interested in. Merge fields are available for any attribute related to a customer's unified profile, including account information and recent engagement activity.
  * **[Create an Expression for a Personalized Merge Field in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_expression_create.htm&language=en_US&type=5)**  
Get more consistency and control over how data is referenced in your marketing content by saving criteria for personalized merge fields in an expression. Define filter and sort options across related data objects to select the right attribute for the merge field. Save the expression, including the references to those data objects, in Salesforce CMS. You can reuse the expression in email, SMS, and WhatsApp messages. 
  * **[Add a Repeater to a Marketing Email](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_repeater.htm&language=en_US&type=5)**  
Show a series of items such as new or best-selling products, recent order updates, upcoming events or promotions, and more with a repeater component. Connect the repeater to a data source, such as an event or default data graph attribute. Customize the repeater layout, and add merge fields to the nested components to show data from the repeater source.
  * **[Show Personalization Recommendations by Using Repeaters](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_repeater_recommendation.htm&language=en_US&type=5)**  
To show a series of recommendations to customers, such as suggested products or services, connect a repeater to a Salesforce Personalization recommender.


