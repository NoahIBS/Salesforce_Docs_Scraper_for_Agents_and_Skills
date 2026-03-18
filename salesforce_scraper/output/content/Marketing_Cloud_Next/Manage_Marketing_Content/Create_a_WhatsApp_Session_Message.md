<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5 -->

# Create a WhatsApp Session Message

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create a WhatsApp Session Message 

After a customer initiates a conversation, you sometimes need to respond with a custom message. A session message is an on-the-fly reply that you can send within 24 hours of the customer's message, without having to select a preapproved templated message. 

### Required Editions

Available in: Salesforce Enterprise and Unlimited Editions with Marketing Cloud Next Growth and Advanced Editions   
---  
User Permissions Needed  
---  
To create or edit content:  | Marketing Cloud Manager permission set AND Any CMS workspace contributor role   
To publish content:  | Marketing Cloud Manager permission set AND A CMS workspace contributor role of Content Admin or Content Manager   
  
In this topic: 

  * [General Messages ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#general_message "General messages include various types of content to engage your audience.")
  * [Quick Reply Message](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#quickreply_message "A quick reply message includes buttons that allow recipients to respond immediately with a single tap. It is ideal for encouraging engagement through structured, predefined options.")
  * [List Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#list_message "A list message displays a menu of up to 10 options, making it great for presenting users with a selection of choices \(like a FAQ or product menu\) without decluttering the chat history.")
  * [Location Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#location_message "A location message allows you to send specific coordinates to a user, helping them find a physical storefront, event, or service point.")
  * [Flow Message](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#flow_message "A flow message guides customers through a structured interaction using a flow template created in the WhatsApp Business management console. This is ideal for complex interactions like booking appointments or collecting survey data.")
  * [Sticker Message](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#sticker_message "Sticker messages help strengthen your brand or add a visual element to the conversation using static or animated stickers.")
  * [Contact Message](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_session_message_types.htm&language=en_US&type=5#contact_message "Contact messages make it easy for customers to save your information or reach out to a specific agent by sharing contact details directly in the chat.")



  1. From your CMS workspace, click **Add** , and then select **Content**. 
  2. In the Create CMS content window, select **WhatsApp Session Message** , and then click **Create**.
  3. Specify a name and description for internal use. 
  4. Select the Message Type.



Note: Location, flow, sticker, and contact messages are supported only in accounts with Unified Messaging.

Proceed to the specific configuration section below that matches your selected message type. 

[](https://help.salesforce.com/s?language=en_US)

## General Messages 

General messages include various types of content to engage your audience.

  1. Select the message type. 
  2. Configure the specific details based on your selection: 
     1. Text: Specify the text body in the Header Details section.
     2. Image, Document, Video, or Audio: 

        * Upload a file from your computer. 
        * Select a file in your content workspace. 
        * Select a value from a merge field. 
        * Specify a public URL. 

     3. For images and videos, add a caption. 
     4. For audio content, provide a brief description or context. 
  3. Save the message.



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Quick Reply Message 

A quick reply message includes buttons that allow recipients to respond immediately with a single tap. It is ideal for encouraging engagement through structured, predefined options. 

  1. Select the message type **Quick Reply**. 
  2. Include up to 3 quick reply buttons. 
  3. Each button can have a unique action identifier, which you can use to trigger a flow. 
  4. Save the message. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## List Message 

A list message displays a menu of up to 10 options, making it great for presenting users with a selection of choices (like a FAQ or product menu) without decluttering the chat history. 

  1. Select the message type **List**. 
  2. Specify the title of each section. 
  3. In each section, specify a title and action identifier for each item in the list. 
  4. Save the message. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Location Message

A location message allows you to send specific coordinates to a user, helping them find a physical storefront, event, or service point. 

  1. Select the message type **Location**. 
  2. Enter the location's name, address, and coordinates in decimal degrees. 
  3. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Flow Message 

A flow message guides customers through a structured interaction using a flow template created in the WhatsApp Business management console. This is ideal for complex interactions like booking appointments or collecting survey data. 

  1. Select the message type **Flow**. 
  2. Configure the header and body to use for the session message. 
  3. Under Flow Details, select your WhatsApp Business Account and a flow template that you created in the WhatsApp Business management console. 
  4. For Flow Button Label, enter the text that appears on the button customers click to begin the flow. 
  5. If your template contains images, add images using public URL, merge fields, or select from CMS. Add variables using merge field. 
  6. To preview the flow, click View Interaction on the canvas. 
  7. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Sticker Message 

Sticker messages help strengthen your brand or add a visual element to the conversation using static or animated stickers. 

  1. Select the message type **Sticker**. 
  2. In Content Details, enter a title and description. 
  3. Under Header, add an image. Under Body, add variables using merge field. 
  4. Enter the sticker’s URL. 

The format must be .webp. The maximum size for an animated sticker is 500 KB, and 100 KB for a static sticker. 

  5. In the Display Preview, review the message. 
  6. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Contact Message 

Contact messages make it easy for customers to save your information or reach out to a specific agent by sharing contact details directly in the chat. 

  1. Select the message type **Contact**. 
  2. In Content Details, enter a title and description. 
  3. Under Header, add an image. Under Body, add variables using merge field. 
  4. Under All Contact Details, enter the contact’s name and phone number. 
  5. To add more information, such as an email address, mailing address, or birthday, click Additional Fields. 
  6. Enter the unique WhatsApp ID assigned by Meta to enable customers to instantly save or message the contact. 
  7. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 
