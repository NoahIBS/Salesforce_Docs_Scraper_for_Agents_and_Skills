<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_in_app_create.htm&language=en_US&type=5 -->

# Create an In-App Message

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Create an In-App Message

Create and send a banner, modal, full-screen or push primer message to engage users while they're using your app. The message contains body text and can optionally include a title, an image, buttons, and additional text.

### Required Editions

Available in: Marketing Cloud Next Advanced Edition accounts with the Salesforce Message Credits - Mobile App Regional add-on.  
---  
User Permissions Needed  
---  
To create or edit content:  | Marketing Cloud Manager permission set AND any CMS workspace contributor role   
To publish content: | Marketing Cloud Manager permission set AND a CMS workspace contributor role of content admin or content manager   
  
An in-app message is a banner, modal, full-screen, or push primer message. A banner message appears at the top or bottom of the user's screen, a modal message partially covers the screen, and a full-screen message completely covers the screen. A push primer message prompts users to turn on push notifications.

Recommended Image Dimensions for In-App Messages In-App Layout | Aspect Ratio  
---|---  
Banner | 1:1  
Modal | 16:9, 9:16, 1:1, 3:2, 2:3, 4:3, 3:4, 5:1  
Full Screen | 16:9, 9:16, 1:1, 3:2, 2:3, 4:3, 3:4, 5:1  
Push Primer | 16:9, 9:16, 1:1, 3:2, 2:3, 4:3, 3:4, 5:1  
  
[](https://help.salesforce.com/s?language=en_US)

## Add Content to a Message

  1. On the Content tab, click **Add** , and then select **Content**.
  2. From the list of content types, select **In-App Message**.
  3. Click **Create**.
  4. Select the orientation for the message.
  5. On the editing panel, for Message Type, select **Banner** , **Modal** , **Full Screen** , or **Push Primer**.
  6. From the Image Layout dropdown, select the aspect ratio for the image in the message. Select **No Image** if the message doesn't have an image.
  7. Optionally, give the content an internal title and a description. These values aren't visible to your customers.
  8. On the Content tab, in the Title section, enter the message title. To personalize the title, click **Add Merge Field**.
     * To insert a value from the recipient’s unified profile, select **Unified Individual**.

     * To select event data, such as a subscription confirmation or a product from a confirmed order, click **Select Event**. 

     * To select from a curated list of values, such as products purchased, select **Data Graph Attribute**.

     * If saved expressions are available, select a saved expression, which includes pre-saved criteria for selecting a data graph attribute.

  9. To add text to the message, expand the Text section, and then enter the text. To personalize the message, click **Add Merge Field**. The options available are the same as those for the title.
  10. To add an image to the message, expand the Media section, and then configure the image.
     1. For Image, select the location where the image is stored.

If you select a file from CMS or a trusted URL, the image appears in the message preview. You can add a trusted URL in Setup.

     2. For Alt Image, select an alternative image to show if the original image fails to load.
     3. For Alt Text, enter the text to show if the original image fails to load and the alternative image isn't found.
  11. To add buttons to the message, expand the Actions section, and then configure your buttons.
     1. Click **Add**.
     2. For Label, enter the text that appears on the button.
     3. For Action, select the action that occurs when a user taps the button. **Dismiss Message** closes the message, **Go to Web URL** opens a web page URL, **Open Page in App** opens a page in your app, **Open Device Settings** opens the user’s device settings, and **Open Location Settings** opens the user’s location settings. For a push primer message, **Turn On Push Notifications** prompts users to enable push notifications.
     4. If you selected the **Go to Web URL** action, enter the destination URL for a web page.
     5. If you selected the **Open Page in App** action, enter the destination URLs for Android and iOS.
     6. Repeat these steps for each button you want to include. A message can include up to two buttons.
  12. To add more text to a modal, full-screen, or push primer message, expand the Additional Text section, and then configure the text. This text appears after the main message.
     1. For Display Text, enter the additional text for the message. Optionally, enclose some or all the text in double angle brackets to link it to a specific URL.
     2. Enter the URL for the linked text.



To make an in-app message available to include in a flow, publish it. You can’t activate a flow that contains an in-app message until the message is published.

[](https://help.salesforce.com/s?language=en_US)

## Customize Layout and Style

You can also control the position, layout, and style of each message on the Style tab. 

For color options, choose one from the dropdown or enter a hex code. For font options, use your brand’s font to match the app’s style. The selected font displays on users’ devices if it’s bundled in the app, else the system font is used. 

  1. To customize the message layout, expand Settings, and then configure the layout.
     1. For a banner message, choose whether you want the message to appear at the top or bottom of the screen. For a modal, full-screen, or push primer message, choose whether you want the image or title at the top of the message.
     2. Select the color and opacity for the message's overlay and background.
     3. Select the corner radius for the message.
     4. The dismiss icon is enabled by default. To not include the icon, deselect this option.

For modal, full-screen, and push primer messages, the dismiss icon can only be removed if you’ve added a dismiss button. Banner messages can be swiped away.

     5. Choose whether you want a border, a shadow, or animation for the message. If you select any of these options, configure their style settings.
  2. To customize the message title, expand Title, and then configure the settings.
     1. Select the font details for the title.
     2. Select the title alignment.
     3. Choose whether you want padding around the title and configure its style settings.
  3. To customize the message text, expand Text, and then configure the settings.
     1. Select the font details for the message.
     2. Select the message text alignment.
     3. Choose whether you want padding around the message and configure its style settings.
  4. To customize the image, expand Media, and then configure the settings.
     1. For a modal, full-screen, or push primer message, choose whether you want an edge-to-edge image that spans the entire width of the message or an inset image that appears within a defined margin.
     2. For a modal, full-screen, or push primer message, if you selected an inset image, choose an inset size to define the margin around the image.
     3. Select the corner radius for the image.
     4. Choose whether you want padding, a border, or a shadow around the image. If you select any of these options, configure their style settings.
  5. To customize the buttons, expand Buttons, and then configure the settings.
     1. For a push primer message, choose whether you want a vertical or horizontal layout for the buttons.
     2. Select the font details for the button text.
     3. Select the button color.
     4. Select the corner radius for the button.
     5. Select the button text alignment.
     6. Choose whether you want padding, a border, or a shadow around the button. If you select any of these options, configure their style settings.
  6. To customize the additional text, expand Additional Text, and then configure the settings.
     1. Select the font details for the message.
     2. Select the color for the linked text.
     3. Choose whether you want padding for the additional text and configure its style settings.
     4. Select the additional text alignment.
  7. Save your work.


