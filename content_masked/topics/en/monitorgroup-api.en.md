{
  "hero": {
    "title": "MonitorGroup API"
  },
  "title": "MonitorGroup API",
  "summary": "The available API methods for manipulating monitor groups.",
  "url": "[URL_BASE_TOPICS]api/monitorgroup-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_11] **Note:** Effective 27 August 2025, some fields in the **GET and POST /Monitor/MonitorGroup/{monitorGroupGuid}** endpoints will be deprecated. For more information, refer to the [API changelog]([LINK_URL_1]).
[SHORTCODE_12]

This page describes the available API methods for manipulating monitor groups. To learn more, refer to [Uptrends Monitor Group API]([LINK_URL_2]).

## MonitorGroup object description

The following MonitorGroup object is used in the MonitorGroupAPI endpoints:

| Name               | Description                                                                         | Data type |
|--------------------|-------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1] | The unique identifier for the monitor group.                                       | String |
| [INLINE_CODE_2]      | The name of the monitor group.                                              | String |
| [INLINE_CODE_3]            | [SHORTCODE_1] 
Indicates whether the monitor group is the default [All Monitors]([LINK_URL_3])
 group. [SHORTCODE_2] | Boolean  |
| [INLINE_CODE_4] | Indicates whether the number of credits for the monitor group is unlimited or not.  |  Boolean  |
| [INLINE_CODE_5] |[SHORTCODE_3] 
Returns the number of credits used for [Uptime monitors]([LINK_URL_4]). [SHORTCODE_4] | Integer |
| [INLINE_CODE_6]            | [SHORTCODE_5] 
Returns the number of credits used for [Browser monitors (Full-Page Check)]([LINK_URL_5]). [SHORTCODE_6] | Integer |
| [INLINE_CODE_7]            | [SHORTCODE_7]
Returns the number of credits used for [Transaction monitors]([LINK_URL_6]).  [SHORTCODE_8] | Integer |
| [INLINE_CODE_8]            | [SHORTCODE_9] 
Returns the number of credits used for [Multi-step API (MSA)]([LINK_URL_7]) and [Postman]([LINK_URL_8]) monitors. [SHORTCODE_10] | Integer |
| [INLINE_CODE_9]            | Returns the number of credits used by existing accounts that are using a single credit pricing tier. | Integer |

### All Monitors group

The **All Monitors** group is a monitor or system group that contains all of your monitors by default. Use the Guid of this group to manage operations that affect all monitors, such as, starting or stopping all monitors or alerts.
Note that you cannot change the membership of this group.


## Monitor group management endpoints

The following API endpoints are available for creating, modifying, and removing monitor groups, as well as the monitors within those groups.

| Request type | Endpoint                                                 | Usage                                                          |
|--------------|----------------------------------------------------------|----------------------------------------------------------------|
| GET          | [INLINE_CODE_10]                                          | Gets all monitor groups                                        |
| POST         | [INLINE_CODE_11]                                          | Creates a new monitor group                                    |
| GET          | [INLINE_CODE_12]                       | Gets the details of a monitor group                            |
| PUT          | [INLINE_CODE_13]                       | Updates an existing monitor group                              |
| DELETE       | [INLINE_CODE_14]                       | Deletes a monitor group                                        |
| GET          | [INLINE_CODE_15]               | Gets a list of all monitors that are member of a monitor group |
| POST         | [INLINE_CODE_16] | Adds the specified monitor to the monitor group                |
| DELETE       | [INLINE_CODE_17] | Removes the specified monitor from the monitor group           |

## Additional monitor group operations

The following API endpoints are available to perform operations on all monitors contained in a group:

| Request type | Endpoint                                                            | Usage                                                                       |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------|
| POST         | [INLINE_CODE_18]                  | Stops all monitors in the specified monitor group                           |
| POST         | [INLINE_CODE_19]                 | Starts all monitors in the specified monitor group                          |
| POST         | [INLINE_CODE_20]             | Stops alerting for all monitors in the specified monitor group              |
| POST         | [INLINE_CODE_21]            | Starts alerting for all monitors in the specified monitor group             |
| POST         | [INLINE_CODE_22] | Adds the provided maintenance period to all monitors in the group specified |
