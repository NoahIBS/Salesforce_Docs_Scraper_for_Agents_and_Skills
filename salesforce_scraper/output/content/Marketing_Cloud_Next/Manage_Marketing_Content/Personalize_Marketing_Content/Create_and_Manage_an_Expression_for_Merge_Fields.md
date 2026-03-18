<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_expression_create.htm&language=en_US&type=5 -->

# Create an Expression for a Personalized Merge Field in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create an Expression for a Personalized Merge Field in Marketing Cloud Next

Get more consistency and control over how data is referenced in your marketing content by saving criteria for personalized merge fields in an expression. Define filter and sort options across related data objects to select the right attribute for the merge field. Save the expression, including the references to those data objects, in Salesforce CMS. You can reuse the expression in email, SMS, and WhatsApp messages. 

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
You must have a data graph set up to create an expression. See [_Set Up Personalization Features for Marketing Cloud_](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5).

  1. From the Content tab, open your marketing workspace.
  2. Select **Add** | **Content** | **Expression**.
  3. Give your expression a title for internal use.
  4. Select the data source that contains the resources and attributes that you want to use.
  5. Navigate the resource path to select an attribute. 
  6. Add filter and sort conditions for the attribute.
  7. To add another resource to further narrow your expression, click the plus icon next to Resource and define the filter and sort conditions.
  8. Save your work. 



To make your expression available for use in marketing content, you must publish it. To change the expression or to prevent it from being used in content, unpublish it.

#### See Also

  * [Personalizing Content with Merge Fields in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_merge_fields.htm&language=en_US&type=5 "Use merge fields to personalize and enhance your marketing content. For example, personalize an email with your customer's name or customize a landing page with products you know they're interested in. Merge fields are available for any attribute related to a customer's unified profile, including account information and recent engagement activity.")


