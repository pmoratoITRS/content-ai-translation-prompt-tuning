{
  "hero": {
    "title": "Display your monitoring data in Grafana"
  },
  "title": "Grafana Integration",
  "summary": "A guide on how to display your monitoring data in Grafana.",
  "url": "[URL_BASE_TOPICS]dashboards-and-reporting/grafana",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The Uptrends Grafana data source allows information about the status and statistics reported by Uptrends monitors and monitor groups to be displayed within a Grafana environment. It makes use of the Uptrends API to retrieve statistical data, or data about the current status, for your monitors and monitor groups. 

This guide describes how to set up a basic Grafana instance that can connect to and pull data from Uptrends, so that it can be displayed in your Grafana environment. If you encounter any issues, have any questions, or would like to submit feedback, please [contact us]([LINK_URL_1]). 

## Prerequisites
- An active Uptrends account.
- A set of Uptrends APIv4 credentials: this guide will cover how to generate those.
- A Grafana instance with access to the server configuration.

## Pre configuration

### Create an Uptrends APIv4 account

[SHORTCODE_1] **Note**: If you already have a set of APIv4 credentials available, you can use those, and skip this step.  [SHORTCODE_2]

Grafana communicates with Uptrends through the API (version 4 - see the [API documentation]([LINK_URL_2]) for more information), by requesting the relevant information and then displaying it in your Grafana dashboards. In order to make those requests, Grafana must have access to a registered API account. You can create an API account by following the instructions in the article [Operator API account management]([LINK_URL_3]).

The result of the steps outlined in that article is a username and password. Make sure to note these down, since you'll need to add them to the data source in Grafana later on. 

An API account is tied to an operator in Uptrends. Please ensure that the operator has at least the [*View monitor data in group* permission]([LINK_URL_4]) for each of the monitors or monitor groups you wish to display in Grafana.

## Installing the plugin

1. **Download the plugin —** Uptrends Grafana plugin is currently at [version 0.9.274]([LINK_URL_5]). You can download the latest zip file from this [link]([LINK_URL_6]).
2. **Extract the .zip and copy its contents to the Grafana plugin directory —** the default location for the plugin directory is [INLINE_CODE_1]. For more information, refer to the Grafana documentation.
3. **Enable the plugin —** the plugin is currently unsigned, which means that it must be enabled explicitly within the Grafana configuration. To enable the plugin, do the following:

    - On the server that hosts your Grafana instance, locate *grafana.ini* (the default location is [INLINE_CODE_2]) and open the file with your preferred file editor.
    - Under [INLINE_CODE_3] (you may have to scroll down quite far or use a search function), locate key [INLINE_CODE_4]. 
    - Add the value [INLINE_CODE_5] to the command [INLINE_CODE_6].

![Allow unsigned plugin]([LINK_URL_7])

4. **Restart Grafana —** the plugin should now be available for use in the Grafana interface.

## Creating the data source
1. In your Grafana interface, go to _Configuration_ (the gear icon in the left-hand menu) -> _Data sources_.
2. Click _Add data source_.
3. Filter on _Uptrends_ and click on the resulting plugin (it should be called [INLINE_CODE_7]).
4. Enter the APIv4 username and password generated in the first step of this guide, or use an existing set of credentials.
5. Click _Save & test_.

![Creating data source]([LINK_URL_8])

### Create a dashboard

Now that the data source has been set up, it can start pulling data from Uptrends and populating Grafana dashboards with this data.

1. Go to *Dashboards > + New dashboard*, or edit an existing dashboard.
2. Click *Add a new panel*.

![Editing a panel]([LINK_URL_9])

3. Ensure that the correct data source (called [INLINE_CODE_8]) is selected as the panel's **Data source**.
4. Choose a panel type in the top right corner, and fill out any further options as required in the right-hand menu.
5. Choose the data you wish to display.

    \- You can choose between either monitor status data (relating to your monitors' current error/ok status), or monitor statistics (related to monitor performance over time).

    \- You can filter on a specific monitor or monitor group per query you add. The lists of monitors and monitors groups should automatically populate. 

  ![Selecting Uptrends data to display in the panel]([LINK_URL_10])

6. Click *Apply* in the top right corner.

The guide above is a very basic description of getting Uptrends data into Grafana. As a full product, Grafana supports many additional options.
