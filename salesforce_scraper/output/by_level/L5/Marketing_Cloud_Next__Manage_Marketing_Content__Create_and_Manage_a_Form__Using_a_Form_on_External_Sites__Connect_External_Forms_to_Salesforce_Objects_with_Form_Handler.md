<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_connect_external_forms_to_salesforce_objects_with_form_handler.htm&language=en_US&type=5 -->

# Connect External Forms to Salesforce Objects with Form Handler

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Connect External Forms to Salesforce Objects with Form Handler

Use a form handler to capture data from a form on an external website and use that data to create or update records in Salesforce. Form handlers make it possible to use the existing forms on your site without updating your site to use forms created in Salesforce. When you create a form handler, you specify the field names in your existing form and the Salesforce fields that they map to.

### Required Editions

Available in: **Enterprise** and **Unlimited** Editions with Marketing Cloud **Growth** or **Advanced** Edition, and **Pro Suite** Editions. They also apply to these editions when Salesforce Foundations is enabled. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create a form handler: | Marketing Cloud Manager permission setANDAny CMS workspace contributor role  
To publish a form handler: | Marketing Cloud Manager permission setANDA CMS workspace contributor role of content admin or content manager  
  
When you create a form handler, you also create a data source in Data 360. This data source stores the data that you capture in your form. Before you create a form handler and a corresponding data source, think about how best to structure the data that you capture from the form. There are two general patterns for designing the data structure: explicit field names and generic field names.

In a data source that uses explicit field names, you specify each field name in the data model. This structure is easy to understand, but it requires you to modify the object every time you add a new field. A data model with an explicit structure resembles this example.

Field Name | Type  
---|---  
First Name | Text  
Last Name | Text  
Email | Text  
Address | Text  
Occupation | Text  
... | ...  
  
Alternatively, a data source can use generic field names, or more often a combination of explicit and generic field names. This approach gives you more flexibility, because you can handle new field names without modifying the object. However, generic field names are ambiguous and require you to use metadata to describe the attributes in the payload. A data model with a generic structure resembles this example.

Field Name | Type  
---|---  
First Name | Text  
Last Name | Text  
Email | Text  
Attribute1 | Text  
Attribute2 | Text  
Attribute3 | Text  
... | ...  
  
#### See Also

  * [ _Salesforce Developers_ : Integrate Form Submissions with the Connect API](https://developer.salesforce.com/docs/marketing/marketing-cloud-growth/guide/mc-manage-content-form-handlers.html)



[](https://help.salesforce.com/s?language=en_US)

## Create a Form Handler

  1. On the Content tab, select a content workspace to create the form handler in.
  2. Click **Add** | **Content**.
  3. On the Create CMS Content window, select Form Handler, and then click **Create**.
  4. In the top-left corner of the window, next to Untitled, click the pencil icon (). Enter a name for the form handler.
  5. Add a Data Source.
     1. In the panel on the right, under Data Source, click **Add Data Source**.
     2. Enter a name for the data source.
     3. For Type, select **Salesforce Record**.
     4. For Object, select the type of record the form handler operates on. For example, if you plan to use the form handler to update Contact records, select **Contact**.
     5. Save your changes.
  6. Map the form fields.
     1. From the panel on the left, click a field that you want to capture from the form and drag it to the center of the page. For example, select the Contact object if your form collects information about the user’s First Name, Last Name, or Email address. Repeat this step for every field that the form data interacts with.
     2. In the center of the page, click one of the field names that you added. Then, in the panel on the right, enter an External Field Name. Repeat this step for all of the selected fields.

Note

Keep these requirements in mind when you specify the fields to capture:

     * The external field name that you enter must exactly match the HTML name attribute of the field in your form.
     * Date values must use the format `YYYY-MM-DD`.
     * Time values must use the format `hh:mm:ss`.
     * DateTime values must use the format `YYYY-MM-DDTHH:mm:ss.sssZ` (ISO 8601 format).
     * For checkbox values, if the checkbox is selected on the form, it’s recorded as `true` in the Salesforce object.

  7. Save your changes.



For information about updating your site to handle form submissions securely, see _Developer Documentation_ : [Integrate Form Submissions with the Connect API](https://developer.salesforce.com/docs/marketing/marketing-cloud-growth/guide/mc-manage-content-form-handlers.html).

[](https://help.salesforce.com/s?language=en_US)

## Add Spam Protection to a Form Handler (Optional)

Protect against hacking and spam by adding a hidden honeypot field to your form. When a bot tries to submit a form, it often completes every field in the form, even if the field is hidden. If you include a honeypot field in your form, the form handler blocks all submissions that include a value in that field.

Note Honeypot fields are one component of an effective spam-prevention strategy, but they shouldn’t be the only component you use. Consider using other anti-abuse measures, including [_reCAPTCHA_](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_recaptcha.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

  1. From the Spam Protection Fields panel, add the **Honeypot** field.
  2. For External Field Name, enter a field name to use for the honeypot.

Tip Bots try to exploit form fields that let users freely enter text. They search for fields with generic labels, such as `company`, `website`, or `fax`. Enter a name that makes the honeypot field an appealing target, but also one that doesn’t overlap with the data you want to capture in the form. Don’t use an obvious name such as `honeypot` or `do_not_fill`.

  3. In your form’s HTML, add a hidden input field with the matching name attribute.



[](https://help.salesforce.com/s?language=en_US)

## Automate Actions with a Flow

Connect a Salesforce Flow to automate tasks like creating leads or sending emails after a form is submitted. In the Flow section of the form handler, click **New Flow** to open Flow Builder.

[](https://help.salesforce.com/s?language=en_US)Important

Add and map all required fields before creating the flow. If you edit the fields after you add the flow, the changes aren’t automatically reflected. Create a new version of the flow to include the updated mappings.

When you create a flow from the form handler page, the external field names that you specified are available as resources in the flow. You can use the values of these external fields in flow decision steps, to personalize message content, and in other flow actions. You can also use these resources to modify any object, not just the object you selected when you created the form handler. 

[](https://help.salesforce.com/s?language=en_US)

## Configure Submission Redirects

In the Submission Redirect section, enter the full URLs to send users to when a form submission succeeds or fails.

[](https://help.salesforce.com/s?language=en_US)

## Configure CORS Allowlist

Authorize your website’s domain by adding it to the [_CORS Allowlist_](https://help.salesforce.com/s/articleView?id=xcloud.extend_code_cors.htm&language=en_US&type=5). This step is required to permit form submissions.

[](https://help.salesforce.com/s?language=en_US)

## Publish the Form Handler

Publish the form handler to generate the code to add to your website.

[](https://help.salesforce.com/s?language=en_US)Note

If your form uses [_reCAPTCHA_](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_form_lp_recaptcha.htm&language=en_US&type=5), generate and send the required token with the form submission.

[](https://help.salesforce.com/s?language=en_US)

  1. When you’re ready to publish the form and its flow, click **Publish**.
  2. Under Tracking Script, click **Copy**.
  3. In your webpage’s HTML, insert the copied script before the closing `</body>` tag.
  4. Under Form Attributes, click **Copy**.
  5. Add the attributes to your website’s `<form>` tag.
  6. Turn on [_web tracking_](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_tracking_external.htm&language=en_US&type=5) to monitor user engagement.


