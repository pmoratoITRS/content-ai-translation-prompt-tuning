{
  "hero": {
    "title": "Alerting system variables"
  },
  "title": "Alerting system variables",
  "summary": "An overview of available system variables, for use in (custom) integrations",
  "url": "/support/kb/alerting/integrations/custom-integrations/alerting-system-variables",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/alerting-system-variables",
  "tableofcontents": false
}

This article contains an overview of all available **System variables**, which can be used to populate the outgoing alert message with relevant information about things like the monitor that caused it, what error occurred, or the alert itself. For more information on how to make use of these system variables, please read our article on [building the right message content]({{< ref path="support/kb/alerting/integrations/custom-integrations/building-the-right-message-content" lang="en" >}}).

In short, to use the variables listed here, they will have to be included in the message content wrapped in double curly brackets. As an example: `{{@alert.alertGuid}}`.

|  Variable   | Description    |  Example value   |
| --- | --- | --- |
| `@account.accountId` | Your Uptrends account id. | `299840` |
| `@alert.alertGuid` | Unique id of this alert. | `cbfc7769-edb2-46a7-89d0-1e1b1fb0815b` |
| `@alert.checkpointName` | Contains the checkpoint's name or location where the alert was last checked. | `Ghent, Belgium` |
| `@alert.description` | Text description of the error that triggered this alert. Will include step number if applicable. | `Step 1: Navigate to https://www.galacticresorts.com failed.` |
| `@alert.downtimeDuration` | The time between the first error and the current (OK) alert timestamp. | `48:03:21` |
| `@alert.errorTypeId` | {{< tableformatter >}} The error type id of the error that triggered this alert, see [Error types]({{< ref path="/support/kb/alerting/errors/error-types" lang="en" >}}) for a list of error types. {{< /tableformatter >}} | `5407` |
| `@alert.failureMessage` | The custom failure message for the specific action in a transaction step that caused the error.  | `Login failed` |
| `@alert.firstError` | The same date and time as @alert.firstErrorUtc, but in the timezone of your account. Also formatted as ISO 8601. | `2018-11-08T10:21:58` |
| `@alert.firstErrorCheckId` | The Id of the error that triggered this alert. | `30833627687` |
| `@alert.firstErrorCheckUrl` | The URL of a deep link that takes you to the details of the error that triggered this alert. | `https://app.uptrends.com/Report/ProbeLog/Check/30833627687` |
| `@alert.firstErrorDescription` | The error description of the first monitor check that received the error. Will include step number if applicable. | `Step 1: Navigate to https://www.galacticresorts.com failed.` |
| `@alert.firstErrorFormatted` | The same date and time as @alert.firstErrorUtc, but in the timezone and culture of your account. | `8/28/2020 12:23 PM` |
| `@alert.firstErrorUtc` | The date and time of the original error that triggered this alert, expressed in UTC time, and formatted as ISO 8601. | `2018-11-08T16:21:58` |
| `@alert.firstErrorUtcFormatted` | The date and time of the original error that triggered this alert, expressed in UTC time, and formatted in the culture of your account. | `8/28/2020 10:23 PM` |
| `@alert.numberOfConsecutiveErrors` | Contains the total number of consecutive errors (confirmed errors) of the alert. | `2` |
| `@alert.resolvedIpAddress` | The ip address that was used to perform the check. Can be either a ipv4 or a ipv6 address. | `178.217.84.4 OR 2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@‌alert.responseHeaders` | {{< tableformatter >}} Contains the response headers of the alert in key-value pairs. Note that the value of this variable can be empty if the [Private location data protection]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) is enabled on a private checkpoint location performing the alert check. {{< /tableformatter >}} | `Content-Type": "text/html` |
| `@alert.responseBody` | {{< tableformatter >}} Contains the response body received when it's available. Note that the response body may contain characters that need to be encoded, e.g. [using @JsonEncode or @XmlEncode]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-formatting" lang="en" >}}). The response body will be truncated when it's larger than 1 MB. {{< /tableformatter >}} | `{"Status": "error"}` |
| `@alert.serverIpv4` | The IPv4 address of the server on which the check was performed. | `178.217.84.4` |
| `@alert.serverIpv6` | The IPv6 address of the server on which the check was performed. | `2a02:2658:103e:4:461:81bb:adbe:82a5` |
| `@alert.sslValidUntil` | Contains the date and time when the SSL certificate is set to expire for SSL monitor alerts. | `2024-11-07T15:05:43` |
| `@alert.timestamp` | The same date and time as @alert.timestampUtc, but in the timezone of your account. Also formatted as ISO 8601. | `2018-11-08T10:26:58` |
| `@alert.timestampFormatted` | The same date and time as @alert.timestampUtc, but in the timezone and culture of your account. | `8/28/2020 12:23 PM` |
| `@alert.timestampUtc` | The date and time of the alert, expressed in UTC time, and formatted as ISO 8601. | `2018-11-08T16:26:58` |
| `@alert.timestampUtcFormatted` | The date and time of the alert, expressed in UTC time, and formatted in the culture of your account. | `8/28/2020 10:23 PM` |
| `@alert.type` | The type of this alert message:<br><br>- Alert: a new error was detected.<br>- Ok: the original error has been resolved.<br>- Reminder: the original error is still ongoing. | `Alert` \| `Ok` \| `Reminder` |
| `@alertDefinition.guid` | The unique id of the alert definition that was used to generate this alert. | `2C97E464-6112-435B-8C8D-6DEF1E18273A` |
| `@alertDefinition.name` | The name of the alert definition that was used to generate this alert. | `Default Alert` |
| `@CustomField(customFieldReference)` | {{< tableformatter >}} A reference to a [custom field]({{< ref path="/support/kb/alerting/integrations/custom-integrations/building-the-right-message-content#including-external-ids-or-custom-data" lang="en" >}}), which can be used to include custom data for individual monitors. {{< /tableformatter >}} | `Alert for Ops team` |
| `@escalationLevel.id` | The id of the escalation level that was used to generate this alert. | `1` |
| `@escalationLevel.message` | The custom message that was specified in the escalation level. | `Please use checklist THX-1138 to investigate this issue.` |
| `@incident.key` | Unique id of the incident this alert belongs to. An error alert and an Ok alert share the same incident key. | `ba8ffcb7-5de0-489e-b649-f00f0b447e80-0-30099055746` |
| `@monitor.dashboardUrl` | The URL of a deep link that takes you to the dashboard for this monitor. | `https://app.uptrends.com/Probe/Dashboard?probeGuids=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.editUrl` | The URL of a deep link that takes you to the settings for this monitor. | `https://app.uptrends.com/Report/Probe?probeGuid=fe1ad4a2-57c1-49db-af16-ff3a6beaa8d4` |
| `@monitor.monitorGuid` | The unique id of the monitor in your account that triggered this alert. | `849b2046-213d-43ad-9efc-5af1faaeb222` |
| `@monitor.name` | The name of the monitor in your account that triggered this alert. | `GalacticResorts.com - DNS` |
| `@monitor.notes` | Any custom notes that were filled in the monitor settings. | `Please check Amazon Route53 DNS entries` |
| `@monitor.type` | Contains the type of the monitor. | `Transaction` |
| `@monitor.url` | The URL or network address this monitor is checking. | `https://galacticresorts.com` |