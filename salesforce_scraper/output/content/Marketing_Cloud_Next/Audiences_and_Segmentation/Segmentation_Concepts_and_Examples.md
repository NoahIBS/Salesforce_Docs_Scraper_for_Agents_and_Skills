<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_audiences_segmentation_concepts.htm&language=en_US&type=5 -->

# Segmentation Concepts and Examples

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Segmentation Concepts and Examples

The segment canvas offers several features to help you identify the right audience. Understanding the data behind the attribute library and the robust nesting and grouping features available can help you create the segments you need.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
To find out more about the fields available on each data model object (DMO), check out the [DMO reference in the Data 360 Reference Guide](https://developer.salesforce.com/docs/data/data-cloud-dmo-mapping/guide/c360dm-model-data.html).

For more information about segmentation concepts, check out these resources.

Concept | Description  
---|---  
[Hierarchical Aggregation in Segment Filters](https://help.salesforce.com/s/articleView?id=data.c360_a_segmentation_b2b_hierarchical_aggregation.htm&language=en_US&type=5) | Lets you accurately reflect your hierarchical account structures and gain a comprehensive view of your data by rolling up revenues for accounts and their subsidiaries, leading to more precise and meaningful segment filters.  
[Aggregation](https://help.salesforce.com/s/articleView?id=data.c360_a_aggregation.htm&language=en_US&type=5) | Defines your results by a grouping of values, such as a total number of records or minimum currency amount. Aggregation relates to the Measurement, Operator, and Value fields of a container object.  
[Event Time](https://help.salesforce.com/s/articleView?id=data.c360_a_container_basics_attributes.htm&language=en_US&type=5) | Determines a time frame during which related records can match your rules. Segments return data within the last 24 months. To expand that range, use an event time.  
[Container](https://help.salesforce.com/s/articleView?id=data.c360_a_use_a_container.htm&language=en_US&type=5), [Container Path](https://help.salesforce.com/s/articleView?id=data.c360_a_container_path.htm&language=en_US&type=5) | Groups attributes together and specify which values to build the segment on.  
[Operators](https://help.salesforce.com/s/articleView?id=data.c360_a_datatype_expression_operators.htm&language=en_US&type=5) | Determines what operation is used to match the attribute value, such as Day of Week or Is Equal To. Operators vary based on the DMO type (date, number, text).   
  
Note Aggregation and nesting aren’t available on direct attributes (Unified Individual fields).
