{
  "hero": {
    "title": "Monitor groups"
  },
  "title": "Monitor groups",
  "summary": "Organizing your monitors in to monitor groups makes reporting and alerting setup easier.",
  "url": "/support/kb/synthetic-monitoring/monitor-management/monitor-groups",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-management/monitor-groups"
}

Monitor groups are all about organization and making things easier. Once you have your monitor groups set up, they make [applying templates]({{< ref path="support/kb/synthetic-monitoring/monitor-management/monitor-templates" lang="en" >}}), adding monitors to [alert definitions]({{< ref path="support/kb/alerting/create-alert-definitions" lang="en" >}}), and configuring dashboards and reports faster and easier.

## Deciding on monitor groups

Although your *All Monitors* group isn’t editable, any other group you make is editable, and a monitor can belong to multiple monitor groups. You can set up your monitor groups in several different ways. Here are some examples of common ways other users have set up their monitor groups.

**Monitor type**: It can be useful to set up monitor groups based on [monitor type]({{< ref path="support/kb/basics/monitor-types" lang="en" >}}) such as website performance monitors, mobile performance monitors, uptime monitors, API monitors, transaction monitors, and certificate monitors. This type of grouping is especially helpful when setting up reports.

**Location specific**: If you like getting your reporting based on geographic location, you might find it useful to set up your monitor groups by region or country. Typically these geographic specific monitors will share the same checkpoints making it easy to manage them using monitor templates.

**Data Center**: If you have sites supported by different data centers, you may want to set up groups based on the data center. You can quickly check for performance and uptime based on the data center. Grouping on the data center may come in helpful when setting up maintenance periods using monitor templates.

**Importance**: You may want to group monitors based on the importance of the monitor. For example, availability of your blog will not carry the same weight as your login page, so setting up monitor groups based on the importance of the URL is a great way to organize monitors and prioritize your reports.

**Domain**: You may maintain several domains or subdomains. Organizing based on domain makes it simple to escalate alerts accordingly.

**Page purpose**: There are also several users that group their monitors based on the URL's purpose such as the login pages, homepages, and support pages.

## Monitor groups overview

The **Monitor groups** page gives you an overview of the monitor groups in your account. Open it by going to {{< AppElement type="menuitem" >}} Account setup > Monitor groups {{< /AppElement >}}.

![screenshot dashboar "Monitor groups"](/img/content/scr-monitor-groups-overview.min.png)

You will see all monitor groups where you have at least the *View permission* for. Learn more about this and other  [permission types]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#permission-types" lang="en" >}}) for monitors and monitor groups.

The *All monitors* group is there by default in every Uptrends account. It contains every monitor in your account and you cannot change it or delete it. You may need a group similar to the *All monitors* group containing (nearly) all monitors but with the option to edit permissions and remove monitors from it. Look into setting up a [default monitor group]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions#default-monitor-group" lang="en" >}}) to achieve this.

The overview shows information about *Monitors in use* which refers to the maximum number of monitors (per type) set in your monitor groups. You can also choose to allow unlimited monitors - and set no limits per monitor type.

**Examples**

- If no limit is set and 4 basic monitors are used you'll see "Basic monitors: 4". 
- If the limit is set to 10 basic monitors and 4 are used you'll see "Basic monitors: 4/10".

## Creating a new monitor group

To create a new monitor group:

1. Go to {{< AppElement type="menuitem" >}} Account setup > Monitor groups {{< /AppElement >}} .
2. Click the {{< AppElement type="button" >}} Add monitor group {{< /AppElement >}} button at the top right.
   Alternatively, click the + sign in the menu {{< AppElement type="menuitem" >}}  Account setup > Monitor groups {{< /AppElement >}}. 
   
   The *New monitor group* page appears.

   ![screenshot](/img/content/scr_monitor-group-settings.min.png)

3. Fill in a descriptive name in the **Description**.
4. Decide whether you want to limit the number of monitors that may be added to this group. Choose *Allow unlimited monitors* if you don't want to limit this. Remember that the total number of monitors in all groups can never be higher than the number of monitors in your account.
5. Add monitors that should be a member of this group: click on the existing monitor group in the *Monitors contained in this group* section to expand it, then select the monitor names. Note that you can also add a monitor to a monitor group from the monitor itself. Open the {{< AppElement type="tab" >}} Member of {{< /AppElement >}} tab to make those changes.
6. On the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab, add the operator (groups) with their corresponding access rights to this monitor group. The knowledge base article [Monitor permissions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}}) has more info about the options here.
7. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} at the bottom of the page.


Monitor groups play an important role when setting up a team and giving each member (operator) the necessary access rights. The article [How to set up a team in your account]({{< ref path="support/kb/account/permissions/how-to-team-setup" lang="en" >}}) contains detailed steps for this task.