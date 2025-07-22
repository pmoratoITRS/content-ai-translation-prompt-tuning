{
  "hero": {
    "title": "MonitorGroup API"
  },
  "title": "MonitorGroup API",
  "summary": "The available API methods for manipulating monitor groups.",
  "url": "/support/kb/api/monitorgroup-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorgroup-api"
}

{{< callout >}} **Note:** Effective 27 August 2025, some fields in the **GET and POST /Monitor/MonitorGroup/{monitorGroupGuid}** endpoints will be deprecated. For more information, refer to the [API changelog]({{< ref path="/support/kb/api/changelog" lang="en" >}}).
{{< /callout >}}

This page describes the available API methods for manipulating monitor groups. To learn more, refer to [Uptrends Monitor Group API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/MonitorGroup).

## MonitorGroup object description

The following MonitorGroup object is used in the MonitorGroupAPI endpoints:

| Name               | Description                                                                         | Data type |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| `MonitorGroupGuid` | The unique identifier for the monitor group.                                       | String |
| `Description`      | The name of the monitor group.                                              | String |
| `IsAll`            | {{< tableformatter >}} 
Indicates whether the monitor group is the default [All Monitors]({{< ref path="/support/kb/api/monitorgroup-api#all-monitors-group" lang="en" >}})
 group. {{< /tableformatter >}} | Boolean  |
| `IsQuotaUnlimited` | Indicates whether the number of credits for the monitor group is unlimited or not.  |  Boolean  |
| `UsedBasicMonitorQuota` |{{< tableformatter >}} 
Returns the number of credits used for [Uptime monitors]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="en" >}}). {{< /tableformatter >}} | Integer |
| `UsedBrowserMonitorQuota`            | {{< tableformatter >}} 
Returns the number of credits used for [Browser monitors (Full-Page Check)]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="en" >}}). {{< /tableformatter >}} | Integer |
| `UsedTransactionMonitorQuota`            | {{< tableformatter >}}
Returns the number of credits used for [Transaction monitors]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="en" >}}).  {{< /tableformatter >}} | Integer |
| `UsedApiMonitorQuota`            | {{< tableformatter >}} 
Returns the number of credits used for [Multi-step API (MSA)]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}) and [Postman]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="en" >}}) monitors. {{< /tableformatter >}} | Integer |
| `UsedClassicQuota`            | Returns the number of credits used by existing accounts that are using a single credit pricing tier. | Integer |

### All Monitors group

The **All Monitors** group is a monitor or system group that contains all of your monitors by default. Use the Guid of this group to manage operations that affect all monitors, such as, starting or stopping all monitors or alerts.
Note that you cannot change the membership of this group.


## Monitor group management endpoints

The following API endpoints are available for creating, modifying, and removing monitor groups, as well as the monitors within those groups.

| Request type | Endpoint                                                 | Usage                                                          |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET          | `/MonitorGroup`                                          | Gets all monitor groups                                        |
| POST         | `/MonitorGroup`                                          | Creates a new monitor group                                    |
| GET          | `/MonitorGroup/{monitorGroupGuid}`                       | Gets the details of a monitor group                            |
| PUT          | `/MonitorGroup/{monitorGroupGuid}`                       | Updates an existing monitor group                              |
| DELETE       | `/MonitorGroup/{monitorGroupGuid}`                       | Deletes a monitor group                                        |
| GET          | `/MonitorGroup/{monitorGroupGuid}/Members`               | Gets a list of all monitors that are member of a monitor group |
| POST         | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Adds the specified monitor to the monitor group                |
| DELETE       | `/MonitorGroup/{monitorGroupGuid}/Members/{monitorGuid}` | Removes the specified monitor from the monitor group           |

## Additional monitor group operations

The following API endpoints are available to perform operations on all monitors contained in a group:

| Request type | Endpoint                                                            | Usage                                                                       |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST         | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitors`                  | Stops all monitors in the specified monitor group                           |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitors`                 | Starts all monitors in the specified monitor group                          |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StopAllMonitorAlerts`             | Stops alerting for all monitors in the specified monitor group              |
| POST         | `/MonitorGroup/{monitorGroupGuid}/StartAllMonitorAlerts`            | Starts alerting for all monitors in the specified monitor group             |
| POST         | `/MonitorGroup/{monitorGroupGuid}/AddMaintenancePeriodToAllMembers` | Adds the provided maintenance period to all monitors in the group specified |
