{
  "hero": {
    "title": "Error conditions overview"
  },
  "title": "Error conditions overview",
  "summary": "What are error conditions and how to use them? ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true,
  "sectionlist": false
}

Error conditions play a major role in generating your monitor alerts. Setting up an error condition is the first step of the [alert and error flow cycle]([LINK_URL_1]) that lets you receive alert messages.

An **Error condition** lets you define a set of criteria to inform your monitor of any errors on your website, web service, or server. It serves as your monitor's basis for deciding which website behaviors result in an error and which don't.

If, for example, you want to ensure that your website takes less than three seconds to load, you can set an error condition and specify thresholds for the page load time. Similarly, if you want to check if your website's contents, plugins, or scripts load correctly, you can set specific error conditions for each.

Once any error condition is met, an error is generated, triggering an alert. If alerting is configured, you'll be notified by an alert message right away.

## Error conditions for monitor types [ANCHOR_1]

The [SHORTCODE_15] Error conditions [SHORTCODE_16] tab lets you set different error conditions available for each monitor type. Note that the availability of error conditions may vary depending on the monitor's category and which data it collects:

![screenshot error conditions monitor setup]([LINK_URL_2])

### Uptime monitor

The following error conditions are available for [Uptime monitor]([LINK_URL_3]) types:

| Monitor type | Error conditions | 
|--|--|
| HTTPS, Webservice HTTP and HTTPS | [SHORTCODE_1] 
- [Check page availability]([LINK_URL_4]) 
- [Check page content]([LINK_URL_5])
- [Check page load time]([LINK_URL_6])
- [Check resources]([LINK_URL_7])
[SHORTCODE_2] |
| DNS, SSL, SFTP, FTP | [SHORTCODE_3]
- [Check  resources]([LINK_URL_8])
- [Check total running time]([LINK_URL_9])
[SHORTCODE_4] |
| SMTP, POP3, IMAP | [SHORTCODE_5]
- [Check  resources]([LINK_URL_10])
- [Check total running time]([LINK_URL_11])
[SHORTCODE_6] |
| Microsoft SQL servers,  MySQL | [SHORTCODE_7]
- [Check  resources]([LINK_URL_12])
- [Check total running time]([LINK_URL_13])
[SHORTCODE_8] |
| Ping, Connect | [SHORTCODE_9]
- [Check  resources]([LINK_URL_14])
- [Check total running time]([LINK_URL_15])
[SHORTCODE_10] |

### Browser or Full-Page Check (FPC) monitor

The following error conditions are available for [Browser or Full-Page Check (FPC) monitor]([LINK_URL_16]):

| Monitor type | Error conditions |
|--|--|
| Browser or Full-Page Check | [SHORTCODE_11]

- [Check page availability]([LINK_URL_17]) 
- [Check page content]([LINK_URL_18])
- [Check URLs loaded by the page]([LINK_URL_19]) 
- [Check page load time]([LINK_URL_20])
- [Check Core Web Vitals]([LINK_URL_21])
- [Check W3C metrics]([LINK_URL_22])
- [Check console content]([LINK_URL_23])
- [Check resources]([LINK_URL_24])
[SHORTCODE_12] |

### Transaction monitor

Error conditions in [transaction monitors]([LINK_URL_25]) are also available for each step. Depending on the [transaction step setup]([LINK_URL_26]), the following error conditions may or may not be available:

![screenshot error conditions monitor setup]([LINK_URL_27])

| Monitor type | Error conditions |
|--|--|
| Transaction or User journey | [SHORTCODE_13] 
- [Content checks]([LINK_URL_28])
- [Check resources]([LINK_URL_29])
- [Check URLs loaded by the page]([LINK_URL_30]) 
- [Check Core Web Vitals]([LINK_URL_31])
- [Check W3C metrics]([LINK_URL_32])
- [Check console content]([LINK_URL_33])
- [Check site availability]([LINK_URL_34]) 
- [Check total running time]([LINK_URL_35])
[SHORTCODE_14] |

Note that the [Multi-step API (MSA) monitor]([LINK_URL_36]) uses a different way to detect errors. It uses **Assertions** to let you define checks to validate if the API response meets your expected conditions. To learn more, refer to [MSA Assertions]([LINK_URL_37]).

## Set up an Error condition [ANCHOR_2]

You can add error conditions when [setting up your monitor from scratch]([LINK_URL_38]) or editing an existing monitor.

To set up error conditions:

1. Go to [SHORTCODE_17] Monitoring > Monitor setup [SHORTCODE_18].
2. Click the monitor to which you wish to add an error condition.
3. Go to the [SHORTCODE_19] Error conditions [SHORTCODE_20] tab.
4. Click the error condition to expand the section and configure the monitor settings.
5. (Optional) To add new checks for an error condition, click the [SHORTCODE_21] \+ New check [SHORTCODE_22] button.
6. Continue configuring conditions.
7. Click [SHORTCODE_23] Save [SHORTCODE_24] to confirm the monitor changes.

If you want to get notified when an error condition is met, [create an alert definition]([LINK_URL_39]).

![screenshot error conditions monitor setup]([LINK_URL_40])