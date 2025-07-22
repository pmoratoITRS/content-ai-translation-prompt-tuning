{
  "hero": {
    "title": "Dashboard and tile filtering"
  },
  "title": "Dashboard and tile filtering",
  "summary": "Show your monitoring data only with selected data by using filters on a dashboard or in individual tiles.",
  "url": "[URL_BASE_TOPICS]dashboards-and-reporting/dashboards/tile-filtering",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

There are two different ways in which you can filter your dashboard data: by individual tile (which enables you to see two similar tiles side-by-side, but with different settings), or applying a filter across the entire dashboard.

## Dashboard filtering

To filter across an entire dashboard, open the dashboard in question and then use the filter options of the Quick Action menu (at the top right of the dashboard).  

![screenshot dashboard filters]([LINK_URL_1])


You will see a variety of filtering options that change based on the dashboard you are on, including:

- **Monitor filtering**  
  This filter comes in handy if you’re looking to only see data for certain monitors. You can select one or more monitor(s) or [monitor group(s)]([LINK_URL_2]).
- **Error level filtering**  
  This filter enables you to display everything, only [unconfirmed/confirmed errors]([LINK_URL_3]), only confirmed errors or only successful checks (OK results).
- **Partial checks filtering**  
  A filter for [concurrent monitoring]([LINK_URL_4]) only which allows you to show or hide partial checks. 
- **Checkpoint filtering**  
  Displays data output filtered by certain [checkpoints]([LINK_URL_5]).
- **Date/Time filtering**  
  Filter by a specified time frame. 

## Tile filtering

To filter within an individual tile:

1. Access the dashboard that contains the tile you wish to filter.
2. On the tile in question open the three-dot menu [SHORTCODE_3][SHORTCODE_4] to access the tile settings.
   A pop-up window will appear, containing a series of tabs and configuration options associated with the tile.
  
    ![screenshot tile settings]([LINK_URL_6])

   It depends on the [tile type]([LINK_URL_7]) which tabs and options are available. These can be (a combination of):

   **Tile**  
   The options contained in the [SHORTCODE_5]Tile[SHORTCODE_6] tab relate only to the way data is presented in that tile.

   **Groups and monitors**  
   The [SHORTCODE_7]Groups and monitors[SHORTCODE_8] tab enables you to display data pertaining to the context of the dashboard (typically the default) or to filter it to show data for any series of monitors or monitor groups. 

   **Checkpoints**  
    Filter data by the checkpoint(s) that carried out the monitoring checks. See the steps for [Checkpoint filtering]([LINK_URL_8]) below for more information.

   **Period**  
   The [SHORTCODE_9]Period[SHORTCODE_10] tab enables you to filter the time frame in which to show data, typically set by default to the context of the dashboard.  
3. Set all filters that you want to apply to the tile.
4. In the tile settings dialog click the [SHORTCODE_11] Set [SHORTCODE_12] button.
5. Important: your changes are not automatically saved. Whenever you make any changes to individual tiles (or the dashboard), be sure to save them using the [SHORTCODE_13]Save[SHORTCODE_14] button at the top right of your dashboard.



[SHORTCODE_1] **Note**: The knowledge base article [Adding a custom report tile]([LINK_URL_9]) explains how to add individual tiles to dashboards. [SHORTCODE_2]  

## Checkpoint filtering for tiles [ANCHOR_1]

Checkpoint filters are available for the [tile types]([LINK_URL_10]):
- Simple data list/chart
- Checkpoint data list/chart
- Multicheckpoint list/chart
- Step duration list/chart
- Monitor log

To apply a checkpoint filter to a tile:

1. Go to the menu [SHORTCODE_15] Dashboards [SHORTCODE_16]. 
2. Select a dashboard. 
3. Open a tile’s three-dot menu [SHORTCODE_17] [SHORTCODE_18] to access the settings. 
4. Go to the [SHORTCODE_19] Checkpoints [SHORTCODE_20] tab. 

   ![screenshot tile's checkpoint selection]([LINK_URL_11]) 

5. Select the checkpoint(s) which you need the tile to display check data from.  
   You can select individual checkpoints, checkpoint regions or countries (within regions).
6. Click the [SHORTCODE_21] Set [SHORTCODE_22] button.
7. Click the [SHORTCODE_23]Save[SHORTCODE_24] button at the top right of your dashboard.
