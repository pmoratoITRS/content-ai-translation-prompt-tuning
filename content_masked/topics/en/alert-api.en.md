{
  "hero": {
    "title": "Alert API"
  },
  "title": "Alert API",
  "summary": "Get started with Alert API to retrieve and work with the alerting information in your Uptrends account.",
  "url": "[URL_BASE_TOPICS]api/alert-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": true,
  "tableofcontents": true
}

The [Alert API]([LINK_URL_1]) contains endpoints that provide alert information from a specific monitor or monitor groups.

## Alert parameters

The following parameters are available in the Alert API:

| Name | Description |
|--|--|
| [INLINE_CODE_1] | The unique identifier of the monitor. |
| [INLINE_CODE_2] | The unique identifier of the monitor group. |
| [INLINE_CODE_3] | A boolean set to **false** by default. If set to **true**, this parameter includes the reminder alerts in the API response. |
| [INLINE_CODE_4]| [SHORTCODE_1]  A string (query) value used for traversing the dataset. For more detailed explanation, refer to [Cursor]([LINK_URL_2]). [SHORTCODE_2]|
| [INLINE_CODE_5]| A string that sorts the alerts in **Ascending** or **Descending** order. |
| [INLINE_CODE_6]| An integer ranging from **0** to **100**, indicating the number of alert records returned. |
| [INLINE_CODE_7]| A custom date parameter (YYYY-mm-dd) used with the [INLINE_CODE_8] parameter to specify the start date for the returned alert records. This parameter cannot be used along with the PresetPeriod. |
| [INLINE_CODE_9]| A custom date parameter (YYYY-mm-dd) used with the [INLINE_CODE_10] parameter to specify the end date for the returned alert records. This parameter cannot be used along with the PresetPeriod. |
| [INLINE_CODE_11]| [SHORTCODE_3] A list of time duration to filter alerts within a specific period. This cannot be used along with the [INLINE_CODE_12] and [INLINE_CODE_13] parameters. For more detailed explanation, refer to [PresetPeriod]([LINK_URL_3]).  [SHORTCODE_4]|

### Cursor

The Cursor parameter acts as a pointer that lets you traverse the alert data set. It serves as an identifier of which alert records were generated and which alert record to go to next.

For example, you have a total of 300 monitor alerts, and you want to retrieve alerts from 101-200. As the Alert API allows you to retrieve a maximum of 100 alert records per batch, calling the first batch from the API response generates the **Cursors** JSON object with the **Next** and **Self** values:

[CODE_BLOCK_1]

For this example, use the **Next** value to retrieve alerts from the 101st alert and onwards. Use the **Self** value as the cursor to retrieve the first batch of alerts from 1 to 100.

[SHORTCODE_5] **Note:** The **Cursor** is generated per batch and not per alert record. If you retrieve the first batch of alerts without any succeeding alert records left, no **Cursor** will be generated. If more data is available, a **Cursor** will be created for that specific batch. Use the **Take** parameter to specify the batch size, ranging from 1 to 100 alert records. [SHORTCODE_6]

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

[CODE_BLOCK_2]

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
        "ErrorDescription": "Step 4 ([URL_1]): Element '.wn-product-btn' not found.",
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
