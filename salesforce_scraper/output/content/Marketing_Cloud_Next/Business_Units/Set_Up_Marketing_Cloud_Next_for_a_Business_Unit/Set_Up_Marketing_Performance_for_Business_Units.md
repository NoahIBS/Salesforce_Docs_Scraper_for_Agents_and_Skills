<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_set_up_marketing_perf_for_bus.htm&language=en_US&type=5 -->

# Set Up Marketing Performance for Business Units

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Marketing Performance for Business Units

To get detailed analytics, configure the Marketing Performance app for a specific business unit. Get embedded reporting in your campaign records, and access a comprehensive dashboard with insights and trends about your overall marketing efforts.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To set up marketing performance:  | Marketing Cloud Admin ANDData Cloud Architect permission setsANDTableau Next Included App Business User  
  
Note If you installed the Marketing Performance app before creating business units or before Winter ’26, update the app. First, remove the current version, and then reinstall the latest version.

  1. From Setup, in the Quick Find box, enter `Business Units` and select **Business Units**.
  2. From the Business Units page, select a business unit.
  3. Click **Marketing Performance**.
  4. Confirm these prerequisites:
     1. You installed the [required marketing data kits](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5).
     2. To personalize marketing content with data, you [set up Personalization](https://help.salesforce.com/s/articleView?id=mktg.mc_pers.htm&language=en_US&type=5).
     3. To include web tracking data in reports, such as custom tracked link activity, you [configured web tracking](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_parent.htm&language=en_US&type=5).
  5. In the Install Marketing Performance section, click **Install**. 

You can monitor the install progress on the new Marketing Performance tab. To view the success or failure messages for your installation, under Monitoring, click the **Event** name.

  6. Assign the **Tableau Next Included App Business User** permission set to any users who require access to Marketing Performance data. 

See [Assign Marketing Permission Sets](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_perms_assign.htm&language=en_US&type=5).

  7. In the Marketing app, go to the **Marketing Performance** tab to view the main dashboard and confirm that your install is complete.
  8. Repeat steps 1–7 for each business unit.



To learn more about Marketing Performance dashboards, see [Measure Success](https://help.salesforce.com/s/articleView?id=mktg.mktg_reporting.htm&language=en_US&type=5).
