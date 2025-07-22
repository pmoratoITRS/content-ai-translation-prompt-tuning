{
  "hero": {
    "title": "Working with multiple SLA definitions"
  },
  "title": "Working with multiple SLA definitions",
  "summary": "You can monitor multiple SLAs using SLA definitions and custom dashboards.",
  "url": "/support/kb/dashboards-and-reporting/sla/working-with-multiple-SLA-definitions",
  "translationKey": "https://www.uptrends.com/support/kb/sla/working-with-multiple-SLA-definitions"
}

One SLA definition is enough for most Uptrends users, but some companies maintain or monitor multiple SLAs with different minimum percentages, page load times, or operator response times. To learn how to set up additional SLA definitions or modify the default SLA definition, visit the [Setting up an SLA]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="en" >}}) article. If you have your SLA definitions set up and you want to learn how to use multiple SLA definitions within your Uptrends account, you’re in the right place.

Uptrends calculates the SLA numbers/compliance for each SLA definition for each monitor in your account. There's no need to link certain monitors to certain SLA definitions, for you can view data for any monitors or monitor groups with any SLA definition applied. You can work within the default SLA Overview dashboard switching between definitions and monitors or monitor groups, or you can create custom SLA Overview dashboards for specific monitors or monitor groups and SLA definitions.

{{< callout >}}
**Note:** If you see dashes and zeros instead of data in your SLA Overview report, your tile/dashboard settings have caused a conflict in the data resulting in invalid data. The knowledge base article [Missing SLA overview data]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="en" >}}) has more information on this kind of conflict.
{{< /callout >}}

## Switching between SLA definitions in the SLA overview dashboard

Once you have created additional SLA definitions, you can choose which to view in your **SLA overview** dashboard. To switch between SLA definitions:

1. Go to the menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics: SLA overview {{< /AppElement >}}.
2. Open the tile's three-dot menu {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} to access the tile settings.
3. Choose an SLA definition from the list in **SLA based on**.
5. Click {{< AppElement type="button" >}}Set{{< /AppElement >}}.

Your tile refreshes based on the changed SLA definition. If the SLA definition is new, you will most likely see dashes (-) instead of data. Uptrends calculates and stores the SLA data in real time after the creation of the definition. Since the SLA definition is new, the system does not have a complete dataset based on this new definition and the date/time settings, so the report displays a dash rather than display percentages based on an incomplete data set. Learn more by reading the knowledge base article [Missing SLA overview data]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="en" >}}).

## Customized SLA overview dashboards {id="custom-sla-overview-dashboard"}

When working with multiple SLA definitions, you can create separate tiles based on different combinations of SLA definitions and monitors in a custom dashboard or create different custom dashboards based on different combinations of SLA definition and monitors or monitor groups.

To make a custom SLA dashboard, you need to start with creating a custom dashboard or save a copy of the **SLA overview** dashboard for customization.

### Create a customized SLA overview dashboard

1. Go to the menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics: SLA overview {{< /AppElement >}}.
2. Open the tile's three-dot menu {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} to access the settings.
3. (Optional) If using multiple definitions, change the SLA definition in **SLA based on**.
4. Click the {{< AppElement type="tab" >}}Groups and monitors{{< /AppElement >}} tab.
5. Uncheck **Use dashboard's context** (if checked) and select the monitor(s) or group(s) to include for the custom dashboard.
6. Click {{< AppElement type="button" >}}Set{{< /AppElement >}}.
7. Click the hamburger icon {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
8. Select {{< AppElement type="savebutton" >}}Save as{{< /AppElement >}}.
9. Give the new dashboard a descriptive name.
10. Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.

You now have a custom dashboard you can access from the {{< AppElement type="menuitem" >}}Dashboards > Custom dashboards{{< /AppElement >}} menu.  
  
### Create additional SLA tiles

Instead of creating multiple dashboards, you can also create a multi-view dashboard with tiles based on different combinations of SLA definitions, monitors, or monitor groups. Start by creating a copy of the Default SLA dashboard for your customization (see instructions above starting at step 7). To add tiles:

1. Open your custom dashboard by going to the menu {{< AppElement type="menuitem" >}}Dashboards > Custom dashboards {{< /AppElement >}} and selecting your dashboard.
2. Click the hamburger icon {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
3. Select *Add tile*.
4. Select **Monitor data list** from tile types.
5. Click {{< AppElement type="button" >}}Next{{< /AppElement >}}.
6. Select the monitor(s) or monitor group(s) you want to use for this tile.
7. Click {{< AppElement type="button" >}}Finish{{< /AppElement >}} and the new tile is created.
8. Open the tile's three-dot menu {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} to access the tile settings.
9. Select an SLA definition from the list in **SLA based on**.
10. Check the boxes for the values you would like displayed.
11. Adjust any other settings you would like.
12. Click {{< AppElement type="button" >}}Set{{< /AppElement >}}.
13. Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} on the *Quick Access* menu.

Add all the tiles you need.
