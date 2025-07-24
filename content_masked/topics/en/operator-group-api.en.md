{
  "hero": {
    "title": "Operator Group API"
  },
  "title": "Operator Group API",
  "summary": "The available API methods for manipulating operator groups.",
  "url": "[URL_BASE_TOPICS]api/operator-group-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

This page describes the available API methods for manipulating operator groups. Operator groups are used to organize the operators (user accounts) in your account. This API provided methods for managing each group, and for adding/removing operators to and from a group.

## Operator group object description

The following OperatorGroup object is used in the API methods described below:

| Name                   | Description                                                 | Data type |
|------------------------|-------------------------------------------------------------|-----------|
| [INLINE_CODE_1]    | The unique identifier for this operator group.              | Guid      |
| [INLINE_CODE_2]          | A string containing a descriptive name.                     | String    |
| [INLINE_CODE_3]           | Indicates whether this is the “Everyone” system group.      | Boolean   |
| [INLINE_CODE_4] | Indicates whether this is the “Administrators” system group | Boolean   |

The "Everyone" group is an automatic, system-created group. The Everyone group cannot be changed: each operator is automatically added to this group.

The "Administrators" is also a system-created group, but you can add individual operators to it or remove them again from this group. When an operator is added as a member of the Administrators group, all administrative privileges are automatically assigned to that operator.

## OperatorGroup endpoints

The following API endpoints for retrieving, creating, updating and removing operator groups are available:

| Request type | Endpoint                                                           | Usage                                                         |
|--------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| GET          | [INLINE_CODE_5]                                                   | Gets all operator groups.                                     |
| GET          | [INLINE_CODE_6]                               | Gets the details of an operator group.                        |
| POST         | [INLINE_CODE_7]                                                   | Creates a new operator group.                                 |
| PUT          | [INLINE_CODE_8]                               | Updates an existing operator group.                           |
| DELETE       | [INLINE_CODE_9]                               | Deletes an existing operator group.                           |
| GET          | [INLINE_CODE_10]                        | Gets the off-duty schedules for an existing operator.             |
| POST         | [INLINE_CODE_11]                  | Adds a off-duty schedule to all operators in the specified group. |
| PUT          | [INLINE_CODE_12] | Updates the specified off-duty schedule.                          |
| DELETE       | [INLINE_CODE_13] | Deletes the specified off-duty schedule.                          |

#### GET OperatorGroup

This GET request will return a collection containing all operator groups, including the special system groups.

[CODE_BLOCK_1]

#### GET OperatorGroup/{operatorGroupGuid}

This GET request will return the details of the specific operator group identified by the operator group GUID specified.

Example output:

[CODE_BLOCK_2]

#### POST OperatorGroup

This will create a new operator group with the details provided.

Example input:

[CODE_BLOCK_3]

The response will contain the created operator group, including the operator GUID that was assigned:

json
{
    "OperatorGroupGuid": "2c4abb71-4c40-4f57-bd3d-672c08c4ad82",
    "Description": "Example Operator Group"
} 
```


#### DELETE OperatorGroup/{operatorGroupGuid}

This method will delete the operator group identified by the operator GUID specified, using the data provided in the request.
