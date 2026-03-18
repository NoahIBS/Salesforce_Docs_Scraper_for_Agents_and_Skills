<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_flow_performance.htm&language=en_US&type=5 -->

# Set Up Flow Performance

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Flow Performance

Get detailed flow performance analytics for Marketing Cloud Next segment-triggered and automation event-triggered flows, powered by Tableau Next. These analytics can provide deeper insights into your flow's element runs, so you can make data-driven decisions.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To enable Flow Performance: | Data Cloud Architect and Marketing Cloud Admin permission sets  
To view Flow Performance dashboards: | Tableau Next Included App Business User permission set  
  
[](https://help.salesforce.com/s?language=en_US)Note Using the Flow Performance feature consumes Data 360 credits, which can increase your bill. For more information, see _Salesforce Help_ : [https://help.salesforce.com/s/articleView?id=data.c360_a_dc_billing_impact.htm&language=en_US](https://help.salesforce.com/s/articleView?id=data.c360_a_dc_billing_impact.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Install Flow Performance

Set up Flow Performance for the first time with Data 360 integration and analytics workspace.

  1. From Setup, in the Quick Find box, enter `Flow Performance` and click **Flow Performance**. 
  2. Select a data space to associate with Flow Performance analytics.
  3. In the Install Data 360 Integration section, click **Install**.
  4. Select the **Source Object** type for Flow Analytics. **Individuals** is the required Source Object for Marketing Cloud Next Flow analytics. 
  5. In the Install Analytics Workspace section, click **Install**. 

To start the installation, you must have both the Data Cloud Architect and Marketing Cloud Admin permission sets. Monitor the install progress on the Flow Performance tab. The tab name contains the selected data space, enabling easy differentiation if multiple apps have been installed (the tab name format is "Flow Performance Analytics - <dataspace name>"). To view the success or failure messages associated with your install, under Monitoring, click the event name.

  6. Assign the Tableau Next Included App Business User permission set to any users who require access to Flow Performance data. 
  7. Go to the Flow Performance Analytics tab to confirm the installation was successful. 



[](https://help.salesforce.com/s?language=en_US)

## Get the Latest Flow Performance Dashboard

To access the latest features and dashboards, update your Flow Performance app by first removing and then reinstalling the current version. Salesforce regularly updates Flow Performance reports and dashboards with new features, fields, and enhancements. You can find these updates in the release notes.

  1. From Setup, in the Quick Find box, enter `Flow Performance`, and then click **Flow Performance**.
  2. Go to the Flow Performance tab with the name that contains the corresponding data space. 
  3. Click **Delete** to remove the existing app. 
  4. Make sure that you've updated the [required Marketing data kits](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.").
  5. After the data kits are updated and show a Deployed status, reinstall the Flow Performance app from the Setup tab.
  6. To view the updated dashboard, follow the steps in [View Embedded Element Analytics and Detailed Insights](https://help.salesforce.com/s/articleView?id=platform.flow_monitor_on_canvas_insights.htm&language=en_US&type=5).


