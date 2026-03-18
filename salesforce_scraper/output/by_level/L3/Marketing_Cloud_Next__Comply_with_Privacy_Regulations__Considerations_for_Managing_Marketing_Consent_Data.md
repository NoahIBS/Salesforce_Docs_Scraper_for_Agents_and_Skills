<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_considerations.htm&language=en_US&type=5 -->

# Considerations for Managing Marketing Consent Data

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Considerations for Managing Marketing Consent Data

When working with consent management tools in Marketing Cloud Next, keep these considerations in mind.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
[](https://help.salesforce.com/s?language=en_US)

## Consent Imports

[](https://help.salesforce.com/s?language=en_US)

  * To update the consent status for existing prospects, leads, and contacts, import consent data from the Consent tab.
  * Consent imports update the status and date of consent for each contact point in the import file. To create or update prospects, leads, or contacts, import from the Prospects, Leads, or Contacts tab.
  * After you update consent data in Marketing Cloud Next, it syncs to Data 360. It can take some time for changes to appear on prospect, lead, and contact records.



[](https://help.salesforce.com/s?language=en_US)

## Subscriptions and Preferences

[](https://help.salesforce.com/s?language=en_US)

  * You’re responsible for complying with any laws or regulations that apply to your business.
  * Deleting a communication subscription also deletes all of its related consent data. We recommend that you don’t delete communication subscriptions after you collect consent data.
  * Before you delete a communication subscription, make sure it’s removed from any preference pages first. When you delete a subscription that’s used on a preference page, you must remove it from the consent template in Preference Manager to remove it from the preference page.
  * The Preference Manager merge field doesn’t work with custom preference pages.


