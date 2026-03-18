<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5 -->

# Set Up Personalization Features in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Personalization Features in Marketing Cloud Next

When you personalize marketing messages using merge fields or dynamic content, you can improve the customer experience and increase engagement. Before you can start personalizing content, set up Personalization and configure a data graph based on the Unified Individual object. A data graph is also necessary for personalizing flow decisions.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User permissions needed  
---  
To set up Personalization | Data Cloud Architect permission setANDSalesforce Admin profileANDMarketing Cloud Admin permission set  
To create a data graph: | Data Cloud Architect permission set  
To select a data graph in Marketing Cloud Next setup: | Data Cloud Architect permission setANDSalesforce Admin profileANDMarketing Cloud Admin permission set  
  
[](https://help.salesforce.com/s?language=en_US)

## Set Up Personalization

To create dynamic content in your marketing emails and measure the effectiveness of personalized emails in your marketing campaign, first set up Personalization.

  1. From Setup, in the Quick Find box, enter `Customer` and select **Customer Engagement**.
  2. Click **Go to Personalization Setup**.
  3. Click **Start Setup**.
  4. Select the data space for your marketing data and click **Deploy**.
  5. To view personalization metrics, enable CRM analytics and install the Personalization Pipeline Intelligence dashboard.



[](https://help.salesforce.com/s?language=en_US)

## Configure a Data Graph

To choose which attributes to use for personalization in marketing content and flow decisions, start with a data graph that’s based on the Unified Individual object. How you configure the data graph determines what data points are available when defining targeting rules for dynamic content or cross object merge fields.

  1. In Data 360, [create a data graph](https://help.salesforce.com/s/articleView?id=data.c360_a_create_a_data_graph.htm&language=en_US&type=5) with these customizations.
     1. Select the data space for your marketing data.
     2. For the primary data model object (DMO), select **Unified Individual** , which consolidates an individual’s multiple lead and contact records into one record.
     3. Next to Unified Individual object, click ​​the plus icon to expand the related objects.

     4. Add these required fields. Click the plus icon to expand an object, and, in the right panel, select fields for each related object.

Related Object | Required Field  
---|---  
Unified Individual > Unified Link Individual > **Individual** | Individual ID  
Unified Individual > Unified Link Individual > Individual > **Contact Point Email** | Email Address  
Unified Individual > Unified Link Individual > Individual > **Contact Point Phone** | Telephone Number  
  
     5. Select any additional objects and fields to use for personalization, such as **Account** > **Account Name**.
  2. From Setup, in the Quick Find box, enter `Customer` and select **Customer Engagement**.
  3. In the Configure Basic Personalization section, from the Data Graph dropdown, select the data graph that you created.

In the Marketing app, without Salesforce Personalization, you can use only one data graph at a time. 




Now the objects and fields you selected are available to use in merge fields and flow decisions.

If you edit your data graph or switch to a different data graph in Marketing Cloud Next setup, the updated data graph applies only to future content and campaigns. You can't reuse personalization points created for one data graph with a different data graph. 

#### See Also

  * [Personalization and Data 360 Setup](https://help.salesforce.com/s/articleView?id=mktg.persnl_setup.htm&language=en_US&type=5)
  * [Data Graphs](https://help.salesforce.com/s/articleView?id=data.c360_a_data_graphs.htm&language=en_US&type=5)


