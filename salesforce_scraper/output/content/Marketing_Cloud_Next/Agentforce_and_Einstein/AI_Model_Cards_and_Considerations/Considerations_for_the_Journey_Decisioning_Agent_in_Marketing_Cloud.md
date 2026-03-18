<!-- Source: https://help.salesforce.com/s/articleView?id=mktg.mktg_einstein_journey_decisioning_considerations.htm&language=en_US&type=5 -->

# Considerations for the Journey Decisioning Agent in Marketing Cloud Next

You are here:

  1. [Salesforce Help](/s/?language=en_US)
  2. [Docs](/s/products?language=en_US)
  3. [Marketing Cloud Next](https://help.salesforce.com/s/articleView?id=mktg.mktg_main.htm&language=en_US&type=5)



# Considerations for the Journey Decisioning Agent in Marketing Cloud Next

To use the Journey Decisioning agent, consider supported functionality, usage, limitations and allowances, limits, and other issues.

### Required Editions

Available in: Salesforce **Enterprise** and **Unlimited** Editions with Marketing Cloud Next **Growth** or **Advanced** Edition and Marketing Cloud Engagement+  
---  
  
## Language and Locale Support

The Journey Decisioning agent supports the languages and locales supported on the Salesforce generative AI platform, as described in [_Einstein Generative AI Supported Languages and Locales_](https://help.salesforce.com/s/articleView?id=ai.generative_ai_platform_languages.htm&language=en_US&type=5).

[](https://help.salesforce.com/s?language=en_US)

## Large Language Model Support

The Journey Decisioning agent supports the models on the Salesforce generative AI platform, as described in [_Large Language Model Support_](https://help.salesforce.com/s/articleView?id=ai.generative_ai_large_language_model_support.htm&language=en_US&type=5). By default, calls use OpenAI GPT-4o.

[](https://help.salesforce.com/s?language=en_US)

## Einstein Trust Layer Service Support

The Journey Decisioning agent supports the Trust Layer services provided on the Saleforce generative AI platform, as described in [_Einstein Trust Layer_](https://help.salesforce.com/s/articleView?id=ai.generative_ai_trust_layer.htm&language=en_US&type=5). Ask your system administrator about which Einstein Trust Layer services are enabled in your org and available for the Journey Decisioning Agent.

[](https://help.salesforce.com/s?language=en_US)

## Region Support

The Campaign creation agent supports the geo-aware models supported on the Salesforce generative AI platform, as described in [_Geo-Aware LLM Request Routing on the Einstein Generative AI Platform_](https://help.salesforce.com/s/articleView?id=ai.generative_ai_platform_geo_aware_routing.htm&language=en_US&type=5).

## Usage Types Consumed by Journey Decisioning

Journey decisioning uses generative AI and Data 360 to ingest, store, and process data. You’re billed in these categories when you use journey decisioning. Before deployment, work with your Salesforce account team to confirm license availability and plan credit usage.

Tip

This feature has access to Digital Wallet, a free account management tool that offers near real-time consumption data for enabled products across your active contracts. Access Digital Wallet and start tracking your org's usage. To learn more, see [About Digital Wallet](https://help.salesforce.com/s/articleView?id=xcloud.wallet_about.htm&language=en_US&type=5).

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
  
When you use Journey Decisioning, credits can be consumed in usage types on other consumption cards by related features such as [_Agentforce Data Library_](https://help.salesforce.com/s/articleView?id=ai.data_library_parent.htm&language=en_US&type=5), [_Audit and Feedback_](https://help.salesforce.com/s/articleView?id=ai.generative_ai_audit_feedback_usage_types.htm&language=en_US&type=5), or [Data 360 Billable Usage Types](https://help.salesforce.com/s/articleView?id=data.c360_a_data_usage_types.htm&language=en_US&type=5).

## Data Cloud One Support

Journey decisioning isn't supported in Data Cloud One companion orgs.

## Associated Standard Actions

These standard actions are associated with the Journey Decisioning agent.

  * Marketing Cloud: Select Journey
  * Marketing Cloud: Create Journey Content


