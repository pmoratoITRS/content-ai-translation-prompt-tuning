{
  "hero": {
    "title": "API changelog"
  },
  "title": "API changelog",
  "summary": "Check out the changes, updates, and improvements for the Uptrends API",
  "url": "[URL_BASE_TOPICS]api/changelog",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "type": "[FRONTMATTER_TYPE]"
}

{{[HTML_TAG_1]}}

Uptrends API will be improved and extended over time. We'll be adding new endpoints and methods for new functionalities.

When adding a new functionality, our goal is always to stay backward-compatible. However, sometimes change is inevitable and a new version of the API may not be compatible with what you've coded and used so far. You should check the API changelog regularly to stay on top of all changes and to act on those changes when necessary.

If you are looking for the documentation of the API, please check out the articles in the [Uptrends API]([LINK_URL_1]) category.

Also, if you are interested in the changes to the Uptrends app, check out the [general changelog]([LINK_URL_2]).

## May 2025

### Upcoming breaking change: Deprecating API fields

As part of our ongoing efforts to optimize the Uptrends API, specific fields in the following [Monitor]([LINK_URL_3]) endpoints will be deprecated, effective **27 August 2025**:

- [INLINE_CODE_1] and [INLINE_CODE_2] [INLINE_CODE_3]
- [INLINE_CODE_4], [INLINE_CODE_5], and [INLINE_CODE_6] [INLINE_CODE_7]
- [INLINE_CODE_8] and [INLINE_CODE_9] [INLINE_CODE_10]

The following deprecated fields will now be treated as [Error condition types]([LINK_URL_4]) under the [INLINE_CODE_11] array. Related fields will be merged into a single entry, replacing their previous usage as individual fields:

| Deprecated fields | Replacement fields |
|--|--|
| [INLINE_CODE_12], [INLINE_CODE_13]| [SHORTCODE_1] [LoadTimeLimit1]([LINK_URL_5]) |
| [INLINE_CODE_14], [INLINE_CODE_15] | [LoadTimeLimit2]([LINK_URL_6]) |
|[INLINE_CODE_16], [INLINE_CODE_17] | [TotalMaxBytes]([LINK_URL_7]) |
|[INLINE_CODE_18], [INLINE_CODE_19] | [TotalMinBytes]([LINK_URL_8]) | 
|[INLINE_CODE_20], [INLINE_CODE_21] | [PageElementMaxSizeWithPercentage]([LINK_URL_9]) |
|[INLINE_CODE_22], [INLINE_CODE_23] | [PageElementFailedWithPercentage]([LINK_URL_10])
|[INLINE_CODE_24], [INLINE_CODE_25] | [HttpStatus]([LINK_URL_11]) |

Below is an example of the updated API response. It is recommended that you adjust your API calls to use the [INLINE_CODE_26] array. This aligns with the latest API structure and ensures correct API functionality.

[CODE_BLOCK_1]

### Private Checkpoint Health Update

The [INLINE_CODE_27] endpoint now returns the [INLINE_CODE_28] field, which contains all warning information associated with the server's checkpoint. To know more, refer to the [Uptrends API v4 Private location Checkpoint health documentation]([LINK_URL_12]).

## April 2025

### Introducing the Private locations API​

A new set of API endpoints has been added to help you manage your Private locations configuration, including health and checkpoint information. To know more, refer to the [Uptrends API v4 Private locations documentation]([LINK_URL_13]).

## March 2025

### Monitor Group API Update

The [INLINE_CODE_29] endpoint now returns the number of credits used per [monitor type]([LINK_URL_14]):
- [INLINE_CODE_30] — returns the number of credits used for [Uptime or Basic monitors]([LINK_URL_15]).
- [INLINE_CODE_31] — returns the number of credits used for [Browser or Full-Page Check (FPC) monitors]([LINK_URL_16]).
- [INLINE_CODE_32] — returns the number of credits used for [Transaction monitors]([LINK_URL_17]).
- [INLINE_CODE_33] — returns the number of credits used for [Multi-step API (MSA)]([LINK_URL_18]) and [Postman]([LINK_URL_19]) monitors.

Previously, the MonitorGroup API only returned the total number of credits available to the group for each monitor category. Now, it also returns the number of credits in use in the group for each monitor category.

## February 2025

### Cursor Parameter Value Update

The API Cursor parameter is a string value that works as a pointer to traverse data from the API response.

Cursors have now been updated to a longer string format to ensure safer data handling. All newly created cursors will now follow the new format, and the old formatted cursors will still continue to work until 1 April 2025. After that period, old cursors will no longer be available for use. It is recommended to generate new cursor values to keep them updated and working as expected.

Note that the Cursor parameter is available in the [Monitor Check API]([LINK_URL_20]) and Alert API endpoints.

## January 2025

### Monitor API Update

The [INLINE_CODE_34] endpoint now returns the [INLINE_CODE_35], which contains the date and time the monitor was last updated. Previously, only the [INLINE_CODE_36] could be retrieved from the Monitor API.

## November 2024

### VaultItem Update

The [INLINE_CODE_37], [INLINE_CODE_38], and [INLINE_CODE_39] now accept the [INLINE_CODE_40] field when updating or creating the [One-time password configuration]([LINK_URL_21]) vault item. This new field accepts *Hex* or *Base32* as string values. The *Base32* format is the default encoding method if the [INLINE_CODE_41] field is not specified.

## September 2024

### VaultItem Update

The [INLINE_CODE_42] now returns an additional data item, [INLINE_CODE_43], which returns details about which items or monitors are using each vault item.

## August 2024

### Checkpoint API

The API endpoint [INLINE_CODE_44] now also returns private location servers.

### VaultItem Update

The [INLINE_CODE_45] endpoint is now able to return the same extent of details for each vault item, similar to how details are returned for a single item in a [INLINE_CODE_46].

## June 2024

### Breaking change: the /Register API for SSO-only operators

The Uptrends API requires [registration]([LINK_URL_22]) before it can be used. Operators can create a set of API-specific credentials, based on their regular Uptrends credentials. There are two ways to register a set of API credentials:

- Operators can make use of the regular Uptrends interface, and add an API user through the [SHORTCODE_2]API management[SHORTCODE_3] tab in their operator settings.
- Alternatively, operators can register for credentials in the API itself, via a request [INLINE_CODE_47] by supplying their regular Uptrends credentials.

As of this update, operators who can only [log in using Single sign-on (SSO)]([LINK_URL_23]) can no longer attempt to make use of this second option for registering API credentials, since they do not have 'regular' Uptrends credentials to use. 

In such cases, we recommend making a separate operator account, and using that to register for API credentials. 

## October 2023

### Breaking change: page load metrics for browser-based monitoring

**Note:** the following is a **breaking change** to the *MonitorCheck* API. The change will go live on **Wednesday, November 8th**.

The Uptrends [MonitorCheck API]([LINK_URL_24]) can be used to retrieve detailed information about individual monitor checks. For browser-based monitoring, the [waterfall chart]([LINK_URL_25]) can be retrieved via the [INLINE_CODE_48] call, which returns all the waterfall metrics, including [Core Web Vitals]([LINK_URL_26]) and [W3C navigation timings]([LINK_URL_27]), if they are present in the check result. 

Currently, the MonitorCheck API returns Core Web Vitals and W3C navigation timings in two separate JSON objects: [INLINE_CODE_49] and [INLINE_CODE_50]. Going forward, these separate objects will be combined into a single array, [INLINE_CODE_51] as follows:

[CODE_BLOCK_2]


### Specifying variables in alert definitions via the API

When configuring [alerting]([LINK_URL_28]) through a [custom integration]([LINK_URL_29]) in Uptrends, operators can use the UI to specify certain required variables [in the escalation level of the alert definition]([LINK_URL_30]), instead of in the integration options. This allows users to use a single integration for various scenarios, such as sending alerts for different sets of monitors to different teams, but with the same message content.

When the option to specify variables in the escalation level is selected in the integration settings, the variables must instead be configured when the integration is set to be used in the settings of the alert definition. To do this, an extra text field appears in the integration selection list in the alert definition settings. 

Until now, this option was unavailable when configuring alert definitions through the API. We've added a new option to the [INLINE_CODE_52] request (where you configure which integrations are tied to each escalation level in the alert definition). The new property will be:

[CODE_BLOCK_3]

This property is the equivalent of this option in the application UI:

![Configuring integration variable in alert definition]([LINK_URL_31])


## September 2023

### Change in checkpoint's IPv6 addresses

Previously, when using the checkpoint API to retrieve checkpoint information, the checkpoint's IPv4 addresses were displayed as a simple list in an array, while the IPv6 addresses (if applicable) were a list of objects. For example, the Amsterdam checkpoint IP addresses were previously listed as follows:

[CODE_BLOCK_4]

Uptrends has resolved this inconsistency now, and returns the IPv6 addresses in the same way:

[CODE_BLOCK_5]

Be aware that if you've automated the retrieval of checkpoint IP addresses, e.g. for whitelisting purposes, this may be a **breaking change**.

## January 2023

Version 3 of the API has reached its end of life as of January 2023, and has been disabled. You can still find [its documentation]([LINK_URL_32]) in our knowledge base, but it will no longer work. If you have existing scripts or procedures in place that are still making use of version 3, these will fail, and we recommend you switch to version 4 as quickly as possible. See our [upgrade guide]([LINK_URL_33]) for more information on switching from API version 3 to version 4.

**Update May 2023:** The documentation for version 3 of our API has been removed, and is no longer accessible. 

## December 2022

### Monitor creation date info through the API

The [/Monitor endpoint]([LINK_URL_34]) can be used to retrieve definitions of the monitors in your account (via *GET /Monitor/{monitorGuid}*), among other things. The response will now also include a [INLINE_CODE_53], indicating when the monitor was created.


## November 2022

### Small changes to /Register endpoint

As you may have read [in our regular changelog]([LINK_URL_35]), this release we've added the option to ['Create and revoke Uptrends API credentials via UI']([LINK_URL_36]). In order to align the Uptrends API v4 with the user interface, we have added 2 new options to the /Register endpoint:

- It's now possible to specify an optional description when registering a new API account by using the [INLINE_CODE_54] field.
- It's now possible to create an API account for another operator when the calling operator has sufficient rights by using the [INLINE_CODE_55] field.

## September 2022

### Upcoming change: timestamps in the API response

Currently, timestamps that are part of the response for any [API v4]([LINK_URL_37]) call are being converted to JSON in one of two ways:

- Millisecond count is equal to 0:  _2022-09-21T13:08:47_
- Millisecond count is not equal to 0: _2022-09-21T13:08:47[HTML_TAG_2].682[HTML_TAG_3]_

This inconsistency can lead to problems when the data containing these timestamps is automatically parsed and handled. Because of this, we're making a change: the millisecond count will no longer be shown for any timestamps included in the API response. Going forward, all timestamps will have the format _2022-09-21T13:08:47_.

## June 2022

### Upcoming checkpoint IP addresses 

The Uptrends API can be used to retrieve checkpoint IP addresses, for automated whitelisting. Previously, responses to such requests to our [checkpoint API]([LINK_URL_38]) were typically an up-to-date list of current checkpoint IP addresses. However, Uptrends' checkpoint network is always in motion. New checkpoints are added, existing checkpoints are removed or relocated, or IP addresses are changed. That could mean that the list of IP addresses you were using to whitelist might fall behind until the next synchronization, leading to unnecessary errors.

We're now registering upcoming checkpoint IP addresses and including them in the API response. That way your whitelist will be up to date ahead of time.

### Relationships in statistics API

Responses from the [Statistics API]([LINK_URL_39]) (which can be used to retrieve statistical data for your monitors or monitor groups) will now include some additional metadata about the response. The new [INLINE_CODE_56] array already exists for other API endpoints, and contains additional information about the request like a link to the Monitor or MonitorGroup API request to retrieve additional information about the monitor (group) itself.


[CODE_BLOCK_6]

## May 2022

### Fix for start/end parameters in statistics API

Our API supports retrieving statistical monitor data, with the [Statistics API]([LINK_URL_40]). You can specify either a preset period for which to retrieve the data (with available values such as [INLINE_CODE_57]), or set a custom period using start and end URL parameters. For example, [INLINE_CODE_58] retrieves statistical data for a single monitor, for the specified period.

There was an issue where the minute indicator in the start and end timestamps wasn't being mapped correctly, which could have led to incomplete (or even empty) results in the API response. This issue has been resolved.

## February 2022

### Update to status API

The [Status API]([LINK_URL_41]) retrieves status information for a specific monitor, based on the most recent monitor check. This endpoint can be used for information regarding the current monitor status. We've expanded the response to now also include a value for [INLINE_CODE_59] - information about the [total time metric]([LINK_URL_42]) for the most recent monitor check.

## January 2022

### Returning the correct monitor data

When a non-Administrator operator with [the **View data** permission]([LINK_URL_43]) on a certain monitor retrieved that monitor definition through the API (via [INLINE_CODE_60]), the response did not include all relevant data. That was incorrect, since the same data was already available through the UI but not the API, and has been rectified. Now, when these operators retrieve a monitor, the response will include values for *MonitorGuid*, *Name*, *MonitorType*, *MonitorMode*, *IsActive*, and *GenerateAlert*.

## August 2021

### Announcement: deprecation of version 3 of our API

The [Uptrends API]([LINK_URL_44]) currently supports two versions side-by-side. Version 3 is the older legacy version of our API, and version 4 is the currently recommended version. With a much more complete set of features, version 4 has been the focus of our development for some time. As such, we've decided to deprecate version 3 of our API, and it will be retired and become unavailable by **December 2022**. 

For customers currently still making active use of version 3 of our API, it should be noted that it will still be supported up until that time. However, we do recommend switching over to making use of version 4 as soon as possible. To assist you in this, we've written an [API v3 to v4 upgrade guide]([LINK_URL_45]), which will cover the key differences between the two API versions and how to bridge them in your scripts and software. 

## July 2021

### Breaking change: changes in OperatorGroup authorization response

The Uptrends API allows you to manage [permissions for operators and operator groups]([LINK_URL_46]), assigning roles such as **Administrator**, **Financial operator**, or allowing **Infra access**. The [OperatorGroup API]([LINK_URL_47]) contains several options for retrieving, adding or deleting such permissions. 

We have changed the way in which the permissions are specified for operator groups in the API, which could affect any automated creation, removal, or retrieval of information about operator group permissions you may have set up. Currently, retrieving information about permissions works by requesting:

[INLINE_CODE_61]

which returns a response along the following lines (depending on which permissions have been set up for that particular operator group):

[CODE_BLOCK_7]

Going forward, that same request will have its response simplified, simply listing the permissions granted and no other information. The response will no longer contain an [INLINE_CODE_62] or [INLINE_CODE_63] (the latter will disappear completely, meaning permissions will no longer have an individual GUID assigned to them). It will look like this:

[CODE_BLOCK_8]

Adding a new operator group permission currently works by sending a POST request to:

 [INLINE_CODE_64] 
 with a request body specifying an "AuthorizationType". The currently available values for AuthorizationType for operator groups is available in the [Uptrends API Swagger UI]([LINK_URL_48]), under **Models** (at the bottom), and then **OperatorGroupAuthorizationType**.
 
 Going forward, new permissions can be added to an operator group by sending a POST request to: 

 [INLINE_CODE_65] 
 without including a request body. 

Deleting a permission from an operator group is currently done by sending a DELETE request to [INLINE_CODE_66] - but as noted above, "authorizationGuid" will disappear entirely as an entity and can no longer be used. Instead, you can delete permissions by referring to them directly by name in the request URL: [INLINE_CODE_67]

## February 2021

### Breaking change: sensitive values in multi-step API monitors

Our [multi-step API monitor type]([LINK_URL_49]) allows you to execute multiple consecutive HTTP requests, where each new request uses one or more pieces of data retrieved from a previous request to perform its task. Often, one of the steps will involve submitting credentials to gain access to a particular resource. In the past, these credentials would be added as predefined variables to the monitor definition, and then marked as *Sensitive*.

To improve the security of how we handle such credentials, we're going to be moving away from that setup. Instead, the credentials will be placed in the [vault]([LINK_URL_50]). With that change, the option to mark predefined variables as sensitive in multi-step API monitors becomes obsolete, and we will be removing it.

This will affect the way in which you can create or interact with multi-step API monitors through our API. Currently, the monitor definition for this monitor type will contain an array "PredefinedVariables", where each of the individual variables has a true/false boolean "Sensitive". In the near future, this boolean will be removed from the definition. If you wish to create or update an existing multi-step API monitor in your account through the Uptrends API, this field must no longer be included. 

### Change: renamed routing
 
 For Uptrends APIv4 we have an inconsistent way of naming routes. In most cases singular is used, but plural on a few occasions. The route now contains only singular parts, 
 e.g. [INLINE_CODE_68] instead of [INLINE_CODE_69].

 We still support the old routes for backwards compatibility.

{{[HTML_TAG_4]}}
