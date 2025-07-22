{
  "hero": {
    "title": "Working with SLA data and reports"
  },
  "title": "Working with SLA data and reports",
  "summary": "Learn how to read and manage your SLA data. ",
  "url": "/support/kb/dashboards-and-reporting/sla/working-with-sla-data-and-reports",
  "translationKey": "https://www.uptrends.com/support/kb/sla/working-with-sla-data-and-reports"
}

Uptrends comes with a default **SLA overview** dashboard that can be accessed from the menu {{< AppElement type="menuitem" >}} Dashboards > Synthetics > SLA overview {{< /AppElement >}}. If you have created [custom SLA overview dashboards]({{< ref path="support/kb/dashboards-and-reporting/sla/working-with-multiple-SLA-definitions#custom-sla-overview-dashboard" lang="en" >}}) those are located under {{< AppElement type="menuitem" >}} Dashboards > Customized dashboards {{< /AppElement >}}. 

Your overview dashboard is your place to check your SLA compliance, download PDFs and Excel files of your SLA data, and schedule regular SLA reports.

## The SLA overview

By default, the **SLA overview** shows you your SLA targets and actual values in column pairs based on the period chosen in the Quick Access menu.

- **SLA target uptime and SLA uptime** – Your SLA target uptime percentage is your defined uptime goal, and the SLA uptime is the actual uptime percentage taking into account any excluded days or times you've set up in your SLA definition.
- **SLA target total time and SLA total time** – Your SLA target total time is the maximum amount of time in seconds that a page can take to load and remain in SLA compliance, and the SLA total time is the actual average load times for the period in seconds.
- **SLA operator response time target and SLA operator response time** — The SLA operator response time target is the maximum amount of time allowed for an operator to confirm an issue in Uptrends, and SLA operator response time is the actual amount of time taken.
- **Confirmed errors** – The number of verified errors recorded for the period.
- **Downtime** – The sum of all downtime for the period displayed in seconds.
- **Downtime percentage** - all downtime for the period shown as a percentage.

{{< callout >}}
**Note:** If you see dashes and zeros instead of data in your **SLA overview** report, your tile/dashboard settings have caused a conflict in the data resulting in invalid data. [Learn more]({{< ref path="support/kb/dashboards-and-reporting/sla/missing-sla-overview-data" lang="en" >}}).
{{< /callout >}}

## Recalculating SLA Data

We all forget from time to time to set maintenance windows and set up temporary exclusions in our SLA definitions. These things can really mess up your SLA reports, but you’re not completely stuck with the bad data.

### Same day

If you notice your mistake right away, you can [clear the errors]({{< ref path="support/kb/alerting/errors/clearing-errors#clear-individual-errors" lang="en" >}}) in your monitor logs.

### Past days (up to 90)

Clearing errors for SLA reporting from yesterday and every day before is a bit more complicated. Uptrends stores SLA data separately from your regular monitoring data. At the end of each day, your SLA data is extracted, so clearing errors in your monitor logs from yesterday won’t do a thing for your SLA reports. 

However, you can get help from Uptrends to fix this problem. Follow the steps in [Clearing errors in bulk]({{< ref path="support/kb/alerting/errors/clearing-errors#bulk-error-clearance" lang="en" >}}) to fill out a request form with the necessary info. Based on the info a ticket will be created in Uptrends' ticket system. Just remember that it may take a while to clear the errors and recalculate the SLA data. You will be updated by the ticket system once the process has been completed. 

## Download or share SLA overview reports

You have multiple ways to download SLA report data as a file or share your SLA overview data by sending emails.

### Downloading

You can download the contents of your SLA overview dashboard in PDF and Excel format at any time.

From your default or custom **SLA overview** dashboard:

1.  Set the date parameters and monitors for the download on the Quick Access menu.
2.  Click the hamburger icon {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
3.  In the menu click either {{< AppElement type="menuitem" >}}PDF export{{< /AppElement >}} or {{< AppElement type="menuitem" >}}Excel export{{< /AppElement >}}.
4.  Wait for Uptrends to generate the report (this could take a while if you have a lot of data) and locate the file in your downloads folder.

### Sending a one-off email

You can send data from your SLA dashboards via email and choose between data in PDF, Excel, or HTML format. 

1. Open the SLA dashboard for which you want to send out data.
2. Click the hamburger icon {{< AppElement type="iconFeather" >}}{{< /AppElement >}} and click {{< AppElement type="menuitem" >}}Send as email{{< /AppElement >}}.
3. Fill in the email addresses of the recipients, choose the type of file and add notes, if desired.
4. Click the {{< AppElement type="button" >}} Send report {{< /AppElement >}} button.

### Sending recurring emails by scheduling reports {id="scheduling-reports"}

You can set up regularly scheduled reports emailed to yourself and other operators on your account with **Report Definitions**. Your report will go out to your recipient list from your **SLA overview** dashboard (default or custom):

1.  Click the hamburger icon {{< AppElement type="iconFeather" >}}{{< /AppElement >}}.
2.  Click {{< AppElement type="menuitem" >}}Schedule Report{{< /AppElement >}} to open the scheduled report definition.
3.  Complete the fields on both the {{< AppElement type="tab" >}}Main{{< /AppElement >}} and {{< AppElement type="tab" >}}Recipients{{< /AppElement >}} tabs.
4.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.
5.  Manage your scheduled report definitions by going to the {{< AppElement type="menuitem" >}} Account setup > Scheduled reports {{< /AppElement >}} menu.
