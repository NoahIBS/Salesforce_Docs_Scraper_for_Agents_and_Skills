<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 -->

# Manage Data Sources for Personalizing Content

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Manage Data Sources for Personalizing Content

To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
  
In each content item, in the Data Sources tab, view, add, and manage data sources. Keep these considerations in mind.

  * If you change a data source after its attributes are used in merge fields, to save the content, you must delete those merge fields. Then, add a new data source and recreate the merge fields.
  * When you combine content types that contain data sources, make sure the data sources match. For example, when you add a form to a landing page, the data graph for the form must be the same as the data graph in the landing page.

Data Source Type | Editions | Content Types  
---|---|---  
Data Graph | 

  * Marketing Cloud Next Growth
  * Marketing Cloud Next Advanced

| 

  * Content Block: Email
  * Content Block: Landing Page
  * Email
  * Landing Page
  * SMS Message
  * WhatsApp Message

  
Event | 

  * Starter and Pro Suite
  * Marketing Cloud Next Growth
  * Marketing Cloud Next Advanced

| 

  * Content Block: Email
  * Email
  * SMS Message
  * WhatsApp Message

  
Personalization Recommender | Marketing Cloud Next Advanced with [Personalization Decision Credits](https://help.salesforce.com/s/articleView?id=mktg.persnl_basics_billable_usage_types.htm&language=en_US&type=5) | 

  * Content Block: Email
  * Email

  
Unified Individual Data Model Object | 

  * Starter and Pro Suite
  * Marketing Cloud Next Growth
  * Marketing Cloud Next Advanced

| 

  * Email

  
  
## Data Graph

A [data graph](https://help.salesforce.com/s/articleView?id=data.c360_a_data_graphs.htm&language=en_US&type=5) is built from a primary data model object (DMO) and its related objects, and it combines this data to create a streamlined table that contains only the data you need for common tasks. Most of the data graphs that you use when personalizing marketing content are profile data graphs, which contain details about people and are based on the Unified Individual DMO.

A data graph can be either standard or real-time. Real-time data graphs provide faster response times, but they can cost a bit more. See [Billing Considerations for Data Graphs](https://help.salesforce.com/s/articleView?id=data.c360_a_billing_considerations_for_data_graphs.htm&language=en_US&type=5).

When a default data graph is [configured in Setup](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5), it appears in the Data Sources panel with a Default badge.

In an email or email content block, the default data graph is sufficient for most personalization tasks. You can’t remove or replace the data graph if the email contains any dynamic content variations or a Personalization recommender data source.

For a landing page, we recommend using a real-time data graph for faster response times and better performance. In a landing page content block, you can't remove or replace the data graph when the block is published.

In SMS and WhatsApp messages, only the default data graph is available. It doesn’t appear in the Data Source panel, but you can still use its data in merge fields.

## Event

An event is a specific activity that can trigger a flow, such as an order confirmation or subscription signup. Learn more about [campaigns and flows](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_ref.htm&language=en_US&type=5 "A campaign record shows information about each flow in the campaign, and it's designed to reflect certain elements from the Flow Builder canvas. Note, however, that some features and settings appear in Flow Builder that aren't available on the campaign record, and vice versa.") or about [marketing tasks based on events](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_event.htm&language=en_US&type=5 "Let Marketing Cloud Next take on some of your team’s manual tasks. To automate common tasks, message sends, and actions based on customer events, create a blank event campaign. For example, send an SMS message when someone signs up for an event, or send an email when someone subscribes to your email list.")

  * A content item can contain only 1 event data source, such as an email series that’s triggered each time a certain form is submitted.
  * In emails, repeater components don’t support custom event data.
  * You can't remove or replace an event when content is published.



## Personalization Recommender

A recommender is an element of [Salesforce Personalization](https://help.salesforce.com/s/articleView?id=mktg.mc_persnl.htm&language=en_US&type=5) that shows recommendations to customers based on their interests. In emails, you can use recommender data only in a repeater component and in merge fields within that component.

  * When you add a recommender data source, you can only select from trained recommenders that are based on the same data graph as the email.
  * When you want to use a new recommender, allocate time for the training period so that there’s at least one successful refresh.
  * You can replace but not remove recommender data sources.



## Unified Individual Data Model Object

Even when you don’t have a data graph or data source, you can still add merge fields based on the Unified Individual DMO.

In emails created in Starter and Pro Suite, you can only personalize content with merge fields using the Unified Individual DMO. In emails created in Marketing Cloud Next, dynamic content and Personalization Recommenders aren’t available until you add a data graph as a data source. 

#### See Also

  * [Using Data Graphs With Personalization](https://help.salesforce.com/s/articleView?id=mktg.persnl_setup_data_graphs_using.htm&language=en_US&type=5)
  * [Creating and Training Salesforce Personalization Recommenders](https://help.salesforce.com/s/articleView?id=mktg.persnl_recommender.htm&language=en_US&type=5)
  * [Data Sources for Forms in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_data_sources.htm&language=en_US&type=5 "A data source represents a Salesforce object, which you can use with a form. It creates a bridge between a form field and a CRM object field so that you can save the captured form data in Salesforce records.")


