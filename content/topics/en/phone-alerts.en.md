{
  "hero": {
    "title": "Phone (voice) alert setup"
  },
  "title": "Phone (voice) alerts setup",
  "summary": "Everything you need to know about Uptrends' Phone alerts: setup, sample messages, testing, and outgoing number selection. ",
  "url": "/support/kb/alerting/phone-alerts",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/phone-alerts"
}

Sometimes an e-mail, text message, or integrated messages from Slack or PagerDuty just can't get the job done. Sometimes you need the phone to ring to grab your attention from a sound sleep or an important game. Phone alerts give you that option. Based on your alert, escalation levels, and operator schedules you can have the phone ring and your on-duty operator then receives an automated voice message about the alert situation. In this Knowledge Base article, you will learn about:

-   [Setting up your phone alerts](#set-up-phone-alert-integration)
-   [Setting up your operators for phone alerts](#setting-up-operators)
-   [Setting up your alert definitions with phone alerts](#setting-up-escalations-for-phone-alerts)
-   [Using message credits](#cost-for-using-phone-alerts)
-   [What to expect when you answer the phone](#what-to-expect-when-the-phone-rings)

## Set up Uptrends for phone alert integration {id="set-up-phone-alert-integration"}

To add phone alerts to your arsenal of messaging tools you first need to have a Premium level account or higher.

{{< callout >}}
**Note:** You can easily upgrade your Starter Level account by calling your account manager, or you can create a service ticket and someone will get back with you quickly. Visit the [Contact]({{< ref path="contact" lang="en" >}}) page for more details.
{{< /callout >}}

By default, phone alerting isn't enabled right away; for phone integration you have to enable them on the **Integrations** page of the {{< AppElement type="menuitem" >}}Alerts{{< /AppElement >}} menu. Once enabled, you can then add phone alerts to your alert escalations. To enable phone alerts:

1.  Select **Phone** from the **Integration type** box.
2.  Use the default or change the name in the **Integration name** box.
3.  Choose an **Outgoing phone number** from the box. Choose a number based on your location; if your country is not in the list, choose the country nearest you. You (and your team) can add the number to your contacts for quick identification. If you leave **System default** selected, Uptrends will choose the best number based on the receivers (operators) country code.  
    {{< callout >}}**Note:** Check the [list of supported countries]({{< ref path="support/kb/alerting/phone-alerts-troubleshooting" lang="en" >}}) and country codes for the operator's receiving phone number. If you don't find the operator's country and code on the list, they will NOT receive alert calls.{{< /callout >}} 
4.  Select the **Language** for the phone alert only if you want to override the language settings at the operator level.
5.  Check to ensure that the monitor's name is text to speech friendly; if not, select the **Use alternate monitor names** check box. Learn more about [enabling and setting speech friendly monitor names]({{< ref path="support/kb/alerting/speech-friendly-monitor-names-for-phone-alerts" lang="en" >}}).
6.  Select the **Active** check box if not already selected
7.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.

![screenshot phone integration](/img/content/scr_integrations-phone.min.png)

## Setting up operators {id="setting-up-operators"}

On the {{< AppElement type="tab" >}}Main{{< /AppElement >}} tab of the Operator's Setup page, you have the option of adding a **Mobile phone** number and overriding the **Outgoing phone number** you defined when enabling phone integrations. If you already use SMS/text messaging in your alert definitions, you may not need to adjust any of your operator profiles.

### Add a mobile phone number

The system uses the operator's mobile phone number to send SMS/text alerts, and Uptrends uses this same number for phone alerts. To add a phone number:

1.  Type a plus sign (\+) followed by the country code followed the phone number.
2.  Do not use any other non-numeric characters; e.g., the phone number should look something like \+15551234567 for a US number.
3.  Click {{< AppElement type="savebutton" >}}Save.{{< /AppElement >}} 

{{< callout >}}
**Note:** Yes, you can use a landline number in the **Mobile phone** box (does anyone have landlines anymore?), but if you also use SMS/text alerts, that operator will not receive the SMS/text alerts. If you need to use a landline for an operator's mobile phone number, make sure that you never include that operator in escalations that you've defined for SMS/text alerts.
{{< /callout >}}

### Override the default outgoing phone number

If you have defined an **Outgoing phone number** on the Phone Integration page, you may need to override that choice on an individual operator basis. By selecting **Override phone integration settings**, Uptrends will use the alternative number you select in the phone selection box.

![screenshot operator phone settings](/img/content/scr_integrations-override-phone-settings.min.png)
## Setting up escalations for phone alerts {id="setting-up-escalations-for-phone-alerts"}

Now that you have your phone alerts enabled and your operators all have their mobile phone numbers in the system, it is time to set up your escalations for phone alerting.

1.  Select **Alert definitions** from the **Alerts** option on the Main Menu.
2.  Click to choose an existing definition, or create a new definition by clicking {{< AppElement type="button" >}}Add alert definition{{< /AppElement >}} on the Quick Action Menu to create a new one.
3.  Select one of the {{< AppElement type="tab" >}}Escalation level{{< /AppElement >}} tabs.
4.  Select the check box labeled **Phone** in the **Alerting by integrations** section. If you do not see Phone as an option, either you still need to enable phone integration or you need to select the **Active** box on the Phone Integrations page (see [set up](#set-up-uptrends-for-phone-alert-integration) above).
5.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.

![screenshot alert definition phone integration](/img/content/scr_phone-integration-alert-definition.min.png)

That's it! When an error triggers an alert for this definition and escalation level, Uptrends will locate the on-duty operator's number and call their cell phone with an automated message.

## Cost for using phone alerts {id="cost-for-using-phone-alerts"}

If you already use SMS/text messages, you probably already know about message credits. Each account level comes with some included credits, but once used, you have to purchase additional credits or we'll stop sending phone or SMS alerts. Phone alerts and SMS messages use the same credits. For more information, visit the [SMS/phone message credits]({{< ref path="support/kb/alerting/sms-credit-usage" lang="en" >}}) page.

{{< callout >}}
**Note:** Testing your phone alerts and text messages is FREE. Uptrends doesn't use your message credits for your testing purposes.
{{< /callout >}}

## What to expect when the phone rings {id="what-to-expect-when-the-phone-rings"}

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

Are you having trouble with receiving phone alerts? We've set up a [troubleshoot guide for Phone Alerts]({{< ref path="support/kb/alerting/phone-alerts-troubleshooting" lang="en" >}}).

## Have questions?

If you need more help with setting up operators, defining alerts, and setting up escalations, visit the Uptrends [knowledge base]({{< ref path="support/kb" lang="en" >}}). If you still can't find the information you need, we are here to help. Visit the [Contact]({{< ref path="contact" lang="en" >}}) page to get support numbers or open a support ticket.
