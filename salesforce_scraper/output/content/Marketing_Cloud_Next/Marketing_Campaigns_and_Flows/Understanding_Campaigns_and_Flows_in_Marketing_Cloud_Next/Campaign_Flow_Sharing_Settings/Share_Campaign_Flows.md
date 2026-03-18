<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing_categorize.htm&language=en_US&type=5 -->

# Share Campaign Flows

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Share Campaign Flows

To plan for long-term, dynamic sharing, create categories and sharing rules for campaign flows. If you need to share a single campaign flow at any time, share a campaign flow manually.

In this topic: 

  * [Dynamic Sharing](https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing_categorize.htm&language=en_US&type=5#categories "Organize campaign flows into categories and subcategories. After an admin creates criteria-based sharing rules that control access to campaign flows, users can add categories and subcategories to apply the rules")
  * [Manual Sharing](https://help.salesforce.com/s/articleView?id=mktg.flow_distribute_sharing_categorize.htm&language=en_US&type=5#manual)



#### See Also

  * [ _Salesforce Help_ : What Is a Group?](https://help.salesforce.com/s/articleView?id=platform.user_groups.htm&language=en_US&type=5)
  * [_Salesforce Help_ : Create and Edit Groups](https://help.salesforce.com/s/articleView?id=platform.creating_and_editing_groups.htm&language=en_US&type=5)
  * [ _Salesforce Help_ : Sharing Settings](https://help.salesforce.com/s/articleView?id=platform.managing_the_sharing_model.htm&language=en_US&type=5)
  * [ _Salesforce Help_ : Create Criteria-Based Sharing Rules](https://help.salesforce.com/s/articleView?id=platform.security_sharing_rules_criteria.htm&language=en_US&type=5)
  * [ _Salesforce Help_ : Control Manual Sharing for User Records](https://help.salesforce.com/s/articleView?id=platform.security_sharing_owd_user_manual.htm&language=en_US&type=5)
  * [ _Salesforce Help_ : Manual Sharing Considerations](https://help.salesforce.com/s/articleView?id=platform.manual_sharing_considerations_lex.htm&language=en_US&type=5)
  * [ _Salesforce Help_ : Grant Access to Records with Manual Sharing in Lightning Experience](https://help.salesforce.com/s/articleView?id=platform.granting_access_to_records_lex.htm&language=en_US&type=5)



[](https://help.salesforce.com/s?language=en_US)

## Dynamically Share Campaign Flows

Organize campaign flows into categories and subcategories. After an admin creates criteria-based sharing rules that control access to campaign flows, users can add categories and subcategories to apply the rules

What you enter for category and subcategory must match exactly what’s defined in the sharing rule, especially if the sharing rule uses the Equals operator. Alternatively, if the sharing rule operator is **contains** , then your flow category only has to include what’s entered for the category in Sharing Settings.

  1. Select the flow that you want to share with sharing rules.
     * From the Marketing app, open the Flows tab, and then select a flow.
     * From the App Launcher, find and select Flows, and then select a flow.
  2. On the Details tab, add a category, subcategory, or both.

  3. Save your work.



Example

An admin categorizes flows by team, such as marketing, sales, and operations, and include subcategories related to how that team functions. The marketing team plans to use subcategories like Email, SMS, and Forms.

You're working with a group of email marketers and a group of SMS marketers. Each group needs different access to categories of flows, so you configure these sharing rules.

For email flows:

  * Category | equals | `Marketing`
  * Subcategory | equals | `Email`
  * Access Level is **Read/Write** for Group 1 users.
  * Access Level is **Read Only** for Group 2 users.



For SMS flows:

  * Category | equals | `Marketing`
  * Subcategory | equals | `SMS`
  * Access Level is **Read Only** for Group 1 users.
  * Access Level is **Read/Write** for Group 2 users.

Now, when marketers apply categories on a flow’s detail page, the appropriate access is granted.

[](https://help.salesforce.com/s?language=en_US)

## Manually Share Campaign Flows

  1. Select the flow that you want to share.
     * From the Marketing app, open the Flows tab, and then select a flow.
     * From the App Launcher, find and select Flows, and then select a flow.
  2. On the flow record, click **Sharing**.
  3. In the Search field, select who you want to share with.
  4. Search for and select the user, public group, role, or role and internal subordinates.
  5. Save your work.


