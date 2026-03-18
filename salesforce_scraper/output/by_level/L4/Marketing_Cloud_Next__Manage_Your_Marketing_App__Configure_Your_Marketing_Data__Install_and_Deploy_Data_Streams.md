<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 -->

# Install and Deploy Data Streams for Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Install and Deploy Data Streams for Marketing Cloud Next

Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To install data kits and packages: | System Administrator profile AND Data Cloud Architect AND Marketing Cloud Admin permission sets  
To deploy data streams: | Data Cloud Architect permission set  
  
#### See Also

  * [Install a Package](https://help.salesforce.com/s/articleView?id=xcloud.distribution_installing_packages.htm&language=en_US&type=5)
  * [ _Knowledge Article_ : Tips for Managing Data Cloud Credit Consumption](https://help.salesforce.com/s/articleView?id=004633782&language=en_US&type=1)



[](https://help.salesforce.com/s?language=en_US)

## Install or Update Data Kits

To begin the data configuration process, install the data kits listed on the Basic Settings page of marketing setup.

Data streams consume Data 360 credits based on the amount of batch data that's processed. See [Data 360 Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5).

  1. From Setup, in the Quick Find box, enter `Basic`.
  2. Under Marketing Setup, click **Basic Settings**.
  3. In the Install Marketing Data Kits section, click **Install** or **Update**.

If you’re installing for the first time, the listed data kits are installed, and their related CRM and ingestion data streams are deployed. If you’re updating, the data kits with changes are reinstalled and redeployed.




The status of each data kit and its related data streams is shown, so you can confirm that they’re installed and deployed successfully. This process takes a few minutes.

[](https://help.salesforce.com/s?language=en_US)

## Manually Deploy the Updated Data Streams (Optional)

Sometimes, the required ingestion data streams don't deploy as expected. A user with the Data Cloud Architect permission set can manually deploy the updates.

The data stream names and field values are predefined by the package and can’t be changed.

  1. From the App Launcher, find and select **Data Streams**.
  2. On the Data Streams tab, click **New**.
  3. Select **Installed Data Kits and Packages** and click **Next**.
  4. On the Data Kits tab, select a data kit.
  5. Select a data stream or bundle from the list and click **Next**.

Some data kits include more than one bundle of data streams. You can deploy only one bundle at a time.

  6. Select the connector associated with the data stream that you're deploying and click **Next**.
  7. Review the fields that you’re adding, click **Next** , and click **Deploy**.



After you deploy a data stream, it’s removed from the data stream list. When the sidebar shows an empty list, you’re done with this step.
