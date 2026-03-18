<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_eef.htm&language=en_US&type=5 -->

# Model Card: Einstein Engagement Frequency

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Model Card: Einstein Engagement Frequency

In Marketing Cloud Next, Einstein Engagement Frequency analyzes each contact’s engagement record to determine the optimal frequency for sending messages to that contact.

### Required Editions

[](https://help.salesforce.com/s?language=en_US) Available in: [](https://help.salesforce.com/s?language=en_US)Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud **Advanced** Edition  
---  
  
[](https://help.salesforce.com/s?language=en_US)

## Model Details

The Einstein Engagement Frequency model optimizes the frequency of customer engagement with email content using training algorithms, parameters, fairness constraints, and features.

**Person or Organization**

Salesforce Marketing Cloud Next Advanced Edition

**Model Data and Version**

[](https://help.salesforce.com/s?language=en_US)

  * October 2024
  * Minor changes can occur throughout the release
  * Major changes are communicated via release notes



**Model Type**

Matrix factorization, recommendation system

**General Information**

Einstein Engagement Frequency helps marketers determine the right number of emails to send to individual subscribers, reducing the unsubscribes that result from email fatigue. 

Marketers can use Einstein Engagement Frequency to identify opportunities to further engage subscribers with emails. The model analyzes individual subscribers’ historical engagement patterns over different frequencies. It uses the data of other users with similar patterns to adjust the scoring of each frequency. The ideal frequency range of each individual is then calculated based on those scores to find the best frequency to maximize engagement. Salesforce trains each customer’s model using only that customer’s data.

**Constraints**

[](https://help.salesforce.com/s?language=en_US)

  * A minimum of 10 subscribers is required to model for engagement frequency.
  * A minimum of five frequencies is required to model for engagement frequency. The audience must receive at least five variants of your email messaging over a 28-day period. For Einstein Engagement Frequency, a variant is defined as an email sending pattern, which is sending email to subscribers with at least five different intervals.



Note Customers that have Data Cloud One enabled and use Marketing Cloud Next Growth or Advanced edition operate from, store, and process customer data in the same location as the customer's Data 360 home organization, without reference to companion organization locations.

[](https://help.salesforce.com/s?language=en_US)

## Intended Use

The Einstein Engagement Frequency model powers the Frequency split activity in Expression Builder. The Frequency split activity is designed for marketing professionals to send the optimal number of emails to every subscriber, reducing subscriber email fatigue. The feature predicts the optimal number of emails to send an individual contact across all campaigns.

[](https://help.salesforce.com/s?language=en_US)

## Relevant Factors

Einstein Email Engagement Frequency analyzes up to 90 days of subscribers’ historical engagement patterns. The engagement history includes these factors.

[](https://help.salesforce.com/s?language=en_US)

  * Email sends, bounces, and engagement events, including opens, clicks, unsubscribes, spam complaints, and associated timestamps
  * Data and metadata about customer sending patterns, including how campaigns are executed



The engagement history that Einstein Engagement Frequency analyzes excludes these factors.

[](https://help.salesforce.com/s?language=en_US)

  * Data purchased or collected from third parties
  * Demographic data
  * Specific content in an email template or rendered email body



[](https://help.salesforce.com/s?language=en_US)

## Metrics

Einstein evaluates and monitors model performance metrics to ensure and improve the quality of the model. 

Model performance metrics include metrics like the spread and sparsity of input metrics and the correlation of output scores to historical observations. All metrics are aggregated and anonymized.

[](https://help.salesforce.com/s?language=en_US)

## Training Data

You have a customized version of the model that’s trained on your data alone.

[](https://help.salesforce.com/s?language=en_US)

## Ethical Considerations

To avoid bias and other ethical risks, the Einstein Engagement Frequency model doesn’t include demographic data.

[](https://help.salesforce.com/s?language=en_US)

## Refresh Cadence

Einstein Engagement Frequency scores and models for email are updated weekly. The refresh cadence varies by one to several days.
