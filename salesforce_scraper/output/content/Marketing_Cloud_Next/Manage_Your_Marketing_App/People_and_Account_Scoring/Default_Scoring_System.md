<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_data_scoring_default_ref.htm&language=en_US&type=5 -->

# Default Scoring System in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Default Scoring System in Marketing Cloud Next

Leads, contacts, prospects, and accounts are scored based on the rules that you publish. You can use the default rules for both engagement and fit, or you can customize them to fit your needs. All engagement rules are available for the Account object and all people objects. Fit rules are available only for the object that they’re listed under.

### Required Editions

Scoring on people objects is available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
Scoring on the Account object is available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
  
## People Scoring

Rule Type | Condition Details | Value | Points  
---|---|---|---  
Engagement | Website Engagement | Engagement Channel Action | Is | error | -5  
Engagement | Website Engagement | Engagement Channel Action | Is | form-submit | +10  
Engagement | Website Engagement | Engagement Channel Action | Is | anchor-click | +3  
Engagement | Website Engagement | Engagement Channel Action | Is | button-click | +3  
Engagement | Website Engagement | Engagement Channel Action | Is | search | +3  
Engagement | Website Engagement | Engagement | Engagement Channel Action | Is | page-view | +1  
Engagement | Message | Engagement | Engagement Channel Action | Is | SUBSCRIBE | +5  
Engagement | Message | Engagement | Engagement Channel Action | Is | CLICK | +3  
Engagement | Message | Engagement | Engagement Channel Action | Is | UNSUBSCRIBE | -5  
Engagement | Email | Engagement | Engagement Channel Action | Is | | CLICK | +3  
Engagement | Email | Engagement | Engagement Channel Action | Is | UNSUBSCRIBE | -5  
Fit | Contact Point Address | Country | Is | United States | +3  
  
[](https://help.salesforce.com/s?language=en_US)

## Account Scoring

Rule Type | Condition Details | Value | Points  
---|---|---|---  
Engagement | Account Contact | Activity Participant | Activity | Email Message | Is | Incoming | Is Equal ToANDAccount Contact | Activity Participant |Activity Participant Role | Is Equal To | 

  * true
  * From

| +50  
Engagement | Party | Lead | Activity Participant | Activity | Email Message | Is | Incoming | Is Equal ToANDLead | Activity Participant | Activity Participant Role | Is Equal To | 

  * true
  * From

| +50  
Fit | Account Type | Is Equal To | 

  * Prospect

| +30
