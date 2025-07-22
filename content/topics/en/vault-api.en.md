{
  "hero": {
    "title": "Vault API"
  },
  "title": "Vault API",
  "url": "/support/kb/api/vault-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/vault-api"
}

The Vault is used to store reusable data, often sensitive data like certificates, public keys, and username/password combinations. Each entry in the Vault is called a *vault item*, and vault items are organized in *vault sections*. Organizing items into different sections is also helpful for restricting access to particular operators and groups.

This article describes the available API methods for managing vault items, vault sections and vault section authorizations. For a discussion of Vault usage scenarios, please read the [Vault introduction]({{< ref path="/support/kb/account/vault" lang="en" >}}). To learn how to get access to the API, refer to [API v4 introduction]({{< ref path="/support/kb/api/v4" lang="en" >}}).

## Vault items

This set of endpoints lets you retrieve, create, update and delete individual vault items. Due to the sensitive nature of some vault item types, the sensitive data itself is never returned.

### Vault item object description

The following VaultItem object is used in the API methods described below:

| Name | Description |
|------|-----------------------------|
| `VaultItemGuid` | The unique identifier of the vault item. |
| `Name` | The display name of the vault item. |
| `VaultSectionGuid	` | The unique identifier of the vault section in which this vault item is stored. |
| `VaultItemUsedBy` | Indicates which items or monitors are using the vault item. |
| `VaultItemType` | Defines the type of vault item. Currently, the supported types are: {{< tableformatter >}}

- `CertificateArchive`: for certificate archive files (i.e. .pfx files), used for client certificates in Multi-step API monitors.
- `Certificate`: for public keys, used for Single Sign-On configuration.
- `CredentialSet`: for username/password combinations, used for authentication settings in monitors.
- `File`: for file storage, used for self-service transaction monitors. Any file format is supported, with a maximum size limit of 2MB.
- `OneTimePassword`: for one-time password generation, contains a secret value and is used for two-factor authentication.
{{< /tableformatter >}} |
| `Value` | The value stored in the vault item. The content of this field depends on the type of vault item: {{< tableformatter >}} 
- For type `CertificateArchive`: specify a Base-64 encoding of your binary .pfx file when you create or update a vault item of this type. When you retrieve the item again, the Value field will always be empty (since it is sensitive information).
- For type `Certificate`: specify the text content of your public key when you create or update a vault item of this type. When you retrieve the item again, the Value field contains the original public key data.
- For type `CredentialSet`: this field is unused. Use the UserName and Password fields instead.
{{< /tableformatter >}} |
| `IsSensitive` | Indicates whether the value stored in the vault item is encrypted. When a vault item has this set to true, the value or values stored will not be exposed to the web application or the API. This value should not be specified when creating a new item: `CertificateArchive` and `CredentialSet` items are always encrypted (since they contain sensitive data by definition) while a `Certificate` public key is inherently public information and can be stored as plain text. |
| `Notes` | Notes or description pertaining to this vault item. |
| `UserName` | The username part of a credentialset. |
| `Password` | The password of a credentialset. |

### Vault item endpoints

The following API methods are available:

| Request type | Endpoint                    | Usage                                                               |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET          | `VaultItem`                 | Returns all vault items in sections the user context has access to. |
| GET          | `VaultItem/{VaultItemGuid}` | Returns the specified vault item.                                   |
| POST         | `VaultItem`                 | Creates a new vault item with the specified values.                 |
| PUT          | `VaultItem/{VaultItemGuid}` | Updates the specified vault item.                                   |
| PATCH        | `VaultItem/{VaultItemGuid}` | Partially updates certain parts of the specified vault item. The `VaultItemType` and `VaultItemUsedBy` cannot be changed and remain as is in this operation. |
| DELETE       | `VaultItem/{VaultItemGuid}` | Deletes the specified vault item.                                   |

#### GET /VaultItem

The GET request `VaultItem` has no parameters. It will return a list containing all vault items from sections you have view access to.

Example content:

```json
[
  {
    "VaultItemGuid": " FE1656C1-A606-43BB-BD61-1EEE9715EE9E ",
    "Name": "Web shop test login",
    "Value": "",
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "test@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
    "VaultItemUsedBy": "1 monitor"
  },
  {
    "VaultItemGuid": "A9CB1BE3-1715-4C31-9040-51CBBFAE23CB",
    "Name": "Marketing web site login",
    "Value": "",
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F ",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "testmarketing@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
  "VaultItemUsedBy": "-"
  }
]
```

#### GET /VaultItem/{VaultItemGuid}

The GET request `VaultItem/{VaultItemGuid}` will return the vault item identified by the vault item Guid.

Example of a vault item returned in the content of a 200 response:
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "IsSensitive": true,
  "Notes": "Certificate archive test",
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Issuer": "Acme Corp, Inc.",
    "NotBefore": "2018-06-12T14:10:50.489Z",
    "NotAfter": "2020-06-12T14:10:50.489Z",
    "Password": "",
    "ArchiveData": ""
  },
  "VaultItemUsedBy": "1 monitor"
}
```

Please note that values that contain sensitive information are returned as an empty string.

#### PUT /VaultItem/{VaultItemGuid}

The PUT request to endpoint `VaultItem/{VaultItemGuid}` will update the vault item identified by the vault item guid. As soon as you update a vault item, any monitor that contains a reference to this vault item will also be updated, so your change is effective immediately.

This request requires ChangeVaultSection authorization.

A PUT request expects the following object structure:
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CredentialSet",
  "IsSensitive": true,
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

In the above example, if there was a value in the original vault items Notes field, the Notes field will be emptied. `If you omit a parameter, it will not remain unchanged, but be considered empty.` The only values that do not need to be supplied are the sensitive values. If, for instance, you leave out the Value or Password field, or the entire CertificateArchive object, these will remain unchanged. Furthermore, the attributes IsSensitive and VaultSectionGuid cannot be changed.

#### DELETE /VaultItem/{VaultItemGuid}

The DELETE request to endpoint `VaultItem/{VaultItemGuid}` will delete the requested vault item.

If the vault item specified is still in use (for instance, a monitor refers to that particular vault item), the service will return status code 400, including a relevant message. This request requires ChangeVaultSection authorization.

#### POST /VaultItem

The POST request to endpoint `VaultItem` will create a new VaultItem object. When specifying the VaultItem data, omit the VaultItemGuid: the new Guid for this item will be returned as part of the response. This request requires ChangeVaultSection authorization.

Example content:
```json
{
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "Notes": "Certificate archive test",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

## Vault sections

There are several endpoints in this API that lets you manage your vault sections. Each vault item belongs to exactly one vault section. If you only need a few vault items in your entire account, you can simply keep them in a single vault section. However, if the number of vault items in your accounts is growing, you may want to start organizing them into separate sections.

Every Uptrends account starts out with one default vault section. The Administrators group has full access to this section, which means they can edit the section, and any of the vault items contained in that section.

When a new vault section is created, the user (operator) associated with the API account that creates the vault section automatically gets the ChangeVaultSection authorization for the new section. No other authorizations will be created.

### Vault section object description

The following VaultSection object is used in the API methods described below:

| Name               | Description                                |
|--------------------|--------------------------------------------|
| `VaultSectionGuid` | The unique identifier of the vault section |
| `Name`             | The name of the vault section              |

### Vault section endpoints

| Request type | Endpoint                          | Usage                                                      |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET          | `VaultSection`                    | Returns all vault sections the user context has access to. |
| GET          | `VaultSection/{VaultSectionGuid}` | Returns the specified vault section.                       |
| POST         | `VaultSection`                    | Creates a new vault section with the specified name.       |
| PUT          | `VaultSection/{VaultSectionGuid}` | Updates the specified vault section.                       |
| DELETE       | `VaultSection/{VaultSectionGuid}` | Deletes the specified vault section.                       |

#### GET /VaultSection

The GET request `VaultSection` has no parameters. It will return a list containing all vault sections you have view access to.

Example content:
```json
[
  {
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "Name": "Vault items"
  },
  {
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F",
    "Name": "Marketing web site vault items"
  }
]
```

#### GET /VaultSection/{VaultSectionGuid}

The GET request `VaultSection/{VaultSectionGuid}` will return the vault section identified by the vault section Guid.

Example content:
```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Vault items"
}
```


#### POST /VaultSection

The POST request to endpoint `VaultSection` will create a new VaultSection object. The operator under whose user context the request is issued will be given ViewVaultSection and ChangeVaultSection authorizations to the new section. No other authorizations are granted. When specifying the VaultSection data, omit the VaultSectionGuid: the new Guid for this item will be returned as part of the response.
```json
{
  "Name": "Development vault items"
}
```

#### PUT /VaultSection/{VaultSectionGuid}

The PUT request to endpoint `VaultSection/{VaultSectionGuid}` will update the vault section identified by the vault item guid. Typically, the only purpose of this is to change the vault section name. This request requires ChangeVaultSection authorization.

```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Web shop vault items"
}
```

#### DELETE /VaultSection/{VaultSectionGuid}

The DELETE request to endpoint `VaultSection/{VaultSectionGuid}` will delete the requested vault section.

If the vault section specified is still in use (meaning there are vault items stored in that section), the service will return status code 400, including a relevant message. If this is the case, you will need to delete the vault items before you can delete the vault section. Keep in mind that you cannot delete a vault item if the item is still in use (for instance, when a monitor is configured to use that vault item). This request requires ChangeVaultSection authorization.

## Vault section authorizations

Aside from keeping vault items separated, vault sections also allow you to control who has access to what. If you need a specific group of operators to have exclusive access to certain vault items, put those vault items in a separate section. Only people who have access to that vault section can see the vault items contained in that section.

As soon as you create a new vault section (either through the API or using the online app), that section is only visible to you at first. If you added vault items to it, other operators would not be able to edit or use those vault items.

In order to let other people use the new vault section, add items to it and/or let them select those vault items in monitor settings, you'll need to give them access. You can accomplish this with the following API methods.

There are two types of authorizations: `ViewVaultSection` and `ChangeVaultSection`. These authorization types can be granted to operators and operator groups.

### Authorization object description

The following Authorization object is used in the API methods described below:

| Name                | Description                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AuthorizationId`   | The unique id of the authorization.                                                                                                                        |
| `ContextId`         | The unique identifier of the context for which the authorization is created. In the case of a vault section authorization, this is the vault section Guid. |
| `AuthorizationType` | `ViewVaultSection` or `ChangeVaultSection`.                                                                                                                |
| `OperatorGuid`      | If the authorization is to be applied to a single operator, this specifies the operator Guid. Set to `null` for operator group authorizations.             |
| `OperatorGroupId`   | If the authorization is to be applied to an operator group, this specifies the operator group ID. Set to `null` for single operator authorizations.        |

### Vault section authorization endpoints

| Request type | Endpoint                                                            | Usage                                                                                   |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET          | `VaultSection/{VaultSectionGuid}/Authorization`                     | Returns a list of all authorizations for the vault section specified.                   |
| POST         | `VaultSection/{VaultSectionGuid}/Authorization`                     | Creates a new authorization for the specified vault section, using the values provided. |
| DELETE       | `VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}` | Deletes the specified authorization.                                                    |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

The GET request to `VaultSection/{VaultSectionGuid}/Authorization` returns a list of all authorizations for the vault section specified in VaultSectionGuid.

Example content:
```json
[
  {
    "AuthorizationId": "7210DD2D-3AAE-4F89-A2A8-000060F118F1 ",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ChangeVaultSection",
    "OperatorGuid": "5F71AFD7-8BEE-4C8D-9827-A107308473BE",
    "OperatorGroupId": ""
  },
  {
    "AuthorizationId": "0BACEE61-0582-40FD-B1A2-00034401421A",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ViewVaultSection",
    "OperatorGuid": "",
    "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
  }
]
```


An authorization is either for an operator, or for an operator group. An operator-specific authorization will have the OperatorGuid populated and the OperatorGroupId empty; an authorization for an operator group will have a value in OperatorGroupId, and an empty OperatorGuid.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

The POST request to `VaultSection/{VaultSectionGuid}/Authorization` will create a new authorization for the specified vault section.

Example content:

```json
{
  "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "AuthorizationType": "ViewVaultSection",
  "OperatorGuid": "",
  "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
}
```

If you create an authorization of type ChangeVaultSection, an additional ViewVaultSection authorization for the same operator or operator group will be added automatically. If an operator or operator group has Change \+ View authorizations for a vault section, this will show up as *Full control* in the Uptrends app.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

The DELETE request to `VaultSection/{VaultSectionGuid}/ Authorization/AuthorizationGuid` will delete an existing authorization.
