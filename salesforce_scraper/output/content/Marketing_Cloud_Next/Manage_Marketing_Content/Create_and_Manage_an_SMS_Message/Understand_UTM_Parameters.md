<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_sms_utm_parameters.htm&language=en_US&type=5 -->

# Understand UTM Parameters

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Understand UTM Parameters

Use UTM (Urchin Tracking Module) parameters to track campaign performance and gain insights into traffic sources, how users arrive at your page, and the overall success of your SMS campaigns.

## UTM Parameters

UTM parameters are customizable tags that you can append to your URLs to track and measure the success of various aspects of your campaigns. UTM parameters can track traffic, referral sources, external campaigns, keywords, and content. 

While creating a UTM link, you can either enter the static values for the UTM parameters or map them to relevant campaign or flow attributes using merge fields. While this parameter mapping isn't restrictive, it's best to map the parameters logically based on your tracking requirements.

Parameter | Parameter Key | Description  
---|---|---  
UTM Campaign  | `utm_campaign` | Identifies the campaign  
UTM Medium | `utm_medium` | Identifies the communication channel, such as SMS or Email. This parameter maps to the channel name by default, and you can’t edit it.  
UTM Source | `utm_source` | Identifies the source of the traffic, such as Google or AdWords  
UTM Term | `utm_term` | Identifies the keywords that generate clicks  
UTM Content | `utm_content` | Identifies the content, such as a call-to-action message
