<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_configure_identity_resolution_rulesets.htm&language=en_US&type=5 -->

# Configure Identity Resolution Rulesets for Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure Identity Resolution Rulesets for Marketing Cloud Next

Identity resolution is a critical step to organizing and unifying your data. Usually, when your data originates from many systems, it’s modeled and labeled differently in each place. Identity resolution rulesets define the relationships among data model objects (DMOs) and their fields. After you configure these rules, Data Cloud can organize and reference related and duplicate data into unified individual records that marketers can use to target audiences.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To create an identity resolution ruleset:  | Marketing Cloud Admin ANDData Cloud Architect permission sets  
  
Identity resolution rulesets consume Data Cloud credits, which impacts billing. We recommend having only one active ruleset per data space for the Individual object, and one active ruleset per data space for the Account object. Maintaining two rulesets per object increases the amount that you’re billed for identity resolution. See [Data Cloud Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5).

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units list page, select a business unit.
  3. Click **Basic Settings**.
  4. Generate a ruleset for the Individual object. When you generate a ruleset for the Individual object, it uses Normalized Email, Lead to Contact, and Device to Known as match rules. Lead to Contact prevents duplication when leads become contacts, and Device to Known matches web visitors to known profiles. To manually create a ruleset instead, follow step 5 and select **Individual** as the Primary Data Model Object.
     1. In the Unified Individual section, click **Generate Ruleset**.
     2. Review the confirmation details, and then click **Generate**.
     3. On the Identity Resolutions tab, confirm that your new ruleset published.
  5. Configure a custom Identity Resolution ruleset for the Account object.
     1. On the Identity Resolutions tab, click **New**.
     2. Select Create New Ruleset, and then click **Next**.
     3. Select the data space that you use for marketing, and then select **Account** for the Primary Data Model Object.
     4. Enter a recognizable, 4-character ID for the ruleset, and then click **Next**.
     5. Name the ruleset, and save your work.
     6. From the record, in the Match Rules section, click **Configure**.
     7. Follow the prompts to define the rules that unify related records.
     8. Return to the Setup page for your business unit.
     9. On the Basic Settings tab, select the Unified Account object that’s related to your ruleset.
  6. Repeat steps 1–5 for each business unit.


