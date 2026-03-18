<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_considerations.htm&language=en_US&type=5 -->

# Using a Form with Landing Pages

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Using a Form with Landing Pages

Landing pages can support campaign goals, such as customer awareness or lead generation. In Marketing Cloud Next, you can create a landing page with or without a form, depending on your needs. Each landing page can contain one form only.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
A form has two parts: the form fields and their settings, and the flow that processes the captured data. To process the form-submitted data, you must add the form record to a flow. You can relate a form to only one flow. When you create a sign-up form campaign, the landing page, form, and flow are created and related for you. However, if you create the components individually, you must manually relate the parts.

## Form Requirements

A form must include at least one input element and one button. To capture form submission data, set up these fields with the following Unique Name values.

[](https://help.salesforce.com/s?language=en_US)

  * An email address field must have the unique name `Email`.
  * A first name field must have the unique name `FirstName`.
  * A last name field must have the unique name `LastName`.



Unique names aren’t case-sensitive, but they can’t include extra characters or spaces.

Example

  * Accepted: EMAIL, Email, FirstName, Firstname
  * Not Accepted: email1, 1stname, FirstNameA, first name



## Other Considerations

  * If you have a dropdown field as the last field on a form, the dropdown list can get cut off, especially if the form is embedded in an external site. As a workaround, move the dropdown field further up on your form. If the dropdown must be the last field, add padding to the bottom of the form to make enough room for the dropdown list to appear properly.
  * If a form has more than one version and you add the form to a landing page, the latest published version of the form is shown.
  * If you add, remove, or change fields on your form, make sure that the updated fields are mapped correctly.
  * To add an image that’s hosted outside of Marketing Cloud Next, you must allowlist the domain that hosts the image and select the Content Security Policy (CSP) directives in Trusted URLs in Salesforce Setup. See [Manage Trusted URLs](https://help.salesforce.com/s/articleView?id=xcloud.security_trusted_urls_manage.htm&language=en_US&type=5).
  * When a form uses data source fields, the fields inherit the language of the person building the form, not the language associated with the CMS workspace.
  * If your org is configured to manage duplicates, the CreateRecords element in a form’s flow can’t create a record if it matches an existing one. See [Duplicate Rules](https://help.salesforce.com/s/articleView?id=sales.duplicate_rules_map_of_reference.htm&language=en_US&type=5).



#### See Also

  * [Create and Manage Forms in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_create.htm&language=en_US&type=5 "To capture user information, create a form and add it as a component on a landing page. Landing pages and forms are connected together with a campaign and flow. We recommend that you use a signup form campaign because it automatically creates and connects a form and flow for you.")


