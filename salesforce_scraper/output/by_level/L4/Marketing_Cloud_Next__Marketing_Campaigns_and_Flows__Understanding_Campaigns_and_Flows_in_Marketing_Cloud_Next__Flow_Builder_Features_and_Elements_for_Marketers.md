<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_reference.htm&language=en_US&type=5 -->

# Flow Builder Features and Elements for Marketers

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Flow Builder Features and Elements for Marketers

Flow Builder is a robust tool for creating automation solutions to business challenges faced by a variety of industries and roles. Marketers have access to portions of Flow Builder that are helpful for accomplishing marketing jobs.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
[](https://help.salesforce.com/s?language=en_US)

## Flow Features for Marketers

Many Flow Builder features are available only in other clouds and to users and Salesforce admins with certain permissions. This list contains features that are accessible to Marketing Cloud Next users.

Feature | Description | Availability  
---|---|---  
Flow Reports | Standard reports for flow data. These reports are installed at setup as part of the provided data kits. | Marketing Cloud Next Growth and Advanced editions  
[On-Canvas Insights](https://help.salesforce.com/s/articleView?id=platform.flow_monitor_on_canvas_insights.htm&language=en_US&type=5) | Recent metrics for active and completed flows that appear on the flow canvas. Turn on Insights in the Analytics tab of a flow element's editing panel. | Marketing Cloud Next Advanced edition  
[Path Experiments](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_path_experiment.htm&language=en_US&type=5) | An element that triggers different experiences within a group of people. Use path experiments to create up to 10 versions of an A/B/N-style test. | Marketing Cloud Next Advanced edition with Personalization.  
  
## Flow Elements for Marketing Automation

Element | Description | In Segment-Triggered Flows | In Automation Event-Triggered Flows | In Activation-Triggered Flows  
---|---|---|---|---  
[Assignment](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_assignment.htm&language=en_US&type=5) | An Assignment element sets values in variables, collection variables, record variables, record collection variables, and global variables. | Yes | Yes | Yes  
[Collection Filter](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_filter.htm&language=en_US&type=5) | A Collection Filter element applies criteria to a collection, and then outputs a new collection that contains only the items that meet the criteria. | Yes | Yes | Yes  
[Collection Sort](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_sort.htm&language=en_US&type=5) | A Collection Sort element reorders the items within a collection and optionally limits the number of items that remain in the collection after the sort. | Yes | Yes | Yes  
[Create Consent](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_consent_request.htm&language=en_US&type=5) | A Consent Request element creates or updates the consent status for a contact point related to a unified individual in the flow. | No | Yes | No  
[Create Records](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_data_create.htm&language=en_US&type=5) | A Create Records element creates one or more records in your Salesforce org. | Yes | Yes | Yes  
[Decision](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_decision.htm&language=en_US&type=5) | A Decision element is like an IF/ELSE statement. It evaluates a set of conditions and routes individuals to paths based on the outcome of those conditions.  | Yes | Yes | Yes  
[Delete Records](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_data_delete.htm&language=en_US&type=5) | A Delete Records element permanently deletes Salesforce records in your org. | Yes | Yes | Yes  
[Get Records](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_data_get.htm&language=en_US&type=5) | A Get Records element finds Salesforce records that meet filter conditions and stores values from the records in variables. | Yes | Yes | Yes  
[Loop](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_loop.htm&language=en_US&type=5) | A Loop element starts a loop path for iterating over items in a collection variable. | Yes | Yes | Yes  
[Path Experiment](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_path_experiment.htm&language=en_US&type=5) | A Path Experiment element contains up to 10 versions of an experience to test content, scheduling, and other variables. Available in Advanced edition only. | Yes | Yes | No  
[Send Email Message](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_send_email_message.htm&language=en_US&type=5) | A Send Email Message element sends an email message to segment members based on conditions defined in the flow. | Yes | Yes | No  
[Send Mobile App Message](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_send_mobile_app_message.htm&language=en_US&type=5) | A Send Mobile App Message element sends a push notification message to flow members based on conditions defined in the flow. | Yes | Yes | No  
[Send SMS Message](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_send_sms_message.htm&language=en_US&type=5) | A Send SMS Message element sends an SMS message to flow members based on conditions defined in the flow. | Yes | Yes | No  
[Send to Journey](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_send_to_journey.htm&language=en_US&type=5) | A Send to Journey element sends flow members into Marketing Cloud Engagement journey. | Yes | Yes | Yes  
[Subflow](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_subflow.htm&language=en_US&type=5) | A Subflow element launches another active flow that’s available in your org. | Yes | Yes | Yes  
[Transform](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_transform.htm&language=en_US&type=5) | A Transform element maps and transforms source data to target data. | Yes | Yes | Yes  
[Update Records](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_data_update.htm&language=en_US&type=5) | An Update Records element creates one or more records in your Salesforce org. | Yes | Yes | Yes  
[Wait for Conditions](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_wait_for_conditions.htm&language=en_US&type=5), [Wait Until Date](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_wait_until_date.htm&language=en_US&type=5), and [Wait for Amount of Time](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_wait_for_amount_of_time.htm&language=en_US&type=5) | Wait elements pause the flow when wait conditions are met, such as a date and time, a length of time, or an event. | Yes | Yes | Partial
