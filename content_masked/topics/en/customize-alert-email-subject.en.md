{
  "hero": {
    "title": "Customizing email alert message subject and formatting"
  },
  "title": "Customizing email alert message subject and formatting",
  "summary": "In this article you find instruction on how to customize the subject of alerting emails, and enable HTML formatting.",
  "url": "[URL_BASE_TOPICS]alerting/customize-alert-email-subject",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true,
  "sectionlist": true
}

To easily track and categorize the status of your monitors via email, Uptrends allows you to customize alert email subjects in the **Alerting by email** integration. You can receive alerts for both single monitors and groups of monitors, depending on the errors generated within a specific timeframe. Any subject you set will be applied to all outgoing alert emails.

To customize the email subject:

1. Go to [SHORTCODE_1] Alerting > Integrations [SHORTCODE_2] > **Alerting by email** integration. 
2. Check the **Customize integration** checkbox to show the [SHORTCODE_3] Customizations [SHORTCODE_4] tab.
3. Go to the [SHORTCODE_5] Customizations [SHORTCODE_6] tab.
4. To receive emails in HTML format, refer to the [HTML formatting]([LINK_URL_1]) instructions. Otherwise, proceed to the next step.
5. Choose the [Alert types]([LINK_URL_2]) (Error, Reminder, OK) checkbox to customize the subject for each single or multiple monitors. 
6. Enter a new subject. You can use a wide range of variables, such as the [Automatic variables]([LINK_URL_3]) and [Alert system variables]([LINK_URL_4]) in the email subject field. For example, use the [INLINE_CODE_1] and [INLINE_CODE_2] variables to refer to the monitor's name and the date and time value of the alert.

7. Click [SHORTCODE_7] Save [SHORTCODE_8] to confirm changes.


![Customizing alerting email subject]([LINK_URL_5])

## HTML formatting

You can set the outgoing alert emails in HTML format to receive emails with rich formatting (banners, colors, images, and hyperlinks) instead of plain text. Note that by setting the default plain text emails to HTML formatting, you may encounter some issues with the automated systems that processes the formatting. By default, the HTML formatting is only enabled for new accounts. If you wish to enable or disable this setting, refer to the instructions below.

To enable HTML formatting:

1. Go to the [SHORTCODE_9] Customizations [SHORTCODE_10] tab and check the **Use HTML mail** checkbox.
2. Click [SHORTCODE_11] Save [SHORTCODE_12] to confirm changes.

To disable HTML formatting:

1. Go to the [SHORTCODE_13] Customizations [SHORTCODE_14] tab and uncheck the **Use HTML mail** checkbox.
2. Click [SHORTCODE_15] Save [SHORTCODE_16] to confirm changes.
