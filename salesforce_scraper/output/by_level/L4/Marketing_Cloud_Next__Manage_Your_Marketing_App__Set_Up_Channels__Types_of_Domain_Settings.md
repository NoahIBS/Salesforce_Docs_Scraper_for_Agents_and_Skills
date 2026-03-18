<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_domains_ref.htm&language=en_US&type=5 -->

# Domain Settings in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Domain Settings in Marketing Cloud Next

Depending on your business needs, you can configure one or more domains to handle different jobs. You can choose My Domain to use a Salesforce subdomain or configure your own custom domain for hosting content. You can also create a tracking domain if you plan to use SMS messaging. Configuring DKIM (DomainKeys Identified Mail) authentication for sending emails is required.

### Required Editions

Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and the Salesforce Message Credits - SMS add-on  
  
## Default Domains

Marketing Cloud Next provides some default domains that support various content assets. This table outlines the default values that are used. Values in brackets indicate a variable that a marketing admin can configure. For further control over these URLs, you can configure custom domains for each usage type.

Usage | Domain Type | Default Values  
---|---|---  
Salesforce login URL | My Domain | [mydomain].salesforce.comAfter an admin configures the preferred My Domain for your org, its [used in many locations](https://help.salesforce.com/s/articleView?id=xcloud.domain_name_brand_your_org.htm&language=en_US&type=5).  
Email Links | Tracker Domain | cdp3.tracking.e360.salesforce.com  
Email Images | My Domain | https://[mydomain].cdn.salesforce-experiences.com  
Email Preference Center | My Domain | https://[mydomain].salesforce.com  
Landing Pages | Custom Domain | https://[mydomain].cdn.salesforce-experiences.com  
SMS Links | Tracker Domain, Shortener | https://[a].sfmsg.co  
  
Email sending domains for Marketing Cloud Next aren't provided by default. 

## My Domain

My Domain allows you to showcase your company’s brand with a custom subdomain name in your Salesforce org login, application URLs, and [some other locations](https://help.salesforce.com/s/articleView?id=xcloud.domain_name_brand_your_org.htm&language=en_US&type=5).

An admin can access My Domain setup pages here: **Salesforce Setup** | **Company Settings** | **My Domain** .

## Tracker Domain

A tracking domain monitors opens and link clicks in emails and SMS messages. The default tracking domain is owned by Salesforce, but you can configure a branded domain that your organization manages.

This process is sometimes called link rewriting, because we "rewrite" the original URLs in your message with the tracker domain. The page loads quickly through that domain where we capture the engagement, and then forwards them to the target URL. 

To use tracking, an admin must configure the domains on these pages, and then marketers can enable tracking on individual messages.

  * Email: **Salesforce Setup** | **Unified Messaging** | **Email** | **Email Links**
  * SMS: **Salesforce Setup** | **Unified Messaging** | **Branded Domain** | **URL Shortening Domain**



Separately, marketers can create a Marketing Tracked Link in the Content tab. These marketing links also support UTM parameters. See [Create and Manage a Custom Tracked Link](https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_custom_link_create.htm&language=en_US&type=5 "A custom tracked link reports clicks from content that you manage outside of Marketing Cloud Next, such as an ad, that points to a connected external website.").

## Email Sending Domain

You can use a custom domain to use for email sending, as long as you have access to the web registrar. Add the domain in Unified Messaging Setup, and then work with a IT or web administrator to apply DKIM and DMARC authentication methods to the DNS records. The authenticated sending domain is also used in your From email addresses and reply mail management.

DKIM (DomainKeys Identified Mail) is a method of email authentication that protects email recipients from messages that use spoofed email addresses. It can improve the deliverability of your emails by defining you as a legitimate sender.

DMARC (Domain-Based Message Authentication, Reporting & Conformance) is a toolset that tells receiving message servers how to handle messages that have failed authentication checks. An admin can get started here:

  * **Salesforce Setup** | **Unified Messaging** | **Email** | **Authenticated Domains**



## Custom Domains

For control over the page and asset URLs that appear to customers, configure a custom domain. Then, you can use it with subdomains for various purposes throughout Marketing Cloud Next. If you configure email link tracking, SMS, and landing pages, you must authenticate a different domain or subdomain for each use case.

If you plan to use a custom domain with marketing landing pages, we recommend that you select serving content with the Salesforce Content Delivery Network (CDN) during setup. To track activity on a landing page that uses a custom domain, add a custom URL for that domain in Setup and define the path as `/lp.`

To configure a custom domain for landing pages, visit **Salesforce Setup** | **User Interface** | **Sites and Domains** | **Domains**.
