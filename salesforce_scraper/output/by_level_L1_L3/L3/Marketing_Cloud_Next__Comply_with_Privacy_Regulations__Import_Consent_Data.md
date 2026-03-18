<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_import_create.htm&language=en_US&type=5 -->

# Import Consent Data to Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Import Consent Data to Marketing Cloud Next

If you collect consent data outside of Marketing Cloud Next, import it as a CSV. Each import corresponds to a single marketing channel, communication subscription, and consent status.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
User Permissions Needed  
---  
To create a consent import: | Marketing Cloud Admin ORMarketing Cloud Manager permission set  
  
Before you import consent data, make sure that each person's contact points, such as email and phone number, already exist in Marketing Cloud Next. A consent import adds and updates consent information for existing contact points, but it doesn't create new leads or contacts or update other fields.

  1. From the Consent page, select **Consent Imports** , and then click **Import**.
  2. Select a channel and a communication subscription.
  3. For SMS consent imports, enter the Sender Code that you plan to use with the subscription.
  4. Select a consent status to apply to all of the items in your import, and then click **Next**.
  5. Upload your CSV, and then click **Next**.

Note For each contact point, make sure that the consent date in the CSV file is later than the existing consent date. The importer ignores all incoming consent dates that occur before the existing consent dates.

  6. On the preview step, review the sample fields from your file.
  7. To complete your import, click **Import**.



Example Lyn wants to import a list of consent data for the communication subscription Product Updates. She has data for both SMS and email. To import all of her consent data, Lyn creates four import files:

  * One for people who opted into emails
  * One for people who opted out of emails
  * One for people who opted into SMS messages
  * One for people who opted out of SMS messages



After the import completes, we send a notification email to the user who imported the file. It can still take some additional time to sync updated consent statuses to Data 360.

#### See Also

  * [Formatting Marketing Consent Import Files](https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_import_format.htm&language=en_US&type=5 "Before you import consent data into Marketing Cloud Next, make sure that your import file is saved as a CSV and that the columns and values are formatted correctly.")


