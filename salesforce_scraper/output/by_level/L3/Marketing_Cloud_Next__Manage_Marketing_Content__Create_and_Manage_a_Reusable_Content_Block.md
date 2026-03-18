<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_reusable_content_blocks.htm&language=en_US&type=5 -->

# Create and Manage a Reusable Content Block

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage a Reusable Content Block

Content admins and content managers can combine text, images, links, and buttons into reusable content blocks. The blocks are stored in a marketing workspace, where they’re easily available to content authors, who can add them to any email or landing page. Create different content blocks for different audiences, and use variation rules to personalize which block is delivered to which audience.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create, edit, publish, or unpublish a content block: | Marketing Cloud Manager permission setANDa CMS workspace contributor role of content admin or content manager  
To use a content block in an email or landing page: | Marketing Cloud Manager permission setANDany CMS workspace contributor role   
  
When you use content blocks, keep these considerations in mind.

  * A content author can add any content block to an email or landing page, even if the content block is in Draft status. If a content admin or manager publishes the parent content, the draft content block is also published.
  * A content block's latest saved version appears on the canvas and in preview, regardless of whether it's published. The latest saved version also appears on the content block’s detail page in Salesforce CMS.
  * A content block inherits the brand values of the email or landing page where it’s included. However, a block creator can customize individual style values in a content block. Those choices persist wherever the block is used, regardless of the content’s assigned brand.
  * You can’t use dynamic content when creating or editing a reusable content block. To personalize which audience gets a particular content block, create different versions of the content block. Then, in an email, create a variation of the Content Block component and use targeting rules to personalize who gets which content block.
  * You can't create variations of the Content Block component on a landing page.



[](https://help.salesforce.com/s?language=en_US)

## Create a Content Block

  1. From your marketing workspace, create a content block. 
     * For an email, click **Add** | **Content Block: Email**.
     * For a landing page, click **Add** | **Content Block: Landing Page**.
  2. Add the components for the content block to the canvas and configure them.

  3. Save and publish the content block.



[](https://help.salesforce.com/s?language=en_US)

## Use a Content Block in an Email or Landing Page

  1. In an email or on a landing page, add the Content Block component to the canvas and click **Select Block**.
  2. Select a content block and click **Add**.

  3. Optional: In an email only, you can [create a variation](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_create_variations.htm&language=en_US&type=5 "Personalize emails or landing pages with dynamic content. Create a single variation and configure a targeting rule to determine when that variation appears. Or create variations that use existing personalization settings and targeting rules by cloning a personalization point. Prioritize the most relevant content if someone qualifies for more than one variation.") of the Content Block component for a different audience.
     1. In the property panel for the Content Block, click **New Variation**.
     2. Name the variation and set its rules.
     3. Replace the default content block with the version of the block that you want to use.
  4. Save your work.
  5. Preview and test your content.
     * [Preview and test an email.](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_email_create.htm&language=en_US&type=5#preview-test "To make sure that your customers get the best experience from your content, preview and test your email. Before you can preview and test, publish at least one segment. You can preview and test an email in any status. Test sends count toward message credits.")
     * [Preview and test a landing page.](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_lp_create.htm&language=en_US&type=5#preview_lp "To see your landing page the same way it appears to the public, preview it from the content detail page or the editor. You must be a site contributor to the Marketing Landing Pages site to preview landing pages. When you preview your landing page, also review any attached forms.")
  6. Publish the content.



[](https://help.salesforce.com/s?language=en_US)

## Convert a Content Block to a Section

To customize a content block in an email or landing page, convert it to a section. Then, edit the contents of the section. The original content block is unchanged.

  1. In the canvas of an email or landing page, select a content block.
  2. Click  in the toolbar.

If the content block contains multiple sections, the block is converted to multiple sections in your email or landing page.

  3. Save your changes.



#### See Also

  * [How Dynamic Content and Salesforce Personalization Work Together](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ep.htm&language=en_US&type=5 "Dynamic content in Marketing Cloud Next improves conversations and relationships with customers, and it can lead to more effective campaigns. Personalization points, decisions, and targeting rules from Salesforce Personalization power dynamic content. Dynamic components and fields are associated with personalization points, and variations are associated with decisions and targeting rules.")
  * [Manage Data Sources for Personalizing Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.")


