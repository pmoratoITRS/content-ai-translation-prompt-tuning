{
  "hero": {
    "title": "Alert definition permissions"
  },
  "title": "Alert definition permissions",
  "summary": "",
  "url": "[URL_BASE_TOPICS]alerting/alert-definition-permissions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]Alert definition permissions are only available to **Enterprise-level** accounts.[SHORTCODE_2]

Alert definitions in Uptrends are used to define when alerts are generated at which escalation level and which messages are sent to operators or systems by means of integrations. The alert definitions are crucial to your monitoring and alerting, therefore you want to control who can change them. The alert definition permissions let you do just that.

The permissions are set in two places; e.g. the **Edit alert definition** permission is set on an alert definition and the **Create alert definitions** is set for an operator or operator group. This is how the Uptrends permission system works where some permission are set for an item (like a monitor or an alert definition) and some are set for operators or operator groups.  

The permissions set on an alert definition are described in this article. For the the **Create alert definition** permission take a look at the knowledge base article [Permissions]([LINK_URL_1]) that are related to operators.

## Who can manage permissions?

The alert definition permissions can be set and changed by administrators in general. 
Additionally, an operator with both the permissions **Create alert definitions** (set for an operator or operator group) and **Edit alert definition** (set on an alert definition) can also manage the permissions of that specific definition. 

## Permission types

### Edit alert definition

This permission gives the operator or operator group the right to change an alert definition.

A few things need to be taken into account:

- The operator may change the alert definition and add or remove monitors and monitor groups to or from it. This applies to all monitors the operator can view as set in the [monitor permissions]([LINK_URL_2]) for that operator. If the operator does not have the view permission on a certain monitor (group), they won't be able to select it in the alert definition.

- The operator may change the alert definition and add/remove operators or operator groups. This works only for operators or operator groups where the editing operator has view access rights for. 

- It is possible that other operators add monitors or monitor groups that you cannot see, because you don't have the view permission. The same is true for operators or operator groups. In case that there a hidden items attached to the alert definition, a note will be shown about this.

- The edit alert definition permission includes the right to delete the definition. This works only if there are no items (monitors/monitor groups or operators/operator groups) attached to the definition that are not visible to you because of lacking view permissions.

## Managing permissions

The permissions for alert definitions can be set either from the alert definition or from an operator group. Any change made in one place is reflected in the other one.
### Set up permissions through operator groups

1. Go to [SHORTCODE_3] Account setup > Operators, groups (and subaccounts) [SHORTCODE_4].
2. Click [SHORTCODE_5] View all operator groups [SHORTCODE_6] to get to the overview of operator groups for your account.
3. Select the group you want to add permissions for and open the [SHORTCODE_7] Permissions [SHORTCODE_8] tab.
   ![screenshot operator group permissions tab]([LINK_URL_3])
4. In the **Alert definition permissions** section, add an alert definition by choosing it from the drop-down list. To remove an alert definition from the operator group, click the x right to the definition's name.
5. Click the [SHORTCODE_9] Save [SHORTCODE_10] button to save the changes.

### Set or change permissions inside the alert definition

1. Go to [SHORTCODE_11] Alerting > Alert definitions [SHORTCODE_12].
2. In the list of alert definitions, click the one you want to edit.
3. Open the [SHORTCODE_13] Permissions [SHORTCODE_14] tab.
4. Click the [SHORTCODE_15] Add permission [SHORTCODE_16] button.
5. From the pop-up dialog choose the operator group and the permission, then click the [SHORTCODE_17] Add [SHORTCODE_18] button.
6. To remove a permission, select [SHORTCODE_19] Delete [SHORTCODE_20] from the list **Permissions**.
7. Select [SHORTCODE_21] Save [SHORTCODE_22] to save the changes you just made.