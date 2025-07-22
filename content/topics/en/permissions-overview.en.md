{
  "hero": {
    "title": "Permissions overview"
  },
  "title": "Permissions overview",
  "url": "/support/kb/account/permissions/permissions-overview",
  "translationKey": "https://www.uptrends.com/support/kb/permissions/permissions-overview",
  "sectionlist": false
}

The Uptrends app works with a permission system to give access rights to operators such that operators can view, edit, or create the items that are relevant to their roles.

In general there are two types of permissions: **system-wide permissions** are assigned to an operator (group), while **context permissions** are set on an item giving the operator (group) access to that particular item. Both types are described in more detail below.

 {{< callout >}} The system-wide permissions are available for all subscription plans, while the context permissions are available only for Enterprise level accounts. {{< /callout >}}


## Who can edit (grant/revoke) permissions?

Administrators (members of the **Administrators** operator group) can always edit permissions.

Regarding context permissions the situation is a bit different as also non-administrators may have the right to edit permissions. In fact this depends on which level of context permission has been granted to them, in combination with a system-wide permission.
Check out the information for the individual [context permissions]({{< ref path="#context-permissions" lang="en" >}}) to find out how this works.

## System-wide permissions

The system-wide permissions are explained in detail in the knowledge base article [Permissions]({{< ref path="support/kb/account/users/operators/permissions" lang="en" >}}).

In general it is recommended to set the permissions on operator groups instead of individual operators. This makes it easier to keep an overview. In most cases you will deal with teams (operator groups) where each member should have the same permissions as all other members of the team.

## Context permissions {id="context-permissions"}

The following items in Uptrends let you set permissions (like *view*, *edit*, *use*, *create*) on a per-item basis by attaching the operator group with permissions to the item. See the following knowledge base articles that describe how to set permissions:

- [Alert definitions]({{< ref path="support/kb/alerting/alert-definition-permissions" lang="en" >}})
- [Dashboards]({{< ref path="support/kb/dashboards-and-reporting/dashboards/sharing-dashboards"
 lang="en" >}})
- [Integrations]({{< ref path="support/kb/alerting/integrations/integrations-permissions" lang="en" >}})
- [Monitors]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="en" >}})
- [Vault]({{< ref path="/support/kb/account/vault#who-can-access-the-vault" lang="en" >}})

## How-to guide

The guide has step-by-step instructions on setting up permissions for a new team in your account.

- [Set up a team in your account]({{< ref path="support/kb/account/permissions/how-to-team-setup" lang="en" >}})
