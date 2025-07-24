{
  "hero": {
    "title": "Creating alert definitions"
  },
  "title": "Creating alert definitions",
  "summary": "In this article you find instruction on how to define your website availability and performance alerts, so you only get alerted when you want to.",
  "url": "[URL_BASE_TOPICS]alerting/create-alert-definitions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

An alert definition states how and to whom to send an alert using escalation levels. Before an alert definition works (as desired) you have to set up [error conditions]([LINK_URL_1]), which are the rules that trigger an alert.

An [escalation level]([LINK_URL_2]) contains a series of parameters for alert generation, number of reminders, notification method, and who will receive it.

[SHORTCODE_1]
**Note**: A default alert definition is already configured within your Uptrends account. You can either change its rules or create your own from scratch.
[SHORTCODE_2]

## Creating an alert definition

To configure a custom alert definition:

1. Go to to the menu [SHORTCODE_5] Alerting > Alert definitions [SHORTCODE_6].
2. Click the [SHORTCODE_7]Add Alert Definition[SHORTCODE_8] button.
3. Add an alert definition name.
3. Select the **Active** check box to enable the alert.
4. Choose the monitors the alert definition applies to.
5. Set up your escalation levels, see the article on [escalation levels]([LINK_URL_3]) for detailed information.
6. Click the [SHORTCODE_9] Save [SHORTCODE_10] button.

You've just created your very own alert definition! This is now reflected in the **Alert definition dashboard** when you navigate to [SHORTCODE_11] Alerting > Alert definitions [SHORTCODE_12].

## Alert definition dashboard

The **Alert definition dashboard** presents a summarized table to see all your alert definitions in just one place. You can easily visualize and check your alert definition settings, including:

- **Name** - specifies the name of your alert definition setup.
- **Active escalation levels** - specifies the number of active or enabled escalations levels. Currently, the minimum number of escalation levels is 0, and the maximum is 3. All inactive escalation levels will not generate any alerts.
- **Active** - specifies the status of your alert definition. You can see *Yes* if the alert definition is active, else, *No*.

All Uptrends dashboards can be exported for better monitoring insights and future reference. Check this [article]([LINK_URL_4]) to find the step-by-step process on how to export your dashboards.

Once you've successfully exported your data in any format, you can see additional details aside from the alert definition settings mentioned in the first paragraph of this section. Additional columns of information are as follows:

- **Monitors** - specifies which monitor/s uses the alert definition.
- **Monitor groups** - specifies which monitor group/s uses the alert definition.
- **Is alert definition active** - shows *Yes* if the alert definition is enabled and active, else, *No*.
- **Is escalation level n active** - shows *Yes* if the escalation level is enabled and active, else, *No*.
- **Operators for escalation level n** - specify which operators are assigned for each escalation level.
- **Operator groups for escalation level n** - specify which operator groups are assigned for each escalation level.
- **Integrations for escalation level n** - specify the type of integration or which platform you'll receive your alerts for each escalation level. Integrations can be *Alerting by email, Alerting by SMS, Alerting by phone*, or [custom integrations]([LINK_URL_5]).

[SHORTCODE_3]
As Uptrends have three escalation levels, the **n** refers to the number corresponding to the alert escalation level you've set up on the alert definition editor screen.
[SHORTCODE_4]