{
  "hero": {
    "title": "Permissions"
  },
  "title": "Permissions",
  "summary": "The people in your team have different roles and responsibilities. How does that compare to the operators in the Uptrends app?",
  "url": "[URL_BASE_TOPICS]account/users/operators/permissions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1] The availability of permission types depends on your subscription plan, i.e. some types may or may not be available to you. All permissions are available to **Enterprise-level** accounts. [SHORTCODE_2]


Users of the Uptrends app are called operators within the app. An operator holds the user's profile with contact info, personal settings, and more.
The operators are members of one or multiple operator groups. More info on this topic can be found in the article [Operators and operator groups]([LINK_URL_1]).

Operators have different roles and responsibilities, so they need different permissions within the Uptrends app. One example is the typical administrator role, where the operator has access to everything. Other operators may need access only to certain products or monitors. Or you simply want to restrict who has insight into information or the right to change settings.

The Uptrends app uses two approaches when it comes to permissions: system-wide (or global) permissions which are bound to operator groups (or operators) and permissions bound to specific items. To make the set up easier, both system-wide and item based permissions can be set from the [SHORTCODE_3] Permissions [SHORTCODE_4] tab of operators or operator groups.

In addition, [item based permissions]([LINK_URL_2]) might be set on the item (monitor, alert definition, etc.) directly.

Independent of where you set the permissions, they are reflected in the other, corrresponding location.

## Who can manage permissions?
Only operators with administrator rights can change permissions. The operator has to be a member of the *Administrators* operator group where the *Administrative permissions* are default and mandatory. For Enterprise accounts, you can set up [Operator (group) permissions]([LINK_URL_3]) to give specific permission rights to operator and operator groups.

## Managing permissions

We recommend managing permissions on the operator group level. Technically you can also add permissions to individual operators. In most situations it will be easier to add the operator to the operator group which already has the permissions defined, instead of having to add all the permissions to the operator.

The process for granting and revoking permissions is the same. The steps for operator groups are described below.

To grant a permission follow these steps:

1. Go to the [User management hub]([LINK_URL_4]) by navigating to [SHORTCODE_5] Account setup > Operators and groups[SHORTCODE_6] in the menu. From here, click [SHORTCODE_7] View all operator groups [SHORTCODE_8] to get to the overview of operator groups for your account.
2. Select the group you want to add permissions for.
  The permissions are located on the [SHORTCODE_9] Permissions [SHORTCODE_10] tab on the *Operator group* page.
3. Choose the **System-wide permissions** you wish to assign or revoke by selecting or clearing their respective boxes. 
![Operator group permissions]([LINK_URL_5])
4. Set up [item-based permissions]([LINK_URL_6]) for monitors and alert definitions and more.
5. Click [SHORTCODE_11] Save [SHORTCODE_12] to save the changes you just made.

## Permission types

All permission types are available on operator and operator group level, unless otherwise mentioned. Some permissions are mandatory, details can be found in the permission descriptions below.

### Basic operator [ANCHOR_1]

This permission is added to every new operator by default, and is not visible from the operator group settings. 

The permission includes the right to log in, view monitors and dashboards.

Only an administrator within an Enterprise subscription plan can grant or revoke this permission and it can be set for individual operators and for groups.
Once this permission is revoked, the operator can only log in and go to a [protected status page]([LINK_URL_7]). No other actions are available anymore.

### Administrative permissions

This permission is mandatory for the default operator group *Administrators* and cannot be given to any other operator group or individual operator.

If operators need to have administrative rights, add them to the operator group *Administrators*.

### Create alert definitions [ANCHOR_2]

If an operator (or the operator group) has this permission, they can create new alert definitions. Note that there is also the related permission [Edit alert definition]([LINK_URL_8]) which is set in the alert definition itself and not for an operator or operator group.

Once you've created an alert definition you will automatically get the **Edit alert definition** permission for that definition. This is to ensure that you can make changes to the alert definition for later maintenance.

The combination of the permissions **Create alert definitions** and **Edit alert definition** also gives you the right to change permissions of the alert definition. This way you can share your own alert definition with other operators.

Administrators have the **Create alert definitions** permission by default.

### Create integration [ANCHOR_3]

This permission gives you the right to create integrations in general. And once you created an integration, you automatically get the [Edit integration]([LINK_URL_9]) permission for it. This way you can maintain the integration afterwards.

Administrators have the **Create integration** permission by default.

### Financial operator [ANCHOR_4]

An operator with this permission can place orders, view invoices, and make payments.   
The operator will get notified about account expiration, reaching the SMS credits limit, and will also receive payment reminders. 

It is mandatory to have at least one operator within your Uptrends' account with this permission. It is included in the *Administrators* group's permissions by default.
### Infra access

If you have a subscription to Uptrends Infra, you can give operators access to this product.

This permission is mandatory for the default operator group *Administrators*.
### Technical contact

The permission is set for the operator who should be contacted regarding any technical problems. 

It is mandatory to have at least one operator with the permission type *Technical contact*. Additional technical contact permissions may be added and deleted, provided that you always keep at least one operator with this permission.

### Manage private locations [ANCHOR_5]

Operators who have the *Manage private locations* permission type can create, delete or manage existing [private locations]([LINK_URL_10]) within the account. For operators to create a private location, they need access to at least one [monitor group]([LINK_URL_11]) with permission type *Create and delete monitors in group*. 
The *Manage private locations* permission is included in the *Administrators* group’s permissions by default.

### Manage monitor templates [ANCHOR_6]

Operators granted the *Manage monitor templates* permission can manage and apply [monitor templates]([LINK_URL_12]) to those monitors within the account to which they have edit rights, without the need for additional administrative rights.

## Item-based permissions [ANCHOR_7]

The following permissions are set on the item, e.g. integration, monitor, while system-wide permissions are set globally.

- [Alert definitions]([LINK_URL_13])
- [Dashboards]([LINK_URL_14])
- [Integrations]([LINK_URL_15])
- [Monitors]([LINK_URL_16])
- [Vault]([LINK_URL_17])
- [Operators and operator groups]([LINK_URL_18])