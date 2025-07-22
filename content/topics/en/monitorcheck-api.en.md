{
  "title": "MonitorCheck API",
  "url": "/support/kb/api/monitorcheck-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorcheck-api"
}

Monitor check data can be retrieved using the **MonitorCheck** API endpoints that are part of [API v4](/support/kb/api/v4). Monitor checks are the individual measurements we collect for each monitor, so the MonitorCheck API gives access to that raw data. Once retrieved, that data can be stored in a database for offline analysis, or for audit or backup purposes. The following three endpoints are available:

| MonitorCheck endpoint      | Usage                                              |
|----------------------------|----------------------------------------------------|
| /MonitorCheck              | Returns all Monitor check data in account.         |
| /MonitorCheck/Monitor      | Returns Monitor check data for a specific monitor. |
| /MonitorCheck/MonitorGroup | Returns Monitor check data for a Monitor-group.    |

A typical scenario is to download your data (for all monitors, for a group or a specific monitor) for a particular time period (for the previous month, for example). Depending on the number of monitors you have and the monitoring interval at which they are running, this might be a substantial amount of data. A good way to keep API calls quick and responsive is to download and process data in chunks, e.g. 100 items at a time. The MonitorCheck API methods are optimized for downloading data in chunks.

All MonitorCheck endpoints take the following parameters:

| Parameter      | Description                                                                                                                       |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Date period to filter on (default: Last24Hours). Leave this empty if you want to specify a custom period using *start* and *end*. |
| **start**      | The start of a custom period. Leave this empty if you're using the *period* parameter.                                            |
| **end**        | The end of a custom period. Leave this empty if you're using the *period* parameter.                                              |
| **errorLevel** | The minimum error level of checks to return (default: NoError, which means that no filter is applied)                             |
| **cursor**     | Parameter for traversing through the data, see below.                                                                             |
| **take**       | The number of rows to return (default: 100; this is also the maximum).                                                            |
| **sorting**    | Specifies if the data should be sorted by date in Ascending or Descending order (default: Descending)                             |

## Traverse your data by using a cursor

A cursor is a string value that acts as a pointer in the timeline of your data. When you start requesting a large amount of data (say, all monitor data for last month), the API returns the first chunk of 100 items. Along with that data, it also gives you a cursor value you can use to easily get to the second chunk of data, and so on. You can repeat this process until you've downloaded all data for the time period you requested. An empty cursor indicates that you've reached the end of the sequence, and that no more data is to be expected.

## Forwards or backwards in time

You can decide whether you want to start with recent data and work your way backwards in time (sorting=Descending), or start at the beginning of a time period and move towards the present time (sorting=Ascending).  
  
The latter is particularly useful and efficient if you're using an automated process that gets regular updates for current data. For example, you could access the API every 5 minutes by requesting Last24Hours, Ascending, and specifying the cursor value from the previous response: the API will only return data that was generated since your last API request. The result may contain an empty list if no new data is available yet, but if the API response contains a non-empty cursor value, new data may be retrieved in a later request.

## Retrieving MonitorCheck details

When you retrieve a list of MonitorChecks, each MonitorCheck entry contains the basic metrics for that check, as described below. However, depending on the monitor type, more detailed data may be available. Those details can be retrieved using separate API calls. The link between the main MonitorCheck and any related details are described as relationships. When a MonitorCheck does indeed have one or more details linked to it, they are presented in the 'Relationships' member (see below): it will contain a link to each appropriate details endpoint that gives access to that data. The following detail endpoints are currently available:

| Detail endpoint                              | Usage                                                                             |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| `/MonitorCheck/{monitorCheckId}/Http`        | Returns details for an HTTP check, including HTML content and header information. |
| `/MonitorCheck/{monitorCheckId}/Waterfall`   | Returns the full waterfall of a Full Page Check monitor or a Transaction step.    |
| `/MonitorCheck/{monitorCheckId}/Transaction` | Returns results of each transaction step, including the step times.               |

## Generic data structure

A MonitorCheck response uses the following format to separate the actual data from the provided meta data:

### Root

Root contains the following members:

|            |                                                                        |
|------------|------------------------------------------------------------------------|
| **Data**   | An array or single object containing (a subset of) the requested data. |
| **Links**  | Links that reference to self and next data set.                        |
| **Cursor** | Contains cursor values that should be used to traverse the dataset.    |

### Data

The data member can contain an array of objects, or a single object. Either way, the single MonitorCheck object or the MonitorCheck objects inside the array will have the following members:

<table>
<thead>
  <tr>
    <th class="cell-small"></th>
    <th class="cell-large"></th>
    <th class="cell-large"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="bold">Id</td>
    <td>The unique monitor check identifier. This Id corresponds to the monitor check Id you see in the address bar when you view the details of a check in Uptrends.<br></td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Type</td>
    <td>The object type (a fixed value "MonitorCheck" for these API methods)<br></td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Attributes</td>
    <td>The attributes of the object that contain the actual data. These attributes include:</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">MonitorGuid</td>
    <td>The Guid of the monitor that corresponds to this monitor check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">Timestamp</td>
    <td>The date and time at which the monitor check was completed based on the signed in operator's local time.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorCode</td>
    <td>The numeric Uptrends error code in case of an error result, or 0 in case of an OK result.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalTime</td>
    <td>The number of milliseconds needed to complete the monitor check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolveTime</td>
    <td>The number of milliseconds needed to perform the DNS query for this check, when appropriate.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ConnectionTime</td>
    <td>The number of milliseconds needed to establish a connection.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">DownloadTime</td>
    <td>The number of milliseconds needed to download the response data.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalBytes</td>
    <td>The number of downloaded bytes for this check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolvedIpAddress</td>
    <td>The IP address that was found for the specified domain name as part of this monitor check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorLevel</td>
    <td>A value that represents the OK/Error state for this check: NoError if the result was OK, Unconfirmed if an error was found, Confirmed if an error was found as a double check, right after an Unconfirmed error.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorDescription</td>
    <td>A text value that describes the error that was found, or OK if no error was found. </td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorMessage</td>
    <td>Any additional error information, if available. </td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ServerId</td>
    <td>The Id of the Uptrends checkpoint server that performed this check.</td>
  </tr>
   <tr>
    <td></td>
    <td class="bold">HttpStatusCode</td>
    <td>The HTTP status code returned (if applicable).</td>
  </tr>
  <tr>
    <td class="bold">Relationships</td>
    <td>The relationships array contains a list of related data/objects to the current data. This list can contain links to retrieve the related data. Relation data has the same structure, in the sense that those entries also contain the Id, Type and Links members.</td>
    <td></td>
  </tr>
</tbody>
</table>