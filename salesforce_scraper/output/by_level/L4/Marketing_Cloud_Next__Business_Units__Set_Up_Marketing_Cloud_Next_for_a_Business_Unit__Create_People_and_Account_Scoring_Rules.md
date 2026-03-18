<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_create_people_and_account_scoring_rules.htm&language=en_US&type=5 -->

# Create People and Account Scoring Rules

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create People and Account Scoring Rules

To begin scoring leads, contacts, prospects, and accounts, create scoring models and use default scoring rules or customize them. When you create a scoring model or scoring rule for a business unit, you work from the business unit settings page instead of the main scoring model page in Salesforce Setup. Otherwise, the steps are the same.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To manage and publish scoring models: | Configure Marketing Cloud Scoring ModelsANDData Cloud Architect  
  
  1. Create [identity resolution rulesets for the Individual and Account objects](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_configure_identity_resolution_rulesets.htm&language=en_US&type=5 "Identity resolution is a critical step to organizing and unifying your data. Usually, when your data originates from many systems, it’s modeled and labeled differently in each place. Identity resolution rulesets define the relationships among data model objects \(DMOs\) and their fields. After you configure these rules, Data Cloud can organize and reference related and duplicate data into unified individual records that marketers can use to target audiences.").
  2. Create a scoring model.
     1. From Setup, in the Quick Find box, enter `Business Units` and select **Business Units**.
     2. From the Business Units list page, select a business unit.
     3. In the Optimization and Personalization section, click **Scoring Models** , and then click **New**.
     4. Follow steps 2–7 of [Create a Scoring Model](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_scoring_setup.htm&language=en_US&type=5).
  3. Create custom scoring rules.
     1. In the **Scoring Rules** section of your business unit settings, select a scoring model.
     2. Follow steps 2–8 of [Create a Custom Scoring Rule](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_scoring_setup.htm&language=en_US&type=5).



For more information, including important considerations and how to create more complex rules, see [Score People and Accounts in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_scoring_parent.htm&language=en_US&type=5).
