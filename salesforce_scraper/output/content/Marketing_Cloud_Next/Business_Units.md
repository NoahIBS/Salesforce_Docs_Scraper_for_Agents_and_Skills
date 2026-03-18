<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.bu_get_started_with_business_units.htm&language=en_US&type=5 -->

# Business Units in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Business Units in Marketing Cloud Next

Business units create divisions within your org to focus on specific marketing goals, while also providing global visibility and control across the entire enterprise. Business units act as a junction between data and content, making sure that marketing efforts are aligned with specific organizational divisions.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
  
Define a business unit based on the structures and marketing needs of your business. For example, separate brands, localize by geographic region, organize different product lines, or focus on specific audience segments.

[](https://help.salesforce.com/s?language=en_US)

## Data Spaces and Business Units

Business units are designed to keep data separate, making sure that data from one business unit isn't shared with other business units. Business units use the existing capability of data spaces to enforce data separation. 

A business unit can be mapped to only one data space and that data space can't be related to any other business unit, establishing a one-to-one relationship. This one-to-one relationship keeps data isolated and simplifies how you manage marketing content for each business unit. For more information, see [About Data Spaces](https://help.salesforce.com/s/articleView?id=data.c360_a_data_spaces.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## The Initial Business Unit

To enable business units, start by creating the first two business units. Your current marketing configuration, including data space and default content workspace, are used to create your initial or first business unit.

  * All existing users with the selected marketing permission sets are added as members to the first business unit. Business unit members require Marketing Cloud Admin, Marketing Cloud Manager, or both permission sets.
  * The default marketing workspace in the org is assigned to the first business unit as the default workspace. In this workspace, all users with the selected permission sets get the Content Manager role.
  * Any existing marketing workspaces are also assigned to this first business unit, and you can create more workspaces for the business unit.



[](https://help.salesforce.com/s?language=en_US)

## Business Unit Members

Add users to a business unit as its members in one of these two roles: 

  * Marketer-Standard: Only users with the Marketing Cloud Admin or Marketing Cloud Manager permission sets can be added in this role. Only members with this role can activate flows in campaigns in the business unit. In the marketing workspaces of the business unit, these users have the Content Manager role and can create, edit, view, and publish content in the workspace.
  * Marketer-ReadOnly: Members with this role can’t activate campaigns in the business unit. They can send promotional messages and view performance dashboards. They don’t have access to the marketing workspaces in the business unit.



Business unit members in both these roles have access to the business unit’s data space. 

## Considerations for Business Units

[](https://help.salesforce.com/s?language=en_US)

  * After you create a business unit, you can’t delete it.
  * After you assign a data space, marketing workspace, campaign, or brief to a business unit, you can’t change the business unit.
  * A business unit can have multiple marketing workspaces, with one workspace designated as the default. See [Working with CMS Workspaces](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_working_with_cms_workspaces.htm&language=en_US&type=5 "When you create, organize, and share content in a marketing CMS workspace, keep these business unit considerations in mind.").
  * To make sure that campaigns only target audiences within that specific business unit while maintaining data integrity and compliance, all elements of a campaign operate within the selected business unit. See [Working with Campaigns](https://help.salesforce.com/s/articleView?id=mktg.working_with_campaigns_in_business_units.htm&language=en_US&type=5 "When you create a campaign, you must also select a business unit to relate to the campaign.").
  * You can create a maximum of 50 business units.



## Example: Business Units Use Case

To illustrate how business units work, consider Welo, a US-based ecommerce company specializing in sustainable home goods. Welo has successfully established its brand and customer base in the American market and now aims to expand into Latin America. The existing single-account setup isn't optimal for this expansion and can lead to customer confusion, irrelevant messaging, and compliance issues.

To localize its marketing efforts, manage separate campaigns, and adhere to different data privacy regulations in Latin America, Welo’s marketing admin creates a Welo Latam business unit. The Welo Latam business unit now serves as a dedicated, partitioned space for the company's expansion.

This framework also provides a scalable model for future market expansions, along with these benefits:

  * Partition data and content: Keep Latin American customer data, campaigns, flows, and content separate from its North American marketing operations.
  * Maintain local control: Provide the regional team with tools and data for a successful local marketing strategy.
  * Maintain global visibility: Enable Welo's leadership to track and analyze performance in both markets from a single platform, maintaining consistency and alignment with global goals.



  * **[Enable Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_enable_marketing_cloud_next.htm&language=en_US&type=5)**  
Before you create your first business units, review the prerequisites, and enable Marketing Cloud Next for your org.
  * **[Create Business Units in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_create_bus_in_mktg_cloud_next.htm&language=en_US&type=5)**  
To get started with business units in Marketing Cloud Next, create the first two business units. The first two business units are created consecutively. Next, select the marketing permission sets for the users to add to the first business unit.
  * **[Set Up Marketing Cloud Next for a Business Unit](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_setup_mktg_cloud_next_for_a_bu.htm&language=en_US&type=5)**  
When you have multiple business units, you configure some Marketing Cloud Next settings for each business unit separately, and other settings for the overall org. This means that you complete some tasks on the Business Units Setup page, some tasks in the Marketing Cloud Next Setup Assistant, and other tasks on specialized setup for messaging channels or other features.
  * **[Assign a Communication Subscription to Business Units](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_assign_a_communication_subscription.htm&language=en_US&type=5)**  
When you create a communication subscription, you can assign it to either a single business unit or all business units. All existing subscriptions are assigned to all business units. A subscription’s business unit assignment determines which channels can be added to it and in which business units it can be used.
  * **[Working with Campaigns in Business Units](https://help.salesforce.com/s/articleView?id=mktg.working_with_campaigns_in_business_units.htm&language=en_US&type=5)**  
When you create a campaign, you must also select a business unit to relate to the campaign.
  * **[Working with CMS Workspaces in Business Units](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_working_with_cms_workspaces.htm&language=en_US&type=5)**  
When you create, organize, and share content in a marketing CMS workspace, keep these business unit considerations in mind.


