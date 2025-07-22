{
  "title": "MonitorCheck API",
  "url": "[URL_BASE_TOPICS]api/monitorcheck-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Monitor check data can be retrieved using the **MonitorCheck** API endpoints that are part of [API v4]([LINK_URL_1]). Monitor checks are the individual measurements we collect for each monitor, so the MonitorCheck API gives access to that raw data. Once retrieved, that data can be stored in a database for offline analysis, or for audit or backup purposes. The following three endpoints are available:

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
| [INLINE_CODE_1]        | Returns details for an HTTP check, including HTML content and header information. |
| [INLINE_CODE_2]   | Returns the full waterfall of a Full Page Check monitor or a Transaction step.    |
| [INLINE_CODE_3] | Returns results of each transaction step, including the step times.               |

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

[HTML_TAG_1]
[HTML_TAG_2]
  [HTML_TAG_3]
    [HTML_TAG_4][HTML_TAG_5]
    [HTML_TAG_6][HTML_TAG_7]
    [HTML_TAG_8][HTML_TAG_9]
  [HTML_TAG_10]
[HTML_TAG_11]
[HTML_TAG_12]
  [HTML_TAG_13]
    [HTML_TAG_14]Id[HTML_TAG_15]
    [HTML_TAG_16]The unique monitor check identifier. This Id corresponds to the monitor check Id you see in the address bar when you view the details of a check in Uptrends.[HTML_TAG_17][HTML_TAG_18]
    [HTML_TAG_19][HTML_TAG_20]
  [HTML_TAG_21]
  [HTML_TAG_22]
    [HTML_TAG_23]Type[HTML_TAG_24]
    [HTML_TAG_25]The object type (a fixed value "MonitorCheck" for these API methods)[HTML_TAG_26][HTML_TAG_27]
    [HTML_TAG_28][HTML_TAG_29]
  [HTML_TAG_30]
  [HTML_TAG_31]
    [HTML_TAG_32]Attributes[HTML_TAG_33]
    [HTML_TAG_34]The attributes of the object that contain the actual data. These attributes include:[HTML_TAG_35]
    [HTML_TAG_36][HTML_TAG_37]
  [HTML_TAG_38]
  [HTML_TAG_39]
    [HTML_TAG_40][HTML_TAG_41]
    [HTML_TAG_42]MonitorGuid[HTML_TAG_43]
    [HTML_TAG_44]The Guid of the monitor that corresponds to this monitor check.[HTML_TAG_45]
  [HTML_TAG_46]
  [HTML_TAG_47]
    [HTML_TAG_48][HTML_TAG_49]
    [HTML_TAG_50]Timestamp[HTML_TAG_51]
    [HTML_TAG_52]The date and time at which the monitor check was completed based on the signed in operator's local time.[HTML_TAG_53]
  [HTML_TAG_54]
  [HTML_TAG_55]
    [HTML_TAG_56][HTML_TAG_57]
    [HTML_TAG_58]ErrorCode[HTML_TAG_59]
    [HTML_TAG_60]The numeric Uptrends error code in case of an error result, or 0 in case of an OK result.[HTML_TAG_61]
  [HTML_TAG_62]
  [HTML_TAG_63]
    [HTML_TAG_64][HTML_TAG_65]
    [HTML_TAG_66]TotalTime[HTML_TAG_67]
    [HTML_TAG_68]The number of milliseconds needed to complete the monitor check.[HTML_TAG_69]
  [HTML_TAG_70]
  [HTML_TAG_71]
    [HTML_TAG_72][HTML_TAG_73]
    [HTML_TAG_74]ResolveTime[HTML_TAG_75]
    [HTML_TAG_76]The number of milliseconds needed to perform the DNS query for this check, when appropriate.[HTML_TAG_77]
  [HTML_TAG_78]
  [HTML_TAG_79]
    [HTML_TAG_80][HTML_TAG_81]
    [HTML_TAG_82]ConnectionTime[HTML_TAG_83]
    [HTML_TAG_84]The number of milliseconds needed to establish a connection.[HTML_TAG_85]
  [HTML_TAG_86]
  [HTML_TAG_87]
    [HTML_TAG_88][HTML_TAG_89]
    [HTML_TAG_90]DownloadTime[HTML_TAG_91]
    [HTML_TAG_92]The number of milliseconds needed to download the response data.[HTML_TAG_93]
  [HTML_TAG_94]
  [HTML_TAG_95]
    [HTML_TAG_96][HTML_TAG_97]
    [HTML_TAG_98]TotalBytes[HTML_TAG_99]
    [HTML_TAG_100]The number of downloaded bytes for this check.[HTML_TAG_101]
  [HTML_TAG_102]
  [HTML_TAG_103]
    [HTML_TAG_104][HTML_TAG_105]
    [HTML_TAG_106]ResolvedIpAddress[HTML_TAG_107]
    [HTML_TAG_108]The IP address that was found for the specified domain name as part of this monitor check.[HTML_TAG_109]
  [HTML_TAG_110]
  [HTML_TAG_111]
    [HTML_TAG_112][HTML_TAG_113]
    [HTML_TAG_114]ErrorLevel[HTML_TAG_115]
    [HTML_TAG_116]A value that represents the OK/Error state for this check: NoError if the result was OK, Unconfirmed if an error was found, Confirmed if an error was found as a double check, right after an Unconfirmed error.[HTML_TAG_117]
  [HTML_TAG_118]
  [HTML_TAG_119]
    [HTML_TAG_120][HTML_TAG_121]
    [HTML_TAG_122]ErrorDescription[HTML_TAG_123]
    [HTML_TAG_124]A text value that describes the error that was found, or OK if no error was found. [HTML_TAG_125]
  [HTML_TAG_126]
  [HTML_TAG_127]
    [HTML_TAG_128][HTML_TAG_129]
    [HTML_TAG_130]ErrorMessage[HTML_TAG_131]
    [HTML_TAG_132]Any additional error information, if available. [HTML_TAG_133]
  [HTML_TAG_134]
  [HTML_TAG_135]
    [HTML_TAG_136][HTML_TAG_137]
    [HTML_TAG_138]ServerId[HTML_TAG_139]
    [HTML_TAG_140]The Id of the Uptrends checkpoint server that performed this check.[HTML_TAG_141]
  [HTML_TAG_142]
   [HTML_TAG_143]
    [HTML_TAG_144][HTML_TAG_145]
    [HTML_TAG_146]HttpStatusCode[HTML_TAG_147]
    [HTML_TAG_148]The HTTP status code returned (if applicable).[HTML_TAG_149]
  [HTML_TAG_150]
  [HTML_TAG_151]
    [HTML_TAG_152]Relationships[HTML_TAG_153]
    [HTML_TAG_154]The relationships array contains a list of related data/objects to the current data. This list can contain links to retrieve the related data. Relation data has the same structure, in the sense that those entries also contain the Id, Type and Links members.[HTML_TAG_155]
    [HTML_TAG_156][HTML_TAG_157]
  [HTML_TAG_158]
[HTML_TAG_159]
[HTML_TAG_160]