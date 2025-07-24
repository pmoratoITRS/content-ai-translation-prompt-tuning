{
  "hero": {
    "title": "Operator API"
  },
  "title": "Operator API",
  "summary": "The available API methods for manipulating operators.",
  "url": "[URL_BASE_TOPICS]api/operator-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

This page describes the available API methods for manipulating operators, i.e. user-specific login accounts. Methods for manipulating an operator's off-duty schedules are described in a separate section below. The last section on this page describes the timezone API, which you may need for updating an operator's specific timezone setting.

## Operator object description

The following Operator object is used in the API methods described below:

| Name                     | Description                                                                                                                                                                                                                                                                             | Data type |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_1]           | The unique identifier for this operator.                                                                                                                                                                                                                                                | Guid      |
| [INLINE_CODE_2]                  | The operator's primary email address and login name.                                                                                                                                                                                                                                    | String    |
| [INLINE_CODE_3]               | The operator's password.                                                                                                                                                                                                                                                                | String    |
| [INLINE_CODE_4]               | The full name for this operator.                                                                                                                                                                                                                                                        | String    |
| [INLINE_CODE_5]            | The operator's mobile phone number.                                                                                                                                                                                                                                                     | String    |
| [INLINE_CODE_6]    | The operator's outgoing phone number.                                                                                                                                                                                                                                                   | String    |
| [INLINE_CODE_7] | Indicates whether the operator is the administrator of the account. This is a read-only field.                                                                                                                                                                                          | Boolean   |
| [INLINE_CODE_8]            | The backup email address for this operator.                                                                                                                                                                                                                                             | String    |
| [INLINE_CODE_9]               | Indicates whether this operator is currently on duty.                                                                                                                                                                                                                                   | Boolean   |
| [INLINE_CODE_10]            | If filled, this sets the culture for this operator. Possible values: en-US, en-GB, fr-FR, de-DE, nl-NL or empty. When this value is set to empty, the overal account culture/language will be used.                                                                                     | String    |
| [INLINE_CODE_11]             | Optional. The Id for the time zone setting for this user. Please refer to the Timezone API mentioned below for available values. If not specified, the account's time zone will be used for this user.                                                                                  | Short     |
| [INLINE_CODE_12]            | The SMS provider used by the operator. Possible values: UseAccountSetting, SmsProviderEurope, SmsProviderEurope2, SmsProviderUSA, SmsProviderInternational                                                                                                                              | String    |
| [INLINE_CODE_13]       | If the SMS provider is configured specifically for this operator, this field indicates whether a numeric sender should be used.                                                                                                                                                         | Boolean   |
| [INLINE_CODE_14]          | The provider used for phone alerts.                                                                                                                                                                                                                                                     | String    |
| [INLINE_CODE_15]       | If Native Login (username/password) is available and configured for your account, this indicates whether this operator is allowed to log onto Uptrends using their Uptrends username and password. Possible values: True, False or keep unspecified to use the overall account setting. | Boolean   |
| [INLINE_CODE_16]      | If Single Signon is available and configured for your account, this indicates whether this operator is allowed to use Single Sign-on.Possible values: True, False or keep unspecified to use the overall account setting.                                                               | Boolean   |

## Operator endpoints

The following API endpoints for retrieving, creating, updating and removing operators are available:

| Request type | Endpoint                                                 | Usage                                                                                                             |
|--------------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| GET          | [INLINE_CODE_17]                                              | Gets all operators.                                                                                               |
| GET          | [INLINE_CODE_18]                               | Gets the details of an operator.                                                                                  |
| POST         | [INLINE_CODE_19]                                              | Creates a new operator.                                                                                           |
| PUT          | [INLINE_CODE_20]                               | Updates an existing operator.                                                                                     |
| DELETE       | [INLINE_CODE_21]                               | Deletes an existing operator. Note: you cannot delete the operator associated with the API account you are using. |
| GET          | [INLINE_CODE_22]                  | Gets the off-duty schedules for an existing operator.                                                                 |
| POST         | [INLINE_CODE_23]                  | Adds an off-duty schedule for an existing operator.                                                                    |
| PUT          | [INLINE_CODE_24] | Updates the specified off-duty schedule.                                                                              |
| DELETE       | [INLINE_CODE_25] | Deletes the specified off-duty schedule.                                                                              |

#### GET Operator

This GET request will return a collection containing all operators, including the account administrator.

[CODE_BLOCK_1]
#### GET Operator/{operatorGuid}

This GET request will return the details of the specific operator identified by the operator GUID specified.

Example output:

[CODE_BLOCK_2]

#### POST Operator

This will create a new operator with the details provided.

Example input:

[CODE_BLOCK_3]

The response will contain the created operator, including the operator GUID that was assigned:

[CODE_BLOCK_4]


#### PUT Operator/{operatorGuid}

This method will update the operator identified by the operator GUID specified, using the data provided in the request.

Example input:

[CODE_BLOCK_5]


#### DELETE Operator/{operatorGuid}

This method will delete the operator identified by the operator GUID specified, using the data provided in the request.

## Operator off-duty schedule object description

| Name            | Description                                                                                               | Data type |
|-----------------|-----------------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_26]            | The unique identifier for this off-duty schedule. This field is readonly and will be automatically generated. | Guid      |
| [INLINE_CODE_27]  | The schedule mode. Possible values: OneTime, Daily, Weekly, Monthly                                       | String    |
| [INLINE_CODE_28] | The start date and time (for a one-time schedule)                                                         | DateTime  |
| [INLINE_CODE_29]   | The end date and time (for a one-time schedule)                                                           | DateTime  |
| [INLINE_CODE_30]       | The day of the week (for a weekly schedule). Possible values: Monday, Tuesday, ..., Sunday.               | String    |
| [INLINE_CODE_31]      | The date of the month (for a monthly schedule)                                                            | Int       |
| [INLINE_CODE_32]     | The start time (for a daily, weekly or monthly schedule). Format: “HH:mm”, in 24-hour format.             | String    |
| [INLINE_CODE_33]       | The end time (for a daily, weekly or monthly schedule). Format: “HH:mm”, in 24-hour format.               | String    |

## Operator off-duty schedule endpoints

The following API endpoints are available for retrieving, creating, updating and deleting off-duty schedules for a specific operator:

#### GET Operator/{operatorGuid}/DutySchedule

This method will return a collection containing all off-duty schedules for the specified operator.

Example output:

[CODE_BLOCK_6]
#### POST Operator/{operatorGuid}/DutySchedule

This method will create a new off-duty schedule for the specified operator.

Example input (for a weekly schedule):

[CODE_BLOCK_7]
As you can see in this example, you are expected to only specify the parameters that are relevant to the schedule type you’re creating. For example, the MonthDay is not relevant for a weekly schedule, and StartDateTime and EndDateTime are only for one-time schedules.

Elaborating on this a bit more, a daily schedule, does not expect a weekday value, just ScheduleMode “Daily” and a start time and end time. Similarly, a monthly schedule only expects ScheduleMode “Monthly”, the month day, the start time and the end time.

When you create a new off-duty schedule, the output contains the Id of the new schedule. Example output for creating a daily schedule:

[CODE_BLOCK_8]

#### PUT Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

This method will update the off-duty schedule with the specified off-duty schedule ID, for the specified operator.Example input:

[CODE_BLOCK_9]
#### DELETE Operator/{operatorGuid}/DutySchedule/{dutyScheduleId}

This method will delete the off-duty schedule with the specified off-duty schedule ID, for the specified operator.

## Timezone object description

| Name                   | Description                                                                                      | Data type |
|------------------------|--------------------------------------------------------------------------------------------------|-----------|
| [INLINE_CODE_34]           | The unique identifier for this time zone                                                         | Short     |
| [INLINE_CODE_35]          | The description for this time zone                                                               | String    |
| [INLINE_CODE_36]        | The offset from UTC in minutes                                                                   | Short     |
| [INLINE_CODE_37]    | Whether or not this time zone has daylight saving time                                            | Boolean   |
| [INLINE_CODE_38] | The offset, in minutes, for daylight saving time. Not specified when HasDaylightSaving is false. | Short     |

## Timezone endpoints

The following methods can be used to retrieve time zone information. You can use this data to identify which timezoneId to use, when you want to specify a timezoneId for an operator's settings.

#### GET Timezone

This GET request will return a collection containing all time zones.

Example output:

[CODE_BLOCK_10]
#### GET Timezone/{timezoneId}

This method will get the time zone details for the time zone with the specified Id.

Example output:

[CODE_BLOCK_11]