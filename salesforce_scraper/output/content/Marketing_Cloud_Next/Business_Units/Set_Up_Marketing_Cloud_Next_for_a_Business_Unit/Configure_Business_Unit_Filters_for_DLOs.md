<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.configure_dlo_filters_for_bu.htm&language=en_US&type=5 -->

# Configure Business Unit Filters for DLOs

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure Business Unit Filters for DLOs

To make sure that a business unit’s data is available only in its data space and supports accurate segmentation and analytics, add business unit filters for marketing Data Lake Objects (DLOs) automatically. Filters are appended to your existing filters with the `BusinessUnitId` or `DataSpaceId` field by using an OR condition. Filters aren’t added to existing DLO filters with an AND condition.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User Permissions Needed  
---  
To create DLO filters:  | Marketing Cloud Admin ANDData Cloud Architect permission sets  
  
To view analytics from across business units or your entire enterprise, you can add filters that aggregate data from multiple or all business units. If you don’t use any filters, the DLOs include data from all business units. The business units still maintain their own fully partitioned campaigns and content.

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. From the Business Units list page, select a business unit.
  3. In the Business Unit Data Alignment section, click **Add DLO Filters**.
  4. Review the DLO filters to be added with the `BusinessUnitId` or `DataSpaceId` field. 

Any DLO filters with an AND condition are skipped from automated filtering.

  5. Click **Add Filter**.

Adding filters can take a few seconds.

  6. To view the added filters in Data 360, click **Go to this Data Space**.


  * **[DLOs Supported for Automated Filtering](https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_dlos_supported_for_automated_filtering.htm&language=en_US&type=5)**  
Automated filters are supported for several DLOs.


