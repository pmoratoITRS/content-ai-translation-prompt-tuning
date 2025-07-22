{
  "hero": {
    "title": "Dashboard and tile filtering"
  },
  "title": "Dashboard and tile filtering",
  "summary": "Show your monitoring data only with selected data by using filters on a dashboard or in individual tiles.",
  "url": "/support/kb/dashboards-and-reporting/dashboards/tile-filtering",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/tile-filtering"
}

There are two different ways in which you can filter your dashboard data: by individual tile (which enables you to see two similar tiles side-by-side, but with different settings), or applying a filter across the entire dashboard.

## Dashboard filtering

To filter across an entire dashboard, open the dashboard in question and then use the filter options of the Quick Action menu (at the top right of the dashboard).  

![screenshot dashboard filters](/img/content/scr_dashboard-filters.min.png)


You will see a variety of filtering options that change based on the dashboard you are on, including:

- **Monitor filtering**  
  This filter comes in handy if you’re looking to only see data for certain monitors. You can select one or more monitor(s) or [monitor group(s)]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="en" >}}).
- **Error level filtering**  
  This filter enables you to display everything, only [unconfirmed/confirmed errors]({{< ref path="support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}}), only confirmed errors or only successful checks (OK results).
- **Partial checks filtering**  
  A filter for [concurrent monitoring]({{< ref path="support/kb/synthetic-monitoring/concurrent-monitoring" lang="en" >}}) only which allows you to show or hide partial checks. 
- **Checkpoint filtering**  
  Displays data output filtered by certain [checkpoints]({{< ref path="#checkpoint-filtering" lang="en" >}}).
- **Date/Time filtering**  
  Filter by a specified time frame. 

## Tile filtering

To filter within an individual tile:

1. Access the dashboard that contains the tile you wish to filter.
2. On the tile in question open the three-dot menu {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} to access the tile settings.
   A pop-up window will appear, containing a series of tabs and configuration options associated with the tile.
  
    ![screenshot tile settings](/img/content/scr_tile-settings.min.png)

   It depends on the [tile type]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="en" >}}) which tabs and options are available. These can be (a combination of):

   **Tile**  
   The options contained in the {{< AppElement type="tab" >}}Tile{{< /AppElement >}} tab relate only to the way data is presented in that tile.

   **Groups and monitors**  
   The {{< AppElement type="tab" >}}Groups and monitors{{< /AppElement >}} tab enables you to display data pertaining to the context of the dashboard (typically the default) or to filter it to show data for any series of monitors or monitor groups. 

   **Checkpoints**  
    Filter data by the checkpoint(s) that carried out the monitoring checks. See the steps for [Checkpoint filtering]({{< ref path="#checkpoint-filtering-tiles" lang="en" >}}) below for more information.

   **Period**  
   The {{< AppElement type="tab" >}}Period{{< /AppElement >}} tab enables you to filter the time frame in which to show data, typically set by default to the context of the dashboard.  
3. Set all filters that you want to apply to the tile.
4. In the tile settings dialog click the {{< AppElement type="button" >}} Set {{< /AppElement >}} button.
5. Important: your changes are not automatically saved. Whenever you make any changes to individual tiles (or the dashboard), be sure to save them using the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button at the top right of your dashboard.



{{< callout >}} **Note**: The knowledge base article [Adding a custom report tile]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/custom-report-tiles-add" lang="en" >}}) explains how to add individual tiles to dashboards. {{< /callout >}}  

## Checkpoint filtering for tiles {id="checkpoint-filtering-tiles"}

Checkpoint filters are available for the [tile types]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="en" >}}):
- Simple data list/chart
- Checkpoint data list/chart
- Multicheckpoint list/chart
- Step duration list/chart
- Monitor log

To apply a checkpoint filter to a tile:

1. Go to the menu {{< AppElement type="menuitem" >}} Dashboards {{< /AppElement >}}. 
2. Select a dashboard. 
3. Open a tile’s three-dot menu {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} to access the settings. 
4. Go to the {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} tab. 

   ![screenshot tile's checkpoint selection](/img/content/scr-cp-selection-tiles.min.png) 

5. Select the checkpoint(s) which you need the tile to display check data from.  
   You can select individual checkpoints, checkpoint regions or countries (within regions).
6. Click the {{< AppElement type="button" >}} Set {{< /AppElement >}} button.
7. Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button at the top right of your dashboard.
