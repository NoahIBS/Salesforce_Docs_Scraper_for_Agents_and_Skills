<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_mobile_app.htm&language=en_US&type=5 -->

# Set Up Mobile App Messaging in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Mobile App Messaging in Marketing Cloud Next

In Marketing Cloud Next, you can use segments and Flow Builder to send timely, personalized notifications to users of your apps. To start sending mobile app messages, add and configure your app in Setup.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Advanced** Edition and the Salesforce Message Credits - Mobile App Regional add-on  
---  
  
Note

Mobile App messaging isn’t supported in Government Cloud. See [Marketing Cloud Next in Government Cloud](https://help.salesforce.com/s/articleView?id=ind.government_cloud_marketing_cloud.htm&language=en_US&type=5).

Mobile App Messaging is available only in Marketing Cloud Next instances hosted in Germany and the United States. If you aren’t sure which region your instance is hosted in, contact your account executive.

The Your Apps page in Setup shows the apps that are associated with your account. This table describes the information shown for each app.

Label | Description  
---|---  
**Application Name** | The name associated with the app.  
**Sending Services** | The mobile app notification services that are configured for the app. Possible values are iOS and Android.  
**Status** | Indicates whether the app is active. An app becomes active when at least one sending service is configured. You can only send messages through an active app.  
**Active Users** | The number of active users of the app who have opted in to receive messages.  
**Created** | The date when the app was added to your account.  
**Created By** | The name of the user who added the app to your account.  
**Last Modified** | The date when the app was last modified.  
  
[](https://help.salesforce.com/s?language=en_US)

## Add Your App

  1. In Setup, go to **Unified Messaging** | **Mobile App** | **Your Applications**.
  2. Click **Add Application**.
  3. On the Add Application window, click **Next**.
  4. For **Application Name** , enter a name.
  5. Click **Next**.



After you create the app, configure at least one sending service.

[](https://help.salesforce.com/s?language=en_US)

## Configure iOS Settings

If your application has a version that runs on Apple iOS, configure the settings for Apple Push Notification service (APNs).

  1. On the Sending Services tab, expand the iOS section.
  2. For Environment Type, choose whether to use a **Production** or **Sandbox** environment.
  3. For Key Type, choose whether to use an **APNS p8 Auth Key** or an **APNS p12 Auth Key**.
  4. Click Upload Files, and then upload your APNs certificate file.
  5. For Key ID, enter your key ID.

For more information about finding your key ID, see _Apple Developer_ : [Get a key identifier](https://developer.apple.com/help/account/keys/get-a-key-identifier).

  6. For Team ID, enter your team ID.

To find your Team ID, sign in to your Apple Developer account and click **Membership details**.

  7. For Bundle ID, enter the bundle ID associated with your app. The bundle ID is an alphanumeric string that uses reverse DNS notation, such as `com.northerntrailoutfitters.app`.
  8. Save your changes.



[](https://help.salesforce.com/s?language=en_US)

## Configure Android Settings

If your application has a version that runs on Android devices, configure the settings for Firebase Cloud Messaging (FCM).

  1. On the Sending Services tab, expand the Android section.
  2. Click **Upload Files** , and then upload your Firebase Developer certificate.
  3. Save your changes.



[](https://help.salesforce.com/s?language=en_US)

## (Optional) Configure Category Names for iOS Carousels

If you plan to use create carousel messages for iOS devices, specify a category name. Specifying your category names helps ensure that your messages render correctly. When you create a carousel message template, you provide the category name.

  1. On the Categories tab, for iOS Carousel Category Name, enter a unique name.
  2. Save your changes.



[](https://help.salesforce.com/s?language=en_US)

## Test Your App’s Configuration

After you create an app in Setup and add the Engagement SDK to your app, perform a test to make sure that the app is properly configured.

  1. On the Your Apps page in Setup, from the list of apps, select an app to test.
  2. On the Test tab, for **Select Identifier** , select the type of identifier to use to send a test message. Choose from these options:
     * **System Token** : Send a message to a recipient based on their unique, device-generated token.
     * **Device ID** : Send a message to a specific device based on its unique device ID. 
     * **Individual ID** : Send a message to a subscriber based on their Unified Individual ID in Marketing Cloud Next.
  3. Specify the unique ID for the type of identifier you selected.
     * If you selected System Token, select the operating system of the target device, and then enter the token in the **System Token** field.
     * If you selected Device ID, enter the target device ID in the **Device ID** field.
     * If you selected Individual ID, enter the target device ID in the **Individual ID** field.
  4. Click **Test Configuration**.



The Results section on the right side of the page indicates whether the test was successful. If the test fails, verify that you provided the correct credentials for the push notification services.
