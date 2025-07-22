{
  "hero": {
    "title": "Missing SLA Overview data"
  },
  "title": "Missing SLA Overview data",
  "summary": "SLA Overview will not display data if the reporting period includes time before the monitors creation.",
  "url": "/support/kb/dashboards-and-reporting/sla/missing-sla-overview-data",
  "translationKey": "https://www.uptrends.com/support/kb/sla/missing-sla-overview-data"
}

You have gone to the trouble of setting up an SLA (Service Level Agreement) monitor or you chose to use the default SLA monitor created when you opened your account, but when you look at the SLA Overview, your data is just a bunch of dashes (e.g., "-") or zeros. Why? Because your reporting options have resulted in invalid data. Rather than show incomplete or invalid data sets, Uptrends shows zeros and dashes.

## The possible scenarios

We have found two common scenarios for the missing SLA Overview data problem: you have included time before the SLA definition or monitor creation date and time, or you have chosen **Monitor groups** for the **Show rows** option in the tile menu.

### You've included time before the SLA definition or monitor creation date and time

When selecting a reporting period, it is important to remember if the SLA definition or monitor was created after the reporting period start date and time, even by just a few seconds, your results for the monitor will appear as either all dashes (newer SLA definition)or result in zeros (newer monitors). Even if you created your SLA Definition January 1, 2016, and it is now December 31, 2016, if you select "This Year" for your reporting period, you do not get data. You don't get any data because there is time on January 1st where the system does not have any data, so the report displays dashes. To get a valid report, use the custom date tool and pick a day and hour after you created the account or SLA definition; e.g., 1/2/2016 to 12/31/2016.

### You've selected "Monitor Groups" in the "Show rows for" option on the tile menu

When you open the three-dot menu {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}} to access the tile settings, you have many options for the data displayed in this tile. If you select **Monitor groups** from the **Show rows for** selection box, you will not get any SLA data. The tile will display the other fields like Total time, Checks, Confirmed errors, Uptime percentage, and Downtime for the monitor groups, but you will not get any values in the SLA fields because SLA data is not data that we can aggregate across monitors. You can show data for specific monitors or monitor groups by selecting them on the Quick Access menu or in the tile settings, but your data will still appear in rows for individual monitors in those groups.
