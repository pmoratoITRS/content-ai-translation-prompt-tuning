{
  "hero": {
    "title": "Vault API"
  },
  "title": "Vault API",
  "url": "[URL_BASE_TOPICS]api/vault-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The Vault is used to store reusable data, often sensitive data like certificates, public keys, and username/password combinations. Each entry in the Vault is called a *vault item*, and vault items are organized in *vault sections*. Organizing items into different sections is also helpful for restricting access to particular operators and groups.

This article describes the available API methods for managing vault items, vault sections and vault section authorizations. For a discussion of Vault usage scenarios, please read the [Vault introduction]([LINK_URL_1]). To learn how to get access to the API, refer to [API v4 introduction]([LINK_URL_2]).

## Vault items

This set of endpoints lets you retrieve, create, update and delete individual vault items. Due to the sensitive nature of some vault item types, the sensitive data itself is never returned.

### Vault item object description

The following VaultItem object is used in the API methods described below:

| Name | Description |
|------|-----------------------------|
| [INLINE_CODE_1] | The unique identifier of the vault item. |
| [INLINE_CODE_2] | The display name of the vault item. |
| [INLINE_CODE_3] | The unique identifier of the vault section in which this vault item is stored. |
| [INLINE_CODE_4] | Indicates which items or monitors are using the vault item. |
| [INLINE_CODE_5] | Defines the type of vault item. Currently, the supported types are: [SHORTCODE_1]

- [INLINE_CODE_6]: for certificate archive files (i.e. .pfx files), used for client certificates in Multi-step API monitors.
- [INLINE_CODE_7]: for public keys, used for Single Sign-On configuration.
- [INLINE_CODE_8]: for username/password combinations, used for authentication settings in monitors.
- [INLINE_CODE_9]: for file storage, used for self-service transaction monitors. Any file format is supported, with a maximum size limit of 2MB.
- [INLINE_CODE_10]: for one-time password generation, contains a secret value and is used for two-factor authentication.
[SHORTCODE_2] |
| [INLINE_CODE_11] | The value stored in the vault item. The content of this field depends on the type of vault item: [SHORTCODE_3] 
- For type [INLINE_CODE_12]: specify a Base-64 encoding of your binary .pfx file when you create or update a vault item of this type. When you retrieve the item again, the Value field will always be empty (since it is sensitive information).
- For type [INLINE_CODE_13]: specify the text content of your public key when you create or update a vault item of this type. When you retrieve the item again, the Value field contains the original public key data.
- For type [INLINE_CODE_14]: this field is unused. Use the UserName and Password fields instead.
[SHORTCODE_4] |
| [INLINE_CODE_15] | Indicates whether the value stored in the vault item is encrypted. When a vault item has this set to true, the value or values stored will not be exposed to the web application or the API. This value should not be specified when creating a new item: [INLINE_CODE_16] and [INLINE_CODE_17] items are always encrypted (since they contain sensitive data by definition) while a [INLINE_CODE_18] public key is inherently public information and can be stored as plain text. |
| [INLINE_CODE_19] | Notes or description pertaining to this vault item. |
| [INLINE_CODE_20] | The username part of a credentialset. |
| [INLINE_CODE_21] | The password of a credentialset. |

### Vault item endpoints

The following API methods are available:

| Request type | Endpoint                    | Usage                                                               |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET          | [INLINE_CODE_22]                 | Returns all vault items in sections the user context has access to. |
| GET          | [INLINE_CODE_23] | Returns the specified vault item.                                   |
| POST         | [INLINE_CODE_24]                 | Creates a new vault item with the specified values.                 |
| PUT          | [INLINE_CODE_25] | Updates the specified vault item.                                   |
| PATCH        | [INLINE_CODE_26] | Partially updates certain parts of the specified vault item. The [INLINE_CODE_27] and [INLINE_CODE_28] cannot be changed and remain as is in this operation. |
| DELETE       | [INLINE_CODE_29] | Deletes the specified vault item.                                   |

#### GET /VaultItem

The GET request [INLINE_CODE_30] has no parameters. It will return a list containing all vault items from sections you have view access to.

Example content:

[CODE_BLOCK_1]

#### GET /VaultItem/{VaultItemGuid}

The GET request [INLINE_CODE_31] will return the vault item identified by the vault item Guid.

Example of a vault item returned in the content of a 200 response:
[CODE_BLOCK_2]

Please note that values that contain sensitive information are returned as an empty string.

#### PUT /VaultItem/{VaultItemGuid}

The PUT request to endpoint [INLINE_CODE_32] will update the vault item identified by the vault item guid. As soon as you update a vault item, any monitor that contains a reference to this vault item will also be updated, so your change is effective immediately.

This request requires ChangeVaultSection authorization.

A PUT request expects the following object structure:
[CODE_BLOCK_3]

In the above example, if there was a value in the original vault items Notes field, the Notes field will be emptied. [INLINE_CODE_33] The only values that do not need to be supplied are the sensitive values. If, for instance, you leave out the Value or Password field, or the entire CertificateArchive object, these will remain unchanged. Furthermore, the attributes IsSensitive and VaultSectionGuid cannot be changed.

#### DELETE /VaultItem/{VaultItemGuid}

The DELETE request to endpoint [INLINE_CODE_34] will delete the requested vault item.

If the vault item specified is still in use (for instance, a monitor refers to that particular vault item), the service will return status code 400, including a relevant message. This request requires ChangeVaultSection authorization.

#### POST /VaultItem

The POST request to endpoint [INLINE_CODE_35] will create a new VaultItem object. When specifying the VaultItem data, omit the VaultItemGuid: the new Guid for this item will be returned as part of the response. This request requires ChangeVaultSection authorization.

Example content:
[CODE_BLOCK_4]

## Vault sections

There are several endpoints in this API that lets you manage your vault sections. Each vault item belongs to exactly one vault section. If you only need a few vault items in your entire account, you can simply keep them in a single vault section. However, if the number of vault items in your accounts is growing, you may want to start organizing them into separate sections.

Every Uptrends account starts out with one default vault section. The Administrators group has full access to this section, which means they can edit the section, and any of the vault items contained in that section.

When a new vault section is created, the user (operator) associated with the API account that creates the vault section automatically gets the ChangeVaultSection authorization for the new section. No other authorizations will be created.

### Vault section object description

The following VaultSection object is used in the API methods described below:

| Name               | Description                                |
|--------------------|--------------------------------------------|
| [INLINE_CODE_36] | The unique identifier of the vault section |
| [INLINE_CODE_37]             | The name of the vault section              |

### Vault section endpoints

| Request type | Endpoint                          | Usage                                                      |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET          | [INLINE_CODE_38]                    | Returns all vault sections the user context has access to. |
| GET          | [INLINE_CODE_39] | Returns the specified vault section.                       |
| POST         | [INLINE_CODE_40]                    | Creates a new vault section with the specified name.       |
| PUT          | [INLINE_CODE_41] | Updates the specified vault section.                       |
| DELETE       | [INLINE_CODE_42] | Deletes the specified vault section.                       |

#### GET /VaultSection

The GET request [INLINE_CODE_43] has no parameters. It will return a list containing all vault sections you have view access to.

Example content:
[CODE_BLOCK_5]

#### GET /VaultSection/{VaultSectionGuid}

The GET request [INLINE_CODE_44] will return the vault section identified by the vault section Guid.

Example content:
[CODE_BLOCK_6]


#### POST /VaultSection

The POST request to endpoint [INLINE_CODE_45] will create a new VaultSection object. The operator under whose user context the request is issued will be given ViewVaultSection and ChangeVaultSection authorizations to the new section. No other authorizations are granted. When specifying the VaultSection data, omit the VaultSectionGuid: the new Guid for this item will be returned as part of the response.
[CODE_BLOCK_7]

#### PUT /VaultSection/{VaultSectionGuid}

The PUT request to endpoint [INLINE_CODE_46] will update the vault section identified by the vault item guid. Typically, the only purpose of this is to change the vault section name. This request requires ChangeVaultSection authorization.

[CODE_BLOCK_8]

#### DELETE /VaultSection/{VaultSectionGuid}

The DELETE request to endpoint [INLINE_CODE_47] will delete the requested vault section.

If the vault section specified is still in use (meaning there are vault items stored in that section), the service will return status code 400, including a relevant message. If this is the case, you will need to delete the vault items before you can delete the vault section. Keep in mind that you cannot delete a vault item if the item is still in use (for instance, when a monitor is configured to use that vault item). This request requires ChangeVaultSection authorization.

## Vault section authorizations

Aside from keeping vault items separated, vault sections also allow you to control who has access to what. If you need a specific group of operators to have exclusive access to certain vault items, put those vault items in a separate section. Only people who have access to that vault section can see the vault items contained in that section.

As soon as you create a new vault section (either through the API or using the online app), that section is only visible to you at first. If you added vault items to it, other operators would not be able to edit or use those vault items.

In order to let other people use the new vault section, add items to it and/or let them select those vault items in monitor settings, you'll need to give them access. You can accomplish this with the following API methods.

There are two types of authorizations: [INLINE_CODE_48] and [INLINE_CODE_49]. These authorization types can be granted to operators and operator groups.

### Authorization object description

The following Authorization object is used in the API methods described below:

| Name                | Description                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_50]   | The unique id of the authorization.                                                                                                                        |
| [INLINE_CODE_51]         | The unique identifier of the context for which the authorization is created. In the case of a vault section authorization, this is the vault section Guid. |
| [INLINE_CODE_52] | [INLINE_CODE_53] or [INLINE_CODE_54].                                                                                                                |
| [INLINE_CODE_55]      | If the authorization is to be applied to a single operator, this specifies the operator Guid. Set to [INLINE_CODE_56] for operator group authorizations.             |
| [INLINE_CODE_57]   | If the authorization is to be applied to an operator group, this specifies the operator group ID. Set to [INLINE_CODE_58] for single operator authorizations.        |

### Vault section authorization endpoints

| Request type | Endpoint                                                            | Usage                                                                                   |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET          | [INLINE_CODE_59]                     | Returns a list of all authorizations for the vault section specified.                   |
| POST         | [INLINE_CODE_60]                     | Creates a new authorization for the specified vault section, using the values provided. |
| DELETE       | [INLINE_CODE_61] | Deletes the specified authorization.                                                    |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

The GET request to [INLINE_CODE_62] returns a list of all authorizations for the vault section specified in VaultSectionGuid.

Example content:
[CODE_BLOCK_9]


An authorization is either for an operator, or for an operator group. An operator-specific authorization will have the OperatorGuid populated and the OperatorGroupId empty; an authorization for an operator group will have a value in OperatorGroupId, and an empty OperatorGuid.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

The POST request to [INLINE_CODE_63] will create a new authorization for the specified vault section.

Example content:

[CODE_BLOCK_10]

If you create an authorization of type ChangeVaultSection, an additional ViewVaultSection authorization for the same operator or operator group will be added automatically. If an operator or operator group has Change \+ View authorizations for a vault section, this will show up as *Full control* in the Uptrends app.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

The DELETE request to [INLINE_CODE_64] will delete an existing authorization.
