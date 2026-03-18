<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.bu_add_users_to_business_units.htm&language=en_US&type=5 -->

# Add Users to a Business Unit

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Add Users to a Business Unit

When you create your first business unit, users with the required Marketing Cloud Admin or Marketing Cloud Manager permission set are automatically added as members. For the second business unit and any additional business units you create, you can manually add users with one of the required permission sets. Only the users who you add to a business unit can use segments, flows, personalization, and Marketing Performance, and activate flows in campaigns within the business unit.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To add users to business units: | Marketing Cloud Admin permission set  
  
  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units page, select a business unit.
  3. From the selected business unit’s settings page, click **Add Users**.
  4. Select the users that you want to add to the business unit and click **Next**.
  5. Assign one of these roles to each of the selected users. 
     * Marketer-Standard: Users with this role can activate campaigns in the business unit. Only users with the Marketing Cloud Admin or Marketing Cloud Manager permission sets can be added in this role. 
     * Marketer-ReadOnly: Members with this role have only view access to the business unit.
  6. Confirm that each user that you selected has a required permission set, and then click **Next**. If a user doesn’t qualify, assign a required permission set and repeat steps 1–4. See [Assign Permission Sets](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_perms_assign.htm&language=en_US&type=5).
  7. To save your changes, click **Done**.



In the marketing workspaces of the business unit, users with the Marketer-Standard role get the Content Manager role and can create, edit, view, and publish content in the workspace. Users with the Marketer-ReadOnly role don’t have access to the marketing workspaces in the business unit. 

To increase a member’s access to a workspace, add them as a [contributor](https://help.salesforce.com/s/articleView?id=xcloud.cms_access_control_contributors.htm&language=en_US&type=5) to the workspace, and assign them the **Content Admin** role. You can’t decrease a member’s access to CMS workspaces. See [Manage User Access](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_user_access.htm&language=en_US&type=5).
