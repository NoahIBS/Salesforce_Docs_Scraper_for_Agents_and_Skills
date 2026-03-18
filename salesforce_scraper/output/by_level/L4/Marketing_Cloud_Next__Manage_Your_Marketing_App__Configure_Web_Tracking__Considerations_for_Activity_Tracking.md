<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_considerations.htm&language=en_US&type=5 -->

# Considerations for Activity Tracking

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Considerations for Activity Tracking

Before you turn on activity tracking, review considerations, compliance details, and cookie information.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Compliance

You're responsible for complying with privacy laws and regulations applicable to your business. To protect the privacy of site visitors, use the default consent banner on landing pages and external sites. You can choose not to collect consent to track.

If consent to track is required, each visitor’s first page view isn't recorded because it occurs before they provide consent.

## Implementation

Landing pages are served using the Experience Cloud Sites framework. The default Marketing Landing Pages site operates behind the scenes. Don’t add content to it.

The default consent banner is used for both Marketing Cloud Next landing pages and external websites. Settings and styles apply everywhere the banner is used.

## Tracked Data

After you configure web tracking, these activities are tracked.

  * Page views
  * Form submissions
  * Link clicks
  * Button clicks



## Tracking Cookie Reference

We use cookies to identify landing page visitors and track their activity. Cookies store a unique identifier for each landing page visitor but don't store personally identifying information.

On Salesforce-hosted domains, tracking cookies are set at the subdomain level such as example.my-salesforce.com. If you use a custom domain, tracking cookies are set at the root domain level.

To make sure that activity is tracked, set up your website to use first-party tracking by aligning all of your web pages and Salesforce content under your root domain. Industry standards are moving away from third-party cookie tracking, and we recommend using first-party domain alignment.

Cookie Name | Duration | Classification | Details  
---|---|---|---  
guest_uuid_essential_<15-char SiteID> | 365 days | Not required | This cookie is no longer used but is set when someone visits a landing page or tracked site.  
_sfid_${domainHash} | 730 days | Not required | When someone visits a landing page, the _sfid_${domainHash} cookie is set and creates a unique ID for that visitor.  
sfmc_consent | 365 days | Required | Set when a visitor opts in or out of tracking from the consent banner. If a visitor opts in, the value is set to True, and the visitor is tracked. If the visitor opts out or ignores the consent banner, the value is set to False, and the visitor isn’t tracked.
