<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_create.htm&language=en_US&type=5 -->

# Create and Manage a Landing Page in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage a Landing Page in Marketing Cloud Next

A landing page can provide introductory information, inform people about your brand, or host a form to gather prospect details.

### Required Editions

Available in:Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
Not sure where to start? Check out these [basics for creating content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create.htm&language=en_US&type=5 "The content editing experience in Marketing Cloud Next uses a single design framework so that building marketing content is familiar no matter what you’re creating. The layout and functionality are the same, but after you choose the content type, a curated selection of components appears for you to choose from.").

Note

Landing pages are hosted on an automatically generated Experience Cloud site called Marketing Landing Pages. This site is used only to host landing pages and doesn’t need to be edited.

However, if your landing page uses a language other than the default language for the Marketing Landing Pages site, a content admin must edit the site and add the landing page language. Publish the Marketing Landing Pages site for the change to take effect.

[](https://help.salesforce.com/s?language=en_US)

## Create a Landing Page

Before you create a landing page, decide whether to include a form. To include a form on your landing page, create the form first, and then create its landing page. A draft form and landing page are available as part of a Signup Form campaign.

Before you personalize your landing page with merge fields, review and manage its [data sources](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.") [data sources](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5).

  1. Create a landing page.
     1. From the Campaigns tab, create a Signup Form campaign. Then, on the campaign record, open the related landing page and click **Edit**.
     2. From the Content tab, open your marketing workspace, and then, select **Add** | **Content** | **Landing Page**.
  2. Click **Create** and then select the creation method.
     * To start from an existing design, click **Select a Template** , and select the template you want to use.
     * To start designing your own landing page, click **Use Components** , and then add or move components on the canvas to create the layout you want.
  3. To personalize your landing page, select a component on the canvas, and click **{ }** or **Add Merge Field**.
     1. To insert a value from the page viewer’s unified profile, such as their first name, click **Select Data Graph Attribute** and select a field from Primary Objects.
     2. To insert a value from a related data graph object, such as products purchased or other engagement, click **Select Data Graph Attribute**. Define the filter and sort conditions as needed.
  4. To improve your landing page’s visibility in search engine results, [configure its SEO properties](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_create.htm&language=en_US&type=5#seo "To improve your landing page’s visibility in organic search results, define search engine optimization \(SEO\) properties, such as the title, description, and head tags.").
  5. Save your changes, and then [preview your landing page](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_create.htm&language=en_US&type=5#preview_lp "To see your landing page the same way it appears to the public, preview it from the content detail page or the editor. You must be a site contributor to the Marketing Landing Pages site to preview landing pages. When you preview your landing page, also review any attached forms.").
  6. To give your landing page a more relevant or specific URL, edit its URL alias.

By default, the alias is based on the landing page title and content key. After you publish the landing page, you can't change the URL alias.

     1. Exit the content builder and open the landing page record.
     2. Open the URL tab and edit the URL alias.
  7. Publish the landing page.

Publishing a landing page activates its URL aliases. When you publish a landing page that contains a form, the form is published, and the flow related to the form is activated.

  8. Test the page and, optionally, review its consent banner. From the landing page record, select the URL tab, and click the Public URL.



To promote the page, include the link in emails or web and social content.

[](https://help.salesforce.com/s?language=en_US)

## Configure SEO Settings

To improve your landing page’s visibility in organic search results, define search engine optimization (SEO) properties, such as the title, description, and head tags.

For details on editable properties, see [SEO Page Properties for Landing Pages](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_seo.htm&language=en_US&type=5 "To improve search engine optimization \(SEO\), use head tags to add structured data to your landing page. Including structured data provides more control over how your landing page and its information looks in search results.").

  1. On the landing page content detail page, click **Edit**.
  2. Click **SEO**.
  3. Enter a public page title that appears in search results and in the user’s browser tab.
  4. To control which page details appear in the search results, enter a description.

If SEO indexing is enabled and this field is blank, the search engine results show the first text that the search engine finds on the page.

  5. To configure structured data, enter head tags.
  6. To improve a landing page’s visibility in search engine results, click **SEO** , and then select **Let search engines index this page**.
  7. Save your work, and publish the landing page.



[](https://help.salesforce.com/s?language=en_US)

## Preview a Landing Page

To see your landing page the same way it appears to the public, preview it from the content detail page or the editor. You must be a site contributor to the Marketing Landing Pages site to preview landing pages. When you preview your landing page, also review any attached forms.

Merge fields are unresolved in the landing page preview. If your landing page references an image at an external URL, make sure that domain is added to your trusted URL list in Setup. Otherwise, the image can't load correctly.

  1. Open the preview window.
     * When editing your landing page, in the main toolbar, click **Preview**.
     * From the landing page content detail page, click **Preview**.
  2. To see your landing page in a different view mode, such as desktop or mobile, select an option in the Preview Device menu.
  3. To preview personalized content, select a segment and a sample visitor.

When these fields are empty, the preview shows default variations and fallback values for merge fields.

  4. If your landing page includes forms, make sure that they display properly.

To edit a form on your landing page, go to your marketing workspace and open the form in the content builder.




[](https://help.salesforce.com/s?language=en_US)

## Redirect a Landing Page

To redirect visitors to a specific site or URL, deactivate the URL alias and set up a redirect URL.

For more information about a page's URL types, see [URL Details for Landing Pages](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_url_details.htm&language=en_US&type=5 "Each landing page has its own URL that accepts or redirects traffic to the page. In Marketing Cloud Next, you can edit and manage URL details such as the public URL, URL alias, and the URL redirect from the content detail page on the URL tab.").

  1. Open the landing page content detail page and then click **URL**.
  2. Click **Deactivate URL Alias...**.
  3. Enter a redirect URL that begins with `https://` and click **Deactivate**.

The URL must be fewer than 2,000 characters long.




[](https://help.salesforce.com/s?language=en_US)

## Unpublish a Landing Page

After you unpublish a landing page your site visitors can no longer access the public URL or URL alias. To change your landing page back to draft status, hide it from other content, such as forms, and remove it from related flows, unpublish your landing page.

To redirect visitors to a specific URL, follow the steps in Redirect a Landing Page. If you don’t deactivate the alias and set up the redirect before you unpublish, visitors get directed to a generic “URL no longer exists” page.

Unpublish the landing page in one of these ways.

  * From the workspace content list, open the landing page, and then click **Unpublish** on the landing page record.
  * From the workspace content list, click a row action menu, and then select **Edit** | **Unpublish**.



When you unpublish a landing page, it reverts to a draft state and can be republished later. To prevent a 404 error for visitors, set up a redirect URL on the landing page record to send site visitors to a different URL.

#### See Also

  * [Add Site Contributors to Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_contributors_site.htm&language=en_US&type=5 "To let users preview landing pages in Marketing Cloud Next as authenticated users, add contributors to the Marketing Landing Pages site. Assign the Viewer role to each contributor. Site contributors must also be site members.")
  * [Manage Trusted URLs](https://help.salesforce.com/s/articleView?id=xcloud.security_trusted_urls_manage.htm&language=en_US&type=5)


