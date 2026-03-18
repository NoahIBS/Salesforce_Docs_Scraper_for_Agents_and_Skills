<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_data_scoring_considerations.htm&language=en_US&type=5 -->

# Considerations for Scoring in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Considerations for Scoring in Marketing Cloud Next

When working with scoring, keep these considerations in mind.

### Required Editions

Scoring on people objects is available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
Scoring on the Account object is available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
  
  * Before you publish a scoring model for the first time, you can edit its rules and save the scoring model as a draft. Always republish a scoring rule after making any changes.
  * After you publish a scoring model, records are scored retroactively on any relevant data stored in Data 360.
  * If you change the scoring object, it can take some time to process your scoring models and apply their rules to records related to the new object.
  * When you customize or add a rule, enter exact attribute values and use the correct capitalization style. For example, to specify an unsubscribe from an email, you must enter “UNSUBSCRIBE”.
  * To make sure attribute values are exact, enable value suggestions for Text data type fields. See [Edit Data Model Object Properties](https://help.salesforce.com/s/articleView?id=data.c360_a_data_model_object_properties.htm&language=en_US&type=5).
  * Many attribute values are unique to your org or are variable depending on the lead or contact. For example, SMS short codes or a person’s email address. To determine the correct values for those types of attributes, review your data model objects in Data Explorer.
  * You can have up to 30 engagement rules and 30 fit rules.
  * You can have up to 10 conditions per rule. Each condition that is nested in a condition group counts toward this limit.
  * An individual's engagement, fit, and overall marketing scores are normalized to provide a number from 0 to 100. For engagement and fit scores, you can also see the raw aggregate data used to calculate the normalized scores.



#### See Also

  * [SMS Engagement Data in Unified Messaging](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms_engagement.htm&language=en_US&type=5)
  * [Email Engagement Data in Unified Messaging](https://help.salesforce.com/s/articleView?id=mktg.um_channel_email_engagement.htm&language=en_US&type=5)


