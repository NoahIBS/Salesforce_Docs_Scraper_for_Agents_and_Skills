<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_custom_mobile_app_events.htm&language=en_US&type=5 -->

# Set Up Custom Mobile App Events in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Custom Mobile App Events in Marketing Cloud Next

Track user behavioral interactions like button clicks, screen views, or purchases within your mobile app.

### Required Editions

Marketing Cloud Next Advanced Edition accounts with the Salesforce Message Credits - Mobile App Regional add-on.   
---  
  
Note

Custom mobile app events aren't supported in Government Cloud. See [Marketing Cloud Next in Government Cloud](https://help.salesforce.com/s/articleView?id=ind.government_cloud_marketing_cloud.htm&language=en_US&type=5).

Custom mobile app events are available only in Marketing Cloud Next instances hosted in Germany and the United States. If you aren’t sure which region your instance is hosted in, contact your account executive.

The Your Events page in Setup shows the custom mobile app events that are associated with your account. This table describes the information shown for each event.

Label | Description  
---|---  
**Event Name** | The name of the event.  
**Description** | The description of the event.  
**Application** | The app associated with the event.  
**Attributes** | The number of attributes associated with the event.  
**Status** | Indicates whether the event is active.  
**Created** | The date when the event was added to your account.  
**Created By** | The name of the user who added the event to your account.  
**Last Modified** | The date when the event was last modified.  
**Last Modified By** | The user who last modified the event.  
  
[](https://help.salesforce.com/s?language=en_US)

## Create a Custom App Event

Marketers can stream the event in real time from a mobile app via the unified Marketing Cloud SDK. Leverage this data in Data 360 for segmentation and deeper insights, or in Flow Builder to create personalized customer journeys.

You can't delete attributes after you activate your event, so make sure to review them first. 

You can't delete an active event. You can deactivate it if you don't want to use it anymore, but you can still reuse its attributes in other events, and reactivate it later.

If an attribute already exists, reuse it in an event to avoid duplication. For example, most events use attributes like Name and User ID.

  1. In Setup, go to **Unified Messaging** | **Mobile App** | **Your Events**.
  2. Click **New Event**.
  3. On the New Event window, enter an internal name and description for the event.
  4. For Application, select the app associated with the event.
  5. Add attributes to the event.
     * To create an attribute, click **New Attribute**. Enter the attribute name and select a data type for the attribute. Choose whether the attribute requires a value.
     * To add existing attributes, click **Add from Existing**. Select attributes and click **Add**.
  6. Click **Save & Continue**.
  7. To start tracking events, click **Activate**.


