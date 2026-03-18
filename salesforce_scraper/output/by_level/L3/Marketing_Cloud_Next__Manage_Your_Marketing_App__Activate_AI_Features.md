<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_einstein.htm&language=en_US&type=5 -->

# Enable AI Features in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Enable AI Features in Marketing Cloud Next

Marketing Cloud Next includes features that use generative AI and predictive AI to save time and improve your key performance indicators (KPIs). These features aren’t dependent on each other, so you can choose the features that best fit the needs of your business.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To enable AI features, including Agentforce | Marketing Cloud Admin permission set  
To access the marketing agents | Marketing Team Agent Access  
  
  * **[Set Up a Data Graph for Einstein Send Time Optimization](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_esto_personalization_data_graph.htm&language=en_US&type=5)**  
To capture, automate, and personalize Einstein Send Time Optimization scores, set up a data graph based on the Unified Individual object.



[](https://help.salesforce.com/s?language=en_US)

## Set up AI in Marketing Cloud Next

To jumpstart a new marketing effort, AI can draft a campaign brief, a campaign, and campaign components. AI can also suggest a relevant segment. When you use AI, the security of your business and customer data is protected by the Einstein Trust Layer. 

  1. Set up [Salesforce Foundations](https://help.salesforce.com/s/articleView?id=xcloud.base_salesforce_foundations_setup.htm&language=en_US&type=5), which is required to enable marketing agent templates and access the latest Agentforce innovations for Marketing Cloud.
  2. Set up generative AI in Salesforce. See [Set Up Einstein Generative AI](https://help.salesforce.com/s/articleView?id=ai.generative_ai_enable.htm&language=en_US&type=5). For guidance on deploying the Agentforce Employee Agent, see the [Agentforce Implementation Guide for Employee-Facing Agents](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/agentforce_implementation_employee.pdf).
  3. Enable the [Agentforce Employee Agent](https://help.salesforce.com/s/articleView?id=ai.agent_manage_aea_access.htm&language=en_US&type=5) and make sure that users have the required permissions.
  4. Enable Marketing Cloud features and agents.
     1. In Setup, search for `Einstein & Agentforce`.
     2. Enable all the AI features that you want to use, and set up the applicable marketing agent templates.



After you turn on these features, they’re immediately available. 

[](https://help.salesforce.com/s?language=en_US)

## Agentforce Agents and Standard Actions

Agentforce uses several marketing-specific agents and standard actions to create briefs, campaigns, campaign content, and journey selections. 

After you enable Einstein generative AI and Agentforce, verify that the standard actions are there, and create any custom agents you need. For a full list of Agentforce actions, see the [Standard Agent Action Reference](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&language=en_US&type=5). You can [customize the standard actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_edit_reference.htm&language=en_US&type=5), and [add custom actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_custom.htm&language=en_US&type=5) to the agents.

Agent Name | Associated Standard Actions  
---|---  
Campaign Creation | 

  * Marketing Cloud: Draft a campaign Brief
  * Marketing Cloud: Refine Campaign Preview
  * Marketing Cloud: Save Campaign Brief
  * Marketing Cloud: Create a Campaign from a Brief
  * Marketing Cloud: Save Campaign
  * Identify Record by Name
  * Marketing Cloud: Summarize a Campaign
  * Marketing Cloud: Generate Campaign Insights
  * Marketing Cloud: Identify Business Unit

  
Content Builder | 

  * Marketing Cloud: Draft Content
  * Marketing Cloud: Create Section with Content
  * Marketing Cloud: Create Section

  
Journey Decisioning (for Marketing Cloud Engagement+) | 

  * Marketing Cloud: Select Journey
  * Marketing Cloud: Create Journey Content

  
  
[](https://help.salesforce.com/s?language=en_US)

See the [Agentforce Marketing: Campaign Creation Onboarding Guide](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/assets/pdf/agentforce-marketing-campaign-creation_onboarding-guide.pdf?_ga=2.128949388.1070081519.1763488027-310211748.1763488027&_gl=1*yeknj0*_gcl_au*MTQ4MTg1OTg0NS4xNzYzNDg4MDI3*_ga*MzEwMjExNzQ4LjE3NjM0ODgwMjc.*_ga_3VHBZ2DJWP*czE3NjM0ODgwMjYkbzEkZzAkdDE3NjM0ODgwMzUkajUxJGwwJGgw) for information about setting up and using the campaign creation agent.

To ground your results, enter your company’s brand identity and select a default tone in the branding section of the Content Builder.

[](https://help.salesforce.com/s?language=en_US)

## Optimize Email Send Times

Einstein Send Time Optimization is a predictive AI feature that uses historical data to help you send emails on the days and times when your customers are most likely to open them. To use this feature in Marketing Cloud Next Growth Edition, opt in to the Global Data Model for Einstein. In Advanced edition, you can enable global models or disable them to opt out.

  1. Verify that you have an identity resolution ruleset that uses Individual as the primary data model object.

This ruleset must be one of the first two identity resolution rulesets that you create for Marketing Cloud Next.

  2. From Setup, in the Quick Find box, enter `Send Time`, and select **Einstein Send Time Optimization (STO) with Global Models**.
  3. Review the global model information, and click **Enable**.



Einstein Send Time Optimization needs some time to gather data and build a model that’s specific to your data. To check on the model status, return to the setup page. If you disable this feature, new messages can’t use it, but existing email sends still include optimized send times.

For more information about data, review [the Einstein Send Time Optimization Model Card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_esto.htm&language=en_US&type=5 "In Marketing Cloud Next, Einstein Send Time Optimization analyzes the optimal time to send a message to an individual to maximize the probability of the individual engaging with the message.").

You can [build and use a data graph](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_esto_personalization_data_graph.htm&language=en_US&type=5 "To capture, automate, and personalize Einstein Send Time Optimization scores, set up a data graph based on the Unified Individual object.") to capture, automate, and personalize Einstein Send Time Optimization scores for your flows.

[](https://help.salesforce.com/s?language=en_US)

## Filter Non-Human Clicks from Your Report

Einstein Metrics Guard uses predictive AI to filter bot activity from your org’s engagement metrics. It removes most clicks and opens generated by security scanner bots without filtering out legitimate visitor activity.

  1. From Setup, in the Quick Find box, enter `Messaging`.
  2. Under Email, select **Email Feature Settings**.
  3. Turn on the feature.



For more information about data, review the [Einstein Metrics Guard model card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_emg.htm&language=en_US&type=5 "In Marketing Cloud Next, Einstein Metrics Guard analyzes email open and click events and calculates the likelihood that each event is real. The model primarily focuses on filtering emails through large-scale email providers that open messages before the customer opens them. The model is also effective for opens and clicks from email scanners on private, corporate email servers.").

[](https://help.salesforce.com/s?language=en_US)

## Increase Customer Engagement with Einstein Engagement Scoring

Einstein Engagement Scoring is a predictive AI feature that uses historical data to help you increase customer engagement. It assigns individual contact-level scores to determine the most efficient way to message recipients. This feature is available only in Marketing Cloud Next Advanced Edition.

[](https://help.salesforce.com/s?language=en_US)

  1. Verify that you have an identity resolution ruleset that uses Individual as the primary data model object.
  2. From Setup, in the Quick Find box, enter `Scoring`, and select **Einstein Engagement Scoring**.
  3. Review the information, and click **Enable**.



[](https://help.salesforce.com/s?language=en_US)

Einstein Engagement Scoring needs some time to gather data and build a model that’s specific to your campaign. If you disable this feature, Einstein doesn’t score new contacts, but previously scored contact data remains available.

For more information about data, review the [Einstein Engagement Scoring model card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_ees.htm&language=en_US&type=5 "In Marketing Cloud Next, Einstein Engagement Scoring predicts email opens and clicks, subscriber retention, web conversion, and overall engagement for each individual consumer contact.").

Using Einstein Engagement Scoring with the Einstein Decision element in a flow requires configuration of a data graph. In the configuration pane of the Einstein Decision element, select any of the data graph fields as the Resource in a condition. 

[](https://help.salesforce.com/s?language=en_US)

## Analyze Behavioral Data with Einstein Engagement Frequency

Einstein Engagement Frequency is a predictive AI feature that aggregates behavior data to determine how frequently to contact customers and improve the likelihood of customer engagement. This feature is available only in Marketing Cloud Next Advanced edition.

[](https://help.salesforce.com/s?language=en_US)

  1. Verify that you have an identity resolution ruleset that uses Individual as the primary data model object.
  2. From Setup, in the Quick Find box, enter `Frequency`, and select **Einstein Engagement Frequency**.
  3. Review the information, and click **Enable**.



[](https://help.salesforce.com/s?language=en_US)

If you disable this feature, your engagement metrics are more likely to include bot activity.

For more information about data, review the [Einstein Engagement Frequency model card](https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_model_card_eef.htm&language=en_US&type=5 "In Marketing Cloud Next, Einstein Engagement Frequency analyzes each contact’s engagement record to determine the optimal frequency for sending messages to that contact.").

Using Einstein Engagement Frequency with the Einstein Decision element in a flow requires configuration of a data graph. In the configuration pane of the Einstein Decision element, select any of the data graph fields as the resource in a condition.
