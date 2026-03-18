<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_data_sources.htm&language=en_US&type=5 -->

# Data Sources for Forms in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Data Sources for Forms in Marketing Cloud Next

A data source represents a Salesforce object, which you can use with a form. It creates a bridge between a form field and a CRM object field so that you can save the captured form data in Salesforce records.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
## Creating a Data Source

The Account, Contact, Lead, and Prospect objects are available to use as a data source. When you name your data source, enter up to 20 characters. You can use alphanumeric characters and underscores, but no spaces or consecutive underscores.

You can use only one data source object at a time. Changing the selected object can create discrepancies in data, so consider the impacts before changing the data source object.

Example Kyle is editing a form that uses Contact as the data source object. He wants to add the Industry field, so he removes the Contact object and uses the Lead object instead. But when he tries to save the form, he gets an error. Because a form can’t contain fields from multiple objects, he needs to decide which fields to keep.

For now, he removes the Industry field, but he makes a note to talk to his admin about a custom Contact field that can serve the same purpose.

## API Names and Fields

Not all field types are available to use with data source objects. If you update a custom field to use an unsupported field type, the form can no longer save captured data. Avoid changing field types, and remove unsupported fields from the form. You can include a data source field on your form only one time—don't add duplicates.

You can use these field types.

  * Checkbox
  * Date
  * Date/Time
  * Time
  * Email
  * Phone Number
  * Number
  * Picklist
  * Text
  * Text Area
  * Text Area (Long)
  * URL



The Number of Employees standard field in the Account, Lead, and Prospect objects isn't supported and doesn't appear in the Data Source Field List.

A field's API name is the unique ID used to map data source fields. If you edit a CRM field’s API name after using it in a form, any new data that’s submitted to that field isn’t saved.

When you start with a signup form campaign, the form and landing page are predefined with default API names that you can’t change. If it's necessary to control the API names, it's possible to create a form from your content workspace instead. If you choose this option, you must also manually connect the form to a flow and map related fields.

#### See Also

  * [Create and Manage Forms in Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_create.htm&language=en_US&type=5 "To capture user information, create a form and add it as a component on a landing page. Landing pages and forms are connected together with a campaign and flow. We recommend that you use a signup form campaign because it automatically creates and connects a form and flow for you.")
  * [Using a Form with Landing Pages](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_considerations.htm&language=en_US&type=5 "Landing pages can support campaign goals, such as customer awareness or lead generation. In Marketing Cloud Next, you can create a landing page with or without a form, depending on your needs. Each landing page can contain one form only.")


