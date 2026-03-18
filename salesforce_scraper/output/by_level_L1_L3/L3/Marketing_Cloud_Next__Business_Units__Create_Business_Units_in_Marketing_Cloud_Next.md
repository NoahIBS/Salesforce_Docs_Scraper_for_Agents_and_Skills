<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_bu_create_bus_in_mktg_cloud_next.htm&language=en_US&type=5 -->

# Create Business Units in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create Business Units in Marketing Cloud Next

To get started with business units in Marketing Cloud Next, create the first two business units. The first two business units are created consecutively. Next, select the marketing permission sets for the users to add to the first business unit.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition  
---  
User permissions needed  
---  
To create business units: | System Administrator profile AND Marketing Cloud Admin permission set  
  
Before you begin, make sure that you have two or more data spaces in your org.

Important To identify a data space with its related business unit, include the name of the business unit in the Description field of each data space. This description is useful in areas of the Marketing app where you select the data space, such as when creating a segment.

  1. From Setup, in the Quick Find box, enter `Business Units` and select it.
  2. Click **Enable Business Units**.
  3. Add the first business unit.
     1. Enter the name and an optional description for your initial business unit.
     2. Select whether consent and channels apply to all or a single business unit.

If you have created channels or subscription records, this option determines whether they’re available only to this business unit or to all business units.

     3. In the **Data Space Description** field, enter a description that includes the name of the related business unit. 

The default data space is the same data space that you selected for your marketing org. The description helps you identify the related business unit when you create objects in the Marketing app where you select the data space instead of the business unit, such as when creating a segment.

     4. Set the physical address of the initial business unit. If applicable, set the org address as the business unit’s address.
     5. Click **Next**.

Your current marketing conﬁguration, including data space and content workspaces, are assigned to the initial business unit. 

  4. To add users to the first business unit, select **Marketing Cloud Admin** , **Marketing Cloud Manager** , or both permission sets, and then click **Next**.
  5. Add the next business unit.
     1. Enter the name, API name, and an optional description for your second business unit.
     2. Select a data space.
     3. Enter a name and API name for a marketing CMS workspace. A new workspace is created and assigned as the default workspace for this business unit.
     4. Set the physical address of the second business unit, if necessary. 
     5. Click **Next**.
  6. Make sure that the data space and marketing workspaces to be assigned to the business unit are correct.

Important After you create a business unit, you can’t edit or delete it.

  7. Click **Done**.



Depending on your business requirements, create more business units on the Business Units page. Map each business unit to a unique data space.

If you add any users to the selected marketing permission sets later, add them manually to the business unit.
