{
  "title": "Send custom messages through the PagerDuty integration",
  "date": "2024-05-22",
  "url": "/changelog/may-2024-pagerduty-custom-text",
  "translationKey": "https://www.uptrends.com/changelog/may-2024-pagerduty-custom-text"
}

The out-of-the-box [PagerDuty integration]({{< ref path="/support/kb/alerting/integrations/pagerduty" lang="en" >}}) allows users to send their [Uptrends alerts]({{< ref path="/support/kb/alerting" lang="en" >}}) directly to PagerDuty. As part of this update, the message we send to PagerDuty will now include the [custom message configured in the escalation levels]({{< ref path="/support/kb/alerting/alert-escalation-levels#what-are-escalation-levels" lang="en" >}}) of your alert definitions. You can find the message under **Message** in the **Custom details** of the PagerDuty alert.