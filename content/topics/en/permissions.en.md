{
  "hero": {
    "title": "Permissions"
  },
  "title": "Permissions",
  "summary": "The people in your team have different roles and responsibilities. How does that compare to the operators in the Uptrends app?",
  "url": "/support/kb/account/users/operators/permissions",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/permissions"
}

{{< callout >}} The availability of permission types depends on your subscription plan, i.e. some types may or may not be available to you. All permissions are available to **Enterprise-level** accounts. {{< /callout >}}


Users of the Uptrends app are called operators within the app. An operator holds the user's profile with contact info, personal settings, and more.
The operators are members of one or multiple operator groups. More info on this topic can be found in the article [Operators and operator groups]({{< ref path="support/kb/account/users/operators/operator-groups" lang="en" >}}).

Operators have different roles and responsibilities, so they need different permissions within the Uptrends app. One example is the typical administrator role, where the operator has access to everything. Other operators may need access only to certain products or monitors. Or you simply want to restrict who has insight into information or the right to change settings.

The Uptrends app uses two approaches when it comes to permissions: system-wide (or global) permissions which are bound to operator groups (or operators) and permissions bound to specific items. To make the set up easier, both system-wide and item based permissions can be set from the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab of operators or operator groups.

In addition, [item based permissions]({{< ref path="#item-based-permissions" lang="en" >}}) might be set on the item (monitor, alert definition, etc.) directly.

Independent of where you set the permissions, they are reflected in the other, corrresponding location.

## Who can manage permissions?
Only operators with administrator rights can change permissions. The operator has to be a member of the *Administrators* operator group where the *Administrative permissions* are default and mandatory. For Enterprise accounts, you can set up [Operator (group) permissions]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="en" >}}) to give specific permission rights to operator and operator groups.

## Managing permissions

We recommend managing permissions on the operator group level. Technically you can also add permissions to individual operators. In most situations it will be easier to add the operator to the operator group which already has the permissions defined, instead of having to add all the permissions to the operator.

The process for granting and revoking permissions is the same. The steps for operator groups are described below.

To grant a permission follow these steps:

1. Go to the [User management hub]({{< ref path="/support/kb/account/users/operators/user-management-hub" lang="en" >}}) by navigating to {{< AppElement type="menuitem" >}} Account setup > Operators and groups{{< /AppElement >}} in the menu. From here, click {{< AppElement type="buttonPrimary" >}} View all operator groups {{< /AppElement >}} to get to the overview of operator groups for your account.
2. Select the group you want to add permissions for.
  The permissions are located on the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab on the *Operator group* page.
3. Choose the **System-wide permissions** you wish to assign or revoke by selecting or clearing their respective boxes. 
![Operator group permissions](/img/content/scr_operatorgroup-permissions-091624.min.png)
4. Set up [item-based permissions]({{< ref path="#item-based-permissions" lang="en" >}}) for monitors and alert definitions and more.
5. Click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} to save the changes you just made.

## Permission types

All permission types are available on operator and operator group level, unless otherwise mentioned. Some permissions are mandatory, details can be found in the permission descriptions below.

### Basic operator {id="basic-operator"}

This permission is added to every new operator by default, and is not visible from the operator group settings. 

The permission includes the right to log in, view monitors and dashboards.

Only an administrator within an Enterprise subscription plan can grant or revoke this permission and it can be set for individual operators and for groups.
Once this permission is revoked, the operator can only log in and go to a [protected status page]({{< ref path="/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages#protected-status-pages" lang="en" >}}). No other actions are available anymore.

### Administrative permissions

This permission is mandatory for the default operator group *Administrators* and cannot be given to any other operator group or individual operator.

If operators need to have administrative rights, add them to the operator group *Administrators*.

### Create alert definitions {id="create-alert-definition"}

If an operator (or the operator group) has this permission, they can create new alert definitions. Note that there is also the related permission [Edit alert definition]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="en" >}}) which is set in the alert definition itself and not for an operator or operator group.

Once you've created an alert definition you will automatically get the **Edit alert definition** permission for that definition. This is to ensure that you can make changes to the alert definition for later maintenance.

The combination of the permissions **Create alert definitions** and **Edit alert definition** also gives you the right to change permissions of the alert definition. This way you can share your own alert definition with other operators.

Administrators have the **Create alert definitions** permission by default.

### Create integration {id="create-integration"}

This permission gives you the right to create integrations in general. And once you created an integration, you automatically get the [Edit integration]({{< ref path="support/kb/alerting/integrations/integrations-permissions#edit-integration" lang="en" >}}) permission for it. This way you can maintain the integration afterwards.

Administrators have the **Create integration** permission by default.

### Financial operator {id="financial-operator"}

An operator with this permission can place orders, view invoices, and make payments.   
The operator will get notified about account expiration, reaching the SMS credits limit, and will also receive payment reminders. 

It is mandatory to have at least one operator within your Uptrends' account with this permission. It is included in the *Administrators* group's permissions by default.
### Infra access

If you have a subscription to Uptrends Infra, you can give operators access to this product.

This permission is mandatory for the default operator group *Administrators*.
### Technical contact

The permission is set for the operator who should be contacted regarding any technical problems. 

It is mandatory to have at least one operator with the permission type *Technical contact*. Additional technical contact permissions may be added and deleted, provided that you always keep at least one operator with this permission.

### Manage private locations {id="manage-private-locations"}

Operators who have the *Manage private locations* permission type can create, delete or manage existing [private locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations" lang="en" >}}) within the account. For operators to create a private location, they need access to at least one [monitor group]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups#permission-types" lang="en" >}}) with permission type *Create and delete monitors in group*. 
The *Manage private locations* permission is included in the *Administrators* group’s permissions by default.

### Manage monitor templates {id="manage-monitor-templates"}

Operators granted the *Manage monitor templates* permission can manage and apply [monitor templates]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="en" >}}) to those monitors within the account to which they have edit rights, without the need for additional administrative rights.

## Item-based permissions {id="item-based-permissions"}

The following permissions are set on the item, e.g. integration, monitor, while system-wide permissions are set globally.

- [Alert definitions]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="en" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
 lang="en" >}})
- [Integrations]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="en" >}})
- [Monitors]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}})
- [Vault]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="en" >}})
- [Operators and operator groups]({{< ref path="/support/kb/account/users/operators/operator-permissions" lang="en" >}})