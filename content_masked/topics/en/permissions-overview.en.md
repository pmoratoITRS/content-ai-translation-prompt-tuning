{
  "hero": {
    "title": "Permissions overview"
  },
  "title": "Permissions overview",
  "url": "[URL_BASE_TOPICS]account/permissions/permissions-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

The Uptrends app works with a permission system to give access rights to operators such that operators can view, edit, or create the items that are relevant to their roles.

In general there are two types of permissions: **system-wide permissions** are assigned to an operator (group), while **context permissions** are set on an item giving the operator (group) access to that particular item. Both types are described in more detail below.

 [SHORTCODE_1] The system-wide permissions are available for all subscription plans, while the context permissions are available only for Enterprise level accounts. [SHORTCODE_2]


## Who can edit (grant/revoke) permissions?

Administrators (members of the **Administrators** operator group) can always edit permissions.

Regarding context permissions the situation is a bit different as also non-administrators may have the right to edit permissions. In fact this depends on which level of context permission has been granted to them, in combination with a system-wide permission.
Check out the information for the individual [context permissions]([LINK_URL_1]) to find out how this works.

## System-wide permissions

The system-wide permissions are explained in detail in the knowledge base article [Permissions]([LINK_URL_2]).

In general it is recommended to set the permissions on operator groups instead of individual operators. This makes it easier to keep an overview. In most cases you will deal with teams (operator groups) where each member should have the same permissions as all other members of the team.

## Context permissions [ANCHOR_1]

The following items in Uptrends let you set permissions (like *view*, *edit*, *use*, *create*) on a per-item basis by attaching the operator group with permissions to the item. See the following knowledge base articles that describe how to set permissions:

- [Alert definitions]([LINK_URL_3])
- [Dashboards]([LINK_URL_4])
- [Integrations]([LINK_URL_5])
- [Monitors]([LINK_URL_6])
- [Vault]([LINK_URL_7])

## How-to guide

The guide has step-by-step instructions on setting up permissions for a new team in your account.

- [Set up a team in your account]([LINK_URL_8])
