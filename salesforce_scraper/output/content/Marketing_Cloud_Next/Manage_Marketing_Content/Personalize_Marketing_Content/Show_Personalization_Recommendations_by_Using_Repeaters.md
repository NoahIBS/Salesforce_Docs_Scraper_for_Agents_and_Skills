<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_repeater_recommendation.htm&language=en_US&type=5 -->

# Show Personalization Recommendations by Using Repeaters

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Show Personalization Recommendations by Using Repeaters

To show a series of recommendations to customers, such as suggested products or services, connect a repeater to a Salesforce Personalization recommender.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
For basic information about working with repeater components, see [Add a Repeater to a Marketing Email](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_repeater.htm&language=en_US&type=5 "Show a series of items such as new or best-selling products, recent order updates, upcoming events or promotions, and more with a repeater component. Connect the repeater to a data source, such as an event or default data graph attribute. Customize the repeater layout, and add merge fields to the nested components to show data from the repeater source.")

  1. In the [Data Sources tab](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content."), add the Personalization recommender you want to use in the repeater.

Only trained recommenders that are based on the same data graph as the email are shown.

  2. Drag a Repeater to the canvas.
  3. On the Settings tab in the component property panel, adjust the properties in the Data Layout section. Select a Repeater Layout, then adjust the number of items and items per row.

If you ‌change the repeater layout when it contains content or data, the content, data, and any style settings within the repeater get removed.

  4. For the Repeater Source, select the Personalization recommender.
  5. Add a recommendation merge field to a component nested in the repeater. For example, add the name of a recommended product.
     1. Select a heading component in the repeater and click **{ }**.
     2. In the Add Merge Field menu, expand **Recommendations** , and then select **Product Name**.
     3. Configure the rest of the merge field details, and then click **Done**.
  6. Continue adding merge fields to components in the repeater, and customize each component’s settings and style as desired.
  7. Save your changes as you work.



#### See Also

  * [Manage Data Sources for Personalizing Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.")


