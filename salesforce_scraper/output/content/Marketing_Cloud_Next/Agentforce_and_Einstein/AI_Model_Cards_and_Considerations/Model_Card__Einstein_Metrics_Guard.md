<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_emg.htm&language=en_US&type=5 -->

# Model Card: Einstein Metrics Guard

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Model Card: Einstein Metrics Guard

In Marketing Cloud Next, Einstein Metrics Guard analyzes email open and click events and calculates the likelihood that each event is real. The model primarily focuses on filtering emails through large-scale email providers that open messages before the customer opens them. The model is also effective for opens and clicks from email scanners on private, corporate email servers.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
Marketing Cloud Next for Marketing Cloud Engagement **Pro** , **Corporate** , and **Enterprise** Editions  
  
Einstein Metrics Guard is available as a real-time filter on inbound email activity for Marketing Cloud Next email sends. It’s also available as a calculated score on email activity from Marketing Cloud Engagement+ that’s loaded into the Email Engagement DMO in Data Cloud. Each version addresses the same problem by using a different model.

## Model Details

To analyze message opens and clicks and distinguish between bots and humans, the Einstein Metrics Guard model analyzes message opens and clicks to distinguish between bots and humans by using training algorithms, parameters, fairness constraints, features, and other applied approaches.

**Person or Organization**

Salesforce Marketing Cloud Next Growth and Advanced Editions

**Model Data and Version**

  * February 2024
  * Minor changes can occur throughout the release
  * Major changes are communicated via release notes



**Model Types**

Bayesian based calculation and linear regression are used for the real-time prediction service. Logistic regression and isolation forest are used for the batch prediction service.

**General Information**

For each email open and click event, Einstein Metrics Guard assigns a confidence score that assesses human-initiated real opens or clicks. The score ranges from 0% to 100%. Lower scores represent higher confidence that the open or click is real. Higher scores represent a higher chance that the open or click event is machine-generated.

The model analyzes an individual’s historical engagement events and patterns to predict the chance that an open or click is real. The model monitors behavior changes by using event association and attribution. When building the predictions, the most recent behavior changes and engagement patterns are weighted more heavily.

Compared to a standard filtering-based approach, Einstein Metrics Guard reduces the risk of false positive and false negative results and minimizes information loss.

Note Customers that have Data Cloud One enabled and use Marketing Cloud Next Growth or Advanced edition operate from, store, and process customer data in the same location as the customer's Data 360 home organization, without reference to companion organization locations.

## Intended Use

The Einstein Metrics Guard model is intended for these use cases. Anything else is out of scope and not recommended.

  * The model provides a layer of information that helps Einstein calculate how trustworthy each email open or click is. Einstein Metrics Guard is in place in response to mail privacy protection implemented by some email client providers. Einstein can build more accurate models and provide better recommendations.
  * When using the real-time service that's embedded in Marketing Cloud Next sends, events that score poorly aren’t included in marketing statistics, and aren’t used to trigger follow-up actions.
  * When using the batch service for Marketing Cloud Engagement+ data in Data Cloud, all events receive a predictive score for customers to analyze and use in their marketing strategy.



## Relevant Factors

These factors are associated with the Einstein Metrics Guard model.

Model Input

The engagement history includes email sends and engagement events, including opens, clicks, user agent, IP subnet, and associated timestamps.

The engagement history that Einstein Metrics Guard analyzes excludes these factors.

  * Data purchased or collected from third parties
  * Demographic data
  * Specific content in an email template or rendered email body



Model Output

To measure the likelihood that an open or click is real, the model produces a probabilistic metric score for each event. The messaging service uses the score to filter out low-scoring activity.

Environment

The model is trained and deployed in the Salesforce Marketing Cloud Next environment.

## Metrics

Einstein evaluates and monitors model performance metrics to improve the model quality. Performance measures include data such as model mean absolute error score.

## Training Data

Einstein Metrics Guard is trained using a global model of in-house data and outsourced data. Data from one Salesforce customer doesn’t affect the behavior for another Salesforce customer. Each version of the model uses the global model data with optimized sample weights customized for each customer.

## Ethical Considerations

Review the ethical factors associated with the Einstein Metrics Guard model in Marketing Cloud Next. To avoid bias and other ethical risks, the model doesn’t include demographic data.

As you interpret your data, be aware of making assumptions based on the scores generated. Scenarios with potential adverse outcomes can occur in certain circumstances.

Example The model predicts low engagement, so you choose not to send a marketing communication to a set of customers. If the prediction was erroneous, there could be a negative impact to excluding some of those customers from access to benefits or opportunities.
