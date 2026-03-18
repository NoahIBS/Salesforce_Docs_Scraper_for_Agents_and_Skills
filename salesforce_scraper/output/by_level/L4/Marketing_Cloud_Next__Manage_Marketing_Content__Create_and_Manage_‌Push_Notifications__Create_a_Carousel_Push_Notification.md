<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_create_a_carousel_push_notification.htm&language=en_US&type=5 -->

# Create a Carousel Push Notification

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create a Carousel Push Notification 

A carousel message is a push notification that contains several cards that the user can scroll through. You can specify a unique image, text, and open behavior for each card. 

### Required Editions

Available in: Marketing Cloud Next **Advanced** Edition accounts with the Salesforce Message Credits - Mobile App Regional add-on.  
---  
User Permissions Needed  
---  
To create or edit content: | Marketing Cloud Manager permission set AND any CMS workspace contributor role   
To publish content: | Marketing Cloud Manager permission set AND a CMS workspace contributor role of content admin or content manager  
  
  1. In Marketing Cloud Next, on the **Content** tab, select your marketing content workspace.
  2. Click **Add** , and then select **Content**.
  3. From the list of content types, select **Push Notification Message**.
  4. Click **Create**.
  5. In the editing pane on the right side of the screen, for **Push Type** , select **Carousel**.
  6. Give the content an internal title and, optionally, a description. These values aren’t visible to your customers.
  7. On the **Content** tab, specify the title, subtitle, and message text that you want to appear on the message.
  8. In the **Card Details** section, next to **Card 1** , click **Edit**.
  9. Configure the first carousel card.
     1. To add an image, expand the **Media** section, and then select an image.
     2. To add text, expand the **Text** section, and then enter the text.
     3. To specify what happens when a customer taps a carousel page, expand the **Open Behavior** tab, and then select an open behavior.
  10. Next to **Card 1** , click the back arrow.
  11. To add a card, click **Add Card**.
  12. Configure the new card.
  13. Continue adding and configuring cards until the carousel is complete.

You can change the order of the cards by using the up and down arrows.

  14. To add a custom icon to Android messages, expand the **Icons** section, and then configure the icons.
     1. For **Small Icon** , enter the file path for a small icon to show in the message. The small icon is typically similar to the icon for your app.
     2. For **Large Icon** , enter the file path for a large icon to show in the message. The large icon is typically related to the content of the message that you’re sending.
  15. Save your work.



To make a push notification available to send in a campaign, publish it. You can’t activate a Flow that contains a push notification until the message is published.
