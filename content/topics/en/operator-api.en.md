{
  "hero": {
    "title": "Operator API"
  },
  "title": "Operator API",
  "summary": "The available API methods for manipulating operators.",
  "url": "/support/kb/api/operator-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-api"
}

This page describes the available API methods for manipulating operators, i.e. user-specific login accounts. Methods for manipulating an operator's off-duty schedules are described in a separate section below. The last section on this page describes the timezone API, which you may need for updating an operator's specific timezone setting.

## Operator object description

The following Operator object is used in the API methods described below:

| Name                     | Description                                                                                                                                                                                                                                                                             | Data type |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| `OperatorGuid`           | The unique identifier for this operator.                                                                                                                                                                                                                                                | Guid      |
| `Email`                  | The operator's primary email address and login name.                                                                                                                                                                                                                                    | String    |
| `Password`               | The operator's password.                                                                                                                                                                                                                                                                | String    |
| `FullName`               | The full name for this operator.                                                                                                                                                                                                                                                        | String    |
| `MobilePhone`            | The operator's mobile phone number.                                                                                                                                                                                                                                                     | String    |
| `OutgoingPhoneNumber`    | The operator's outgoing phone number.                                                                                                                                                                                                                                                   | String    |
| `IsAccountAdministrator` | Indicates whether the operator is the administrator of the account. This is a read-only field.                                                                                                                                                                                          | Boolean   |
| `BackupEmail`            | The backup email address for this operator.                                                                                                                                                                                                                                             | String    |
| `IsOnDuty`               | Indicates whether this operator is currently on duty.                                                                                                                                                                                                                                   | Boolean   |
| `CultureName`            | If filled, this sets the culture for this operator. Possible values: en-US, en-GB, fr-FR, de-DE, nl-NL or empty. When this value is set to empty, the overal account culture/language will be used.                                                                                     | String    |
| `TimeZoneId`             | Optional. The Id for the time zone setting for this user. Please refer to the Timezone API mentioned below for available values. If not specified, the account's time zone will be used for this user.                                                                                  | Short     |
| `SmsProvider`            | The SMS provider used by the operator. Possible values: UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational                                                                                                                              | String    |
| `UseNumericSender`       | If the SMS provider is configured specifically for this operator, this field indicates whether a numeric sender should be used.                                                                                                                                                         | Boolean   |
| `PhoneProvider`          | The provider used for phone alerts.                                                                                                                                                                                                                                                     | String    |
| `AllowNativeLogin`       | If Native Login (username/password) is available and configured for your account, this indicates whether this operator is allowed to log onto Uptrends using their Uptrends username and password. Possible values: True, False or keep unspecified to use the overall account setting. | Boolean   |
| `AllowSingleSignon`      | If Single Signon is available and configured for your account, this indicates whether this operator is allowed to use Single Sign-on.Possible values: True, False or keep unspecified to use the overall account setting.                                                               | Boolean   |

## Operator endpoints

The following API endpoints for retrieving, creating, updating and removing operators are available:

| Request type | Endpoint                                                 | Usage                                                                                                             |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET          | `/Operator`                                              | Gets all operators.                                                                                               |
| GET          | `/Operator/{operatorGuid}`                               | Gets the details of an operator.                                                                                  |
| POST         | `/Operator`                                              | Creates a new operator.                                                                                           |
| PUT          | `/Operator/{operatorGuid}`                               | Updates an existing operator.                                                                                     |
| DELETE       | `/Operator/{operatorGuid}`                               | Deletes an existing operator. Note: you cannot delete the operator associated with the API account you are using. |
| GET          | `/Operator/{operatorGuid}/DutySchedule`                  | Gets the off-duty schedules for an existing operator.                                                                 |
| POST         | `/Operator/{operatorGuid}/DutySchedule`                  | Adds an off-duty schedule for an existing operator.                                                                    |
| PUT          | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Updates the specified off-duty schedule.                                                                              |
| DELETE       | `/Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}` | Deletes the specified off-duty schedule.                                                                              |

#### GET Operator

This GET request will return a collection containing all operators, including the account administrator.

```json
[
  {
    "OperatorGuid": "36fad910-6e9f-4886-b1a7-9b4637362cb8",
    "FullName": "First Operator",
    "Email": "FirstOperator@acme.com",
    "MobilePhone": "",
    "IsAccountAdministrator": true,
    "BackupEmail": " FirstOperator@gmail.com ",
    "IsOnDuty": true,
    "SmsProvider": "UseAccountSetting",
    "PhoneProvider": "UseAccountSetting",
    "AllowNativeLogin": true,
    "AllowSingleSignon": false
  },
  {
    "OperatorGuid": "23a75d1f-0dec-4963-86d8-0cee21267db4",
    "UserName": "SecondOperator@acme.com",
    "FullName": "Second Operator",
    "Email": "SecondOperator@acme.com",
    "MobilePhone": "",
    "IsAccountAdministrator": false,
    "BackupEmail": "",
    "IsOnDuty": false,
    "SmsProvider": "SmsProviderEurope",
    "UseNumericSender": false,
    "PhoneProvider": "UseAccountSetting",
    "AllowNativeLogin": true,
    "AllowSingleSignon": false
  }
]
```
#### GET Operator/{operatorGuid}

This GET request will return the details of the specific operator identified by the operator GUID specified.

Example output:

```json
{
  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",
  "FullName": "Third Operator",
  "Email": "ThirdOperator@acme.com",
  "MobilePhone": "+31612345678",
  "OutgoingPhoneNumber": "",
  "IsAccountAdministrator": false,
  "BackupEmail": "",
  "IsOnDuty": false,
  "CultureName": "",
  "TimeZoneId": 56,
  "SmsProvider": "SmsProviderUSA",
  "UseNumericSender": false,
  "PhoneProvider": "UseAccountSetting",
  "AllowNativeLogin": true,
  "AllowSingleSignon": false
}
```

#### POST Operator

This will create a new operator with the details provided.

Example input:

```json
{
  "FullName": "Third Operator",
  "Email": "ThirdOperator@acme.com",
  "MobilePhone": "+31612345678",
  "OutgoingPhoneNumber": "",
  "IsAccountAdministrator": false,
  "BackupEmail": "",
  "IsOnDuty": false,
  "CultureName": "",
  "TimeZoneId": 56,
  "SmsProvider": "SmsProviderUSA",
  "UseNumericSender": false,
  "PhoneProvider": "UseAccountSetting",
  "AllowNativeLogin": true,
  "AllowSingleSignon": false
}
```

The response will contain the created operator, including the operator GUID that was assigned:

```json
{
  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",
  "FullName": "Third Operator",
  "Email": "ThirdOperator@acme.com",
  "MobilePhone": "+31612345678",
  "OutgoingPhoneNumber": "",
  "IsAccountAdministrator": false,
  "BackupEmail": "",
  "IsOnDuty": false,
  "CultureName": "",
  "TimeZoneId": 56,
  "SmsProvider": "SmsProviderUSA",
  "UseNumericSender": false,
  "PhoneProvider": "UseAccountSetting",
  "AllowNativeLogin": true,
  "AllowSingleSignon": false
}
```


#### PUT Operator/{operatorGuid}

This method will update the operator identified by the operator GUID specified, using the data provided in the request.

Example input:

```json
{
  "OperatorGuid": "d2782d76-62e7-4946-a41c-fc7f86c96300",
  "FullName": "Third Operator",
  "Email": "ThirdOperator@acme.com",
  "MobilePhone": "+31612345678",
  "OutgoingPhoneNumber": "",
  "IsAccountAdministrator": false,
  "BackupEmail": "",
  "IsOnDuty": false,
  "CultureName": "",
  "TimeZoneId": 56,
  "SmsProvider": "SmsProviderUSA",
  "UseNumericSender": false,
  "PhoneProvider": "UseAccountSetting",
  "AllowNativeLogin": true,
  "AllowSingleSignon": false
}
```


#### DELETE Operator/{operatorGuid}

This method will delete the operator identified by the operator GUID specified, using the data provided in the request.

## Operator off-duty schedule object description

| Name            | Description                                                                                               | Data type |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| `Id`            | The unique identifier for this off-duty schedule. This field is readonly and will be automatically generated. | Guid      |
| `ScheduleMode`  | The schedule mode. Possible values: OneTime, Daily, Weekly, Monthly                                       | String    |
| `StartDateTime` | The start date and time (for a one-time schedule)                                                         | DateTime  |
| `EndDateTime`   | The end date and time (for a one-time schedule)                                                           | DateTime  |
| `WeekDay`       | The day of the week (for a weekly schedule). Possible values: Monday, Tuesday, ..., Sunday.               | String    |
| `MonthDay`      | The date of the month (for a monthly schedule)                                                            | Int       |
| `StartTime`     | The start time (for a daily, weekly or monthly schedule). Format: “HH:mm”, in 24-hour format.             | String    |
| `EndTime`       | The end time (for a daily, weekly or monthly schedule). Format: “HH:mm”, in 24-hour format.               | String    |

## Operator off-duty schedule endpoints

The following API endpoints are available for retrieving, creating, updating and deleting off-duty schedules for a specific operator:

#### GET Operator/{operatorGuid}/DutySchedule

This method will return a collection containing all off-duty schedules for the specified operator.

Example output:

```json
[
  {
    "Id": 2272,
    "ScheduleMode": "Weekly",
    "WeekDay": "Monday",
    "StartTime": "08:00",
    "EndTime": "16:30"
  },
  {
    "Id": 2267,
    "ScheduleMode": "Monthly",
    "MonthDay": 15,
    "StartTime": "08:00",
    "EndTime": "16:30"
  }
]
```
#### POST Operator/{operatorGuid}/DutySchedule

This method will create a new off-duty schedule for the specified operator.

Example input (for a weekly schedule):

```json
{
  "ScheduleMode": "Weekly",
  "WeekDay": "Thursday",
  "StartTime": "08:00",
  "EndTime": "16:30"
}
```
As you can see in this example, you are expected to only specify the parameters that are relevant to the schedule type you’re creating. For example, the MonthDay is not relevant for a weekly schedule, and StartDateTime and EndDateTime are only for one-time schedules.

Elaborating on this a bit more, a daily schedule, does not expect a weekday value, just ScheduleMode “Daily” and a start time and end time. Similarly, a monthly schedule only expects ScheduleMode “Monthly”, the month day, the start time and the end time.

When you create a new off-duty schedule, the output contains the Id of the new schedule. Example output for creating a daily schedule:

```json
{
  "Id": 2272,
  "ScheduleMode": "Daily",
  "StartTime": "08:00",
  "EndTime": "16:30"
}
```

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

This method will update the off-duty schedule with the specified off-duty schedule ID, for the specified operator.Example input:

```json
{
  "Id": 2273,
  "ScheduleMode": "Weekly",
  "WeekDay": "Wednesday",
  "StartTime": "08:00",
  "EndTime": "16:30"
}
```
#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

This method will delete the off-duty schedule with the specified off-duty schedule ID, for the specified operator.

## Timezone object description

| Name                   | Description                                                                                      | Data type |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| `TimeZoneId`           | The unique identifier for this time zone                                                         | Short     |
| `Description`          | The description for this time zone                                                               | String    |
| `OffsetFromUtc`        | The offset from UTC in minutes                                                                   | Short     |
| `HasDaylightSaving`    | Whether or not this time zone has daylight saving time                                            | Boolean   |
| `DaylightSavingOffset` | The offset, in minutes, for daylight saving time. Not specified when HasDaylightSaving is false. | Short     |

## Timezone endpoints

The following methods can be used to retrieve time zone information. You can use this data to identify which timezoneId to use, when you want to specify a timezoneId for an operator's settings.

#### GET Timezone

This GET request will return a collection containing all time zones.

Example output:

```json
[
  {
    "TimezoneId": 1,
    "Description": "GMT-04:00# Brazil West, Chile, Paraguay",
    "OffsetFromUtc": -240,
    "HasDaylightSaving": true,
    "DaylightSavingOffset": 60
  },
  {
    "TimezoneId": 2,
    "Description": "GMT+06:00# Cocos Islands",
    "OffsetFromUtc": 360,
    "HasDaylightSaving": true,
    "DaylightSavingOffset": 60
  },
  {
    "TimezoneId": 3,
    "Description": "GMT+01:00 West Central Africa",
    "OffsetFromUtc": 60,
    "HasDaylightSaving": false
  }
  // (there will be many more)
]
```
#### GET Timezone/{timezoneId}

This method will get the time zone details for the time zone with the specified Id.

Example output:

```json
{
  "TimezoneId": 56,
  "Description": "GMT-06:00* Central time",
  "OffsetFromUtc": -360,
  "HasDaylightSaving": true,
  "DaylightSavingOffset": 60
}
```