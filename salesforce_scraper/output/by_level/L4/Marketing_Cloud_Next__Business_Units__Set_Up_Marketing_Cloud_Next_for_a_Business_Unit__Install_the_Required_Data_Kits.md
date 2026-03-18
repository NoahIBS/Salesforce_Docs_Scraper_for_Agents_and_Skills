<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_install_the_required_data_kits.htm&language=en_US&type=5 -->

# Install the Required Data Kits

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Install the Required Data Kits

Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. You install data kits in each data space that supports a business unit. After you install the data kits, most of the related data streams are deployed. In some cases, you manually deploy the data streams in Data Cloud.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To install data kits and packages: | System Administrator profile AND Data Cloud Architect AND Marketing Cloud Admin permission sets  
To deploy data streams: | Data Cloud Architect permission set  
  
Data streams consume Data Cloud credits based on the amount of batch data being processed. See [Data Cloud Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5).

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units page, select a business unit.
  3. Click **Basic Settings**.
  4. In the Install Marketing Data Kits section, click **Install** or **Update**.

If you’re installing for the first time, the listed data kits are installed and their related data streams are deployed automatically. If you’re updating data kits, you must manually redeploy the ingestion streams. See [Manually Deploy the Updated Data Streams](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5).

  5. Repeat steps 1–4 for each business unit.

This process takes a few minutes. The status of each data kit and its related data streams is shown, so that you can confirm that they’re installed and deployed successfully.



