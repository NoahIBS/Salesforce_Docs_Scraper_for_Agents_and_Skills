<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_landing_pages_parent.htm&language=en_US&type=5 -->

# Track Activity on Landing Pages

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Track Activity on Landing Pages

Track visitor activities on your Marketing Cloud Next landing pages. To protect the privacy of your landing page visitors, use the default consent banner to collect consent to track. You’re responsible for complying with privacy laws and regulations applicable to your business.

#### See Also

  * [Add Markup to the Page <head> to Customize Your Experience](https://help.salesforce.com/s/articleView?id=experience.community_builder_page_head.htm&language=en_US&type=5)



[](https://help.salesforce.com/s?language=en_US)

## Track Activity with Consent Banner

To add tracking and a consent banner to your landing pages, first review your consent banner settings, then add the banner integration to your Marketing Landing Pages site. To track activity on a landing page that uses a custom domain, add a custom URL for that domain in Setup and define the path as `/lp`.

  1. From Setup, in the Quick Find box, enter `Web Tracking`, and then select **Consent Banner**.
  2. Choose whether to require consent to track on all of your Salesforce-hosted landing pages. To help protect the privacy of your site visitors, this setting is on by default.
  3. Follow the steps to [customize the consent banner](https://help.salesforce.com/s/articleView?id=mktg.mktg_tracking_consent_banner.htm&language=en_US&type=5 "To protect the privacy of visitors to your Salesforce-hosted marketing landing pages, as well as your external sites, use the default consent banner to collect consent to track. You’re responsible for complying with privacy laws and regulations applicable to your business.").
  4. Add the banner integration to your landing pages.
     1. From Setup, in the Quick Find box, enter `All Sites`, and select **All Sites** under Digital Experiences.
     2. Next to Marketing Landing Pages, select **Builder**.

Marketing landing pages use the Experience Cloud Sites framework. This site operates behind the scenes. Don’t add content to it.

     3. Click **Settings** and select **Integrations**.

[](https://help.salesforce.com/s?language=en_US)

     4. On the Data Cloud integration, click **Add to Site** , and enable it.
     5. On the Data Cloud Web Tracking Consent Banner integration, click **Add to Site** , and enable it.
     6. To apply the banner and styles to your landing pages, click **Publish**.



After publishing, if you change the banner text or style settings, publish the banner again in Experience Cloud. To test the banner on a real page, create and view a landing page in a web browser.

[](https://help.salesforce.com/s?language=en_US)

## Enable Tracking Without Consent Banner

To track activity without collecting consent, you can publish a code snippet to your landing pages.

  1. From Setup, in the Quick Find box, enter `All Sites`, and then select **All Sites** under Digital Experiences.
  2. Next to Marketing Landing Pages, select **Builder** from the Action column.
  3. Set the Experience Builder security level to Relaxed CSP.
     1. Click **Settings** , and then select **Security & Privacy**.
     2. Click the Security Level dropdown menu and select **Relaxed CSP: Permit Access to Inline Scripts and Allowed Hosts**.
  4. Click **Settings** , and then select **Integrations**.
  5. Find the Data Cloud integration, click **Add to Site** , and enable it. 

Don’t install the Web Tracking Consent Banner for Data Cloud integration.

  6. Click **Settings** , and then click **Advanced**.
  7. Click **Edit Head Markup**. Copy this code and paste it into the Head Markup code block:
         
         [](https://help.salesforce.com/s?language=en_US)<script>
         document.dispatchEvent(
                 new CustomEvent('experience_interaction', {
                     bubbles: true,
                     composed: true,
                     detail: {
                         name: 'set-consent',
                         value: true,
                     },
                 })
             );
         </script>

  8. Save your work.
  9. To begin tracking activity, click **Publish**.


