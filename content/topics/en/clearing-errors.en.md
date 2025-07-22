{
  "hero": {
    "title": "Clearing errors"
  },
  "title": "Clearing Errors",
  "summary": "Find out how to clear the error history of incorrect or unwanted errors",
  "url": "/support/kb/alerting/errors/clearing-errors",
  "translationKey": "https://www.uptrends.com/support/kb/error-analysis/clearing-errors"
}

It is possible to clear individual errors or a group of errors (both unconfirmed and confirmed) which are deemed incorrect or unwanted. Single (or a small number of) errors can be cleared by you. If you have a whole lot of errors to clear, Uptrends will assist you with that, see [Clearing errors in bulk]({{< ref path="#bulk-error-clearance" lang="en" >}}). 

Note that clearing errors does not automatically recalculate the metrics that are based on errors, like service level agreement ([SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="en" >}})) statistics or [public status page]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="en" >}}) numbers. See [Effect on SLAs and public status page data]({{< ref path="#effect-sla-psp-data" lang="en" >}}) on how to deal with recalculating statistics depending on whether you cleared the errors yourself or requested that from Support.

{{< callout >}}
**Note**: Unfortunately it is impossible to recalculate SLAs for data older than 90 days, as that data is not retained past this time period.
{{< /callout >}}

## How to clear individual errors {id="clear-individual-errors"}

To clear an error in your account: 
1. Go to the menu {{< AppElement type="menuitem" >}}Monitoring > Monitor log{{< /AppElement >}}.
2. Click on the error that you wish to clear. The *Check details* related to this error will appear.
3. At the bottom of the pop-up click the {{< AppElement type="editbutton" >}} Clear error {{< /AppElement >}} button.
4. Confirm the action with the {{< AppElement type="editbutton" >}} Clear {{< /AppElement >}} button. 

The error will be changed to an OK result, which is immediately visible in the *Monitor log* dashboard. 

The corresponding uptime percentage data will be changed as well. Due to caching, the changes may take some time to become visible.

## Clearing errors in bulk {id="bulk-error-clearance"}

Sometimes you may want to clear errors for a specific time range (for example, several days of downtime). Rather than clearing each error out individually, we advise that you do the following:

1. If you happen to have some monitoring *Check details* open, click the {{< AppElement type="editbutton" >}} Clear multiple errors {{< /AppElement >}} button at the bottom of the pop-up. The *Clear errors request* form will appear. 
2. Alternatively, navigate to {{< AppElement type="menuitem" >}} Support {{< /AppElement >}} and click the {{< AppElement type="buttonPrimary" >}}  Request to clear errors {{< /AppElement >}} option. The *Clear errors request* form will appear. 
3. Fill in the mandatory information, which are the monitor(s) and date range. Add any optional information relevant to your request, like a status code. 
4. Click the {{< AppElement type="buttonPrimary" >}} Send {{< /AppElement >}} button.

When you send your request, a ticket will be automatically created and your request will be processed. This may take a while, but you will be updated by the ticket system once the clearing of errors and the SLA data recalculation is completed. 

## Effect on SLAs (service level agreements) and public status page data {id="effect-sla-psp-data"}

Clearing errors does not automatically change existing [SLA]({{< ref path="/support/kb/dashboards-and-reporting/sla" lang="en" >}}) data, including [public status page]({{< ref path="/support/kb/dashboards-and-reporting/status-pages" lang="en" >}}) data, which is also calculated SLA data. 

However, it is possible to recalculate it. When you requested [clearing multiple errors]({{< ref path="#bulk-error-clearance" lang="en" >}}) by the Support team, the recalculation of data is included in the process. You don't have to request this separately. 

This is different when you have cleared errors yourself. In that case, please contact Support through a [support ticket]({{< ref path="contact" lang="en" >}}), and express what you would like to do. 
