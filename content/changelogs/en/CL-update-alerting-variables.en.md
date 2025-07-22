{
  "title": "Introducing new alerting variables",
  "date": "2025-02-19",
  "url": "/changelog/february-2025-alert-variable-updates",
  "translationKey": "https://www.uptrends.com/changelog/february-2025-alert-variable-updates"
}

The following alerting variables are now available for use:

- **@alert.numberOfConsecutiveErrors** — contains the total number of consecutive errors (confirmed errors) of the alert. This returns `2` when the API response is  `{"numberOfConsecutiveErrors": "2"}`.
- **@alert.checkpointName** — contains the checkpoint's name or location where the alert was last checked. This returns `Ghent, Belgium` when the API response is  `{"checkpointName": "Ghent, Belgium"}`.
- **@‌alert.responseHeaders** — contains the response headers of the alert in key-value pairs. For example, this returns `{"Content-Type": "text/html"}` from the API response header, similar to how the values are returned for `@alert.responseBody`.

Note that the value of the `@‌alert.responseHeaders` can be empty if the [Private location data protection]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) is enabled on a private checkpoint location performing the alert check. For more information, see [Alerting system variables]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="en" >}}).