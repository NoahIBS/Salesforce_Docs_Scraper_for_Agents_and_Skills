<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_audiences_segmentation.htm&language=en_US&type=5 -->

# Understanding Segmentation in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Understanding Segmentation in Marketing Cloud Next

The Segments page in Marketing Cloud Next is the same one available in the Data Cloud Lightning app for Data 360. However, if you plan to use your segment with marketing campaigns, some specific field settings are required.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Already using Data 360 segments?

If you’re familiar with Data 360 segments, you’re used to selecting a data space and an object to segment on. However, segments used with marketing campaign flows must use the default data space and segment on the Unified Individual object.

You usually select activation targets and activate segments, but Marketing Cloud Next doesn't require activations. After you create a segment and publish it, it’s ready to use with a campaign. Review your publishing schedule if you plan to use it with automated messages.

## New to Data 360 segments?

In its simplest form, a segment is a set of filtering rules that are used to identify matching records in your database. You start with the total available audience, and add filters to reduce that population down to your target audience. In Marketing Cloud Next, the filters are often firmographic or engagement related, and the returned records are IDs for the contact points related to matching unified individuals.

The segment canvas is where you build the rules for your segment. The attribute library shows available objects and fields. Choose the Include or Exclude tab, drag fields into the center, and then define the rule. You can nest existing segments or restrict results by aggregation criteria, such as starting with a population with at least 5 orders.

To build complex segments, group attributes in containers. When multiple container paths are shown, verify the container path for the right results. [See an example](https://help.salesforce.com/s/articleView?id=data.c360_a_container_path.htm&language=en_US&type=5).

## Other Things to Know

  * A segment can contain up to 50 filters on the Include tab and 50 filters on the Exclude tab.
  * You can choose a publishing schedule that meets your business needs. Before choosing these options, consider how the increased usage impacts your billing.
    * Select **Don’t Refresh** when you want to create a static segment that doesn’t change.
    * To update the segment population regularly, choose Standard Publish and refresh at **12 hours** or **24 hours**.
    * Rapid Publish uses only a week of recent data, and can refresh at one or four hours. This option can be helpful if you’re running a time-sensitive campaign or automation.
  * To request the latest segment data in a multitouch campaign, choose the publish setting Immediately before running this flow in Flow Builder. This setting adds a publish to your regular segment schedule that updates the segment before starting a flow.
  * Other required automated processes, such as identity resolution, make your latest data available for use in a segment. When you’ve recently updated many records, consider the timing of these processes before you use a segment. The final population of a segment can be affected depending on when these processes finish and when a message is sent.



#### See Also

  * [ _Salesforce_ : Data Cloud Pricing Calculator](https://www.salesforce.com/data/pricing/calculator/)


