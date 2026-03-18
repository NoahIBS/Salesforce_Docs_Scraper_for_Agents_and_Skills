<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_ref.htm&language=en_US&type=5 -->

# Configure Your Marketing Data

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Configure Your Marketing Data

One of the things that makes Marketing Cloud Next so powerful is its relationship to Data 360. To prepare your Salesforce org, install and deploy the data kits that include the data model objects (DMOs) that support marketing assets. Then, use identity resolution rulesets to organize and unify your data.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
This table lists the data kits that you must install and deploy to get started. The Setup label is used on marketing setup pages, and the package names appear on the installation and data stream deployment pages. 

For complete instructions, see [Install and Deploy Data](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5 "Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.").

Setup Label | Package Name | Details  
---|---|---  
Marketing Setup Objects Data Kit | Marketing Cloud Consent Objects | Contains two data bundles, MarketingSetup_General and SMSAddOn_General. The SMS bundle is required only when using the SMS add-on.  
Consent Objects Data Kit | UnifiedMessagingConsent | Contains ConsentAuditTrail and MessagingConsent data streams.  
Flows Integration Data Kit | Salesforce Data 360 \- Flow Integration | Contains the Flows data bundle and two Flow Run data streams that work with the Ingestion API.  
Email Channel Data Kit | MessagingEventsEmailEngagement | Contains a MessagingEventsEmail data stream.  
SMS Channel Data Kit | MessagingEventsSms | Contains a MessagingEventsSMS data stream. This data kit is only required when using the SMS add-on.  
WhatsApp Channel Data Kit | UnifiedWhatsAppPackage | Contains a MessagingEventsWhatsApp-WhatsAppEngagement data stream. This data kit is only required when using the WhatsApp add-on.  
Sales | — | Contains data streams for accounts, leads, and contacts. Access the installation page for this data kit in Data 360 Setup.  
  
  * **[Install and Deploy Data Streams for Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_kits_install_main.htm&language=en_US&type=5)**  
Data kits and packages contain the objects, fields, and data connections that make Marketing Cloud Next work. After you install the data kits, the related data streams are automatically deployed in Data 360.
  * **[Configure Identity Resolution Rulesets for Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_data_identity_resolution.htm&language=en_US&type=5)**  
Identity resolution is a critical step to organizing and unifying your data. Usually, when your data originates from many systems, it’s modeled and labeled differently in each place. Identity resolution rulesets define the relationships among data model objects (DMOs) and their fields. After you configure these rules, Data 360 can organize related and duplicate data into unified individual records that marketers can use to target audiences.
  * **[Enable Data Governance Permissions for Objects in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_enable_data_governance.htm&language=en_US&type=5)**  
To use Data 360 Data Governance features for Marketing Cloud Next, you need to grant access to the impacted objects according to an access policy.


