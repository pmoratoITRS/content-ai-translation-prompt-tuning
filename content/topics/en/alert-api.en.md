{
  "hero": {
    "title": "Alert API"
  },
  "title": "Alert API",
  "summary": "Get started with Alert API to retrieve and work with the alerting information in your Uptrends account.",
  "url": "/support/kb/api/alert-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/alert-api",
  "sectionlist": true,
  "tableofcontents": true
}

The [Alert API](https://api.uptrends.com/v4/swagger/index.html?url=/v4/swagger/v1/swagger.json#/Alert/Alert_GetMonitorAlerts) contains endpoints that provide alert information from a specific monitor or monitor groups.

## Alert parameters

The following parameters are available in the Alert API:

| Name | Description |
|--|--|
| `monitorGuid` | The unique identifier of the monitor. |
| `monitorGroupGuid` | The unique identifier of the monitor group. |
| `IncludeReminders` | A boolean set to **false** by default. If set to **true**, this parameter includes the reminder alerts in the API response. |
| `Cursor`| {{< tableformatter >}}  A string (query) value used for traversing the dataset. For more detailed explanation, refer to [Cursor]({{< ref path="/support/kb/api/alert-api#cursor" lang="en" >}}). {{< /tableformatter >}}|
| `Sorting`| A string that sorts the alerts in **Ascending** or **Descending** order. |
| `Take`| An integer ranging from **0** to **100**, indicating the number of alert records returned. |
| `Start`| A custom date parameter (YYYY-mm-dd) used with the `End` parameter to specify the start date for the returned alert records. This parameter cannot be used along with the PresetPeriod. |
| `End`| A custom date parameter (YYYY-mm-dd) used with the `Start` parameter to specify the end date for the returned alert records. This parameter cannot be used along with the PresetPeriod. |
| `PresetPeriod`| {{< tableformatter >}} A list of time duration to filter alerts within a specific period. This cannot be used along with the `Start` and `End` parameters. For more detailed explanation, refer to [PresetPeriod]({{< ref path="/support/kb/api/alert-api#presetperiod" lang="en" >}}).  {{< /tableformatter >}}|

### Cursor

The Cursor parameter acts as a pointer that lets you traverse the alert data set. It serves as an identifier of which alert records were generated and which alert record to go to next.

For example, you have a total of 300 monitor alerts, and you want to retrieve alerts from 101-200. As the Alert API allows you to retrieve a maximum of 100 alert records per batch, calling the first batch from the API response generates the **Cursors** JSON object with the **Next** and **Self** values:

```json
{
  ...

  "Cursors": {
    "Next": "qKLVZ/HGD2XeFkiwNFWJK+nRDuOjjBRipct8qOfRjRmGUG8F5P1WzrQ4p3JFfXoErs96xb+DS0SAPW+XDUi9Zw/zdo4uHXL3TYBhodxfQQul3L4mwDk=",
    "Self": "KYhsR26Se8cQbeQm+o3LXawJXu3Pe6NvSefBcMivZ5QA+rFcRUrHTErK+TrhrUN3Ss8QUing/+jUkjgl3QOvB3kf3AZ+EOubhya5s3CWF+HGWEQkQQ=="
  },
  ...
}

```

For this example, use the **Next** value to retrieve alerts from the 101st alert and onwards. Use the **Self** value as the cursor to retrieve the first batch of alerts from 1 to 100.

{{< callout >}} **Note:** The **Cursor** is generated per batch and not per alert record. If you retrieve the first batch of alerts without any succeeding alert records left, no **Cursor** will be generated. If more data is available, a **Cursor** will be created for that specific batch. Use the **Take** parameter to specify the batch size, ranging from 1 to 100 alert records. {{< /callout >}}

### PresetPeriod

The following options are available to easily filter alerts within a specific duration:

- CurrentDay, CurrentWeek, CurrentMonth, CurrentQuarter, CurrentYear
- Previous Day, Previous Week, Previous Month, Previous Quarter, Previous Year
- Last2Hours, Last6Hours, Last12Hours, Last24Hours, Last48Hours
- Last7Days, Last30Days, Last60Days, Last90Days, Last365Days
- Last3Months, Last6Months, Last12Months, Last24Months

Note that the included period for the previous time, last hours, last days, and last months are only applied when the full-time duration is completed.

If you specify a **PresetPeriod** of **Last7Days** and generate alert records on a Monday at 8:00 AM, you'll get the results from Sunday to Sunday, which covers the last seven completed days. Note that the time (Monday) you generated the report was not included because the time hadn't yet elapsed the whole day.

Similarly, if you specify a **PresetPeriod** of **Last12Months** and generated records on 25 January 2025, you'll get the results from 31 December 2024 and the 11 months before. The alerts from January 2024 and January 2025 will not be included in the report because the month range of January has not yet been completed.

## Alert endpoints

The following API methods are available:

### GET /Alert/Monitor/{monitorGuid}

This method returns alert information for a specific monitor.

```json
{
      "Type": "Alert",
      "Id": "cd73d946-8577-44f7-b7ed-134ae2c0985e",
      "Attributes": {
        "AlertType": "Reminder",
        "MonitorGuid": "a591a38a-16e0-4dd2-9f15-d575b4c5a433",
        "Timestamp": "2025-01-02T05:39:21",
        "FirstError": "2024-12-11T20:11:01",
        "MonitorCheckId": 171204791912,
        "FirstErrorMonitorCheckId": 169412140540,
        "ErrorDescription": "Step 4 (https://galacticshirts.com): Element '.wn-product-btn' not found.",
        "IncidentKey": "9632cd34-0c13-4e2c-92cc-cca104432cd9-0-169412140545"
      },
      "Relationships": [
        {
          "Id": 171204791912,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/171204791912"
          }
        },
        {
          "Id": 169412140540,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/169412140540"
          }
        }
      ],
      ....
}
```

### GET /Alert/MonitorGroup/{monitorGroupGuid}

This method returns alert information for a specific monitor group.

```json
{
  "Data": [
    {
      "Type": "Alert",
      "Id": "afd846be-ddbf-49e1-ad15-2eee5f6d7544",
      "Attributes": {
        "AlertType": "Error",
        "MonitorGuid": "a591a38a-16e0-4dd2-9f15-d575b4c5a433",
        "Timestamp": "2025-01-02T02:30:46",
        "FirstError": "2024-12-11T20:11:01",
        "MonitorCheckId": 171193848695,
        "FirstErrorMonitorCheckId": 169412140540,
        "ErrorDescription": "Step 4 (https://galacticshirts.com): Element '.wn-product-btn' not found.",
        "IncidentKey": "9632cd34-0c13-4e2c-92cc-cca104432cd9-0-169412140545"
      },
      "Relationships": [
        {
          "Id": 171193848695,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/171193848695"
          }
        },
        {
          "Id": 169412140540,
          "Type": "MonitorCheck",
          "Links": {
            "Self": "/MonitorCheck/169412140540"
          }
        }
      ]
    },
    .....
  ]
}
