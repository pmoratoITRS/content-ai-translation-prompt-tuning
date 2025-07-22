{
  "hero": {
    "title": "My website is down but I do not receive alerts"
  },
  "title": "Website is down",
  "summary": "Your website is down but you didn't receive an alert? This is what you need to do.",
  "url": "/support/kb/alerting/website-down-no-alerts",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/website-down-no-alerts"
}

So your website, server, or web service went down, but you didn’t receive an alert or a message. What gives?! Well, failure to receive an alert or message can be caused by a number of things…

Remember that there is a whole process behind alerting. It starts with a monitor check that can signal an error. If the error is confirmed, it can generate an alert and this alert can trigger sending a message (defined in an integration). For the fine details of this story, please read on in the KB article [Alerting overview]({{< ref path="support/kb/alerting/alerting-overview" lang="en" >}}) . So, the problem can be in the alert or in the message stage.

If you did not receive an alert or a message, but you think you should have … check out our boilerplate of troubleshooting tips below.

## Check your monitors

- **Is your monitor active?**  
  If a monitor is deactivated, you will not receive any alerts, as it is not actively being monitored.
- **Is your alerting active?**  
  Both the monitor and alerting activation status can be found in the monitor status dashboard: 

  ![screenshot monitor status dashboard](/img/content/scr_monitor-status-dashboard-alerting.min.png)

- **Do you still have message credits?**  
  Sending phone or SMS messages costs message credits. If your message credits are used up, you won't get these kind of messages until you buy new message credits. Check out the article [Message credit usage]({{< ref path="support/kb/alerting/sms-credit-usage" lang="en" >}})  for more info.
- **Did the error that occurred take place during the monitor’s maintenance period?**  
  Alerts will not be sent during any monitor’s configured [maintenance period]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="en" >}}) times. The setting is found on the monitor's {{< AppElement type="tab" >}}Maintenance period{{< /AppElement >}} tab.
- **Do you include a content check in your error conditions?**  
  If you do a check for *Page content match*, (part of) the checked content must exactly match the word or phrase you are checking for. 

## Check your Alert history

The Uptrends app keeps an active log of all alerting activities. The Alert history is one of the most important tools to check, if messages have been sent. If they haven't, this is the place to do some troubleshooting.

To check and see whether alerts were generated and messages were sent, do the following:  
In the Uptrends application, go to the menu item {{< AppElement type="menuitem" >}} Alerting > Alert history{{< /AppElement >}}.   
You will now see an active log of all alerts that have been sent, including date/time, escalation level sent to, and reminder setting data.

Click an entry in the Alert history to get detailed info on that specific alert. An Alert details window will pop up with {{< AppElement type="tab" >}}Details{{< /AppElement >}} and {{< AppElement type="tab" >}}Messages{{< /AppElement >}} tabs.

![screenshot Alert history dashboard with check detail](/img/content/scr_alert-history-with-detail.min.png)

Several situations could occur:

- **There is no entry in the Alert history?**  
  Then check the settings in your monitor, afterwards check the alert definitions.
- **The entry is there, but no message was sent?**  
  In the Message tab, it is clearly shown which messages were sent and to whom.
- **No message was sent for your custom integration?**  
 Check the Message tab to find the error that was received from the third party service. In the example above, if Slack did not receive the message correctly, the Slack - "Slack to Master operator" entry will be marked red and the response of the Slack API (including error codes and info) will be shown when you expand the entry.

## Check the Operator settings

{{< callout >}}
**Note**: You have to be an administrator to access the account information of the operators. Without administrator rights, you can check your own account only.
{{< /callout >}}

To view an operator's settings go to the menu item {{< AppElement type="menuitem" >}}Account > Operators{{< /AppElement >}} and from the list of operators, select the one who does not receive any messages.

Do the following checks:

- Is the phone number and email address for the operator in question correct?  
  {{< callout >}}**Note**: You will need to ensure that the correct country code and area code are filled in for the phone number!{{< /callout >}} 
- Is the operator in question listed as on-duty?  
  ![](/img/content/94102310-1e38-4f93-af1d-01a1fdeeb418.png)
- Try sending a test SMS message from within the operator settings ( {{< AppElement type="menuitem" >}}Account > Operators{{< /AppElement >}}) to verify that it works at all. If you do not receive the test SMS within 10 minutes, try changing the SMS gateway.  
  This can be done as a general setting (valid for all operators) in the SMS Integration, on the {{< AppElement type="tab" >}}Main{{< /AppElement >}} tab by choosing another *SMS provider*.  
  Or you change the settings for an individual operator in the *Phone settings* on the {{< AppElement type="tab" >}}Main{{< /AppElement >}} tab of the Operator. Sometimes it is necessary to change the gateway for operators in a different location separately.  
  Change the gateway and repeat your test.  
  {{< callout >}}**Note**: SMS and voice alerts sent to phone numbers for operators located in China and India may get blocked due to national spam filters and do-not-call registries. [Learn more]({{< ref path="support/kb/alerting/china-india-sms-voice-alert-issues" lang="en" >}}) {{< /callout >}} 
- Try sending a test email message from within the operator settings to verify that it works.  {{< callout >}}**Note**: You should check the blacklist/spam folder on your email server if you are not receiving email messages, as sometimes they can appear there. Check out our recommendation for [whitelisting](#check-your-ip-whitelist) at the end of this article.{{< /callout >}} 

For more information on sending test messages, read the KB article [Testing alert messages]({{< ref path="support/kb/alerting/testing-alert-configurations" lang="en" >}}) .

## Check your alert definitions and escalation levels

In order to generate alerts, an alert definition needs to exist and the monitor must be assigned to it. For messages to be sent out, at least one escalation level needs to be defined and active. 

- **Is the alert definition activated?**  
  The setting can be found on the {{< AppElement type="tab" >}}Main{{< /AppElement >}} tab of an alert definition.
- **Is the monitored service in question assigned to an alert definition?**  
  You have to check all your alert definitions to see which monitors are attached to them. If you have many alert definitions and can't find the info you are looking for, enter a [support ticket]({{< ref path="contact" lang="en" >}}) to get help.
- **Are the escalation levels active?**  
  Check the setting on the corresponding {{< AppElement type="tab" >}} Escalation level {{< /AppElement >}} tab.
- **How is the alert generation set up?**  
  It is important to note that these settings can change how and when we send alerts based on confirmed/unconfirmed errors.  
  **For example:**  
  The setting *Generate an alert when 1 or more errors have occurred* means we send an alert only when one error has been confirmed. This confirmed error would leave a red bar in your monitor log.  
  The setting *Generate an alert when 2 or more errors have occurred* means that we only send alerts after 2 errors have occurred consecutively (with no OK checks between them).

## Check your IP whitelist and email settings {id="check-your-ip-whitelist"}

- Your email servers may be blocking or classifying the alert emails as spam. To prevent this, whitelist the Uptrends email IPs. Check out the [IP whitelist]({{< ref path="support/kb/account/ip-addresses-for-whitelisting" lang="en" >}}) to find the actual IP addresses for email.
- Uptrends uses **DKIM signing** for email authentication, to help prevent spoofing and phishing by adding a signature to our outgoing messages, such as alerting emails. If the DKIM mechanism fails, for whatever reason, such emails may end up being marked as spam.
