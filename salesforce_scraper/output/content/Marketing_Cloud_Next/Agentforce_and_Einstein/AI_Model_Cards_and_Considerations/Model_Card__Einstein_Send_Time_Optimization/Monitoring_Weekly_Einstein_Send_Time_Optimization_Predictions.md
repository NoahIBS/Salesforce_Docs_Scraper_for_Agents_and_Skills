<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_chart_esto_weekly_predictions.htm&language=en_US&type=5 -->

# Monitoring Weekly Einstein Send Time Optimization Predictions

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Monitoring Weekly Einstein Send Time Optimization Predictions

Visualize and analyze customer engagement over the course of a week. Using Data 360 Data Model Object (DMO) information, you can create a chart that shows Einstein Send Time Optimization scores per contact point email rather than by a unified individual. Use the information to adjust your send time parameters and align with maximum engagement send times. Access and run your Email Send Time Optimization report from Data 360 reports or Analytics in the Marketing app.

[](https://help.salesforce.com/s?language=en_US) Field Label | Field API Name | Data Type | Description  
---|---|---|---  
`Organization Id` |  `organizationId` | Text | The core ID for your organization.  
`Contact Point Email Id` |  `contactPointEmailId` | Text | The contact point email IDs that are represented in the time of the week number.  
`Time of Week` |  `timeOfWeek` | Number | A number from 0 through 167 that represents the best send hour for each contact point email ID, starting on Monday at midnight. For example, Monday midnight is 0, Monday 1 AM is 1, and so on, and Sunday 11 PM is 167.  
`Created Date` |  `createdDate` | DateTime | The most recent date-stamped data.
