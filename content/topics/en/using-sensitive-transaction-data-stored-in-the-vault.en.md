{
  "hero": {
    "title": "Using sensitive transaction data stored in the vault"
  },
  "title": "Using sensitive transaction data stored in the vault",
  "summary": "When you record a transaction, Uptrends stores your sensitive information in the Uptrends vault. Learn how to access and use your sensitive data in your transaction scripts.",
  "url": "/support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/using-sensitive-transaction-data-stored-in-the-vault"
}

The Uptrends vault stores the confidential information you need for your monitoring securely from everyone except for operators with permission. When you record a new transaction or Uptrends converts an older transaction to Self-Service Transactions, Uptrends places any sensitive information such as passwords into the vault for you.

## Accessing your new vault items

You can access your vault items by navigating to {{< AppElement type="menuitem" >}} Account setup > Vault {{< /AppElement >}}. Inside the vault, you can find your new vault items inside *Automatically created vault items*. The vault entry uses the same name as the monitor when you or our support team member first created or converted the monitor.

## Modifying your new vault items

If you have the vault section permission rights to access and modify a vault entry, you can open the item and adjust the name, description, and username. The password is editable but not viewable.

![](/img/content/bce5dcae-cd73-4d14-b45d-5eec4a2f703c.png)

## Using a vault item in your script

Your imported script already references the vault item, and you can make any changes you need to make to the credentials directly in the vault. You can change which vault item your script access by clicking the ellipse button in the input field. The pop-up dialog allows you to switch to a plain text value, select a different vault item, or add a new vault item.

![](/img/content/scr_MSA_predefined_variables_1.min.png)

We’ve got a separate [article](https://www.uptrends.com/support/kb/vault) to give you more details about using the vault to protect credentials, public keys, certificates, and files.  The [Uptrends Support](https://www.uptrends.com/contact) team can also help you out with any questions you may have.
