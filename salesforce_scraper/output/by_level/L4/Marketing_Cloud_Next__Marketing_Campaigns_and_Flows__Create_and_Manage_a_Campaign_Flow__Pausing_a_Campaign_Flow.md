<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_pause.htm&language=en_US&type=5 -->

# Stop and Edit a Campaign Flow in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Stop and Edit a Campaign Flow in Marketing Cloud Next

Although it’s rare, sometimes you need to stop a campaign’s flow from running. To fix an issue or make other changes, pause the flow.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create and edit flows: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissions AND Permissions to all elements in the flow  
  
In this topic:

[](https://help.salesforce.com/s?language=en_US)

  * [Pause a Flow](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_pause.htm&language=en_US&type=5#pause)
  * [Edit a Paused Flow](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_pause.htm&language=en_US&type=5#resume-deactivate "To make changes to a paused flow, you have to deactivate the original flow first. Choose to complete work that's already in progress, or to deactivate the flow immediately. Then, make your changes, and then activate the latest version.")
  * [Example Scenarios](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_pause.htm&language=en_US&type=5#examples)



[](https://help.salesforce.com/s?language=en_US)

## Pause a Flow

[](https://help.salesforce.com/s?language=en_US)

When you pause a flow, processing stops at each element and its people and data are held until you resume the flow. After you resume the flow, everything that was held is processed at one time and then the flow continues as usual.

Flow Builder accounts for the time elapsed since you paused the flow. If a flow contains a Wait for Amount of Time or Wait Until Date element, the pause duration counts toward the total wait time. Any past-due tasks are completed immediately after you resume the flow.

[](https://help.salesforce.com/s?language=en_US)

  1. Open a flow for editing. [](https://help.salesforce.com/s?language=en_US)
     * From a campaign, click **Open Flow**.
     * From the Flows tab, click  for the flow, and then select **Open Flow**.
  2. On the button bar, click **Pause**.
  3. Enter a reason for pausing the flow, and then click **Pause**.



[](https://help.salesforce.com/s?language=en_US)

## Edit a Paused Flow

To make changes to a paused flow, you have to deactivate the original flow first. Choose to complete work that's already in progress, or to deactivate the flow immediately. Then, make your changes, and then activate the latest version.

  1. From the open, paused flow, click **Deactivate** in the button bar.
  2. Choose what to do with in-progress work. [](https://help.salesforce.com/s?language=en_US)
     * To deactivate the flow and stop any processes that are in progress, select **Deactivate and cancel work**.
     * To complete in-progress work and then deactivate the flow, select **Deactivate and complete work**.
  3. To confirm your selection, click **Deactivate**.
  4. Click **Edit As New Version** , and update the flow as needed

In the toolbar, the version number is added to the flow name.

  5. To finalize the edits and restart the campaign, click **Activate** in the button bar, and then click **Activate** to confirm.

After activation, the latest version becomes available on the campaign record.




[](https://help.salesforce.com/s?language=en_US)

## Example Scenarios

[](https://help.salesforce.com/s?language=en_US)Example

Example 1: Completing Work

You pause your email campaign flow because you have updated artwork. You want to send queued emails from the previous version, but send the updated version to anyone who hasn’t started the flow yet. When you activate the new version of the paused campaign flow, you choose to complete work.

Example 2: Canceling Work

Your campaign’s email is intended for existing high value customers. You pause your email campaign flow when you realize that the audience segment includes new customers only. You don’t want anyone else to get the email because the information isn’t intended for new customers. When you activate a new version with the correct segment, you choose to cancel work.

Example 3: Wait Time

Your email series has a Wait for Amount of Time element that is set to wait 48 hours. Twelve hours into the pause period, you pause the flow for 12 hours, and then resume it. Since 24 hours have elapsed since you paused the flow, it begins sending the next email 24 hours later.
