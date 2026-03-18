<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_marketing_performance.htm&language=en_US&type=5 -->

# Set Up Marketing Performance

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Marketing Performance

Marketing Performance uses Data 360 and Tableau Next to present detailed metrics about your campaigns and content. Get embedded reporting in your campaign records, and access a comprehensive dashboard with insights and trends about your overall marketing efforts.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Foundations and with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To turn on Marketing Performance: | Data Cloud Architect and Marketing Cloud Admin permission sets  
To view Marketing Performance dashboards: | Tableau Next Included App Business User permission set  
  
[](https://help.salesforce.com/s?language=en_US)Note Using the Marketing Performance feature consumes Data 360 credits, which can increase your bill. Learn more about [the billing impact of Data 360-powered features](https://help.salesforce.com/s/articleView?id=data.c360_a_dc_billing_impact.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Install Marketing Performance

Set up Marketing Performance for the first time with Data 360 integration, data kits, and analytics workspace.

  1. From Setup, in the Quick Find box, enter `Marketing Performance` and click **Marketing Performance**. 
  2. Confirm that you have these prerequisites:
     1. Make sure that you've installed the [required Marketing data kits](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.").
     2. To personalize marketing content with data, [set up Personalization](https://help.salesforce.com/s/articleView?id=mktg.mc_pers.htm&language=en_US&type=5).
     3. To include web tracking data in reports, such as custom tracked link activity, [configure web tracking](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_parent.htm&language=en_US&type=5). 
     4. To view embedded analytics for Flow elements, [install Flow Performance](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_flow_performance.htm&language=en_US&type=5 "Get detailed flow performance analytics for Marketing Cloud Next segment-triggered and automation event-triggered flows, powered by Tableau Next. These analytics can provide deeper insights into your flow's element runs, so you can make data-driven decisions.").
  3. In the Install Marketing Performance section, click **Install**.

To start the installation, you must have both the Data Cloud Architect and Marketing Cloud Admin permission sets. Monitor the progress of the installation on the new Marketing Performance tab. To view the success or failure messages associated with your install, under Monitoring, click the event name.

  4. Assign the Tableau Next Included App Business User permission set to any users who require access to Marketing Performance data. See [Assign Marketing Permission Sets](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_perms_assign.htm&language=en_US&type=5 "After you set up data streams, create users and assign permissions. To make sure that users have access to the right objects and features, use the Marketing Cloud Admin or Marketing Cloud Manager permission sets. You can assign permission sets to individual users or assign them in bulk.").
  5. In the Marketing app, go to the Marketing Performance tab to view the main dashboard and confirm that your install is complete.

To learn more about Marketing Performance dashboards, see [Measure Success](https://help.salesforce.com/s/articleView?id=mktg.mktg_reporting.htm&language=en_US&type=5 "Monitoring performance and reporting on your successes are a significant part of a marketer’s job. Marketing Cloud Next includes reporting options powered by Data 360 and Tableau Next.").




[](https://help.salesforce.com/s?language=en_US)

## Get the Latest Marketing Performance Dashboard

To access the latest features and dashboards, update your Marketing Performance app by first removing and then reinstalling the current version. Salesforce regularly updates Marketing Performance reports and dashboards with new features, fields, and enhancements. You can find these updates in the release notes.

  1. From Setup, in the Quick Find box, enter `Marketing Performance`, and then click **Marketing Performance**.
  2. Go to the Marketing Performance tab.
  3. Delete the existing app. 

  4. Make sure that you’ve updated the [required Marketing data kits](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.").
  5. After the data kits update and show a Deployed status, reinstall the Marketing Performance app from the Setup tab.

  6. To view the updated dashboard, open the Marketing Performance tab in the Marketing app.


