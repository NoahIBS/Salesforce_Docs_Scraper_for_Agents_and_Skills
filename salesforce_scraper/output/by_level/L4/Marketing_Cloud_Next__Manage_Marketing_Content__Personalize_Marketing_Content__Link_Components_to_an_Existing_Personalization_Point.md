<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ppoint_link.htm&language=en_US&type=5 -->

# Link Components to an Existing Personalization Point in Dynamic Content

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Link Components to an Existing Personalization Point in Dynamic Content

To control multiple dynamic components with the same personalization settings and rules, link multiple components or fields to one personalization point. When you add or delete variations, edit targeting rules, or reorder priorities, your changes apply to all the components or fields linked to that personalization point.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
For more information about linking, see [Linked Personalization Points in Dynamic Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ppoint_reuse.htm&language=en_US&type=5). To link, your email or landing page must contain at least one component with dynamic content.

[](https://help.salesforce.com/s?language=en_US)

## Link a Component or Field to an Existing Personalization Point

You can link a component or field to an existing personalization point only when the personalization point is in the content item you’re editing.

  1. Open an email or landing page for editing.
  2. In the builder canvas, select the component that you want to personalize, or click  next to an email subject line or preheader.

You can link to an existing personalization point only when the component doesn’t have variations.

  3. Click **New Variation**.
  4. Select a personalization point from the email that you’re editing. Recently used personalization points are listed. Or, click **View All** to see the complete list.

Personalization points that are already used in your content are marked with .

  5. Select **Link the personalization point to this component or field**.
  6. Review the decisions and targeting rules and save your changes.

The component or field inherits the personalization point’s settings, and the new variations have the default content and style. In the canvas and property panel, you can customize the content and style based on the audience that you want to reach.




To check which personalization point your component is linked to, hover over  in the component property panel. To link another component or field to the same personalization point, select the component from the canvas, and repeat these steps.

[](https://help.salesforce.com/s?language=en_US)

## Add Variations and Manage Personalization Settings for Linked Components

When multiple components or fields are linked to a personalization point, any changes you make apply to all the linked components or fields. When you add a variation to one component, the variation is added to the linked components. Likewise, when you delete a variation, it’s removed from all the linked components. And any changes you make to the personalization priorities or targeting rules apply to all linked components.

  1. In the canvas, select the linked component that you want to edit.
  2. Add a variation.
     1. In the component property panel, from the Variation dropdown, click **New Variation**.
     2. Review the linked components and fields and click **Next**.
     3. Set the new targeting rule and click **Next**.
     4. Confirm the details.
     5. Customize the content and style of the variation for this component and for the linked components or fields.
  3. Change the priority order.
     1. In the component property panel, from the Variation dropdown, click **Edit Priorities**.
     2. Review the linked components and fields and click **Next**.
     3. Edit the priorities. Optionally, use the row-level actions to make other changes to a variation.
     4. Save your changes.
  4. Edit a targeting rule.
     1. In the component property panel, select the variation in the Variation dropdown.
     2. Open the Rules panel, and click **Edit**.
     3. Review the linked components and fields and click **Next**.
     4. Edit the targeting rule and click **Next**.
     5. Confirm your changes.
  5. Rename or delete a variation.
     1. In the component property panel, select the variation in the Variation dropdown.
     2. To change the variation name, click **[](https://help.salesforce.com/s?language=en_US)**and select**Rename**.
     3. To delete the variation, click **[](https://help.salesforce.com/s?language=en_US)**and select**Delete**.



[](https://help.salesforce.com/s?language=en_US)

## Unlink a Component or Field from a Personalization Point

To edit the personalization settings of a linked component or field without affecting the other components in the relationship, you must unlink the component.

  1. In the builder canvas, select the component that you want to unlink.
  2. From the Variation dropdown, click **Unlink**.
  3. Review the details and click **Next**.
  4. Edit the names of the personalization point and the variations and decisions, and save your changes.

This component is now associated with a copy of the personalization point, and the other components or fields remain linked to the original personalization point.




Customize the component’s variations and personalization settings as needed. If the original personalization point has only one component remaining, the linked badge no longer appears in the component’s property panel because it’s not linked to other components.

#### See Also

  * [How Dynamic Content and Salesforce Personalization Work Together](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ep.htm&language=en_US&type=5 "Dynamic content in Marketing Cloud Next improves conversations and relationships with customers, and it can lead to more effective campaigns. Personalization points, decisions, and targeting rules from Salesforce Personalization power dynamic content. Dynamic components and fields are associated with personalization points, and variations are associated with decisions and targeting rules.")
  * [Create and Manage Variations in Marketing Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_create_variations.htm&language=en_US&type=5 "Personalize emails or landing pages with dynamic content. Create a single variation and configure a targeting rule to determine when that variation appears. Or create variations that use existing personalization settings and targeting rules by cloning a personalization point. Prioritize the most relevant content if someone qualifies for more than one variation.")


