<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_audiences_segment_create_manual.htm&language=en_US&type=5 -->

# Manually Create a Segment in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Manually Create a Segment in Marketing Cloud Next

To create a segment, you drag in attributes that describe your target audience. When you build segment rules, make sure that you select objects and fields that align with your data model.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
  1. Create a segment.
     * From a campaign record, click **Select Segment** | **New Segment**.
     * From the Segments tab, click **New**.
  2. Select the default data space.
  3. Segment on the Unified Individual object.
  4. Select a publish schedule.

A more frequent publishing schedule keeps data fresher, but has an impact on the data allocations in your org. To decide later, select Standard Schedule and set the frequency to **Don’t Refresh**.

  5. Add attributes to include in the segment.
     1. Select the **Include** canvas.
     2. Expand and browse the attribute library, find a field that you want to use, and then drag it onto the canvas.
  6. Configure the settings for the attribute.
     1. Set the [aggregator measurement](https://help.salesforce.com/s/articleView?id=mktg.mktg_audiences_segmentation_concepts.htm&language=en_US&type=5 "The segment canvas offers several features to help you identify the right audience. Understanding the data behind the attribute library and the robust nesting and grouping features available can help you create the segments you need.") for when to evaluate the rule.
     2. Select the operator.
     3. Enter a value to match on.
     4. Click **Done**.
  7. Drag other fields onto the Include canvas and configure them as needed.
  8. Set the AND/OR operator across all attributes.
     * **AND** returns results that match all of the rules together.
     * **OR** returns results that match any of the rules.
  9. To configure rules that keep records out of the segment, click **Exclude** , and then add and configure attributes.
  10. Save the segment.



Example Klara wants to exclude people who have received at least 5 emails from her already. On the Exclude canvas, she uses the aggregation fields to group matches using the values Count is at least 5.

Each time you save a segment, Salesforce estimates the number of matching records in the segment population. When you publish a segment, the system requests the latest available data.

After you save the segment, you can use the segment in other campaigns. To base a future segment on this one, drag it from the Segments tab on the attributes pane onto the canvas.

#### See Also

  * [ _Salesforce Help_ : Increase Segment Refresh in Data 360](https://help.salesforce.com/s/articleView?id=data.c360_a_rapid_segment_publish.htm&language=en_US&type=5)


