<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_sandbox.htm&language=en_US&type=5 -->

# Test Marketing Cloud Next in a Sandbox

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Test Marketing Cloud Next in a Sandbox

A sandbox is a copy of your Salesforce org that you can use for development, testing, and training without compromising the data and apps in your production org. Marketing Cloud Next supports every sandbox type: Developer, Developer Pro, Partial Copy, and Full Copy.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create a sandbox: | Manage Dev Sandboxes (Developer or Developer Pro only)ORManage Sandboxes (all sandbox types)  
To deploy Data 360 objects: | Data Cloud Architect  
  
Use a sandbox for:

  * Training and product support—Bring new employees up to speed, and respond to urgent issues faster with data in testing and development environments.
  * Parallel development—Create and collaborate with multiple teams that build and test in their own environments.
  * App development and org customization—Modify objects, content, flows, decisions, forms, and so on. If a test fails, it fails in a safe environment.
  * App testing and automation—Conduct user-acceptance testing, staging, and integration to make apps more robust.
  * Implementing new features—Set up a new channel, third-party app, or integration, or create a proof of concept and customize it for your team’s workflow and business needs.



[](https://help.salesforce.com/s?language=en_US)

## Supported Features and Objects

When you create a sandbox, most Marketing Cloud Next features are available for customization and testing. If an object isn’t replicated from the production org, you can re-create it in the sandbox org.

The table lists the Marketing Cloud Next objects that are replicated to and deployable from a sandbox. To learn how specific platforms work in a sandbox org, see [Sandboxes: Staging Environments for Customizing and Testing](https://help.salesforce.com/s/articleView?id=platform.deploy_sandboxes_parent.htm&language=en_US&type=5).

Feature | Functional in Sandbox | Replicated in developer/developer pro Sandbox | Replicated in partial copy sandbox | Replicated in Full sandbox | Deployable from sandbox  
---|---|---|---|---|---  
Brief | Yes | No | Yes | Yes | No  
Brand content | Yes | No | No | Yes | Yes  
Campaign | Yes | No | Yes | Yes | No  
CMS Marketing Workspace | Yes | No | No | Yes | Yes  
Content block (email) | Yes | No | No | Yes | Yes  
Content block (landing page) | Yes | No | No | Yes | Yes  
Communication Subscription | Yes | No | Yes | Yes | No  
Email content | Yes | No | No | Yes | Yes  
Email template | Yes | No | No | Yes | Yes  
Event-triggered flow | Yes | Yes | Yes | Yes | Yes  
Expression content | Yes | No | No | Yes | No  
Form content | Yes | No | No | Yes | Yes  
Form handler content | Yes | No | No | Yes | Yes  
Image content | Yes | No | No | Yes | Yes  
Landing page content | Yes | No | No | Yes | Yes  
Landing page template | Yes | No | No | Yes | Yes  
Mobile App Messaging content | Yes | No | No | Yes | Yes  
Segment-triggered flow | Yes | Yes | Yes | Yes | Yes  
SMS content | Yes | No | No | Yes | Yes  
Tracked link content | Yes | No | No | Yes | No  
WhatsApp content | Yes | No | No | Yes | Yes  
  
[](https://help.salesforce.com/s?language=en_US)

## Considerations for Marketing Cloud Next in a Sandbox

Refer to these considerations when creating a sandbox and deploying changes from a sandbox in Data 360.

Billing | 

  * Using Marketing Cloud Next in a sandbox consumes credits for Data 360, Unified Messaging, and Salesforce Personalization. See [Billing Considerations for Data 360 Sandbox](https://help.salesforce.com/s/articleView?id=data.c360_a_data_cloud_sandbox_billing_considerations.htm&language=en_US&type=5), [Billing Considerations for Unified Messaging](https://help.salesforce.com/s/articleView?id=mktg.um_credit_usage.htm&language=en_US&type=5), and [Billable Usage Type for Salesforce Personalization](https://help.salesforce.com/s/articleView?id=mktg.persnl_basics_billable_usage_types.htm&language=en_US&type=5).
  * Usage of credits in each sandbox org is visible in the production org's Digital Wallet. To determine which org generated usage, view the usage type and filter by org.

  
---|---  
Unified Messaging | 

  * When testing an SMS campaign in a sandbox, don't use the same sender code that you use in production. Instead, in your production org, acquire a dedicated sender code for sandbox testing. See [Set Up an SMS Unified Messaging Channel](https://help.salesforce.com/s/articleView?id=mktg.um_channel_sms.htm&language=en_US&type=5). 
  * A sender code can't be active in more than one org at a time.
  * You can activate or deactivate a sender code from within each sandbox.
  * Email, mobile app messaging, and WhatsApp require unique configurations in each sandbox. For example, a sandbox requires its own authenticated domain and from addresses for email, as well as its own tracking domains, WhatsApp number, and blockout windows. These settings can't be deployed from one org to another.

  
Marketing content | Due to storage limits in Developer, Developer Pro, and Partial Copy sandboxes, content and digital assets in the CMS Marketing Workspace aren’t copied over when a sandbox is created or refreshed. To move content, use [change sets](https://help.salesforce.com/s/articleView?id=platform.changesets.htm&language=en_US&type=5) or [create an import](https://help.salesforce.com/s/articleView?id=xcloud.cms_import_content.htm&language=en_US&type=5).  
Tests with customer engagement data | To test custom reports or event-based flows, add behavior and messaging events to your sandbox. Create a CSV file with the necessary fields mapped to Data 360 DMOs, and import it by using the File Upload data stream. See [Ingest Data by Uploading a File](https://help.salesforce.com/s/articleView?id=data.c360_a_upload_a_csv_file.htm&language=en_US&type=5).   
  
[](https://help.salesforce.com/s?language=en_US)

## Set Up Marketing Cloud in a Sandbox

To use Marketing Cloud Next in a sandbox, create a sandbox org, turn on Data 360, and then set up Marketing Cloud Next the same way you would in a production org.

Before you begin, make sure that Marketing Cloud Next and Data 360 are turned on in your production org.

  1. Prepare a sandbox.

If you’re using an existing sandbox, make sure that the Marketing Cloud licenses are in the sandbox by [matching production licenses](https://help.salesforce.com/s/articleView?id=xcloud.overview_licenses_and_sandbox.htm&language=en_US&type=5) or [refreshing your sandbox](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_refresh.htm&language=en_US&type=5). Otherwise, [create a sandbox](https://help.salesforce.com/s/articleView?id=platform.data_sandbox_create.htm&language=en_US&type=5).

  2. Turn on Data 360 in the sandbox.

See [Create a Data 360 Sandbox](https://help.salesforce.com/s/articleView?id=data.c360_a_data_cloud_sandbox_create.htm&language=en_US&type=5). 

  3. Confirm that the required Data 360 connectors are active, including the Salesforce CRM connector, the Websites and Mobile Apps connector, and the Ingestion API connectors. See [Check Connector Status](https://help.salesforce.com/s/articleView?id=data.c360_a_check_connector_status.htm&language=en_US&type=5).
  4. Set up Marketing Cloud Next and applicable Unified Messaging channels.

See [Getting Started with Marketing Cloud Next Setup](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_overview.htm&language=en_US&type=5 "To get started with Marketing Cloud Next, complete some basic settings, then continue through the required and recommended steps. The time it takes to complete setup depends on the features that you want to use.").

  5. To test landing pages in your sandbox, publish the Marketing Landing Pages site.

The Marketing Landing Pages site supports landing pages with Experience Cloud tools but isn't designed to contain content. Don't add content directly to this site.

     1. From Setup, in the Quick Find box, enter `All Sites`, and select **All Sites** under Digital Experiences.
     2. Next to Marketing Landing Pages, select **Builder**.
     3. Click **Publish**.



Note Replicated flows always have a Draft status in the target org, even if the status was Active in the source org.

[](https://help.salesforce.com/s?language=en_US)

## Set Up a Blackhole for Email

When you test email in a sandbox, a blackhole prevents the accidental sending of test messages to real customer email addresses. Enable the use of a blackhole in a full or partial sandbox, and then add exceptions for domains that need to receive test emails.

  1. Log in to a sandbox org that includes Marketing Cloud.
  2. From Setup, in the Quick Find box, enter `Blackhole`, and then select **Sandbox Blackhole**. 
  3. Turn on the blackhole feature. 

It takes about 10 minutes for the changes to take effect.

  4. (Optional) In the Add Allowed Email Domains section, add up to five email domains that can receive test emails. For example, if you add `example.org`, a sandbox email sent to any address with the example.org domain will reach the recipient.



Note Blackhole doesn’t suppress sends from the Preview and Test window of the email editor or the Debug flow window of Flow Builder.

[](https://help.salesforce.com/s?language=en_US)

## Deploy Changes

After you make changes in a sandbox, deploy those changes back to the production org by using Salesforce Platform DevOps features. When event-triggered flows, segment-triggered flows, or marketing content have queries or expressions that reference Data 360 objects, deploy the Data 360 objects first.

  1. Deploy Data 360 objects by using one of the provided deployment methods.
     1. Select these objects for deployment: segments, DMOs, DLOs, data graphs, calculated insights, data actions, Personalization Points, recommenders, and engagement signals. See [Deploy Data 360 Changes from a Sandbox](https://help.salesforce.com/s/articleView?id=data.c360_a_data_cloud_sandbox_deploy.htm&language=en_US&type=5). 
     2. After deploying to the target org, activate or publish the objects.
  2. Deploy Marketing Cloud Next objects by using one of the provided deployment methods.
     1. In the Digital Experience component, select content records, email templates, brand, and images.
     2. In the Digital Experience Bundle component, select the CMS workspace.

Deploy content records to the same CMS workspace in the target org. If the CMS workspace is already available in the production org, skip this step.

     3. In the Flow Definition component, select Flows.
     4. After deploying to the target org, activate or publish the objects.



You can use any of these methods to move changes from sandbox to production.

Method | resources  
---|---  
Change Sets | 

  * [Change Sets](https://help.salesforce.com/s/articleView?id=platform.changesets.htm&language=en_US&type=5)
  * [Connect Organizations for Deployment](https://help.salesforce.com/s/articleView?id=platform.deploy_connection_parent.htm&language=en_US&type=5)
  * [Outbound Change Sets](https://help.salesforce.com/s/articleView?id=platform.changesets_about_outbound.htm&language=en_US&type=5)
  * [Inbound Change Sets](https://help.salesforce.com/s/articleView?id=platform.changesets_about_inbound.htm&language=en_US&type=5)

  
DevOps Center | [Improve Release Quality with DevOps Testing](https://help.salesforce.com/s/articleView?id=platform.devops_testing_improve_release_quality_with_devops_testing.htm&language=en_US&type=5)  
Metadata Retrieve and Deploy | 

  * [Understanding Metadata API](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_intro.htm)
  * [File-Based Calls](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_file_based_calls_intro.htm)
  * [Digital Experience Bundle](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_digitalexperiencebundle.htm)

  
CLI Retrieve and Deploy | [Salesforce CLI Setup Guide](https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_setup_intro.htm)  
  
Note Deployed flows and content always have a Draft status in the target org, even if the status was Active or Published in the source org.
