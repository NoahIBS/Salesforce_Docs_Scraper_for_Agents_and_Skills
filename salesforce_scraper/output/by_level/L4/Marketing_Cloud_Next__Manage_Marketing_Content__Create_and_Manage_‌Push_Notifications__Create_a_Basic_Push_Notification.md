<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_create_basic_push_notification.htm&language=en_US&type=5 -->

# Create a Basic Push Notification

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create a Basic Push Notification

A basic push notification is a single message that you send to users of your app. A basic push notification contains body text and an open behavior, which determines what happens when a recipient taps the message. It can optionally include a title, a subtitle, and an image.

### Required Editions

Available in: Marketing Cloud Next Advanced Edition accounts with the Salesforce Message Credits - Mobile App Regional add-on.  
---  
User Permissions Needed  
---  
To create or edit content:  | Marketing Cloud Manager permission set AND any CMS workspace contributor role   
To publish content: | Marketing Cloud Manager permission set AND a CMS workspace contributor role of content admin or content manager   
  
  1. On the Content tab, click **Add** , and then select **Content**.
  2. From the list of content types, select **Push Notification Message**.
  3. Click **Create**.
  4. In the editing pane on the right side of the screen, for Push Type, select **Basic**.
  5. Give the content an internal title and, optionally, a description. These values aren't visible to your customers.
  6. On the Content tab, specify the title, subtitle, and message text that you want to appear on the message.
  7. In the Open Behavior section, configure the action that occurs when a recipient taps the message to open it.
     * **Open the App** \- Open the app as if the user had tapped its icon on their device.
     * **Go to App URL** \- Open the app to a specific location.
     * **Go to Web URL** \- Open a web browser and go to a specific URL.
  8. To add buttons to an Android message, expand the Action Buttons section, and then configure your buttons.
     1. Click **Add**.
     2. For **Label** , enter the text that appears on the button.
     3. For **Icon** , enter the path to the icon file.
     4. For **Action** , select the action that occurs when a user taps the button. The options that are available are the same as the open behaviors for the message.
     5. If you selected the Go to App URL or Go to Web URL actions, enter the destination URL in the **URL** field.
     6. For **Action Identifier** , enter a unique identifier for the button.
     7. Repeat these steps for each button you want to include. A message can include up to 3 buttons.
  9. To add an image to the message, expand the Media section, and then configure the image.
     1. For Image, select the location where the image is stored.
     2. To use different images for iOS and Android, select **Use different image for Android** , and then configure the Android image.
  10. To add a custom icon to Android messages, expand the Icons section, and then configure the icons.
     1. For **Small Icon** , enter the file path for a small icon to display in the message. The small icon is typically similar to the icon for your app.
     2. For **Large Icon** , enter the file path for a large icon to display in the message. The large icon is typically related to the content of the message that you're sending.
  11. Save your work.



To make a push notification available to send in a campaign, publish it. You can’t activate a Flow that contains a push notification until the message is published.
