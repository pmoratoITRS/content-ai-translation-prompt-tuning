{
  "hero": {
    "title": "Vault security"
  },
  "title": "Vault security",
  "url": "/support/kb/account/vault-security",
  "translationKey": "https://www.uptrends.com/support/kb/account/vault-security"
}

## Vault security feature

Uptrends ensures that all sensitive information in the **Vault** are encrypted and stored securely.

Whenever you create a [Vault item]({{< ref path="/support/kb/account/vault" lang="en" >}}), all your sensitive data are automatically encrypted by the **Vault Engine** before storing in the database. The **Vault Engine** utilizes a cryptography library that adheres to the Advanced Encryption Standard (AES) for data encryption. This process involves further steps to be executed, such as generating encryption keys for each Uptrends environment.

Additionally, Uptrends strictly and regularly updates the passphrase, minimizing the risk of attacks and enabling secure access to sensitive data. Access to these protocols are carefully controlled and implemented, ensuring users that secrets are hidden and restricted from Uptrends employees.

As part of Uptrends data security, any secrets stored in the **Vault** cannot be retrieved from the Uptrends web application or the [Vault API]({{< ref path="/support/kb/api/vault-api" lang="en" >}}). If you have a [Credential set]({{< ref path="/support/kb/account/vault#credential-set" lang="en" >}}), only specific information such as Vault description, Vault Item Guid, Vault Section Guid, username, and others are accessible. Other than that, Uptrends displays secrets as masked values (`*****`). These values can be updated and deleted anytime but are not decrypted or viewable in any case. 

Similarly, Uptrends validates the [Permissions]({{< ref path="/support/kb/account/vault#vault-permissions" lang="en" >}}) and usage of each vault item. If you don't have permission to access a vault item used in a monitor, updating the monitor settings and using the **Test Now** functionalities are disabled. This behavior prevents unauthorized users from sending the value of the vault item in situations, such as sending it to external endpoints like webhook sites. Also, this implies that users with access mainly control which monitors or endpoints uses vault items. Therefore, you must also be responsible to avoid exposing your secrets unintentionally.

This way, all your sensitive data are protected from potential risks and vulnerabilities.