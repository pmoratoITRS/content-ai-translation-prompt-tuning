{
  "hero": {
    "title": "Managing permissions for automatically created vault sections"
  },
  "title": "Managing permissions for automatically created vault sections",
  "summary": "When you record a transaction, Uptrends stores your sensitive information in an automatically created section of the Uptrends Vault using default permissions. Learn how to manage permissions for the automatically created vault items.",
  "url": "/support/kb/synthetic-monitoring/transactions/managing-authorizations-for-automatically-created-vault-sections",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/managing-authorizations-for-automatically-created-vault-sections"
}

The [Uptrends vault](/support/kb/vault) gives you a secure place to store certificates and public keys along with the credentials needed for your transaction scripts. When you create a new transaction monitor using the Transaction Recorder or if Support converts an older monitor to the newer Self-Service Transaction monitoring format, Uptrends automatically places your sensitive data in the vault. Your script will access these vault items rather than having the sensitive values visible in the script or your reporting ([learn more](/support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault) about how to use sensitive values in your script).

## Default permissions used

The vault contains items that it stores in vault sections. Only those individual operators or operators in the included [operator groups](/support/kb/account/users/operators/operator-groups) in the *Permissions* tile of each vault section can access and modify vault items in the section.

**New recordings and newly converted scripts have the default permissions applied to the new automatically created vault section(s)**. The default permissions include the Administrators group and the sub-account's user group if applicable.

Newly uploaded recordings always get added to an automatically created vault section with the default permissions unchanged. If you've changed the permissions, the next upload makes a new section that uses the default permissions.

{{< callout >}}
**Note**: to avoid multiple automatically generated sections, leave the permissions set to the default and replicate vault items in a custom section and delete them from the automatically generated section.
{{< /callout >}}

## Changing the default permissions

You can modify the default permissions on any of your vault sections to make them more or less restrictive by including or excluding groups or operators.

1.  Navigate to {{< AppElement type="menuitem" >}} Account setup > Vault {{< /AppElement >}}.
2.  Click to open the section for which you would like to change the permissions.
3.  To remove permissions, click *Delete* to the right of an operator or a group.
4.  To add permissions, click {{< AppElement type="button" >}}\+ Add permission{{< /AppElement >}} in the **Permissions** tile.
5.  Select the group or operator.
6.  Set the *Permission level* to *View only* or *Full control*.
7.  Click {{< AppElement type="button" >}} Add {{< /AppElement >}}.

![](/img/content/scr-vault-add-permission.min.png)
