<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_admin_identity.htm&language=en_US&type=5 -->

# Set Up Identity-Licensed Users in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Set Up Identity-Licensed Users in Marketing Cloud Next

Identity-licensed users can access Marketing Cloud Next using Salesforce single sign-on. You can assign Identity-licensed users the same permissions as Marketing Cloud Managers, including full access to campaigns, segments, flows, and shared Analytics reports. Clone the Identity-licensed user profile and customize the permissions for Marketing Cloud Next, and then assign the profile to new users.

### Required Editions

Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To add users:  | Manage Internal Users  
To create and edit profiles: | Manage Profiles and Permission Sets   
  
[](https://help.salesforce.com/s?language=en_US)

## Configure an Identity Profile for Marketing

  1. From Setup, in the Quick Find box, enter `Profiles` and then select **Profiles**.
  2. Find the Identity User profile, and then click **Clone**. 
  3. Enter a profile name and save your changes.
  4. In Tab Settings, change the visibility to Default On for these tabs: Analytics, Briefs, Campaigns, Consent, Contacts, Content, Flows, Home, Leads, and Segments. 
  5. Customize page layouts and permissions as needed.
  6. Save your changes. 
  7. Repeat steps 1-6 to create additional Identity User profiles for marketing. 



[](https://help.salesforce.com/s?language=en_US)

## Create an Identity-Licensed User for Marketing

  1. From Setup, in the Quick Find box, enter `Users` and then select **Users**.
  2. Click **New User**. 
  3. In the User License dropdown, select **Identity**. 
  4. In the Profile dropdown, select the identity user profile you configured for marketing. 
  5. Save your changes. 
  6. Add the necessary permissions to access marketing manager tools and Marketing Performance dashboards.
     1. In Permission Set Assignments, click **Edit Assignments**.
     2. Add two permission sets: the Marketing Cloud Manager and Tableau Next Included App Business User. 
  7. To add more Identity-licensed users for marketing, repeat steps 1-6. 


