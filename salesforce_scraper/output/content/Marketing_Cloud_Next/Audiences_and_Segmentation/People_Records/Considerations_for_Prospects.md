<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_prospect_considerations.htm&language=en_US&type=5 -->

# Considerations for Prospects

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Considerations for Prospects

When working with prospects in Marketing Cloud Next, keep these considerations in mind.

[](https://help.salesforce.com/s?language=en_US)

  * The prospects that are converted to leads don't show up in the list view.
  * After converting a prospect to an existing lead, only empty fields in the existing lead are overwritten by values in the prospect fields.
  * When converting a prospect to a lead with Multi-Currency enabled in the org, if the annual revenue field is empty in the lead but populated in the prospect, the Currency ISO code and annual revenue of the prospect will replace those in the lead. If the prospect and lead have different currency codes, the prospect's currency code replaces the one in the lead to avoid currency conversion problems.
  * If custom required fields are enabled for leads, you can't convert prospects into leads.
  * You can't add a prospect to campaign as a campaign member. 
  * Prospects are not supported in Data Import Wizard.
  * You can't clone or bulk delete prospects.
  * The status values for prospects are the same as lead status values. 


