{
  "hero": {
    "title": "Custom report tiles"
  },
  "title": "Custom report tiles",
  "summary": "Show your monitoring data as list or chart on custom dashboards by using custom report tiles.",
  "url": "/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles"
}

Uptrends offers a wide variety of report tiles suitable for all your monitoring needs. These report tiles conveniently show the metrics of your monitors, checkpoints, and error status through diagrams. As part of your [dashboard settings]({{< ref path="/support/kb/dashboards-and-reporting/dashboards" lang="en" >}}), these tiles include different types, ranging from a tabular list of information, line graphs, bar graphs, and pie charts.

To start, [add a report tile]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="en" >}}) to your default Uptrends dashboards or create your setup from scratch. Once added, click the {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} icon to access the tile settings and customize the configuration.

This knowledge base article walks you through the different report tile types and their settings.

## Simple data list or chart {id="simple-data-list-chart"}

This report tile type allows you to select monitors or monitor groups to display metrics from the **General**, **Core Web Vitals**, and **W3C navigation** options. These metrics may vary depending on the monitor type and other configuration settings. For more information, refer to [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}) and [W3C navigation]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}})


For Transaction monitors, ensure that you’ve enabled the [Performance metrics]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#step-settings" lang="en" >}}) in the **Waterfall** settings of your transaction step settings. Expect that the period before this change will not reflect any **Core Web Vitals** and **W3C navigation metrics** data. You can adjust the report period in the tile settings to only show the range from which the metrics were enabled.

Once configured, the Simple data list or chart will show a graph corresponding to the metrics. Check the legend and hover over the graph for more information about the steps. To learn more about related metrics, refer to the [Calculation of uptime and downtime]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/calculation-of-uptime-and-downtime" lang="en" >}}) knowledge base article.

![Simple data list or chart metrics](/img/content/scr-data-metrics.min.png)  


### General

Select any of the following metrics to reflect the data in the report tile:

- Total, resolve, connection, and download times
- Uptime percentage, downtime percentage, uptime, and downtime
- Confirmed and unconfirmed errors
- Checks, alerts, and total bytes
- SLA target uptime percentage, SLA target total time, SLA operator response target, and operator response time

![Simple data chart General metrics](/img/content/scr_simple-data-chart.min.png)  

### Core Web Vitals

The FPC and Transaction monitors both collect data from the [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}).

Select any of the following metrics to reflect the data in the report tile:

 - First contentful paint
 - Largest contentful paint
 - Time to interactive
 - Total blocking time
 - Cumulative layout shift

![Simple data chart Core Web Vitals metrics](/img/content/scr_simple-data-chart-steps.min.png)  


### W3C navigation

The FPC and Transaction monitors both collect data from the [W3C navigation]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}}) and [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}).

Select any of the following metrics to reflect the data in the report tile:
  - Request start
  - Time to first byte
  - DOM interactive
  - DOM completed
  - Load event

![Simple data list W3C navigation metrics](/img/content/scr_simple-data-list.min.png)  


## Monitor data list or chart  

Select monitors or monitor groups, period, and then choose to display the following:

- SLA uptime percentage, SLA target uptime percentage
- SLA total time, SLA target total time, SLA downtime
- SLA operator response time, SLA operator response target
- Total time, Checks, Confirmed errors, Unconfirmed errors
- Uptime percentage, Downtime percentage
- Sort by and Show row for options
  
![screenshot monitor data chart tile](/img/content/scr_monitor-data-chart.min.png)  
  
![screenshot monitor data list tile](/img/content/scr_monitor-data-list.min.png)  

## Error type list or chart  

Select monitors or monitor groups, and period options.  
  
![screenshot error type list and chart](/img/content/scr_error-type-list-chart.min.png)  

## Checkpoint data list or chart  

Select monitors or monitor groups, period, and then choose to display: 

- Total time, Resolve time
- Connection time, Download time
- Checks, Confirmed errors, and Sort by options 
  
![screenshot checkpoint data chart tile](/img/content/scr_checkpoint-data-chart.min.png)

![screenshot checkpoint data list tile](/img/content/scr_checkpoint-data-list.min.png)  

## Multi-checkpoint list or chart  

Select monitors or monitor groups, period, and then choose which metric to display throughout the list or chart.  
  

![screenshot multi-checkpoint chart tile](/img/content/scr_multi-checkpoint-chart-tile.min.png) 
  
![screenshot multi-checkpoint list tile](/img/content/scr_multi-checkpoint-list-tile.min.png) 

## Multi-monitor list or chart  

Select monitors or monitor groups, period, and then select the metric that you would like to display via the list or chart.  
  
![screenshot multi-monitor chart tile](/img/content/scr_multi-monitor-chart-tile.min.png)  

![screenshot multi-monitor list tile](/img/content/scr_multi-monitor-list-tile.min.png)

## Last check details {id="last-check-details"}

Display when a monitor or monitor groups were last checked, and select the period in which to display data.  
![screenshot custom report tiles monitor check details](/img/content/scr_custom-report-tiles-lastcheck.min.png)

## Monitor log  

Select monitors or monitor groups, period, and then select how to filter errors, and whether to show the report in an exported file.  
  
![screenshot monitor log tile](/img/content/scr_monitor-log-tile.min.png) 

## Alert history 

Display the history of alert notifications on a by-monitor or monitor group basis, and filter data by period. 

![screenshot alert history tile](/img/content/scr_alert-history-tile.min.png)

## Step duration list or chart  

For transaction and Multi-step API monitors and one monitor at a time only. Shows the duration of steps over time.
  
![screenshot step duration chart tile](/img/content/scr_step-duration-chart-tile.min.png)  

## Average step duration list or chart  

For transaction and Multi-step API monitors and one monitor at a time only. Shows the average duration of steps.
  
![screenshot average step duration chart tile](/img/content/scr_average-step-duration-chart-tile.min.png)  

## Custom metrics list or chart

This report tile lets you select [Custom metric variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#custom-metric-variables" lang="en" >}}) and displays their trends over time.

The **Custom metrics chart** displays the metric variable as a line graph. Hovering your mouse in the chart shows the metric's minimum, average, and maximum values as data points:

![Custom metrics chart](/img/content/scr-custom-metric-min-max-values.min.png)

The **Custom metrics list** displays the metric variable as a table. The list shows the **Date/time** when the metric was retrieved and its numerical values:

![Custom metrics list](/img/content/scr-msa-custom-metrics-list.min.png)

Note that you can select multiple custom metric variables to compare values in a list or chart.
