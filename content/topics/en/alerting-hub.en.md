{
  "hero": {
    "title": "Alerting hub"
  },
  "title": "Alerting hub",
  "summary": "The place to start when exploring Alerting",
  "url": "/support/kb/alerting/alerting-hub",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alerting-hub",
  "tableofcontents": false
}

Alerting is a complex topic and requires many settings to play together smoothly to get the expected result. It depends on the correct setup of error conditions, alert definitions, escalation levels and integrations. There are a lot of parameters to tune and the hub is here to help you with that.

The hub will tell you about the theory of alerting by pointing you to the key concepts and other relevant topics in the knowledge base. From the hub you can directly jump to relevant settings in the Uptrends app. It also tells you about the actual situation: are there active alerts and are the things you rely on, like alert definitions and integrations, active? Lastly it will let you know if you still have message credits.

Open the Alerting hub by going to {{< AppElement type="menuitem" >}}Alerting > Explore alerting{{< /AppElement >}} in the main menu.

![](/img/content/scr-alerting-hub.min.png)

The top part of the hub and the sidebar contain links to the key concepts and where and how to set up alerting. There are a number of links that refer to articles in the knowledge base. Other links will bring you directly to the part of the app, where you can set up definitions that are needed for the functioning of alerts.

The lower part of the hub tells you about the actual situation of your alerting, like how many monitors have alerts at the moment. This overview is personalized and the following applies

- Only the monitors or alert definitions are shown where you have [monitor view permission]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}}) or [alert definition edit permission]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="en" >}}). 
- Only the integrations where you have the **Edit integration** permission are shown. Other integrations are not taken into account here.



From here you can jump directly to:

-   The monitors that are on top of the list of alerts
-   Ongoing alerts, bringing you to the *Alert status* dashboard
-   Full alert history, bringing you to the *Alert log* dashboard

There are also some statistics around your alerting setup that give you a quick overview of the situation and help you with troubleshooting. The statistics show you the number of:

- Active integrations 
- [Monitors covered by alert definitions]({{< ref path="support/kb/alerting/monitor-alerting-coverage" lang="en" >}}) (only monitors in [production mode]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode#monitormodeproduction" lang="en" >}}))
- Active alert definitions
- Available message credits

When looking at the statistic **alert definitions active**, keep in mind that only definitions that are active and have at least one active escalation level will count towards this number. It is fine to have an alert definition that is active with no active escalation levels. There will be alerts generated (if applicable) that can be viewed within the Uptrends app, e.g. in the Alert log, but there will be no alert messages sent to operators and this definition will not count towards the **alert definitions active** statistic.

There also needs to be at least one integration in an escalation level of the alert definition where the **Use integration** (or more powerful) permission is set for the current operator. Otherwise the alert definition will not be shown as active.
