<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_esto.htm&language=en_US&type=5 -->

# Model Card: Einstein Send Time Optimization

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Model Card: Einstein Send Time Optimization

In Marketing Cloud Next, Einstein Send Time Optimization analyzes the optimal time to send a message to an individual to maximize the probability of the individual engaging with the message.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Model Details

The Einstein Send Time Optimization model for Marketing Cloud Next maximizes customer engagement using optimal send times for email content using these training algorithms, parameters, fairness constraints, features, and other applied approaches.

**Person or Organization**

Salesforce Marketing Cloud Next Growth and Advanced Editions

**Model Data and Version**

  * February 2024
  * Minor changes can occur throughout the release
  * Major changes are communicated via release notes.



**Model Type**

Recommendation and prediction, latent factor matrix factorization

**Supported Channels**

Currently only email is supported.

**General Information**

Einstein Send Time Optimization is the Salesforce solution to maximize the engagement rate of email sends based on the send time.

The model chooses the optimal time to send an email to an individual that maximizes the probability of the individual engaging with the message. Because customer sending patterns vary greatly, we developed parameter sets that are suited for different patterns. During training, a parameter selector determines the chosen set for a particular business. 

Einstein Send Time Optimization uses global model data to train the model. Contributed data is anonymized and aggregated at both the business unit and contact levels before being used in local orgs. In this way, the global model can be used without sharing personal data, such as email addresses, between customer business units. When you enable Einstein Send Time Optimization, you automatically are opted-in to use global models.

Einstein Send Time Optimization analyzes the past 90 days of email engagement history.

Note Customers that have Data Cloud One enabled and use Marketing Cloud Next Growth or Advanced edition operate from, store, and process customer data in the same location as the customer's Data 360 home organization, without reference to companion organization locations.

## Intended Use

The primary intended use for the Einstein Send Time Optimization model is for marketing professionals to increase effectiveness in their email marketing campaigns and maximize customer engagement. Anything else is out of scope and not recommended. For example, reducing overall send latency for reservation booking emails isn’t an intended use case.

## Relevant Factors

These factors are associated with the Einstein Send Time Optimization model.

Model Input

The engagement history includes these values.

  * Email sends, bounces, and engagement events including opens, clicks, unsubscribes, spam complaints, and associated timestamps
  * Data and metadata about customer sending patterns, including how campaigns are executed



The engagement history that Einstein Send Time Optimization analyzes excludes these factors.

  * Data purchased or collected from third parties
  * Demographic data
  * Specific content in an email template or rendered email body
  * Transactional emails, such as purchase confirmations, password resets, and others



Environment

The model is trained and deployed in the Salesforce Marketing Cloud Next environment.

## Metrics

Einstein evaluates and monitors model performance metrics to ensure and improve the model quality. Customers are responsible for monitoring the model’s accuracy.

Model Performance Measures

Aggregated model performance metrics are gathered to monitor, ensure, and improve the quality of the model. Model performance metrics include the spread and sparsity of input metrics and the correlation of output scores to historical observations. All metrics are aggregated and anonymized.

## Training Data

Einstein Send Time Optimization is trained using a global model of in-house data and outsourced data. Data from one Salesforce customer doesn’t affect the behavior for another Salesforce customer. Each version of the model uses the global model data with optimized sample weights customized for each customer.

## Ethical Considerations

To avoid bias and other ethical risks, the Einstein STO model doesn’t include demographic data.

## Refresh Cadence

Einstein Send Time Optimization scores and models for email are updated approximately weekly. The refresh cadence varies by one to several days based on a customer's individual business unit.

  * **[Monitoring Weekly Einstein Send Time Optimization Predictions](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_chart_esto_weekly_predictions.htm&language=en_US&type=5)**  
Visualize and analyze customer engagement over the course of a week. Using Data 360 Data Model Object (DMO) information, you can create a chart that shows Einstein Send Time Optimization scores per contact point email rather than by a unified individual. Use the information to adjust your send time parameters and align with maximum engagement send times. Access and run your Email Send Time Optimization report from Data 360 reports or Analytics in the Marketing app.


