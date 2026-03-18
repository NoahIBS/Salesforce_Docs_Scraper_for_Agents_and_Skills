<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5 -->

# Create a WhatsApp Template Message

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create a WhatsApp Template Message 

Use a template for common, reusable messages that share the same basic content and structure. You can use templates to send welcome messages, order confirmations, appointment reminders, and one-time passcodes. 

### Required Editions

Available in: Salesforce Enterprise and Unlimited Editions with Marketing Cloud Next Growth and Advanced Editions   
---  
User Permissions Needed  
---  
To create or edit content:  | Marketing Cloud Manager permission set AND Any CMS workspace contributor role   
To publish content:  | Marketing Cloud Manager permission set AND A CMS workspace contributor role of Content Admin or Content Manager   
  
In this topic: 

  * [Catalog Template Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#catalog_message "A catalog template message features your product catalog. It engages customers by allowing them to browse directly within the chat.")
  * [Flow Template Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#flow_template_message "A flow template message prompts customers to provide additional information using a structured interaction.")
  * [Carousel Template Message](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#carousel_message "This interactive template displays to 10 cards, each potentially including media and a call-to-action making it great for showcasing multiple products or options.")
  * [Location Template Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#location_template_message "This allows you to send your business location to help customers find you.")
  * [Limited-time Offer Template Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#LTO_message "A limited-time offer message encourages quick action by announcing a flash sale or expiring coupon. It is ideal for driving immediate engagement.")
  * [Payment Order Details Template Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#order_details_temp_message "A payment order details message sends an order total with a payment method. This streamlines the checkout process by enabling customers to complete their purchase instantly.")
  * [Payment Order Status Template Message ](https://help.salesforce.com/s/articleView?id=mktg.mktg_content_whatsapp_create.htm&language=en_US&type=5#order_status_template_message "An order status message keeps customers informed about their purchase by sharing real-time updates. This is ideal for notifying customers when a payment is captured or an order ships.")



Before you can create a template message in Marketing Cloud Next, WhatsApp must approve it. Submit your message template in Meta Business Manager, and allow up to 48 hours for a response.

  1. From Meta Business Manager, submit a message template for approval. 
  2. From your CMS workspace, click **Add** , and then select **Content**. 
  3. In the Create CMS content window, select **WhatsApp Template Message** , and then click **Create**.
  4. Select your WhatsApp Business Account, language, and template you want to use. 
  5. In the Content Details section, specify a name and description for internal use.



Note: Flow, carousel, location, limited-time offer, payment order details, and payment order status messages are supported only in accounts with Unified Messaging. 

Proceed to the specific configuration section below that matches your selected message type. 

[](https://help.salesforce.com/s?language=en_US)

## Catalog Template Message 

A catalog template message features your product catalog. It engages customers by allowing them to browse directly within the chat. 

  1. Under Body, add variables using merge fields. 
  2. Under Single Product Template or Multiple Product Template, add a section title and product IDs for each item in the section. 
  3. To add more content, click Add and create one or more sections.
  4. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Flow Template Message 

A flow template message prompts customers to provide additional information using a structured interaction.

  1. Under Header, add variables. 
  2. Under Flow Details, add images using public URL, merge fields, or select from CMS. Add variables. 
  3. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Carousel Template Message 

This interactive template displays to 10 cards, each potentially including media and a call-to-action making it great for showcasing multiple products or options.

  1. Enter the body text and variables. 
  2. In the Carousel section, click the Edit icon to customize each card. 
     1. Select the image or video header based on the template's media type.
     2. If the message body contains text variables, enter the text to replace the variables. 
     3. Add button details (quick reply, phone number, or URL). Each card requires at least one button (up to two). 
     4. Click Update Details. 
  3. Repeat step 2 to personalize each card.
  4. (Optional) In the Carousel section, drag the cards to rearrange them in the desired order.
  5. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Location Template Message

This allows you to send your business location to help customers find you. 

  1. Enter the location's name, address, and coordinates in decimal degrees. 
  2. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Limited-Time Offer Template Message 

A limited-time offer message encourages quick action by announcing a flash sale or expiring coupon. It is ideal for driving immediate engagement. 

  1. Under Header, add an image. Under Body, add variables using merge field. 
  2. Enter when the offer expires, and your preferred time zone, and a coupon code if applicable. 
  3. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Payment Order Details Template Message 

A payment order details message sends an order total with a payment method. This streamlines the checkout process by enabling customers to complete their purchase instantly.

  1. Under Header, add an image. Under Body, add variables using merge field. 
  2. In Amount Details, enter the total amount. 
  3. In Payment Settings, enter the payment reference ID and product type. 
  4. Under Payment Options, click Add. Select a payment type: Pix, Boleto, or Payment links. 
  5. Enter the required details for the payment method. For example, for a Payment Link, enter the URL. For Pix, enter the Pix code, merchant name, key, and key type. 
  6. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 

[](https://help.salesforce.com/s?language=en_US)

## Payment Order Status Template Message 

An order status message keeps customers informed about their purchase by sharing real-time updates. This is ideal for notifying customers when a payment is captured or an order ships. 

  1. Under Header, add an image. Under Body, add variables using merge field. 
  2. In the Order Status section, enter the Payment Reference ID, order status, and payment status. 
  3. Save your changes. 



A user can add a published message to a Marketing Cloud Next campaign flow. 
