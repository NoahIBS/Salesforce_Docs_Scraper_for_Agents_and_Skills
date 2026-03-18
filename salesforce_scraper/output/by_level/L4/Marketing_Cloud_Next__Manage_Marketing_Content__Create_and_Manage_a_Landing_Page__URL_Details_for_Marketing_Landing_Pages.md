<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_url_details.htm&language=en_US&type=5 -->

# URL Details for Marketing Landing Pages

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# URL Details for Marketing Landing Pages

Each landing page has its own URL that accepts or redirects traffic to the page. In Marketing Cloud Next, you can edit and manage URL details such as the public URL, URL alias, and the URL redirect from the content detail page on the URL tab.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Public URL

A public URL is a link to a page that's posted on a public site for anyone to access. When you publish a landing page, Salesforce generates a public URL for the page.

When multiple domains are associated with your site, you can add multiple public URLs. To add more public URLs, add domains to your site or add LWR sites as channels in the workspace, and then republish the landing page. If you have a custom domain, you can use it to create a custom URL that appears in the public URL for your Marketing Landing Pages site.

## URL Alias

A URL alias appears at the end of the public URL and contains no spaces, and is sometimes called a vanity URL. The default alias is based on the content title and key, but you can edit it to something that's easily readable, such as holiday-sale. The URL alias has these statuses.

  * Draft: The URL alias has never been activated and is editable. You can only edit the URL alias in draft status.
  * Active: The landing page was activated and can be accessed online via your URL alias and domain.
  * Inactive: The landing page was deactivated, can no longer be accessed via the URL alias, and users are redirected. Set up a URL redirect to send your landing page visitors to a different URL. You can reactivate a URL alias and use it again.



To make a landing page publicly available, activate the URL alias. When you deactivate an alias, the landing page is no longer publicly available, and visitors can't access the public URLs. To work with a URL alias, navigate to the **URL** tab of the landing page content detail page and then click **Activate** or **Deactivate**.

#### See Also

  * [Add a Custom URL](https://help.salesforce.com/s/articleView?id=platform.custom_url_add.htm&language=en_US&type=5)
  * [Domain Settings in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_domains_ref.htm&language=en_US&type=5 "Depending on your business needs, you can configure one or more domains to handle different jobs. You can choose My Domain to use a Salesforce subdomain or configure your own custom domain for hosting content. You can also create a tracking domain if you plan to use SMS messaging. Configuring DKIM \(DomainKeys Identified Mail\) authentication for sending emails is required.")


