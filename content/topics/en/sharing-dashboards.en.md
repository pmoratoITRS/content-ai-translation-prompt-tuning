{
  "hero": {
    "title": "Sharing dashboards"
  },
  "title": "Sharing dashboards",
  "summary": "In this article you find instructions on how to share your custom dashboards and data with operators and groups within your Uptrends account.",
  "url": "/support/kb/dashboards-and-reporting/dashboards/sharing-dashboards",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
}

Once you have created a custom dashboard that displays your monitoring data in a way that best suits you, it seems only natural that you might want to share it with your colleagues. In this article, you find instructions on how to do that.

## Sharing a custom dashboard

{{< callout >}}
**Note:** Only members of the *Administrators* operator group can share dashboards. Please [contact support](/contact) if you want to activate dashboard sharing for other operator groups as well.
{{< /callout >}}



To share a custom dashboard:

1.  Open the dashboard you want to share.
2.  Click the {{< AppElement type="iconProperties" >}}{{< /AppElement >}} icon in the quick action menu. The dropdown menu opens.
3.  Select the {{< AppElement type="menuitem" >}} Share {{< /AppElement >}} option.  
    
4.  You will then be prompted to choose how you would like to share your custom dashboard:

    ![screenshot dashboard sharing options](/img/content/scr-dashboard-sharing.min.png)

    **Private** — Only you can view and change the dashboard.

    **Everyone** — All operators can view and change the dashboard.

    **Custom** — Specific operators get rights to the dashboard.
    {{< callout >}}**Tip:** You can also click on the gear icon {{< AppElement type="iconProperties" >}}{{< /AppElement >}} (next to the hamburger icon) to open the dashboard settings, then select the {{< AppElement type="tab" >}} Sharing {{< /AppElement >}} tab.{{< /callout >}} 
5.  If you choose **Custom,** you will see a list of operators (and operator groups) currently given permissions to the dashboard in question. You can edit or delete these existing permissions, or click {{< AppElement type="button" >}}Add permission{{< /AppElement >}} to include another operator or operator group.
6.  When you add a permission, you will be prompted to select the operators or operator groups you’d like to give permissions to.  
    The permissions options are **view only** or **full control**, which allows an operator to view and modify the dashboard.
7. When you are done with all changes, click {{< AppElement type="button" >}} Set {{< /AppElement >}}.
8. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} above the dashboard.

## Exporting data from a custom dashboard 

Another way of sharing information from dashboards is to export (manually or scheduled) the data by download or sending emails. This job can be scheduled. Please see the article [Exporting dashboard data]({{< ref path="support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="en" >}}) to find out the details.

When you use data exports, the information becomes available outside the Uptrends app. That way you e.g. can inform your customers (when scheduled, on a regular basis) without giving them access to the app.
