<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_draft_content_considerations.htm&language=en_US&type=5 -->

# Considerations for Drafting Content in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Considerations for Drafting Content in Marketing Cloud Next

When generating campaign content, keep in mind these usage limits and considerations.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition  
---  
  
[](https://help.salesforce.com/s?language=en_US)

## Language and Locale Support

Language | locale | culture code  
---|---|---  
English | English (United States) | en_US  
  
[](https://help.salesforce.com/s?language=en_US)

## Large Language Model Support

Drafting and saving a campaign brief supports this model. 

Model  
---  
OpenAI GPT-4o mini  
  
[](https://help.salesforce.com/s?language=en_US)

## Einstein Trust Layer Service Support

Drafting and saving a campaign supports these Trust Layer services.

Service | Description  
---|---  
Dynamic Grounding with Secure Data Retrieval | Yes  
Prompt Defense (System policies and prompt injection detection) | Yes  
Data Masking | Yes  
Toxicity Detection | No  
Audit and Feedback | Yes  
  
[](https://help.salesforce.com/s?language=en_US)

## Region Support

Drafting content supports these models for geo-aware request routing.

Model | api name  
---|---  
OpenAI GPT-4o | llmgateway_GPT4Omni  
  
## Usage Types Consumed by Content Creation

Content creation uses generative AI and Data 360 to ingest, store, and process data. You’re billed in these categories when you use content creation. Before deployment, work with your Salesforce account team to confirm license availability and plan credit usage, including whether you use Einstein Requests or Flex Credits.

Tip

This feature has access to Digital Wallet, a free account management tool that offers near real-time consumption data for enabled products across your active contracts. Access Digital Wallet and start tracking your org's usage. To learn more, see [About Digital Wallet](https://help.salesforce.com/s/articleView?id=xcloud.wallet_about.htm&language=en_US&type=5).

## Einstein Requests

Einstein Requests is one of the usage metrics for generative AI. The use of generative AI capabilities, in either a production or sandbox environment, can consume Einstein Requests and possibly [Data 360 credits](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5). To learn when Einstein Requests applies, see [Metering for Agentforce and Generative AI Usage](https://csqa6sb1.help.sfdc.sh/s/articleView?id=ai.generative_ai_usage_metering_logic.htm&type=5).Direct API calls to the LLM gateway use Einstein Requests. To learn more, see the [Rate Card for Einstein Requests](https://www.salesforce.com/products/einstein/skus/).Einstein Requests are available in: 

  * Enterprise, Performance, and Unlimited editions with an Einstein for Sales, Einstein for Platform, or Einstein for Service add-on. To purchase the Einstein for Sales, Einstein for Platform, or Einstein for Service add-on, contact your Salesforce account executive.
  * All Einstein 1 Editions
  * Salesforce Enterprise and Unlimited Editions with Marketing Cloud Next Growth or Advanced Edition

  
---  
  
## Flex Credits

Usage Type / Subtype | Description  
---|---  
Standard Action | Usage is determined by the number of standard actions executed by the agent in a text conversation. Each standard agent action includes the processing of up to 10,000 tokens. Tokens are units of data processed by AI models. Actions exceeding this limit are counted as a separate standard action each time the 10,000 token limit is exceeded. For example, processing 20,001 tokens is 3 standard actions. Actions involving lengthy prompts sent to the LLM can be counted as multiple actions where the 10,000 tokens per action limit is exceeded.Standard agent actions are actions that are available out-of-the-box. To check the list of Standard actions, see [_Standard Action Reference_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&language=en_US&type=5).Note Use of some standard agent actions require that a subscription has been purchased for each user that accesses these actions, such as a subscription to Agentforce for Sales Add-on or Agentforce for Service Add-on. To determine which subscription is required for such standard actions, see Standard Action Reference at [_Standard Action Reference_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&language=en_US&type=5). While this requirement is not technically enforced yet, users who don’t have the required add-on license will lose access to such actions for which they don’t have a license when the requirement is enforced.  
Custom Action | Usage is determined by the number of custom actions executed by the agent in a text conversations. Each custom action includes the processing of up to 10,000 tokens. Tokens are units of data processed by AI models. Actions exceeding this limit are counted as a new custom action each time the 10,000 token limit is exceeded. For example, processing 20,001 tokens is 3 custom actions. Actions involving lengthy prompts sent to the LLM can be counted as multiple actions where the 10,000 token action per limit is exceeded.Custom actions are actions that are created by you or which result from your modification of a standard action. To learn more about what customer created actions are, see [_Create a Custom Agent Action_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_custom.htm&language=en_US&type=5). To learn more about how standard actions become custom actions, see [_Editing Standard Agent Action Reference Actions_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_edit_reference.htm&language=en_US&type=5).  
Standard Voice Action | Usage is determined by the number of standard actions executed by the agent in a voice conversation.Note Use of some standard agent actions require that a subscription has been purchased for each user that accesses these actions, such as a subscription to Agentforce for Sales Add-on or Agentforce for Service Add-on. To determine which subscription is required for such standard actions, see Standard Action Reference at [_Standard Action Reference_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&language=en_US&type=5). While this requirement is not technically enforced yet, users who don’t have the required add-on license will lose access to such actions for which they don’t have a license when the requirement is enforced.  
Custom Voice Action | Usage is determined by the number of custom actions executed by the agent in a voice conversation. Custom actions are actions that are created by you or which result from your modification of a standard action. To learn more about what customer created actions are, see [_Create a Custom Agent Action_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_custom.htm&language=en_US&type=5). To learn more about how standard actions become custom actions, see [_Editing Standard Agent Action Reference Actions_](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_edit_reference.htm&language=en_US&type=5).  
Starter Prompts | Usage is calculated based on two factors: the number of direct requests to the LLM via the LLM gateway, and whether the gateway uses a Bring Your Own Large Language Model (BYOLLM).Each starter prompt includes the processing of up to 2,000 tokens. Prompt usage is counted in chunks of 2,000 tokens, rounded up. Prompts that exceed this limit will be metered as multiple prompts, with each additional 2,000-token chunk counting as a new prompt. For example, a prompt with a total of 6,500 input and output tokens will be metered as 4 prompts.Tokens are units of data processed by the AI models.  
Standard PromptsBasic PromptsAdvanced Prompts | Usage is calculated based on two factors: the number of direct requests to the LLM via the LLM gateway, and whether the gateway uses a Salesforce managed large language model. The specific category depends on the model that is used. See Large [Language Model Support](https://help.salesforce.com/s/articleView?id=ai.generative_ai_large_language_model_support.htm&language=en_US&type=5) to find out which usage types apply. All Standard, Basic, and Advanced prompts process up to 2,000 tokens per prompt. Token usage is rounded up in 2,000-token increments. All Standard, Basic, and Advanced prompts that exceed this limit will be metered as multiple prompts, with each additional 2,000-token chunk counting as a new prompt. For example, a prompt with a total of 6,500 input and output tokens will be metered as 4 prompts. Tokens are units of data processed by the AI models.   
Translation | Translation converts text from one human language into text of another, a process executed by machine translation models. Translation usage is metered by the number of characters processed for the translation. To understand how your consumption appears in the Digital Wallet, consider a scenario where you process 9,000 characters for translation. Because this usage is in units of one million characters, your actual consumption is 0.009 units (9,000 divided by 1,000,000). In the Digital wallet, this usage is rounded to two decimal places and the value is displayed as 0.01 units.   
Agentforce Voice Minutes | Usage is determined by the duration of the voice call between an end user and Agentforce Voice. Usage is rounded up to the next full minute, meaning any fraction of a minute is treated as a full minute. For example, 

  * A call of 60 seconds is billed as 1 minute. 
  * A call of 61 seconds is billed as 2 minutes.

If your org has both Agentforce Voice Actions and Agentforce Voice Minutes enabled, Voice Minutes take precedence for billing. When Agentforce Voice Minutes are available in your org, only Agentforce Voice Minutes are metered, and Voice Actions usage types are not applied to the same activity.   
Speech-to-Text | Speech-to-Text converts spoken audio into written text, a process run by automatic speech recognition (ASR) models. Usage is calculated based on the duration of the audio processed for each transcription, in seconds. In Digital Wallet, this usage is aggregated and displayed in minutes.   
Text-to-Speech | Text-to-Speech converts written text into natural-sounding spoken audio, a process run by automatic Speech Synthesis models. Usage is metered by the number of text characters processed for the speech generation. In the Digital Wallet, this usage is aggregated and displayed in units of million characters. To understand how your consumption appears in the Digital Wallet, consider a scenario where you process 9,000 characters for conversion from text to speech. Because this usage is in units of one million characters, your actual consumption is 0.009 units (9,000 divided by 1,000,000). In the Digital wallet, this usage is rounded to two decimal places and the value is displayed as 0.01 units.  
  
When you create content, credits can be consumed in usage types on other consumption cards by related features such as [_Agentforce Data Library_](https://help.salesforce.com/s/articleView?id=ai.data_library_parent.htm&language=en_US&type=5), [_Audit and Feedback_](https://help.salesforce.com/s/articleView?id=ai.generative_ai_audit_feedback_usage_types.htm&language=en_US&type=5), or [Data 360 Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5).

## Data Cloud One Support

Drafting content in Marketing Cloud Next isn't supported in Data Cloud One companion orgs.

[](https://help.salesforce.com/s?language=en_US)

## Limits and Allowances

Generative AI features in Marketing Cloud Next consume AI requests.

#### See Also

  * [Large Language Model Support](https://help.salesforce.com/s/articleView?id=ai.generative_ai_large_language_model_support.htm&language=en_US&type=5)


