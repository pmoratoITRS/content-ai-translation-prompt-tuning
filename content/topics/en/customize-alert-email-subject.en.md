{
  "hero": {
    "title": "Customizing email alert message subject and formatting"
  },
  "title": "Customizing email alert message subject and formatting",
  "summary": "In this article you find instruction on how to customize the subject of alerting emails, and enable HTML formatting.",
  "url": "/support/kb/alerting/customize-alert-email-subject",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/customize-alert-email-subject",
  "tableofcontents": true,
  "sectionlist": true
}

To easily track and categorize the status of your monitors via email, Uptrends allows you to customize alert email subjects in the **Alerting by email** integration. You can receive alerts for both single monitors and groups of monitors, depending on the errors generated within a specific timeframe. Any subject you set will be applied to all outgoing alert emails.

To customize the email subject:

1. Go to {{< AppElement type="menuitem" >}} Alerting > Integrations {{< /AppElement >}} > **Alerting by email** integration. 
2. Check the **Customize integration** checkbox to show the {{< AppElement type="tab" >}} Customizations {{< /AppElement >}} tab.
3. Go to the {{< AppElement type="tab" >}} Customizations {{< /AppElement >}} tab.
4. To receive emails in HTML format, refer to the [HTML formatting]({{< ref path="/support/kb/alerting/customize-alert-email-subject#html-formatting" lang="en" >}}) instructions. Otherwise, proceed to the next step.
5. Choose the [Alert types]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="en" >}}) (Error, Reminder, OK) checkbox to customize the subject for each single or multiple monitors. 
6. Enter a new subject. You can use a wide range of variables, such as the [Automatic variables]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="en" >}}) and [Alert system variables]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="en" >}}) in the email subject field. For example, use the `{{@monitor.name}}` and `{{@alert.timestamp}}` variables to refer to the monitor's name and the date and time value of the alert.

7. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm changes.


![Customizing alerting email subject](/img/content/scr-customizing-email-subjects_020624.min.png)

## HTML formatting

You can set the outgoing alert emails in HTML format to receive emails with rich formatting (banners, colors, images, and hyperlinks) instead of plain text. Note that by setting the default plain text emails to HTML formatting, you may encounter some issues with the automated systems that processes the formatting. By default, the HTML formatting is only enabled for new accounts. If you wish to enable or disable this setting, refer to the instructions below.

To enable HTML formatting:

1. Go to the {{< AppElement type="tab" >}} Customizations {{< /AppElement >}} tab and check the **Use HTML mail** checkbox.
2. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm changes.

To disable HTML formatting:

1. Go to the {{< AppElement type="tab" >}} Customizations {{< /AppElement >}} tab and uncheck the **Use HTML mail** checkbox.
2. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to confirm changes.
