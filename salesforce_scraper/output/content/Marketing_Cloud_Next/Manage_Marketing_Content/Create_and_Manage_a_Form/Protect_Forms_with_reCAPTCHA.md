<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_recaptcha.htm&language=en_US&type=5 -->

# Protect Forms with reCAPTCHA

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Protect Forms with reCAPTCHA

Protect your marketing landing pages with forms from bots, fraudulent activities, spam, and abuse with Google reCAPTCHA. The Google reCAPTCHA v2 integration evaluates visitors' reputations and shows a reCAPTCHA to suspicious actors. It's available only for marketing landing pages with forms, and it doesn’t apply to LWR sites or other sites built from templates.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create and publish a form that uses data source fields: | Modify All Data for the data source object, the object fields on the form, and the record type selected for the data source object  
  
  1. If you haven’t already, get a site key and secret key from Google.
     1. Go to <https://cloud.google.com/security/products/recaptcha>.
     2. Click **v3 Admin Console**.
     3. Enter a label for your landing page site.
     4. Select **Challenge (v2)** , and then select **Invisible reCAPTCHA badge**.
     5. Under Domains, click the plus icon, and add the domain of your published landing page site.

If you change the My Domain details for your org, reCAPTCHA breaks on existing published sites. To fix this, add the new domain to the Google admin console. You can have more than one domain associated with a site key and secret key pair.

     6. Accept the terms, and click **Submit**.
     7. Copy the site key and secret key.
  2. In Salesforce Setup, in the Quick Find box, enter `All Sites`, and then select **All Sites** under Digital Experiences.
  3. Next to Marketing Landing Pages, select **Builder** from the Action column.
  4. Click **Settings** , and then select **Integrations**.
  5. Find the Google reCAPTCHA v2 integration, click **Add to Site** , and enable it.

When you enable the Google reCAPTCHA v2 integration, it’s added to all marketing landing pages that contain forms.

  6. Enter your site key and secret key.
  7. Save your work.



Publish your Marketing Landing Pages site to see reCAPTCHA in action.

Note Google reCAPTCHA functionality is provided by Google LLC. reCAPTCHA is a Non-SFDC Application and is subject to the [Google APIs Terms of Service](https://developers.google.com/terms/) and [Google Terms of Use](https://policies.google.com/terms).

For information about how Google uses data about your websites and customers, see [Google’s Privacy Policy](https://policies.google.com/technologies/partner-sites). Google also provides [advice for safeguarding your data](https://support.google.com/analytics/answer/6004245).
