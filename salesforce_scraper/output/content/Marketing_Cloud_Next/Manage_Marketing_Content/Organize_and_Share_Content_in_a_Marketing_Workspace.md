<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_content_workspaces.htm&language=en_US&type=5 -->

# Organize and Share Content in a Marketing Workspace

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Organize and Share Content in a Marketing Workspace

When you create content in Marketing Cloud Next, it’s stored in a marketing workspace. You can use the default Content Workspace for Marketing Cloud, or create additional workspaces to focus campaign assets, manage collaboration across teams, or organize content by initiatives. Delete unused workspaces that you no longer need. To keep your workspace tidy, add folders. All your workspaces are listed on the Content tab.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** Edition or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create a marketing workspace: | Modify All Data ORMarketing Cloud Admin permission set  
To delete a marketing workspace: | A CMS workspace contributor role of content admin  
To share or unshare a workspace: | Marketing Cloud Manager permission set ANDA CMS workspace contributor role of content admin or content manager  
  
All marketing workspaces are connected to two default channels. The Marketing Messages channel sends emails and SMS messages, and the Marketing Landing Pages site channel hosts your landing pages. When you publish content, it’s available for use in the channels connected to the workspace.

To encourage consistency and reduce duplication of content, you can use a workspace as a source and let other workspaces in your org access the content. Only content contributors in the source workspace can change the source content. You can share a marketing workspace with another marketing workspace or with a general workspace that’s used by other Salesforce CMS users in your org. Sharing workspaces is a great solution for customers using Marketing Cloud Next together with Salesforce CMS in other Salesforce products. For example, create and manage your company logo image in a marketing workspace. Then share that content with a general workspace so that your colleagues in other departments can easily find and use the image.

All content, including drafts and the latest published versions, is available in a Shared with Workspaces folder in each target workspace. The target workspace can use the shared content with its configured channels.

  1. Create a workspace.
     1. Open the Content tab, and click **Add Workspace**.
     2. Choose the Marketing workspace type.
     3. Give the workspace a clear name and description.
     4. Select the default language.
  2. Add at least one content admin to the workspace. See [Add Workspace Contributors to Marketing Cloud](https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_setup_contributors_workspace.htm&language=en_US&type=5 "When marketers create content in Marketing Cloud Next, they use Digital Experiences tools, which require a different set of permissions. Choose a contributor role for each user who needs access to manage or create marketing content, such as emails and forms.").
  3. Add a folder.
     1. Open the workspace.
     2. Click **Add** and select **Folder**.
     3. Enter a name, and save.
     4. To add a child folder, open the folder and repeat these steps.
  4. Configure sharing settings.
     1. Open the workspace.
     2. Click  and select **Workspace Sharing**.
     3. Select an unshared target workspace, and move it to the Shared field.
     4. Add as many workspaces to the Shared field as needed, and then save your work.

Source content is available in a target workspace until you unshare the workspace. To unshare the workspace, move it back to the Unshared field.

  5. To view shared content in a target workspace, open the Shared with Workspaces folder.
  6. To identify where a piece of source content is used across all workspaces, open the source content detail record and click the **Usage Info** tab.



Example

To make sure that your shared content will be published, consider this scenario. You have three enhanced CMS workspaces: Space A, Space B, and Space C. 

You share Space A (source) to Space B (target). You add an image stored in Space A to a landing page in Space B. When you publish the landing page, the image is published, and the landing page and image are both available to Space B’s channels. 

However, if you share Space B (source) to Space C (target), publishing the landing page to Space C’s channels doesn’t publish the image because the image belongs to Space A. To publish the image, you must share Space A to Space C.

Source content is available in a target workspace until you unshare the workspace. If the target workspace’s channels use content from the source workspace, that content is unpublished in the target’s channels and is unavailable wherever it’s referenced.

You can’t delete your org’s default marketing workspace, but you can delete other unused workspaces from the workspace settings menu. Before you delete a marketing workspace, unpublish all the content in it and remove it from all source and target workspace sharing relationships. To delete a workspace, go to the workspace settings, and click **Delete Workspace**.

#### See Also

  * [Create and Manage a CMS Workspace](https://help.salesforce.com/s/articleView?id=xcloud.cms_cmsworkspace-create.htm&language=en_US&type=5)


