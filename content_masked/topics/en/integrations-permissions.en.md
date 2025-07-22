{
  "hero": {
    "title": "Integration permissions"
  },
  "title": "Integration permissions",
  "summary": "Manage operator permissions for integrations",
  "url": "[URL_BASE_TOPICS]alerting/integrations/integrations-permissions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]Integration permissions are only available to **Enterprise-level** accounts.[SHORTCODE_2]

Integrations are used in the escalation levels of alert definitions to set the communication channels for alert messages.
By granting integration permissions to operators, you control who can create, edit, or use the integration in alert definitions.

## Who can manage permissions?

Administrators (members of the Administrators operator group) can always create, use, and edit integrations. They also can set and change all permissions on integrations.

Additionally, an operator with both the permissions **Create integration** (set for an operator or operator group) and **Edit integration** (set on an integration) can also manage the permissions of integrations created by themselves. 
## Permission types

There are two places where permissions are maintained: on the operator (group) or on the integration itself.

### Create integration

The  **Create integrations** permission is set for an operator or operator group. Check out the knowledge base article [Permissions]([LINK_URL_1]) on how this works.

### Use integration

The **Use integration** permission gives an operator the right to use the integration in the escalation levels of an alert definition. In the list of integrations on the escalation level tabs (of an alert definition), you will see all integrations that you have the **Use integration** right for.

This permission does not grant access to the integration itself. You won't see it in the list of integrations ([SHORTCODE_3] Alerting > Integrations [SHORTCODE_4]) where integrations are managed.

The integration **Email** is available for use by all members of the **Everyone** operator group. This is to ensure that you can choose at least one integration, if you have alert definition access rights, but no integrations access has been granted to you yet. The **Email** integration comes with no extra Uptrends cost, while SMS integrations use [SMS credits]([LINK_URL_2]). 

Are you using API calls to get information on integrations? Then a GET request will return all integrations that you have the **Use integration** permission for. This way you can retrieve the [INLINE_CODE_1] information of the integration which is needed to add the integration to an alert definition, also using APIs. The request returns the name, the type and the [INLINE_CODE_2] of the integration.

### Edit integration [ANCHOR_1]

This permission is more powerful than the **Use integration** because it gives you the right to change the integration. In fact, the **Edit integration** permission includes the **Use integration** permission—you don't have to assign both.

If you have the **Edit integration** permission for an integration you will see it in the list of integrations in ([SHORTCODE_5] Alerting > Integrations [SHORTCODE_6]).

This permission includes the right to delete the integration.

## Managing permissions

To set or change permissions:

1. Go to [SHORTCODE_7] Alerting > Integrations [SHORTCODE_8].
2. In the list of integrations, click the one you want to edit.
3. Open the [SHORTCODE_9] Permissions [SHORTCODE_10] tab.
4. Click the [SHORTCODE_11] Add permission [SHORTCODE_12] button.
5. From the popup dialog choose the operator group (or operator) and the permission type, then click the [SHORTCODE_13] Add [SHORTCODE_14] button.
6. To remove a permission, select [SHORTCODE_15] Delete [SHORTCODE_16] from the list **Permissions**.
7. Click the [SHORTCODE_17] Save [SHORTCODE_18] button at the bottom to save the changes you just made.