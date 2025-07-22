{
  "hero": {
    "title": "Monitor permissions"
  },
  "title": "Monitor permissions",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions",
  "summary": "An overview of how to set up monitor permissions for your operators or operator groups.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-permissions"
}

{{< callout >}} Monitor permissions are only available to **Enterprise-level** accounts.{{< /callout >}}

By default, all [basic operators]({{< ref path="/support/kb/account/users/operators/permissions#basic-operator" lang="en" >}}) in your account will be able to view monitor data (dashboards, statistics, check results) for all your monitors. However, they will not be able to edit or delete any existing monitors, or create any new ones. Those actions are, by default, only available to [Administrators]({{< ref path="/support/kb/account/users/operators/giving-an-operator-administrator-rights" lang="en" >}}) (operators who are a member of the *Administrators* operator group). 

For more fine-grained control over which operators are allowed to view or do certain things in your account, Enterprise-level users can set up **monitor permissions**. In short, a monitor permission is a rule that applies to a specific monitor or monitor group, which dictates the level of access that a specific operator or operator group has over those monitors. 

This applies only to monitors in your account. For **operator permissions** such as the ability to place orders, view invoices, access your Uptrends Infra subscription etc, see our article on [operator permissions]({{< ref path="/support/kb/account/users/operators/permissions" lang="en" >}}). 

## Setting up monitor permissions

Monitor permissions can be set up on [monitor groups]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="en" >}}) or individual monitors. This can be done in the monitor (group) settings, but you can also assign monitor permissions directly in the settings for [operator groups]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="en" >}}). To view all your monitors along with their individual operators and operator group permissions, refer to the [Monitor permissions overview]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions-overview" lang="en" >}}).

#### To set up permissions via operator group settings:

1. Navigate to the [Operator groups]({{< AppUrl >}}/Report/OperatorGroups) overview (either by clicking the link, or through the menu at *Account setup > Operators, groups and sub accounts*) and select the operator group to which you wish to assign monitor permissions.
2. You can find the **Monitor permissions** setting in the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab. 
3. If necessary, add the monitor group or individual monitor for which you would like to assign a permission.
4. Set the permission to the correct level using the slider (you can find an overview of available permission levels below).
![Monitor permissions via operator group](/img/content/scr-operator-group-monitor-permissions.min.png)
5. Don't forget to click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} in the bottom left of the screen!

In the example above, members of this operator group can create and delete monitors to and from *Monitor group A*, view monitor data for *All monitors* in the account, and edit the settings of an individual monitor named *Example SSL Cert monitor*.

#### To set permissions via monitor (group) settings:

1. Navigate to the [monitor group]({{< AppUrl >}}/Report/ProbeGroups) or monitor for which you wish to set up a permission.
2. Open the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab for an overview of permissions currently set for that group or monitor. The *Administrators* operator group will always have the **Create and delete monitors in group** permission, which cannot be removed. By default, the *Everyone* operator group will have the **View monitor data in group** permission.
3. To remove an existing permission, click the appropriate button on the right-hand side. Then, proceed to step 7. 
4. To create a new permission, click **Add permission** in the top right corner. To edit an existing permission, click the **Edit** button next to it. 
5. Select the permission you wish to assign. An overview of available permission types will be given below. If creating a new permission, select the individual operator or operator group you wish to give the permission to. 
6. Click **Add** or **Update**, depending on whether you're adding a new or updating an existing permission.
7. Don't forget to click {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} in the bottom left of the screen!

### Monitor permissions and the 'All monitors' group

When a new monitor gets created, it automatically gets added to the *All monitors* group (since that group must contain every monitor in the account, by definition). By default, however, regular (non-Administrator) operators will not have the necessary permission to create/delete monitors in the *All monitors* group. That would mean that an operator without the explicit permission to create monitors in the *All monitors* group would never be able to create anything. To mitigate this, membership to the *All monitors* group will be ignored when creating a new monitor, so long as the monitor gets added to at least one other group. 

For example, consider an operator without any permissions for the *All monitors* group, and with a create/delete permission for *Monitor group A*. This operator is able to view and edit the existing monitors in group A, and can create new monitors which are members of this group. They can not view or edit any existing monitors outside of *Monitor group A*. 

When they create a new monitor, they must add it to at least one of the monitor groups they have the necessary permissions for. 

![All monitors group](/img/content/scr-monitor-permissions-all-mons-group.min.png)

The monitor will be created as a member of both *Monitor group A* and *All monitors*, without the need for an explicit create/delete permission on the latter.

## Permission types {id="permission-types"}

The following permission types are available:

- **View monitor data (in group)**: Operators that have this permission will only be able to view monitor data for the monitor (group) it applies to. Monitor data covers dashboards, statistics and check results. It does **not** include monitor settings.
- **View monitor settings (in group)**: This permission covers monitor data, but also includes monitor settings. Operators with this permission will be able to view monitor settings for the monitor (group) it applies to, such as monitor interval, mode, checkpoint selection, maintenance periods, etc. Keep in mind that with this permission, these settings will be **read-only**, and may not be edited.
- **Edit monitor settings (in group)**: Allows operators with this permission to make changes to the individual monitor(s), or monitors contained in the monitor group this permission is set on. Operators with this permission will be able to disable or enable the monitor, change the interval, edit the checkpoint selection, add maintenance periods, etc. 
- **Create and delete monitors in group**: As the highest permission that can be assigned, this effectively gives an operator Administrative privileges for specific monitor groups. They will be able to create new monitors (albeit only as members of their assigned monitor group), or delete existing monitors. This permission is only available for monitor groups, and cannot be assigned for individual monitors. 

It's worth noting that these permissions are cumulative. Each new permission level contains all permissions before it. For example, an operator with the *View monitor settings in group* can automatically also view the monitor data. 

![Example permissions](/img/content/scr-permissions-example.min.png)

In the image above (which applies to the *Example monitor group*), the *Everyone* operator group can view monitor data only, meaning dashboards, statistics, and individual check results. Operator group *Example operator group* may view monitor data, and edit settings for existing monitors within this group. The *Administrators* group has full CRUD (Create, Update, Delete) permissions for the monitors contained in the *Example monitor group*. 

## Default monitor group {id="default-monitor-group"}

Every monitor in your account is, by definition, a member of the *All monitors* [monitor group]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups" lang="en" >}}). Monitors cannot be removed from this group. That is useful in many cases, but may not be ideal for assigning permissions, depending on your requirements. 

Any permissions you assign to the All monitors group will apply to every monitor in your account. However, you may wish to apply a certain permission to *all but a few* monitors in your account. For example, if a certain [operator group]({{< ref path="/support/kb/account/users/operators/operator-groups" lang="en" >}}) should be able to edit the settings of all monitors in your account except for a specific few, assigning the 'Edit monitor settings' permission to the All monitors group would not work (since they would have the ability to edit every monitor, including the ones they should not be able to edit). 

To help with this, you can set up a **Default monitor group**. This is a custom monitor group, similar to the All monitors group except that monitors may be removed as members of this group. After a default monitor group has been set up, every newly created monitor will automatically also be a member of this group (in addition to the All monitors group), and will therefore receive the same permissions without requiring any further manual intervention. 

Any permissions you wish to assign to all but a few monitors in your account can be assigned to the Default monitor group, rather than the All monitors group. 

To set up a default monitor group:

1. Use an existing monitor group, or create a new group.
2. Make sure this monitor group contains all monitors to which you wish to apply the desired permission. Our [MonitorGroup API]({{< ref path="/support/kb/api/monitorgroup-api" lang="en" >}}) may be useful to add monitors to this group in bulk. 
3. Navigate to your account settings by navigating to {{< AppElement type="menuitem" >}} Account setup > Account settings {{< /AppElement >}} in the menu.
4. Select the monitor group from the drop-down list at the **Default monitor group** option.
![Default monitor group setting](/img/content/scr-default-monitor-group.min.png)
5. Click {{< AppElement type="savebutton" >}} SAVE {{< /AppElement >}} to save your settings.

