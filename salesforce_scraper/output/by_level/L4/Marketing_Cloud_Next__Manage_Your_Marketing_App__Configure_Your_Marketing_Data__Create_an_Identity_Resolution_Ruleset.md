<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_identity_resolution.htm&language=en_US&type=5 -->

# Configure Identity Resolution Rulesets for Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure Identity Resolution Rulesets for Marketing Cloud Next

Identity resolution is a critical step to organizing and unifying your data. Usually, when your data originates from many systems, it’s modeled and labeled differently in each place. Identity resolution rulesets define the relationships among data model objects (DMOs) and their fields. After you configure these rules, Data 360 can organize related and duplicate data into unified individual records that marketers can use to target audiences.

### Required Editions

Scoring on people objects is available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
Scoring on the Account object is available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
User Permissions Needed  
---  
To create an identity resolution ruleset:  | Data Cloud Architect permission set  
  
Identity resolution rulesets consume Data 360 credits, which impacts billing. We recommend having only one active ruleset for the Individual object, and one active ruleset for the Account object. Maintaining two rulesets per object increases the amount that you’re billed for identity resolution. See [Data 360 Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5).

You can do more with identity resolution, such as create defaults or troubleshoot warnings. For details about fuzzy matching and other ruleset information, see Salesforce Help for Data 360.

#### See Also

  * [Unify Source Profiles](https://help.salesforce.com/s/articleView?id=data.c360_a_identity_resolution.htm&language=en_US&type=5)
  * [Identity Resolution Reconciliation Rules](https://help.salesforce.com/s/articleView?id=data.c360_a_reconciliation_rules.htm&language=en_US&type=5)
  * [Fuzzy and Exact Match Methods](https://help.salesforce.com/s/articleView?id=data.c360_a_match_rules_criteria_fuzzy_normalized.htm&language=en_US&type=5)



[](https://help.salesforce.com/s?language=en_US)

## Generate a Ruleset for the Individual Object

When you generate a ruleset for the Individual object, it uses Normalized Email, Lead to Contact, and Device to Known as match rules. Lead to Contact prevents duplication when leads become contacts, and Device to Known matches web visitors to known profiles.

[](https://help.salesforce.com/s?language=en_US)

  1. From Setup, in the Quick Find box, enter `Basic`, and select **Basic Settings**.
  2. Scroll to the Identity Resolution Rulesets section.
  3. In the Unified Individual section, click **Generate Ruleset**.
  4. Review the confirmation details and click **Generate**.
  5. Confirm that your new ruleset is published. [](https://help.salesforce.com/s?language=en_US)
     1. Go to the Identity Resolutions tab, and then find the ruleset you generated.
     2. Confirm that the ruleset status is published.



[](https://help.salesforce.com/s?language=en_US)

## Configure a Custom Ruleset for the Individual or Account Object

You can manually configure a custom ruleset for the Account object and for the Individual object. A custom ruleset creates unified records that meet your specific business needs/specifications.

[](https://help.salesforce.com/s?language=en_US)

  1. Create a ruleset. If you have a ruleset to use, skip this step. [](https://help.salesforce.com/s?language=en_US)
     1. On the Identity Resolutions tab, click **New**.
     2. Select **Create New Ruleset** , and then click **Next**.
     3. Select the data space that you use for marketing, and then select **Account** or **Individual** for the Primary Data Model Object.
     4. Enter an ID for the ruleset, and then click **Next**.

This 4-character ID is appended to the API name to distinguish between rulesets.

     5. Name the ruleset and save your work.
  2. From the identity resolution record, create custom rules.
     1. In the Match Rules section, click **Configure**.
     2. Follow the prompts to define the rules that unify related records.

If your ruleset is for the Individual object, add the [recommended rules to the ruleset](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_identity_resolution.htm&language=en_US&type=5#mktg-admin-data-rules "To get the most out of Identity Resolution, we recommend adding two custom rules to the Individual object ruleset. First, add a rule to match exact values when a lead converts to a contact. If you use web tracking on Marketing Cloud Next landing pages or a connected external site, add a rule that attributes activity to the correct unified individual. If you generate a ruleset for the Individual object after the Winter ’26 release, these rules are included by default.").

  3. Define which object to use for personalization. [](https://help.salesforce.com/s?language=en_US)
     1. From Setup, in the Quick Find box, enter `Basic`, and select **Basic Settings**.
     2. In the Create an Identity Resolution Ruleset section, select the Unified Individual or Unified Account object related to your ruleset.



[](https://help.salesforce.com/s?language=en_US)

## Add Recommended Rules to the Individual Object Ruleset

To get the most out of Identity Resolution, we recommend adding two custom rules to the Individual object ruleset. First, add a rule to match exact values when a lead converts to a contact. If you use web tracking on Marketing Cloud Next landing pages or a connected external site, add a rule that attributes activity to the correct unified individual. If you generate a ruleset for the Individual object after the Winter ’26 release, these rules are included by default.

  1. Go to the Identity Resolutions tab, and then open the ruleset that you created for the Individual object.
  2. Under Match Rules, click **Edit** , and then click **Next**.
  3. Click **Add Match Rule**.
  4. Click **Custom Rule** , and then click **Next**.
  5. Name your rule. For example, "Lead to Contact" or "Device Visitor Identification."
  6. Select the match criteria.
     1. For Data Model Object, select **Identity Match**.
     2. For Field, select **Identity Match Type**.
     3. For Match Method, select **Exact**.
  7. Under Advanced Settings, click **Configure** , and then enter the Identity Match Type for the first custom rule.
     * For lead to contact conversion, enter `lead-to-contact`.
     * For web tracking attribution, enter `device-to-known`.
  8. Click **Back To Basic Settings** , and then click **Next**.
  9. To add the second rule, repeat steps 3 through 8 and use the remaining Identity Match Type.
  10. Save your work.


