{
  "hero": {
    "title": "Sub account operator management"
  },
  "title": "Sub account operator management",
  "summary": "Beyond the initial setup you will need to manage operators for your sub accounts. In this article we cover adding additional operators and removing operators.",
  "url": "[URL_BASE_TOPICS]account/users/sub-accounts/sub-account-operator-management",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

Sub-account operators have limited permissions. If the sub-account operators have the privileges to modify monitors, they also can add new users, but the sub-account operators cannot remove operators from the sub account. Adding and removing operators is the same as [adding regular operators]([LINK_URL_1]) in the parent account, but when adding and removing operators you need to consider the following:

**You cannot add operators in the *Administrator* group to a sub account**. Administrators can already maintain users and monitors in the sub account, so there is no need to add them to a sub account.

**An operator can only belong to one sub account or regular group at a time** with the exception of the Everyone group.

**You cannot delete an operator that is a member of a sub account**. To delete the sub-account operator:

1.  Open the operator's settings page ([SHORTCODE_3]Account setup > Operators[SHORTCODE_4]).
2.  Click the operator you would like to delete.
3.  Click the [SHORTCODE_5]Member of[SHORTCODE_6] tab.
4.  Uncheck the box next to the sub account in the list.
5.  Click [SHORTCODE_7]Save[SHORTCODE_8].
6.  Reopen the operator's settings page.
7.  Click [SHORTCODE_9]Delete this operator[SHORTCODE_10].

[SHORTCODE_1]
**Note**: Until you delete a sub-account operator that you've removed from a sub-account group, **the operator is still active in your account and has read-only access to the primary account**. Delete sub-account operators immediately after removing them from the sub-account operator group.
[SHORTCODE_2]
