{
  "hero": {
    "title": "Phone (voice) alert setup"
  },
  "title": "Phone (voice) alerts setup",
  "summary": "Everything you need to know about Uptrends' Phone alerts: setup, sample messages, testing, and outgoing number selection. ",
  "url": "[URL_BASE_TOPICS]alerting/phone-alerts",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Sometimes an e-mail, text message, or integrated messages from Slack or PagerDuty just can't get the job done. Sometimes you need the phone to ring to grab your attention from a sound sleep or an important game. Phone alerts give you that option. Based on your alert, escalation levels, and operator schedules you can have the phone ring and your on-duty operator then receives an automated voice message about the alert situation. In this Knowledge Base article, you will learn about:

-   [Setting up your phone alerts]([LINK_URL_1])
-   [Setting up your operators for phone alerts]([LINK_URL_2])
-   [Setting up your alert definitions with phone alerts]([LINK_URL_3])
-   [Using message credits]([LINK_URL_4])
-   [What to expect when you answer the phone]([LINK_URL_5])

## Set up Uptrends for phone alert integration [ANCHOR_1]

To add phone alerts to your arsenal of messaging tools you first need to have a Premium level account or higher.

[SHORTCODE_1]
**Note:** You can easily upgrade your Starter Level account by calling your account manager, or you can create a service ticket and someone will get back with you quickly. Visit the [Contact]([LINK_URL_6]) page for more details.
[SHORTCODE_2]

By default, phone alerting isn't enabled right away; for phone integration you have to enable them on the **Integrations** page of the [SHORTCODE_9]Alerts[SHORTCODE_10] menu. Once enabled, you can then add phone alerts to your alert escalations. To enable phone alerts:

1.  Select **Phone** from the **Integration type** box.
2.  Use the default or change the name in the **Integration name** box.
3.  Choose an **Outgoing phone number** from the box. Choose a number based on your location; if your country is not in the list, choose the country nearest you. You (and your team) can add the number to your contacts for quick identification. If you leave **System default** selected, Uptrends will choose the best number based on the receivers (operators) country code.  
    [SHORTCODE_3]**Note:** Check the [list of supported countries]([LINK_URL_7]) and country codes for the operator's receiving phone number. If you don't find the operator's country and code on the list, they will NOT receive alert calls.[SHORTCODE_4] 
4.  Select the **Language** for the phone alert only if you want to override the language settings at the operator level.
5.  Check to ensure that the monitor's name is text to speech friendly; if not, select the **Use alternate monitor names** check box. Learn more about [enabling and setting speech friendly monitor names]([LINK_URL_8]).
6.  Select the **Active** check box if not already selected
7.  Click [SHORTCODE_11]Save[SHORTCODE_12].

![screenshot phone integration]([LINK_URL_9])

## Setting up operators [ANCHOR_2]

On the [SHORTCODE_13]Main[SHORTCODE_14] tab of the Operator's Setup page, you have the option of adding a **Mobile phone** number and overriding the **Outgoing phone number** you defined when enabling phone integrations. If you already use SMS/text messaging in your alert definitions, you may not need to adjust any of your operator profiles.

### Add a mobile phone number

The system uses the operator's mobile phone number to send SMS/text alerts, and Uptrends uses this same number for phone alerts. To add a phone number:

1.  Type a plus sign (\+) followed by the country code followed the phone number.
2.  Do not use any other non-numeric characters; e.g., the phone number should look something like \+15551234567 for a US number.
3.  Click [SHORTCODE_15]Save.[SHORTCODE_16] 

[SHORTCODE_5]
**Note:** Yes, you can use a landline number in the **Mobile phone** box (does anyone have landlines anymore?), but if you also use SMS/text alerts, that operator will not receive the SMS/text alerts. If you need to use a landline for an operator's mobile phone number, make sure that you never include that operator in escalations that you've defined for SMS/text alerts.
[SHORTCODE_6]

### Override the default outgoing phone number

If you have defined an **Outgoing phone number** on the Phone Integration page, you may need to override that choice on an individual operator basis. By selecting **Override phone integration settings**, Uptrends will use the alternative number you select in the phone selection box.

![screenshot operator phone settings]([LINK_URL_10])
## Setting up escalations for phone alerts [ANCHOR_3]

Now that you have your phone alerts enabled and your operators all have their mobile phone numbers in the system, it is time to set up your escalations for phone alerting.

1.  Select **Alert definitions** from the **Alerts** option on the Main Menu.
2.  Click to choose an existing definition, or create a new definition by clicking [SHORTCODE_17]Add alert definition[SHORTCODE_18] on the Quick Action Menu to create a new one.
3.  Select one of the [SHORTCODE_19]Escalation level[SHORTCODE_20] tabs.
4.  Select the check box labeled **Phone** in the **Alerting by integrations** section. If you do not see Phone as an option, either you still need to enable phone integration or you need to select the **Active** box on the Phone Integrations page (see [set up]([LINK_URL_11]) above).
5.  Click [SHORTCODE_21]Save[SHORTCODE_22].

![screenshot alert definition phone integration]([LINK_URL_12])

That's it! When an error triggers an alert for this definition and escalation level, Uptrends will locate the on-duty operator's number and call their cell phone with an automated message.

## Cost for using phone alerts [ANCHOR_4]

If you already use SMS/text messages, you probably already know about message credits. Each account level comes with some included credits, but once used, you have to purchase additional credits or we'll stop sending phone or SMS alerts. Phone alerts and SMS messages use the same credits. For more information, visit the [SMS/phone message credits]([LINK_URL_13]) page.

[SHORTCODE_7]
**Note:** Testing your phone alerts and text messages is FREE. Uptrends doesn't use your message credits for your testing purposes.
[SHORTCODE_8]

## What to expect when the phone rings [ANCHOR_5]

So what will the phone alert tell you? If the system has the error information, you may hear something like this:

> "Hello, this is Uptrends.  
> We detected an error for the monitor, Home Page. The error was HTTP pattern matched, and it started occurring 1 minute ago.  
> The HTTP error code was 500.  
> The time limit of 12 was exceeded.  
> Goodbye."

Of course, we just made that one up; your message will give you verbiage based on your specific alert situation and monitor. If the information is unavailable, you will hear something like this:

> "Hello, this is Uptrends.  
> An error has occurred for one of your monitors. Right now, no more information is available. Please verify the status of your monitors in Uptrends.  
> Goodbye."

## Troubleshooting phone alerts

Are you having trouble with receiving phone alerts? We've set up a [troubleshoot guide for Phone Alerts]([LINK_URL_14]).

## Have questions?

If you need more help with setting up operators, defining alerts, and setting up escalations, visit the Uptrends [knowledge base]([LINK_URL_15]). If you still can't find the information you need, we are here to help. Visit the [Contact]([LINK_URL_16]) page to get support numbers or open a support ticket.
