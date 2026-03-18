<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_esto_personalization_data_graph.htm&language=en_US&type=5 -->

# Set Up a Data Graph for Einstein Send Time Optimization

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up a Data Graph for Einstein Send Time Optimization

To capture, automate, and personalize Einstein Send Time Optimization scores, set up a data graph based on the Unified Individual object.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create a data graph or to select a data graph in Marketing Cloud Next setup | View Setup and ConfigurationOR Salesforce Admin profileORMarketing Cloud Admin permission setANDData Cloud Architect permission set  
  
Customers using Einstein Send Time Optimization must have flows that use Einstein Send Time Optimization based on Data 360 data graphs that include the Email Send Time Optimization data model object and the Hourly Scores By Week attribute. 

Data graphs are only available in Marketing Cloud Next Growth and Advanced editions. Einstein Send Time Optimization in Starter, Pro, and Foundations editions use scores that are based on aggregated data and continue to blend in global model factors.

If Einstein STO was previously enabled in your org, you may need to disable and then re-enable it to get the latest updates to the STO data model. See [Enable AI Features](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_einstein.htm&language=en_US&type=5 "Marketing Cloud Next includes features that use generative AI and predictive AI to save time and improve your key performance indicators \(KPIs\). These features aren’t dependent on each other, so you can choose the features that best fit the needs of your business.").

[](https://help.salesforce.com/s?language=en_US)

## Use an Existing Data Graph for Einstein Send Time Optimization

Follow these steps if your org doesn’t already have a data graph created. To include personalized Einstein Send Time Optimization scores, start with a data graph that’s based on the Unified Individual object.

  1. In Data 360, [create a data graph](https://help.salesforce.com/s/articleView?id=data.c360_a_create_a_data_graph.htm&language=en_US&type=5) and add these customizations.
     1. For the primary data model object, select **Unified Individual**.
     2. Add the **Email Send Time Optimization** attribute. 
     3. Select the **Hourly Scores By Week** checkbox.

For example, the following join order is required when configuring the data graph.
    
    Unified Individual → 
        Unified Link Individual → 
            Individual → 
                Contact Point Email → 
                    Email Send Time Optimization

  2. Save the data graph.



After you build and save the data graph, Einstein Send Time Optimization scores that appear on records and in reports are refreshed weekly.

[](https://help.salesforce.com/s?language=en_US)

## Select a Data Graph for Einstein Send Time Optimization

If you’re already using a data graph for personalization, confirm that it includes the Email Send Time Optimization attribute and the Hourly Scores By Week field. If these attributes are missing, [edit the data graph](https://help.salesforce.com/s/articleView?id=data.c360_a_edit_a_data_graph.htm&language=en_US&type=5) to include them.

[](https://help.salesforce.com/s?language=en_US)

## Use Einstein Send Time Optimization Scores in a Flow

To use the ESTO scores, add the data graph to a flow. 

  1. Open a flow and save it as a new version.
  2. Click **Show Advanced**.
  3. Select the send time optimization data graph and click **Save**.


