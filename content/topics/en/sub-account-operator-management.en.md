{
  "hero": {
    "title": "Sub account operator management"
  },
  "title": "Sub account operator management",
  "summary": "Beyond the initial setup you will need to manage operators for your sub accounts. In this article we cover adding additional operators and removing operators.",
  "url": "/support/kb/account/users/sub-accounts/sub-account-operator-management",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/sub-accounts/sub-account-operator-management",
  "tableofcontents": false
}

Sub-account operators have limited permissions. If the sub-account operators have the privileges to modify monitors, they also can add new users, but the sub-account operators cannot remove operators from the sub account. Adding and removing operators is the same as [adding regular operators](/support/kb/account/users/operators/operator-groups) in the parent account, but when adding and removing operators you need to consider the following:

**You cannot add operators in the *Administrator* group to a sub account**. Administrators can already maintain users and monitors in the sub account, so there is no need to add them to a sub account.

**An operator can only belong to one sub account or regular group at a time** with the exception of the Everyone group.

**You cannot delete an operator that is a member of a sub account**. To delete the sub-account operator:

1.  Open the operator's settings page ({{< AppElement type="menuitem" >}}Account setup > Operators{{< /AppElement >}}).
2.  Click the operator you would like to delete.
3.  Click the {{< AppElement type="tab" >}}Member of{{< /AppElement >}} tab.
4.  Uncheck the box next to the sub account in the list.
5.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.
6.  Reopen the operator's settings page.
7.  Click {{< AppElement type="deletebutton" >}}Delete this operator{{< /AppElement >}}.

{{< callout >}}
**Note**: Until you delete a sub-account operator that you've removed from a sub-account group, **the operator is still active in your account and has read-only access to the primary account**. Delete sub-account operators immediately after removing them from the sub-account operator group.
{{< /callout >}}
