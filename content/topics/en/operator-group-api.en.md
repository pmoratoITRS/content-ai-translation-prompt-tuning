{
  "hero": {
    "title": "Operator Group API"
  },
  "title": "Operator Group API",
  "summary": "The available API methods for manipulating operator groups.",
  "url": "/support/kb/api/operator-group-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/operator-group-api"
}

This page describes the available API methods for manipulating operator groups. Operator groups are used to organize the operators (user accounts) in your account. This API provided methods for managing each group, and for adding/removing operators to and from a group.

## Operator group object description

The following OperatorGroup object is used in the API methods described below:

| Name                   | Description                                                 | Data type |
|------------------------|-------------------------------------------------------------|-----------|
| `OperatorGroupGuid`    | The unique identifier for this operator group.              | Guid      |
| `Description`          | A string containing a descriptive name.                     | String    |
| `IsEveryone`           | Indicates whether this is the “Everyone” system group.      | Boolean   |
| `IsAdministratorGroup` | Indicates whether this is the “Administrators” system group | Boolean   |

The "Everyone" group is an automatic, system-created group. The Everyone group cannot be changed: each operator is automatically added to this group.

The "Administrators" is also a system-created group, but you can add individual operators to it or remove them again from this group. When an operator is added as a member of the Administrators group, all administrative privileges are automatically assigned to that operator.

## OperatorGroup endpoints

The following API endpoints for retrieving, creating, updating and removing operator groups are available:

| Request type | Endpoint                                                           | Usage                                                         |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET          | `/OperatorGroup`                                                   | Gets all operator groups.                                     |
| GET          | `/OperatorGroup/{operatorGroupGuid}`                               | Gets the details of an operator group.                        |
| POST         | `/OperatorGroup`                                                   | Creates a new operator group.                                 |
| PUT          | `/OperatorGroup/{operatorGroupGuid}`                               | Updates an existing operator group.                           |
| DELETE       | `/OperatorGroup/{operatorGroupGuid}`                               | Deletes an existing operator group.                           |
| GET          | `/OperatorGroup/{operatorGroupGuid}/Member`                        | Gets the off-duty schedules for an existing operator.             |
| POST         | `/OperatorGroup/{operatorGroupGuid}/DutySchedule`                  | Adds a off-duty schedule to all operators in the specified group. |
| PUT          | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Updates the specified off-duty schedule.                          |
| DELETE       | `/OperatorGroup/{operatorGroupGuid}/DutySchedule/{dutyScheduleId}` | Deletes the specified off-duty schedule.                          |

#### GET OperatorGroup

This GET request will return a collection containing all operator groups, including the special system groups.

```json
[
    {
        "OperatorGroupGuid": "8ceeddfc-acd0-4afb-9cd5-9400ea9d0d49",
        "Description": "Administrators",
        "IsEveryone": false,
        "IsAdministratorsGroup": true
    },
    {
        "OperatorGroupGuid": "983c3592-be7f-47ac-b53f-da856c841e57",
        "Description": "Everyone",
        "IsEveryone": true,
        "IsAdministratorsGroup": false
    },
    {
        "OperatorGroupGuid": "82f4171a-16c3-4bc6-ab4d-56edee7fd6c8",
        "Description": "Main operators",
        "IsEveryone": false,
        "IsAdministratorsGroup": false
    }
]
```

#### GET OperatorGroup/{operatorGroupGuid}

This GET request will return the details of the specific operator group identified by the operator group GUID specified.

Example output:

```json
{
    "OperatorGroupGuid": "27ef4bcf-92bb-4a84-8786-d91b7ceb0b99",
    "Description": "Everyone",
    "IsEveryone": true,
    "IsAdministratorsGroup": false
}
```

#### POST OperatorGroup

This will create a new operator group with the details provided.

Example input:

```json
{
    "Description": "Example Operator Group"
} 
```

The response will contain the created operator group, including the operator GUID that was assigned:

json
{
    "OperatorGroupGuid": "2c4abb71-4c40-4f57-bd3d-672c08c4ad82",
    "Description": "Example Operator Group"
} 
```


#### DELETE OperatorGroup/{operatorGroupGuid}

This method will delete the operator group identified by the operator GUID specified, using the data provided in the request.
