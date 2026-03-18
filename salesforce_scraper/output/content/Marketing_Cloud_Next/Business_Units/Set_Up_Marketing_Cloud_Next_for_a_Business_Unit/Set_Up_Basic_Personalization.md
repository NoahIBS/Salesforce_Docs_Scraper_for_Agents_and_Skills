<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_set_up_basic_personalization.htm&language=en_US&type=5 -->

# Set Up Basic Personalization

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Basic Personalization

To select attributes for content personalization and flow decisions, create a data graph that’s based on the Unified Individual object. As you build the data graph, select all the data points that you anticipate by using in personalization and automations, such as targeting rules for dynamic content or cross object merge fields.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To set up personalization:  | Marketing Cloud Admin ANDData Cloud Architect permission sets  
  
  1. In Data Cloud, create a data graph with these customizations.
     1. Select the data space for your business unit data.
     2. For the primary data model object (DMO), select **Unified Individual**.
     3. Next to Unified Individual object, click the plus icon to expand the related objects.
     4. Add these required fields. Click the plus icon to expand an object, and, in the right panel, select fields for each related object.

Required Data Graph Fields Related Objects | Required Field  
---|---  
Unified Individual > Unified Link Individual > Individual | Individual ID  
Unified Individual > Unified Link Individual > Individual > Contact Point Email | Email Address  
Unified Individual > Unified Link Individual > Individual > Contact Point Phone | Telephone Number  
  
     5. Select any additional objects and fields to use for personalization, such as Account > Account Name.
  2. From Setup, in the Quick Find box, enter `Business Units` and select it.
  3. From the Business Units list page, select a business unit.
  4. In the Optimization and Personalization section, click **Personalization Setup**.
  5. Select the data graph that you created. 

In the Marketing app, without Salesforce Personalization, you can use only one data graph at a time.

  6. Repeat steps 1–5 for each business unit as needed.



Now, the objects and fields from your data graph are available to use in merge fields and flow decisions.

If you edit your data graph or switch to a different data graph in setup, the updated data graph applies only to future content and campaigns. You can't reuse personalization points created for one data graph with a different data graph.
