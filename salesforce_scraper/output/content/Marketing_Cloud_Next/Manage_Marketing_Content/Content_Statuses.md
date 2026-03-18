<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_status_ref.htm&language=en_US&type=5 -->

# Marketing Cloud Next Content Types and Statuses

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Marketing Cloud Next Content Types and Statuses

An item’s status indicates whether the content is ready to use in a campaign. Understand what each status means and how it relates to your marketing campaigns and flows.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
To find the status of a content item, check the Status column in your marketing workspace or the Details card on the content detail page.

## Draft

Draft indicates that the content either hasn’t been published or has been unpublished. When content is in draft status, you can edit it and relate it to campaigns, flows, or other content items. You can also preview or test the content. Draft content is visible only to contributors in the marketing workspace. Customers can’t see or access content in draft status.

When a brand is in draft status, it’s available to assign as the default brand in your marketing workspace. When you publish content that a draft brand is applied to, the brand is also published.

## Published

Published indicates that the content is available in your channels and ready to use in a campaign. When content is published, you can continue to associate it with campaigns, flows, or content. You can also preview or test the content. When you edit published content, a new content version is created, and the status changes to revised.

When you publish content that contains unpublished content items, such as an email containing an image, make sure you publish the referenced content and parent content at the same time. The referenced content doesn’t appear in the parent content item until it’s also published.

Publishing doesn’t immediately make the content available to external customers. Here’s what the published status means for each content type.

Content Type | What Published Means  
---|---  
Email | The email is ready to send in a messaging campaign flow.Your customers can’t see the email until the campaign or flow is activated.  
SMS Message | The SMS message is ready to send in a messaging campaign flow.Your customers can’t see the SMS message until the flow is activated.  
Landing Page | The landing page is ready to be made publicly available as part of a campaign flow.When you publish a landing page that contains a form, the form is published, and the flow associated with the form is activated.Publishing the landing page activates any URL aliases that aren’t already active.  
Form | The form is ready for user input, and the associated campaign flow is activated.Your customers can’t see the form until it’s added to a landing page, which must be published and have an active URL alias. See [Create and Publish a Form](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_create.htm&language=en_US&type=5 "To capture user information, create a form and add it as a component on a landing page. Landing pages and forms are connected together with a campaign and flow. We recommend that you use a signup form campaign because it automatically creates and connects a form and flow for you.").  
Image | The image is ready to associate with individual content items. If an unpublished image is attached to another content item and you publish that content item, you can publish the image at the same time.  
Brand | The brand is ready to associate with a content item or to assign as a workspace default brand. If an unpublished brand is attached to an email or landing page and you publish the content item, you can publish the brand at the same time. See [Brand Your Content in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_brand.htm&language=en_US&type=5#mktg_content_brand "Apply a consistent look and feel across your marketing content. Specify your company’s colors, fonts, button styles, brand identity, and tone. Create as many brands as you need. We recommend that you assign your primary brand as the default brand in your marketing workspace. The default brand’s settings extend to all your Marketing Cloud Next content, but you can create other brands for specific events or products.").  
Audio, Video, and Document | The rich media content is ready to associate with a WhatsApp message. If you have unpublished rich media content attached to a WhatsApp message when you publish it, the rich media content is also published.  
Expressions | The expression, which is composed of saved filter and sort criteria for selecting a data attribute, is available to use when adding merge fields to your content, such as Email, SMS, or WhatsApp messages.  
  
## Revised

Revised indicates published content versions that have unpublished edits. When you edit published content, the status on the content item updates to revised. The original published content remains available in your campaigns and related content items. Similar to draft content, revised content is visible only to contributors in the marketing workspace.

Example Your email campaign includes a published email. When you edit the email content, the original email in your campaign doesn’t change. Later, when you publish the revised email version, you see the status update to Published, and then the email is updated in your campaign.

## Scheduled Publish or Unpublish

After you schedule content to publish or unpublish, the content remains in the current status until the date and time that you scheduled. You can monitor the schedule in the Publication Activity tab on a content detail page.

## Processing

When a landing page, form, or branding content type is in the process of publishing or unpublishing, the content status is Processing. You can’t make changes while content is processing.

#### See Also

  * [View CMS Content Details in Enhanced CMS Workspaces](https://help.salesforce.com/s/articleView?id=xcloud.cms_content_details.htm&language=en_US&type=5)
  * [Create Publication Schedules in Salesforce CMS](https://help.salesforce.com/s/articleView?id=xcloud.cms_schedule_create.htm&language=en_US&type=5)


