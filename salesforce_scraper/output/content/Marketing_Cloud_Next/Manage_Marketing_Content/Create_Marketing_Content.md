<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_create.htm&language=en_US&type=5 -->

# Create Content in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create Content in Marketing Cloud Next

The content editing experience in Marketing Cloud Next uses a single design framework so that building marketing content is familiar no matter what you’re creating. The layout and functionality are the same, but after you choose the content type, a curated selection of components appears for you to choose from.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
The basic experience for all content types is the same.

When you create a campaign from a template, draft content is created in the default marketing workspace. To store your content in another workspace, create it directly from the Content tab.

  1. Create or open content for editing.
     * From the Campaigns tab, open a campaign or create one. Then, on the campaign record, next to the content that you want to work with, click **Edit**.
     * From the Content tab, open your preferred marketing workspace. Select **Add** | **Content** , and then select a content type.
     * From a flow, open a content element, and edit the related content.
  2. Select a brand to apply, or keep the default brand.

If your marketing workspace admin or manager assigned a default brand to the workspace, that brand is already applied to your email, landing page, or form.

  3. Add or update the components on the canvas.
     * To add a component, drag it to the canvas where you want it to appear.
     * To update a component, select it on the canvas, and edit the content on the canvas or in the property panel. Use the undo and redo buttons as you edit, and the style tab to customize colors, layout, and other style properties.
     * To remove a component, select it on the canvas and click  in the toolbar.
  4. Add or adjust sections and structure with layout components, saving your work as you go.
  5. To use an extension, click , and then select one from the dropdown menu.

Developers can build extensions and add them to the content builder. To learn more, see [Extensions in CMS](https://developer.salesforce.com/docs/platform/cms/guide/cms-developer-guide.html).

  6. To review your work after you save, click **Preview** in the main toolbar.
  7. To make your content available for use in campaigns, publish it.



To make a copy of a saved content record, clone it from the content detail page.

Note When you clone a marketing email that includes personalization, some elements aren't copied to the new email. 

  * Dynamic content: Default variations of components are copied. Other variations and the personalization point, decisions, and rules don't copy. 
  * Recommender data source: The recommender isn't copied, but the merge fields and repeaters that use the recommender are. These items are broken, and must be removed or replaced with new ones, or you can add the same recommender to the new email.



Usually, publishing your content only makes it available for use with a campaign. Unpublishing or deleting content has implications for campaigns and flows. Review details for each content type to confirm publishing, unpublishing, and delete behavior.

  * **[Keyboard Shortcuts for Editing Content in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_keyboard_shortcuts.htm&language=en_US&type=5)**  
Use these keyboard shortcuts to navigate the user interface as you build content.



#### See Also

  * [Types of Content in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_types_ref.htm&language=en_US&type=5 "Create and manage all your marketing content from your CMS workspace. You can create content such as emails, landing pages, forms, images, and SMS messages for use in marketing campaigns.")
  * [Marketing Cloud Next Content Types and Statuses](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_status_ref.htm&language=en_US&type=5 "An item’s status indicates whether the content is ready to use in a campaign. Understand what each status means and how it relates to your marketing campaigns and flows.")
  * [Brand Your Content in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_brand.htm&language=en_US&type=5#mktg_content_brand "Apply a consistent look and feel across your marketing content. Specify your company’s colors, fonts, button styles, brand identity, and tone. Create as many brands as you need. We recommend that you assign your primary brand as the default brand in your marketing workspace. The default brand’s settings extend to all your Marketing Cloud Next content, but you can create other brands for specific events or products.")
  * [Work with Extensions in Salesforce CMS](https://help.salesforce.com/s/articleView?id=xcloud.cms_content_editor_sidebar_extensions.htm&language=en_US&type=5)


