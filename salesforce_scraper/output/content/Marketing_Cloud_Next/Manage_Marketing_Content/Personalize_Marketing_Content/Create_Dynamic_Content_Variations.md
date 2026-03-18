<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_create_variations.htm&language=en_US&type=5 -->

# Create and Manage Variations in Marketing Content

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage Variations in Marketing Content

Personalize emails or landing pages with dynamic content. Create a single variation and configure a targeting rule to determine when that variation appears. Or create variations that use existing personalization settings and targeting rules by cloning a personalization point. Prioritize the most relevant content if someone qualifies for more than one variation.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set ANDany CMS workspace contributor role  
To publish or unpublish content: | Marketing Cloud Manager permission set ANDa CMS workspace contributor role of content admin or content manager  
  
Before creating a variation, make sure that you’ve completed the necessary [setup steps](https://help.salesforce.com/s/articleView?id=mktg.mktg_data_graph_setup.htm&language=en_US&type=5), and review and manage the [data graph](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_data_sources.htm&language=en_US&type=5 "To embed personalized data in your marketing content, add a data source. A data source represents an object or element from your org that contains fields and data. After you select a data source, its fields and attributes can be used in cross object merge fields, expressions, repeater components, and dynamic content.") in the Data Sources panel. The data graph determines which attributes you can use in targeting rules, and it determines which personalization points you can clone.

If you’re working with components or fields that are linked to one personalization point, or to link a component to an existing personalization point, see [Create and Manage Linked Components and Personalization Points](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ppoint_link.htm&language=en_US&type=5 "To control multiple dynamic components with the same personalization settings and rules, link multiple components or fields to one personalization point. When you add or delete variations, edit targeting rules, or reorder priorities, your changes apply to all the components or fields linked to that personalization point.") and [Linked Personalization Points in Dynamic Content](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ppoint_reuse.htm&language=en_US&type=5 "To control variations in an email or landing page with the same personalization settings, link multiple components to a personalization point. Any changes that you make to the personalization settings apply to all the linked components. You can also personalize more components in an email without going over the limit of 25 personalization points per content item.").

[](https://help.salesforce.com/s?language=en_US)

## Create a Variation

  1. Open an email or landing page for editing.
  2. Select the component that you want to personalize, or click  next to an email’s subject line or preheader.
     * If you’re creating the first variation of the component, click **New Variation** in the component property panel, and click **New Variation** again.
     * If the component already has variations, from the Variation dropdown, select **New Variation**.
  3. Enter a name for the variation and decision.
  4. Set when the variation appears.
     * To show the variation to a recipient if they meet all conditions, select **All Conditions Are Met**.
     * To show the variation to a recipient if they meet any one of the conditions, select **Any Conditions Are Met**.
  5. Click **Add Condition**.
  6. Select the resource that you want the condition to use. The available resources are based on the data graph.
  7. Configure the operator, values, or dates.
  8. (Optional) Add a group of conditions to create a more flexible or restrictive rule.
  9. As needed, continue adding conditions or groups to the targeting rule.
  10. Save your changes.
  11. In the canvas and property panel, customize the variation’s content and style based on the audience that you want to reach. You can also use Copilot to generate new content.



To switch to another variation, use the Variation dropdown menu. You can create up to 15 variations for an individual component.

[](https://help.salesforce.com/s?language=en_US)

## Create a Variation by Cloning a Personalization Point

Clone an existing personalization point to use in any content from the same campaign. You can also clone a personalization point that was created in Salesforce Personalization.

  1. In the builder canvas, select the component that you want to personalize, or click  next to an email subject line or preheader.

You can clone a personalization point only when the component doesn’t have variations.

  2. Click **New Variation**.
  3. Select a recently used personalization point, or click **View All** to see the complete list. Only personalization points based on the same data graph as the email are shown.

To create multiple variations of a component at once, select a personalization point with multiple variations.

  4. If the personalization point is already used in this email, select **Clone the personalization point**.
  5. Edit the personalization point and variation names and save your changes.
  6. In the canvas and property panel, customize each variations’ content and style based on the audience that you want to reach. You can also use Agentforce to generate new content.



To switch to another variation, use the Variation dropdown menu. You can create up to 15 variations for an individual component.

[](https://help.salesforce.com/s?language=en_US)

## Prioritize Variations

If an email recipient or landing page visitor qualifies for more than one variation of a content element, prioritize which variation to show.

  1. From the Variations dropdown, select **Edit Priorities**.
  2. Use the arrow buttons to increase or decrease a variation’s priority.

You can’t change the priority of the default variation. The default variation is shown if an individual doesn’t qualify for any personalized variation.

  3. (Optional) To rename the personalization point so you can find it later, click , or use the row-level actions to make other changes to variations.
  4. Save your changes.



[](https://help.salesforce.com/s?language=en_US)

## Edit a Variation’s Personalization Settings

  1. Select the variation in the Variation dropdown.
  2. Edit the variation’s targeting rule.
     1. Open the Rules panel and click **Edit**.
     2. Edit, add, or delete conditions or groups of conditions and save your changes.
  3. Rename or delete a variation.
     1. To change the variation name, click ****and select**Rename**.
     2. To delete the variation, click ****and select**Delete**.



#### See Also

  * [How Dynamic Content and Salesforce Personalization Work Together](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_personalization_ep.htm&language=en_US&type=5 "Dynamic content in Marketing Cloud Next improves conversations and relationships with customers, and it can lead to more effective campaigns. Personalization points, decisions, and targeting rules from Salesforce Personalization power dynamic content. Dynamic components and fields are associated with personalization points, and variations are associated with decisions and targeting rules.")
  * [ _Video_ : Marketing Cloud Growth Edition: Rule Based Dynamic Content (English Only)](https://salesforce.vidyard.com/watch/z4ryspCX8xk42iGXN6LGXH?)


