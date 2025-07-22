{
  "hero": {
    "title": "Alert definition permissions"
  },
  "title": "Alert definition permissions",
  "summary": "",
  "url": "/support/kb/alerting/alert-definition-permissions",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alert-definition-permissions"
}

{{< callout >}}Alert definition permissions are only available to **Enterprise-level** accounts.{{< /callout >}}

Alert definitions in Uptrends are used to define when alerts are generated at which escalation level and which messages are sent to operators or systems by means of integrations. The alert definitions are crucial to your monitoring and alerting, therefore you want to control who can change them. The alert definition permissions let you do just that.

The permissions are set in two places; e.g. the **Edit alert definition** permission is set on an alert definition and the **Create alert definitions** is set for an operator or operator group. This is how the Uptrends permission system works where some permission are set for an item (like a monitor or an alert definition) and some are set for operators or operator groups.  

The permissions set on an alert definition are described in this article. For the the **Create alert definition** permission take a look at the knowledge base article [Permissions]({{< ref path="support/kb/account/users/operators/permissions#create-alert-definition" lang="en" >}}) that are related to operators.

## Who can manage permissions?

The alert definition permissions can be set and changed by administrators in general. 
Additionally, an operator with both the permissions **Create alert definitions** (set for an operator or operator group) and **Edit alert definition** (set on an alert definition) can also manage the permissions of that specific definition. 

## Permission types

### Edit alert definition

This permission gives the operator or operator group the right to change an alert definition.

A few things need to be taken into account:

- The operator may change the alert definition and add or remove monitors and monitor groups to or from it. This applies to all monitors the operator can view as set in the [monitor permissions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}}) for that operator. If the operator does not have the view permission on a certain monitor (group), they won't be able to select it in the alert definition.

- The operator may change the alert definition and add/remove operators or operator groups. This works only for operators or operator groups where the editing operator has view access rights for. 

- It is possible that other operators add monitors or monitor groups that you cannot see, because you don't have the view permission. The same is true for operators or operator groups. In case that there a hidden items attached to the alert definition, a note will be shown about this.

- The edit alert definition permission includes the right to delete the definition. This works only if there are no items (monitors/monitor groups or operators/operator groups) attached to the definition that are not visible to you because of lacking view permissions.

## Managing permissions

The permissions for alert definitions can be set either from the alert definition or from an operator group. Any change made in one place is reflected in the other one.
### Set up permissions through operator groups

1. Go to {{< AppElement type="menuitem" >}} Account setup > Operators, groups (and subaccounts) {{< /AppElement >}}.
2. Click {{< AppElement type="buttonPrimary" >}} View all operator groups {{< /AppElement >}} to get to the overview of operator groups for your account.
3. Select the group you want to add permissions for and open the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab.
   ![screenshot operator group permissions tab](/img/content/scr_alert-definition-permissions-operatorgroups.min.png)
4. In the **Alert definition permissions** section, add an alert definition by choosing it from the drop-down list. To remove an alert definition from the operator group, click the x right to the definition's name.
5. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to save the changes.

### Set or change permissions inside the alert definition

1. Go to {{< AppElement type="menuitem" >}} Alerting > Alert definitions {{< /AppElement >}}.
2. In the list of alert definitions, click the one you want to edit.
3. Open the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab.
4. Click the {{< AppElement type="buttonPrimary" >}} Add permission {{< /AppElement >}} button.
5. From the pop-up dialog choose the operator group and the permission, then click the {{< AppElement type="buttonPrimary" >}} Add {{< /AppElement >}} button.
6. To remove a permission, select {{< AppElement type="deletebutton" >}} Delete {{< /AppElement >}} from the list **Permissions**.
7. Select {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to save the changes you just made.