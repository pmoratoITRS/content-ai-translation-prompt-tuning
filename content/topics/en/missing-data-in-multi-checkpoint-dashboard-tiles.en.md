{
  "hero": {
    "title": "Missing data in Multi-checkpoint dashboard tiles"
  },
  "title": "Missing data in Multi-checkpoint dashboard tiles",
  "summary": "Learn why some times you will have no data or incomplete data in your Multi-checkpoint dashboard tiles",
  "url": "/support/kb/dashboards-and-reporting/dashboards/missing-data-in-multi-checkpoint-dashboard-tiles",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/missing-data-in-multi-checkpoint-dashboard-tiles"
}

Our Multi-Checkpoint data lists and charts show selected metrics based on the checkpoints that conducted the tests. These data tiles are wonderful for identifying latency and other regionalized issues. Occasionally we get a question about missing or incomplete data in these tiles. There are a couple of different causes for these problems.

## Dashboard and monitor checkpoint selections are in conflict

When you set up your monitor, you selected which checkpoints you wanted to be used for the monitor; also, at the top of each dashboard, you have the opportunity to select which checkpoints are used for calculating data for the dashboard. If the checkpoints selected for the monitor or monitors are not included in the dashboard checkpoint selection, you will either get no data or incomplete data sets. Adjust the dashboard checkpoints to include the monitor(s) selected for the tile. If this is not the case, you may have too many checkpoints selected for the tile (keep reading).

{{< callout >}}
**Note**: You also will not see data in the Multi-checkpoint List for any checkpoints used by the monitor that you have not included in the dashboard.
{{< /callout >}}

## To many dashboard checkpoints selected when using the multi-checkpoint chart.

The default for the dashboard is to show data for all checkpoints, but the Multi-checkpoint Chart tile can only show ten checkpoints at a time. If you leave the dashboard at the default or have a large number of checkpoints selected and your monitor only uses a few, you may not see any data, or you will only see data for some checkpoints. The tile takes the first ten checkpoints based on the dashboard's checkpoint selection and shows the data for those checkpoints. If there is no data for the first 10 checkpoints, you will see the message, "There is no data available." If by chance one or more checkpoints selected for your monitor fall into the first 10 checkpoints selected for the dashboard, you will see data for those checkpoints along with the other checkpoints in the first ten—even if there is no data for them. To see all of the data in this tile, you must adjust the dashboard checkpoint selection to reflect the checkpoints used by the monitor (up to ten checkpoints).
