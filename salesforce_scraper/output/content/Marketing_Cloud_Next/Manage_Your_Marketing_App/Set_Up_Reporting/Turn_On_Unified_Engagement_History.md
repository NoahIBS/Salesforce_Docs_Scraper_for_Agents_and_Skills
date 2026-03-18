<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_unified_dashboards_enable.htm&language=en_US&type=5 -->

# Turn On Unified Engagement History

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Turn On Unified Engagement History

To make valuable engagement data available for your sales and marketing teams, turn on Unified Engagement History Dashboards. Then, add the components to account, lead, and contact record pages.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To turn on Unified Engagement History: | System Administrator profile  
To install Marketing Performance: | Data Cloud Architect AND Marketing Cloud Admin permission sets  
  
Note To view unified engagement data from a specific business unit, a user must have a profile in that business unit. See [Business Units in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.bu_get_started_with_business_units.htm&language=en_US&type=5).

  1. From Setup, in the Quick Find box, enter `Unified Engagement`.
  2. Under Marketing Features, select **Unified Engagement History Dashboards**.
  3. Turn on Unified Engagement History Dashboards.
  4. Click **Set Up Permissions**.
  5. From the Permission Sets page in Setup, assign permission sets to users to give them viewer access to unified engagement data. See [Assign Permission Sets for Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_perms_assign.htm&language=en_US&type=5). 
     1. Assign the **View Unified Engagement History Dashboards** permission set.
     2. If you have Salesforce Foundations, assign the **Tableau Next Limited Viewer permission set**. For all other orgs, assign the **Tableau Next Included App Business User** permission set.
  6. [Install or update the Marketing Performance app.](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_marketing_performance.htm&language=en_US&type=5) This process can take several minutes to complete.

If the install button is unavailable, Marketing Performance is installed already.

  7. Add the Unified Engagement History Dashboard component to the record pages. See [Create and Configure Lightning Experience Record Pages](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&language=en_US&type=5).


