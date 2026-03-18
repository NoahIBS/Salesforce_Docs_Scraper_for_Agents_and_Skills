<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_einstein_setup.htm&language=en_US&type=5 -->

# Set up Einstein Features for Business Units

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set up Einstein Features for Business Units

To maximize engagement in each business unit, enable Einstein’s predictive AI features—Send Time Optimization, Engagement Frequency, and Scoring. These tools leverage historical and global data to personalize message timing and frequency.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To set up Einstein Send Time Optimization: | Marketing Cloud AdminANDData Cloud Architect permission sets  
To enable Einstein Engagement Frequency | Marketing Cloud Admin  
To enable Einstein Engagement Scoring | Marketing Cloud Admin  
  
[](https://help.salesforce.com/s?language=en_US)

## Set Up Einstein Send Time Optimization

Einstein Send Time Optimization (ESTO) is a predictive AI feature that uses historical data to send emails on the days and times that customers are most likely to open them. In Marketing Cloud Advanced Edition, you can enable the Global Data Model for Einstein or disable it to opt out.

Verify that your business unit has an identity resolution ruleset that uses **Individual** as the primary data model object. This ruleset must be one of the first two identity resolution rulesets that you create for your business unit.

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units list page, select a business unit.
  3. Click **Einstein**.
  4. In the **Enable Einstein Send Time Optimization** section, enable with the global model or your own org-specific data.



Einstein Send Time Optimization needs some time to gather data and build a model that’s specific to your own org data. To check on the model status, return to the Setup page. If you disable this feature, new messages can’t use ESTO, but existing email sends still include optimized send times.

For more information about data, review the [Einstein Send Time Optimization Model Card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_esto.htm&language=en_US&type=5).

You can build and use a [data graph](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_esto_personalization_data_graph.htm&language=en_US&type=5) to capture, automate, and personalize ESTO scores for your flows.

[](https://help.salesforce.com/s?language=en_US)

## Enable Einstein Engagement Frequency

Einstein Engagement Frequency is a predictive AI feature that aggregates behavior data to determine how frequently to contact customers and improve the likelihood of customer engagement.

Verify that you have an identity resolution ruleset that uses **Individual** as the primary data model object.

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units list page, select a business unit.
  3. Click **Einstein**.
  4. In the **Einstein Engagement Frequency** section, click **Enable**.
  5. Repeat steps 1–5 for each business unit as needed.



For more information about data, review the [Einstein Engagement Frequency model card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_eef.htm&language=en_US&type=5).

To use Einstein Engagement Frequency with the **Einstein Decision** element in a flow, you must configure a data graph. In the configuration pane of the **Einstein Decision** element, select any data graph field as the Resource in a condition.

[](https://help.salesforce.com/s?language=en_US)

## Enable Einstein Engagement Scoring

Einstein Engagement Scoring is a predictive AI feature that uses historical data to assign scores to contacts to determine the most efficient way to message recipients to increase customer engagement.

  1. Verify that you have an identity resolution ruleset that uses **Individual** as the primary data model object.
  2. From Setup, in the Quick Find box, enter `Business Units` and select it.
  3. From the Business Units list page, select a business unit.
  4. Click **Einstein**.
  5. In the **Einstein Engagement Scoring** section, click **Enable**.



Einstein Engagement Scoring needs some time to gather data and build a model that’s specific to one campaign. If you disable this feature, Einstein doesn’t score new contacts, but previously scored contact data remains available.

For more information about data, review the [Einstein Engagement Scoring model card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_ees.htm&language=en_US&type=5).

To use Einstein Engagement Scoring with the **Einstein Decision** element in a flow, you must configure a data graph. In the configuration pane of the **Einstein Decision** element, select any data graph field as the Resource in a condition.
