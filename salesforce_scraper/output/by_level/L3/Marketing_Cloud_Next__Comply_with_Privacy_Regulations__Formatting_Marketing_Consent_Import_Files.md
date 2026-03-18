<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_consent_import_format.htm&language=en_US&type=5 -->

# Formatting Marketing Consent Import Files

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Formatting Marketing Consent Import Files

Before you import consent data into Marketing Cloud Next, make sure that your import file is saved as a CSV and that the columns and values are formatted correctly.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition, and in **Starter**  and **Pro Suite**  Editions. Your edition determines the options that you have.  
---  
  
[](https://help.salesforce.com/s?language=en_US)

## General Guidelines

Each file you import corresponds to one communication subscription, one channel, and one consent status. For example, complete one import for people who opted into your weekly email newsletter subscription and another import for people who opted out of that subscription.

To update the consent status for existing leads and contacts, import consent data from the Consent tab.

To create new leads and contacts and include consent data, import from the Leads or Contacts tab and use the consent values `OptIn` and `OptOut`.

Review these other considerations before you import consent data.

[](https://help.salesforce.com/s?language=en_US)

  * Each import file must include a contact point value as the first column and the date of consent as the second column. A contact point value is either an email address or a phone number.
  * Consent is tied to the contact point. A contact point is associated with a Unified Individual based on the identity resolution ruleset in your org.
  * Consent imports update the status and date of consent for each contact point in the import file. To create or update leads or contacts, import from the Leads or Contacts tab.



## Formatting the Date of Consent

When you import consent data, the system maps the data in your import file to the correct DMOs and converts timestamps based on time zone. To ensure that the system maps the date that you captured consent correctly, you must format each date entry as one of these supported DateTime datatypes, including the use of capital or lowercase letters.

[](https://help.salesforce.com/s?language=en_US)

  * `yyyy-MM-dd HH:mm:ss.SSSZ`
  * `MM/dd/yyyy HH:mm:ss`
  * `MM/dd/yyyy`
  * `yyyy-MM-dd`
  * `M/dd/yyyy`



This table breaks down the format for DateTime datatypes.

Letter Code | Date or Time Component | Example  
---|---|---  
yyyy-MM-dd | Date in year-month-day format | 2023-05-01  
HH:mm:ss:SSS | Timestamp in hour-minute-second-millisecond and format based on a 24-hour clock | 14:30:00:000  
Z | Represents the UTC timezone  | Z OR _blank_ OR +0000  
  
Important

When you use an import to update a record, you can’t change the consent date to a value that occurs before the consent date for the existing record. If the consent date in the update occurs before the consent date for the existing record, the updated date is ignored.

## Email File Guidelines

When you format a CSV file to import email consent data, keep these guidelines in mind.

  * The file must include a column for email addresses and a separate column for recording the date of consent.
  * Each email must be a valid and complete email address. For example, `lyn@ursasolar.com`.
  * Email addresses can’t include special characters.



## SMS and WhatsApp File Guidelines

When formatting a CSV to import consent data for SMS or WhatsApp messages, keep these guidelines in mind.

  * The file must include a column for phone numbers and a separate column for recording the date of consent.
  * For each entry, you must include a country code and the complete phone number. Phone numbers are validated based on [ITU E.164 standards](https://www.itu.int/rec/T-REC-E.164/en). For example, an E.164-formatted United States or Canadian phone number looks like this: `+12065550123`.
  * Spaces, dashes, underscores, and parentheses are automatically removed from phone numbers.
  * Phone numbers can only include numerals.


