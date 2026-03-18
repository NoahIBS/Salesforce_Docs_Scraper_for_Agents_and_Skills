<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_enable_data_governance.htm&language=en_US&type=5 -->

# Enable Data Governance Permissions for Objects in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Enable Data Governance Permissions for Objects in Marketing Cloud Next

To use Data 360 Data Governance features for Marketing Cloud Next, you need to grant access to the impacted objects according to an access policy.

You can use attribute-based access control (ABAC) or role-based access control (RBAC), giving you more granular control over your users' access to data. To assign these objects to an available policy, [_grant access to Data 360 objects_](http://sfdc.co/dc-objects)

## Associated Data 360 Objects

Object TYpe | Name | Additional Information  
---|---|---  
Data Lake Objects (DLOs) | Account | Some DLOs are appended with the org ID or other identifying information.   
BulkMessage   
Campaign  
CampaignMember  
CommSubscription   
CommSubscriptionChannelType  
ConsentAuditTrail-ConsentAuditTrail  
ConsentAuditTrailV2-ConsentAuditTrail  
Contact  
EngagementChannelType  
Flow Runs-FlowElementRun  
Flow Runs-FlowRun  
Flow Runs-IdentityMatch  
Flow_Run_Ingestion-FlowElementRun  
Flow_Run_Ingestion-FlowRun  
Flow_Run_Ingestion- IdentityMatch  
FlowRecord  
FlowRecordElement  
FlowRecordVersion  
FlowRecordVersionOccurrence  
Lead  
ListEmail   
ManagedContent  
ManagedContentPublishedUrl  
MarketSegment  
MessagingChannel   
MessagingChannelUsage  
MessagingConsent-MessagingConsent  
MessagingConsentV2-MessagingConsent  
MessagingEventsEmail-EmailEngagement  
MessagingEventsEmailV2-EmailEngagement  
MessagingEventsSmsV2-SmsEngagement  
MessagingEventsWhatsAppV2-WhatsappEngage Opportunity  
OpportunityContactRole  
Prospect User  
WebEngagementEventsV2-DeviceToIndividual   
Data Model Objects (DMOs) | Account | Each DMO name is appended with the name of the data space. For example, if your data space is called “Marketing,” the Account DMO displays the name as “Marketing_Account.”  
Account Contact  
Bulk Email Message  
Bulk Message  
Campaign  
Campaign Member   
Communication Subscription  
Communication Subscription Channel Type  
Communication Subscription Consent  
Contact Point Address  
Contact Point Email   
Contact Point Phone  
Digital Content  
Email Engagement  
Engagement Channel  
Engagement Channel Type  
Engagement Channel Usage  
Flow  
Flow Element  
Flow Element Run  
Flow Run  
Flow Version  
Flow Version Occurrence  
Identity Match   
Individual  
Lead  
Market Segment  
Message Engagement  
Opportunity  
Opportunity Contact   
Party  
Prospect  
User  
Website Publication  
Calculated Insights (CIOs) | Marketing Engagement Score | N/A  
Marketing Fit Score  
Overall Marketing Score  
  
If you have more than one data space, grant access to objects in each data space. Object names in non-default data spaces follow the convention of <DataSpace Prefix>_<Object Name>.
