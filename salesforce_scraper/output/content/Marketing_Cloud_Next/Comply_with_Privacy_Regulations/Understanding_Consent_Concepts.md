<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tools_ref.htm&language=en_US&type=5 -->

# Understanding Consent Concepts in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Understanding Consent Concepts in Marketing Cloud Next

Review the tools and concepts that can help you collect and store consent data. You can collect consent for multiple engagement channels with communication subscriptions. Email is included with Marketing Cloud Next and all other channels are available as paid add-ons.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Channel Type

A channel type is a specific marketing channel, such as email or SMS. Each communication subscription includes at least one channel type. When someone subscribes to marketing messages, they must give consent for each channel type. For example, someone could opt in to receive SMS text messages about annual sales, but not subscribe to receive those emails.

## Communication Subscription

A communication subscription is the kind of marketing content someone signs up to receive, such as product updates. Subscriptions can store consent for one or more marketing channels, such as email. You have access to an editable default marketing communication subscription. You can create additional communication subscriptions as needed.

## Consent Check

A consent check requires you to select a communication subscription when you send a message and ensures that each recipient is opted in before sending to them. Consent is required when you send a promotional email, and any type of SMS or WhatsApp message. Consent checks for transactional emails are disabled by default.

Marketing admins can edit consent check settings in Salesforce Setup.

## Contact Point

A contact point is the contact information required to consent to a marketing subscription and channel, such as an email address or phone number. A Unified Individual can be associated with multiple contact points. For example, someone could have two different phone numbers on their Unified Individual record. When you send a message that requires a consent check, the consent object is reviewed for the contact points for each Unified Individual in your segment. Only opted-in contact points associated with the Unified Individual receive the message.

## Default Preference Pages

A preference page is where subscribers can manage their own communication preferences when they click the Preference Manager link in a message. After they click the link, they can select which communication subscriptions they want to receive messages for. For example, someone can opt into product update emails and also opt in to your weekly newsletter.

## Unified Individual

A Unified Individual record consolidates metadata related to multiple prospect, lead, or contact records that appear to be the same individual based on identity resolution rules that you set. These rules are how a contact point, such as a phone number, is associated with a Unified Individual. Consent is tied to the contact point value, as opposed to the Unified Individual record itself.

## Consent Objects

We recommend managing consent objects, records, and preference pages from the Consent tab. However, if your org requires more customization, you can also manage consent object records and Data 360 preference pages directly in Preference Manager. There are four objects that come together to store consent data:

  * Communication Subscription
  * Engagement Channel Type
  * Communication Subscription Channel Type
  * Communication Subscription Consent



## Create Consent Flow Action

The Create Consent flow action updates the consent status for a unified individual in a flow. Use this action to automate consent updates based on data such as a link click or form submission. This action is included by default in Signup Form campaign flows and is available in any event-triggered or Data 360-triggered flow. See [Flow Element: Create Consent](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_mktg_consent_request.htm&language=en_US&type=5).

#### See Also

  * [Communication Subscription Objects](https://help.salesforce.com/s/articleView?id=platform.communication_subscription_objects.htm&language=en_US&type=5)


