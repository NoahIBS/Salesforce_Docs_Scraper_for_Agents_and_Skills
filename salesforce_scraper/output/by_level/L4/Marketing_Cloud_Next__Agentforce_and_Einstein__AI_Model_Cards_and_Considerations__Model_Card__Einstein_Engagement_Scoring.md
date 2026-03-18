<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_ees.htm&language=en_US&type=5 -->

# Model Card: Einstein Engagement Scoring

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Model Card: Einstein Engagement Scoring

In Marketing Cloud Next, Einstein Engagement Scoring predicts email opens and clicks, subscriber retention, web conversion, and overall engagement for each individual consumer contact. 

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: [](https://help.salesforce.com/s?language=en_US)Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud **Advanced** Edition  
---  
  
[](https://help.salesforce.com/s?language=en_US)

## Model Details

The Einstein Engagement Scoring model uses training algorithms, parameters, fairness constraints, and features.

**Person or Organization**

Salesforce Marketing Cloud Next Advanced Edition

**Model Data and Version**

[](https://help.salesforce.com/s?language=en_US)

  * October 2024
  * Minor changes can occur throughout the release
  * Major changes are communicated via release notes



**Model Type**

Forecasting, time-series analysis, classification, clustering

**General Information**

The model classifies each score into one of four categories based on customer-defined thresholds or machine-inferred thresholds. The model analyzes an individual subscriber’s historical events and engagement patterns to forecast future engagement scores. The most recent behavior and engagement patterns are emphasized in the predictions. The web conversion model is a classification model with features based on historical web interaction events. The model clusters predicted engagement scores to derive local threshold boundaries to classify contact engagement levels.

**Constraints**

A minimum of one email send is required for a contact to have prediction scores.

Note Customers that have Data Cloud One enabled and use Marketing Cloud Next Growth or Advanced edition operate from, store, and process customer data in the same location as the customer's Data 360 home organization, without reference to companion organization locations.

[](https://help.salesforce.com/s?language=en_US)

## Intended Use

The Einstein Email Engagement Scoring model offers five types of application-specific engagement likelihood for each subscriber. This insight gives you a deeper understanding of your subscribers so that you can fine-tune targeting in future campaigns and sends.

[](https://help.salesforce.com/s?language=en_US)

## Relevant Factors

Einstein Email Engagement Scoring analyzes up to 90 days of subscribers’ historical engagement patterns. The engagement history includes these factors.

  * Email sends, bounces, and engagement events, including opens, clicks, unsubscribes, and associated timestamps
  * User retention and subscription history
  * Subscriber web interaction events with associated timestamps, including view, search, profile, and purchase
  * Data and metadata about customer sending patterns, including how campaigns are executed
  * Categorization thresholds defined by customers when applicable



The engagement history that Einstein Engagement Scoring analyzes excludes these factors.

[](https://help.salesforce.com/s?language=en_US)

  * Data purchased or collected from third parties
  * Demographic data
  * Specific content in an email template or rendered email body



[](https://help.salesforce.com/s?language=en_US)

## Metrics

Einstein evaluates and monitors model performance metrics to ensure and improve the quality of the model. 

Model performance metrics include data such as the model fitness score based on the root mean squared error and mean absolute error, and the data richness score.

[](https://help.salesforce.com/s?language=en_US)

## Training Data

You have a customized version of the model that’s trained on your data alone.

[](https://help.salesforce.com/s?language=en_US)

## Ethical Considerations

To avoid bias and other ethical risks, the Einstein Email Engagement Scoring model doesn’t include demographic data.

Customers are responsible for interpreting Einstein’s insights, and they must be aware of any assumptions that they make when acting based on the model’s insights. However, adverse outcomes are possible due to model error.

Example The model predicted low engagement for a certain segment, so Phil chooses not to send a marketing communication to that set of customers. But if that prediction was inaccurate, Phil inadvertently caused some customers to miss benefits or opportunities.

[](https://help.salesforce.com/s?language=en_US)

## Refresh Cadence

Einstein Engagement Scoring scores and models for email are updated weekly. The refresh cadence varies by one to several days.
