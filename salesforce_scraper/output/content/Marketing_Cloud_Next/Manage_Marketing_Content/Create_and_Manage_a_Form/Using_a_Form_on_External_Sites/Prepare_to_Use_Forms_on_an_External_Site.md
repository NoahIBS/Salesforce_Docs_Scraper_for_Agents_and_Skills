<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_external_prep.htm&language=en_US&type=5 -->

# Prepare to Use Forms on an External Site

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Prepare to Use Forms on an External Site

Before you embed a form on an external site, configure some security-related and administrative settings in Salesforce and on your external site.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create a form: | Marketing Cloud Manager permission set ANDAny CMS workspace contributor role  
To publish a form: | Marketing Cloud Manager permission set ANDA CMS workspace contributor role of content admin or content manager  
  
Note To ensure that activity is tracked, set your website up to use first-party tracking by aligning all of your web pages and Salesforce content under your root domain. Industry standards are moving away from third-party cookie tracking and we recommend using first-part domain alignment.

  1. Ensure that your external site supports iframes.
  2. In Salesforce, configure security settings.
     1. In Setup, enter `Digital Experiences` in the Quick Find box and select **All Sites**.
     2. Next to Marketing Landing Pages, in the Action column, select **Builder**.

The Marketing Landing Pages site is the only type of site that supports external forms.

     3. Click **Settings** and select **Security & Privacy**.
     4. For Clickjack Protection Level, select **Allow framing of site pages on external domains (Good protection)**.
     5. Click **Add Trusted Domain**.
     6. Enter the domain URL of your external site and then click **Add Trusted Domain**.

Enter only the domain URL, and not the complete URL of the web page where the form is being embedded. For example, <https://www.example.com/>.

     7. Publish the site. 
  3. To get engagement analytics for external forms and to manage consent, configure and enable web tracking for both Salesforce and your external site.

These steps are required only once per external site.

     1. [Set up web tracking for your external site](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_external.htm&language=en_US&type=5).
     2. [Enable Data 360 integration on your Digital Experiences Marketing Landing Pages site](https://help.salesforce.com/s/articleView?id=experience.exp_cloud_data_cloud.htm&language=en_US&type=5)

Allow up to 60 minutes for this process to finish.

  4. To protect forms with reCAPTCHA, add reCAPTCHA support to your external site, and [configure reCAPTCHA for the form in Salesforce](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_recaptcha.htm&language=en_US&type=5).

Your external site must use the same reCAPTCHA configuration (site and secret keys) as the Marketing Landing Pages site.




#### See Also

  * [Embed a Form on an External Site](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_external_embed.htm&language=en_US&type=5 "Deliver a form from exactly where you need it by embedding it on your own hosted web page.")


