<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_create.htm&language=en_US&type=5 -->

# Create and Manage Forms in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create and Manage Forms in Marketing Cloud Next

To capture user information, create a form and add it as a component on a landing page. Landing pages and forms are connected together with a campaign and flow. We recommend that you use a signup form campaign because it automatically creates and connects a form and flow for you. 

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create a form on a landing page: | Marketing Cloud Manager permission set ANDAny CMS workspace contributor role  
To publish a form and landing page: | Marketing Cloud Manager permission set ANDA CMS workspace contributor role of content admin or content manager  
To create and publish a form that uses data source fields: | The previous permissions ANDModify All Data permission for the data source object, for the object fields on the form, and for the record type selected for the data source object  
  
When using a dropdown component on a form, you can’t map options to picklist values in Salesforce Setup. To create a dropdown component on your form, add a data source, and manually enter the picklist options.

Each form requires at least one input component and one button. If you remove a field from the default form that's included in a campaign and want to restore it, add the Lead object as the data source and add the affected fields again.

[](https://help.salesforce.com/s?language=en_US)

## Create a Form

  1. Create a form.
     * On the Campaigns tab, create a signup campaign. Then, on the campaign record, next to Start Trigger, click **Edit**.
     * On the Content tab, open your preferred marketing workspace. Select **Add** | **Content** | **Form**.
     * From a flow, click **Edit** in the Start element. On the Form card, click the action menu and select **Edit**.
  2. Add or move components to create the layout that you want.
  3. To include fields that relate to Salesforce records, configure a data source.
     1. On the Fields tab, click **Add Data Source**.
     2. Give your data source a name without spaces.
     3. Select the Salesforce Record data type, and then select an object and a record type.
     4. Save the data source.
     5. Expand the available fields, and drag the object fields onto the canvas.
  4. To include fields that store data in a [unified profile](https://help.salesforce.com/s/articleView?id=data.c360_a_profile_explorer.htm&language=en_US&type=5) instead of a Salesforce object field, use one of these input components: Checkbox, Dropdown, Email, Phone Number, or Plain Text.
  5. To include [hidden fields or default field values](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_hidden_fields.htm&language=en_US&type=5 "Enhance data collection without compromising user experience with short forms that are easy to complete. Use hidden fields to gather contextual data behind the scenes, or add default values in visible fields to speed up form completion. Hidden fields and default values are available on the Checkbox, Dropdown, Number, Plain Text, and Text Area input components.") on a form, use one of these input components: Checkbox, Dropdown, Number, Plain Text, or Text Area.
     * To hide a field, select **Hide this field**.
     * Set a default value in the Default Field Values section of the property panel.
     * .
  6. If needed, assign a brand to the form.

When a form appears on a marketing site, it inherits the branding of its landing page if the landing page’s assigned brand is different. Branding that you assign to a form is preserved when the form appears on an external site.

  7. To customize the form’s colors, layout, and other style properties, select the Style tab.
  8. In the Form Submission section of the configuration panel, select what happens when a visitor submits the form.
  9. Save the form.
  10. Make sure that the form is related to a flow.
     * If you created the form via a signup campaign, the form is already related to a flow.
     * To generate a form-triggered flow that uses your form, expand the Flow section and click **Create a Flow**.
     * To add the form to an existing flow, open the Start element of a form-triggered flow, and assign the form to that flow.
  11. If needed, [relate the flow to a campaign](https://help.salesforce.com/s/articleView?id=mktg.mktg_campaigns_working.htm&language=en_US&type=5 "You can create a campaign flow from any campaign Quick Start or from a blank template, and then add flow elements that listen for activities and trigger actions.").
  12. Save the form again.
  13. When you’re ready to publish the form and its flow, click **Publish**.



[](https://help.salesforce.com/s?language=en_US)

## Add reCAPTCHA to Forms

To protect your forms from suspicious activity, ask a Salesforce admin or marketing admin to add the reCAPTCHA integration to your marketing sites. The Google reCAPTCHA v2 integration is available only for marketing landing pages with forms. When the integration is enabled, reCAPTCHA is automatically displayed on every form you create.

See [Protect Forms with reCAPTCHA](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_recaptcha.htm&language=en_US&type=5 "Protect your marketing landing pages with forms from bots, fraudulent activities, spam, and abuse with Google reCAPTCHA. The Google reCAPTCHA v2 integration evaluates visitors' reputations and shows a reCAPTCHA to suspicious actors. It's available only for marketing landing pages with forms, and it doesn’t apply to LWR sites or other sites built from templates.").

[](https://help.salesforce.com/s?language=en_US)

## Unpublish a Form

Remove customer access to a form by unpublishing it. When you unpublish a form, its flow is also deactivated, and the Submit button no longer works. In the unlikely event that you unpublish a form at the same time as someone clicks Submit, that submission is completed and their form data is saved.

  1. From your marketing workspace, open the form that you want to unpublish.
  2. On the form’s content detail page, click  and select **Unpublish**.
  3. Review the Usage Info tab, and disconnect the form from its related landing page.
     * To unpublish a landing page, open the landing page record, click  and select **Unpublish**.
     * To remove the form from a landing page, open the landing page, click **Edit** , and then remove the Form component from the canvas. Save your work, and then republish the landing page.
  4. Refresh the form page, and click **Unpublish** again.
  5. For a form that’s related to multiple landing pages, repeat steps 3 and 4 until the form is completely disconnected.



After you unpublish a form, the form reverts to draft state and the flow is deactivated so that you can delete both assets. If you want to edit and republish the form, you must save the flow as a new version.

If a form has multiple published versions, the latest published form version is used when the form displays on a landing page. You can find older versions of a form on the form’s content detail page.

#### See Also

  * [Marketing Cloud Next Content Types and Statuses](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_status_ref.htm&language=en_US&type=5 "An item’s status indicates whether the content is ready to use in a campaign. Understand what each status means and how it relates to your marketing campaigns and flows.")
  * [Brand Your Content in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_brand.htm&language=en_US&type=5#mktg_content_brand "Apply a consistent look and feel across your marketing content. Specify your company’s colors, fonts, button styles, brand identity, and tone. Create as many brands as you need. We recommend that you assign your primary brand as the default brand in your marketing workspace. The default brand’s settings extend to all your Marketing Cloud Next content, but you can create other brands for specific events or products.")


