<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_opp_influence_enable.htm&language=en_US&type=5 -->

# Attribute Revenue to a Specific Campaign

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Attribute Revenue to a Specific Campaign

Opportunity Influence for Marketing Cloud Next uses engagement data to tie opportunity revenue back to a specific campaign. An engagement activity is eligible for attribution 30 days before the related opportunity is created to the date that the opportunity is set to Closed/Won. Use this attribution data to help you report on ROI, adjust your strategy for current campaigns, and make decisions about future campaigns.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To enable Opportunity Influence: |  Modify All Data OR Marketing Cloud Admin permission set  
  
To attribute revenue, Opportunity Influence identifies people who have engaged with campaign content and have a contact role on a Closed/Won opportunity. Opportunity Influence uses email and SMS click engagement activities to attribute revenue.

Opportunity Influence doesn't use activity data from external sites.

[](https://help.salesforce.com/s?language=en_US)Note Opportunity Influence replaces previous campaign attribution features. You must disable previous versions before you enable Opportunity Influence. To avoid confusion, remove the metrics fields for Campaign Influence or Customizable Campaign Influence from your campaign page layout. These fields aren’t used for Opportunity Influence.

Before you enable this feature, keep these considerations in mind.

[](https://help.salesforce.com/s?language=en_US)

  * If your org uses multiple currencies, revenue amounts aren’t converted but they show the currency symbol defined in each user’s settings.
  * Campaign hierarchies aren't reflected in Opportunity Influence revenue data.
  * Opportunity Influence attributes revenue based on engagement data related to Individual objects. It doesn’t use unified profile data. For more information, see [Unify Source Profiles](https://help.salesforce.com/s/articleView?id=data.c360_a_identity_resolution.htm&language=en_US&type=5).



  1. From Setup, in the Quick Find box, enter and then select **Opportunity Influence**.
  2. Review the Readiness Check section and complete any remaining tasks.
  3. Click **Enable** , and then turn on the attribution models that you want to use.

First-touch attribution gives credit to the first campaign that an opportunity contact engages with. Last-touch attribution gives credit to the last campaign they engaged with before closing.

When you enable Opportunity Influence, all eligible opportunity records and engagement activity are evaluated to generate attribution data. This process can take up to 1 hour. After that, all opportunity records and related engagement data are assessed hourly. Attribution records are created for opportunities created in the past 30 days based on engagements that have happened in the past 60 days.




After you enable the feature, the Opportunity Influence related list appears on campaign records under Performance. The list shows up to 1,000 opportunity records, in order of revenue.
