<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_page_layouts_ref.htm&language=en_US&type=5 -->

# Recommended Page Customization

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Recommended Page Customization

To help marketers find related information on frequently used pages, add components to Lightning record pages in the Marketing app. A Salesforce or marketing admin can access the Lightning App Builder from the Setup menu on any record page or from the Object Manager.

### Required Editions

Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
For more information, see [Create and Configure Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&language=en_US&type=5).

Lightning Component | Description | Available on…  
---|---|---  
Privacy Consent Status | A list of subscriptions and consent values | Leads, Contacts, and Person Accounts records  
Data 360 Profile Engagement | A table of engagement metrics from automations and messaging channels | Lead and Contact records  
Data 360 Profile Insights | A numerical score that indicates someone’s level of engagement | Lead and Contact records  
  
## Data 360 Profile Engagement Settings

To configure the engagement component, select these values for each field.

  * Match On: Lead ID or Contact ID (or a custom field that stores the Unified Individual ID)
  * Data Space: default
  * Unified Individual DMO: Unified Individual
  * Unified Individual Link: Unified Link Individual



Lastly, select one or more Engagement DMOs. Flow Runs are related to campaigns, and Messaging Engagement refers to SMS messaging.

## Data 360 Profile Insights Settings

Configure this component for each score that you want to show: Marketing Engagement Score, Marketing Fit Score, and Overall Marketing Score. Select these values for each component.

  * Match On: Lead ID or Contact ID (or a custom field that stores the Unified Individual ID)
  * Data Space: default
  * Unified Individual DMO: Unified Individual
  * Unified Individual Link: Unified Link Individual
  * Calculated Insight: Marketing Engagement Score OR Marketing Fit Score OR Overall Marketing Score



For the Measure field, use the value for the calculated insight you selected.

  * Marketing Engagement Score: Engagement__Score__c
  * Marketing Fit Score: Fit_Score__c
  * Overall Marketing Score: People_Score__c


