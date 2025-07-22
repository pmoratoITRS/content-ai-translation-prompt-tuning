{
  "hero": {
    "title": "Maintenance periods in the API"
  },
  "title": "Maintenance periods in the API",
  "url": "/support/kb/api/maintenance-periods",
  "translationKey": "https://www.uptrends.com/support/kb/api/maintenance-periods"
}

There is a specific set of API methods for manipulating maintenance periods for a monitor or for all monitors in a monitor group.

## Maintenance period object description

The following MaintenancePeriod object is used in the API methods described below:

| Name              | Description                                                                                                                                     | Data type        |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| `Id`              | The unique identifier for this maintenance period                                                                                               | Integer          |
| `ScheduleMode`    | OneTime, Daily, Weekly or Monthly                                                                                                               | Enum             |
| `StartDateTime`   | A start date and time (only applicable to a One-time scheduled period)                                                                          | DateTime         |
| `EndDateTime`     | The end date and time of a One-time scheduled maintenance period                                                                                | DateTime         |
| `StartTime`       | The start time (“HH:mm”, which is 24-hour notation) for a recurring (Daily, Weekly or Monthly) maintenance period                               | String (“HH:mm”) |
| `EndTime`         | The end time (“HH:mm”, which is 24-hour notation) for a recurring (Daily, Weekly or Monthly) maintenance period                                 | String (“HH:mm”) |
| `WeekDay`         | The day of the week for a weekly maintenance period (Sunday/Monday/..Saturday)                                                              | Enum             |
| `MonthDay`        | The day number for a monthly maintenance period                                                                                                 | Int (1-31)       |
| `MaintenanceType` | DisableMonitoring (to disable the monitor altogether) or DisableNotifications (monitoring will still occur, but notifications will not be sent) | Enum             |

When a maintenance period is returned through the API, all properties will be present, but depending on the ScheduleMode, some fields related to start and end dates/times will not be used.

For a one-time maintenance period, we will need to know the start and end date *and* time, so the StartDateTime and EndDateTime properties will be used. For recurring maintenance periods, the start and end time fields are appropriate, and, depending on the schedule type, the WeekDay or MonthDay property.

For example, a daily schedule would look like this:
```json
    {
    "Id": 123, 
    "ScheduleMode": "Daily", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
```

The properties that are not relevant for this schedule type (DateTime, WeekDay and MonthDay) are left out.

A weekly schedule would look like this:

```json
    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
```

A monthly schedule would look like this:
```json
    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }
```
A one-time schedule would look like this:
```json
    {
    "Id": 124, 
    "ScheduleMode": "OneTime", 
    "StartDateTime": "2018-09-24T22:00",
    "EndDateTime": "2018-09-24T22:00", 
    "MaintenanceType": "DisableMonitoring" 
    }
```

## Maintenance period endpoints

The following API endpoints are available:

| Request type | Endpoint                                                        | Usage                                                                                               |
|--------------|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| GET          | `Monitor/{monitorGuid}/MaintenancePeriod`                       | Finds all maintenance periods for a monitor.                                                        |
| POST         | `Monitor/{monitorGuid}/MaintenancePeriod`                       | Saves the new maintenance period provided for the specified monitor                                 |
| PUT          | `Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}` | Updates the specified maintenance schedule for the specified monitor                                |
| DELETE       | `Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}` | Deletes the specified maintenance period from the specified monitor                                 |
| POST         | `Monitor/{monitorGuid}/MaintenancePeriod/Cleanup/{beforeDate}`  | Clears out all one-time maintenance periods for the specified monitor older than the specified date |
| POST         | `MonitorGroup/{monitorGroupGuid}/MaintenancePeriod`             | Adds the provided maintenance period to all monitors in the group specified                         |

### GET Monitor

`GET Monitor/{monitorGuid}/MaintenancePeriod`

This GET request will return a collection containing all maintenance periods scheduled for the monitor with the GUID provided.

Example output:
```json
    [
    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }, 
    {
    "Id": 123, 
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
    ]
```

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod`

This method will create the maintenance period provided in the request body and assign it to the monitor with the provided GUID.

A POST request expects an object structure as supplied in the examples under “Maintenance period object description”. As shown there, the structure is dependent on the maintenance period type (OneTime, Daily, Weekly or Monthly). Furthermore, the Id field should not be supplied. A new Id value will be generated automatically.

### PUT Monitor

`PUT Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

This method will update the maintenance period with the supplied maintenance period ID to the values as supplied in the request body.

Expected input (example for a monthly maintenance-period):
```json
    {
    "Id": 125, 
    "ScheduleMode": "Monthly", 
    "MonthDay": 24, 
    "StartTime": "22:00", 
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications" 
    }
```
Please note that the Id of the maintenance period has to be supplied in the body as well as in the maintenancePeriodId parameter. If the Id in the parameter does not match the Id of the maintenance period in the request body, an exception will be returned.

### DELETE Monitor

`DELETE Monitor/{monitorGuid}/MaintenancePeriod/{maintenancePeriodId}`

This method will delete the maintenance period with the Id specified in maintenancePeriodId from the monitor with the supplied monitorGuid.

### POST Monitor

`POST Monitor/{monitorGuid}/MaintenancePeriod/Cleanup/{beforeDate}`

This method will remove all **one-time** schedules with a StartDateTime prior to the date supplied in beforeDate from the monitor with the supplied monitorGuid.

### POST MonitorGroup

`POST MonitorGroup/{monitorGroupGuid}/MaintenancePeriod`

This method will add the maintenance period supplied in the request body to all monitors in the monitor group with the supplied monitor group Guid.

Expected input (example for a weekly maintenance period):
```json
    {
    "ScheduleMode": "Weekly", 
    "WeekDay": "Thursday", 
    "StartTime": "22:00",
    "EndTime": "22:30", 
    "MaintenanceType": "DisableNotifications"
    }
```