{
  "hero": {
    "title": "Using sensitive transaction data stored in the vault"
  },
  "title": "Using sensitive transaction data stored in the vault",
  "summary": "When you record a transaction, Uptrends stores your sensitive information in the Uptrends vault. Learn how to access and use your sensitive data in your transaction scripts.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The Uptrends vault stores the confidential information you need for your monitoring securely from everyone except for operators with permission. When you record a new transaction or Uptrends converts an older transaction to Self-Service Transactions, Uptrends places any sensitive information such as passwords into the vault for you.

## Accessing your new vault items

You can access your vault items by navigating to [SHORTCODE_1] Account setup > Vault [SHORTCODE_2]. Inside the vault, you can find your new vault items inside *Automatically created vault items*. The vault entry uses the same name as the monitor when you or our support team member first created or converted the monitor.

## Modifying your new vault items

If you have the vault section permission rights to access and modify a vault entry, you can open the item and adjust the name, description, and username. The password is editable but not viewable.

![]([LINK_URL_1])

## Using a vault item in your script

Your imported script already references the vault item, and you can make any changes you need to make to the credentials directly in the vault. You can change which vault item your script access by clicking the ellipse button in the input field. The pop-up dialog allows you to switch to a plain text value, select a different vault item, or add a new vault item.

![]([LINK_URL_2])

We’ve got a separate [article]([LINK_URL_3]) to give you more details about using the vault to protect credentials, public keys, certificates, and files.  The [Uptrends Support]([LINK_URL_4]) team can also help you out with any questions you may have.
