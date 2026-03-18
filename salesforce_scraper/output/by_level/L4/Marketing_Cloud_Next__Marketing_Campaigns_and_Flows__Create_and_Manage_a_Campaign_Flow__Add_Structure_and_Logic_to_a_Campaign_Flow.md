<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_add_move.htm&language=en_US&type=5 -->

# Add Structure and Logic to a Campaign Flow in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Add Structure and Logic to a Campaign Flow in Marketing Cloud Next

A campaign flow contains elements that represent certain actions along a customer's journey. To create the structure, add, remove, and move elements around the flow canvas. You can also add logic, such as branching paths and exit rule filters, to further customize the customer experiences.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
User Permissions Needed  
---  
To create and edit flows: | Marketing Cloud Manager permission setORView Flows and Create and Edit Flows user permissionsANDPermissions to all elements in the flow  
To add a decision element to a flow: | Add Decision Element to Flows  
  
In this topic:

  * [Add and Move Elements](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_add_move.htm&language=en_US&type=5#add_move "To organize the steps in a customer journey, position flow elements on the canvas from top to bottom. Click an element to move it or to open its detail panel.")
  * [Branch a Campaign Flow Path](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_add_move.htm&language=en_US&type=5#branch "The Decision element creates a branch in your flow, similar to an IF/ELSE statement in code. You configure one or more outcome paths, and any remaining records follow the default outcome path.")
  * [Remove a User from a Flow](https://help.salesforce.com/s/articleView?id=mktg.mktg_flow_elements_add_move.htm&language=en_US&type=5#exit_rule "To remove a customer from a flow when they meet certain conditions, apply an exit rule. An exit rule is like a filter that identifies people who should no longer be in a flow. For example, you can create a rule that sends someone to the end of a flow after they renew a contract.")



[](https://help.salesforce.com/s?language=en_US)

## Add and Move Elements

To organize the steps in a customer journey, position flow elements on the canvas from top to bottom. Click an element to move it or to open its detail panel.

  1. To add an element between two elements, hover over the circle and click **+**.

  2. Select an element from the list.
  3. In the panel, add a label and any other required information.
  4. To move one element: [](https://help.salesforce.com/s?language=en_US)
     1. Click the element you want to move.
     2. Select **Cut Element**.
     3. In the new location, hover over the circle between two elements and click the plus sign that appears.

The element appears in that location.

  5. To copy and paste one element: [](https://help.salesforce.com/s?language=en_US)
     1. Click the element you want to copy.
     2. Select **Copy Element**.
     3. In the new location, hover over the circle between two elements and click the plus sign that appears. Then select **Paste 1 Element**.
  6. To copy and paste multiple elements: [](https://help.salesforce.com/s?language=en_US)
     1. Click **Select Elements** on the button bar.
     2. Click the plus sign for each element you want to copy.
     3. Click the clipboard icon on the button bar.
     4. In the new location, hover over the circle between two elements and click the plus sign that appears. Then select **Paste Elements**.
  7. To delete an element, click the element, and then select **Delete Element**.



[](https://help.salesforce.com/s?language=en_US)

## Branch a Campaign Flow Path

The Decision element creates a branch in your flow, similar to an IF/ELSE statement in code. You configure one or more outcome paths, and any remaining records follow the default outcome path.

To select record fields in a decision outcome, first select a segment in the Start element. Decision outcomes are evaluated in the order they appear in the outcome list.

  1. On the flow canvas, add a Decision element.
  2. Give the element an internal name.
  3. Configure outcome conditions for each flow path.
  4. To add another outcome and flow path, click the plus sign icon in the Outcome Order section.
  5. To change the order in which outcomes are evaluated, drag outcomes to arrange them.



Example

Ursa Major Solar hosts an event at their industry convention. Account rep Lincoln wants to send a welcome email to people whose contact records were created after the conference and a conference recap email to remaining contacts. In a message series campaign flow, he adds a decision element at the beginning of the flow canvas.

Then, he configures the Decision element.

[](https://help.salesforce.com/s?language=en_US)

  * He labels the Decision element `New Conference Contact?` and the first outcome `Yes`.
  * For Condition Requirement to Execute Outcome, he selects **All Conditions are Met (AND)**.
  * For the Resource he selects **$Record > ssot__Created Date__c**.
  * For the Operator, he selects **Greater Than or Equal to** and gives the Value the start date and time of the conference.
  * For the default outcome, Lincoln changes the name to `No`, so that it’s clear on the canvas which path is which.



Then, he adds a Send Email Message element to each path, and selects the right message for each one. New contacts receive the welcome email and remaining contacts on the default outcome path receive an email with a recap of the conference. Lincoln notices an extra Wait element on the canvas, but he doesn't need it. He deletes the Wait element, and activates the flow.

[](https://help.salesforce.com/s?language=en_US)

When someone in the flow meets the condition for an outcome, they take that path. If an individual meets multiple outcome conditions, the flow takes the first one listed. If no outcome conditions are met, the flow follows the default outcome path.

[](https://help.salesforce.com/s?language=en_US)

## Remove a User from a Flow

To remove a customer from a flow when they meet certain conditions, apply an exit rule. An exit rule is like a filter that identifies people who should no longer be in a flow. For example, you can create a rule that sends someone to the end of a flow after they renew a contract.

The flow evaluates the exit rules each time a user starts a flow or resumes a flow after a pause. You can add up to 10 exit rules to a flow. Create rule conditions based on global attributes of the flow or Data 360 data graph attributes, related attributes, or calculated insights.

  1. Open a flow for editing. [](https://help.salesforce.com/s?language=en_US)
     * From a single email campaign, click the action menu, and then select **Edit Flow**.
     * From other campaigns, click **Edit Flow**.
     * From the Flows tab, click a row action menu, and then select **View Flow**.
  2. In the Start node, click **Edit** next to the count of exit rules.
  3. In the Exit Rules pane, click **Add Exit Rule**
  4. Configure the exit rule. [](https://help.salesforce.com/s?language=en_US)
     1. Enter a user-friendly label.
     2. Use the default API name or enter a unique value without any spaces.
     3. Add conditions to determine when to end a flow for someone.
  5. Configure the first condition of the exit rule.
     1. In the Resource field, select the attribute you want to filter on.
     2. Select an operator, such as **Contains**.
     3. Enter a value.
  6. To add more conditions to the exit rule, click **Add Condition**.
  7. To add more exit rules, click **Add Exit Rule**.
  8. Save your work.


