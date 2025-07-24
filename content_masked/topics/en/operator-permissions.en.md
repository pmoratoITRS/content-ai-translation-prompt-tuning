{
  "hero": {
    "title": "Setup Operator (group) permissions"
  },
  "title": "Setup Operator (group) permissions",
  "url": "[URL_BASE_TOPICS]account/users/operators/operator-permissions",
  "summary": "An overview of how to set up operator permissions for your operators and operator groups.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_1]Operator permissions are only available to **Enterprise-level** accounts.[SHORTCODE_2]

The **Operator (group) permissions** are permissions that add more control and flexibility to operators and operator groups. With this permission, administrators can set specific level of access to which operators or groups can view, create (or add), edit settings, and delete operators. In that sense, such privileges are not only limited to administrators, but can now be shared across operator and groups given that they are granted access to do so. Similarly, you can grant such view, create, edit and delete permission settings even to non-administrator accounts.

By default, two main [operator groups]([LINK_URL_1]) were set up in your Uptrends account: Administrators and Everyone. The *Administrator group* refers to operators with full access rights and can manage everything under your Uptrends account. Whereas the *Everyone group* refers to all the operators added to an account. That said, everyone automatically qualifies for the *see all operators* permission, allowing each to have visibility to all other operators including non-administrators.

However, there are certain cases in which you might want to limit the wide visibility of the *Everyone group* for privacy and security reasons. For example, you only want authorized operators to have access to your organization's sensitive information, but you've also invited contractors and other parties to be members of your Uptrends team. To prevent vulnerability and potential risks, it is better to keep things separated and restrict public access. Using **Operator permissions**, you can remove the default setting of the *Everyone group* in such a way that the *everyone can see everyone* visibility will no longer be applicable.

In a nutshell, **Operator permissions** come in handy to control the visibility and level of access of your operators and operator groups. By setting the appropriate permission rights, teams can collaborate effectively and perform specific group tasks such as dashboard sharing, defining alerts, scheduling reports etc. Likewise, teams can be self-sufficient in handling management tasks for enhanced security, flexibility and control within your organization.

![Operator permissions for the Everyone group and non-administrators]([LINK_URL_2])

## Setting up operator (group) permissions
Operator permissions can be set up individually via **Operators**, or by clusters via **Operator groups**. Members belonging in an operator group will automatically inherit permission settings.

[SHORTCODE_3] All members of the Administrators group have the ability to see, create, edit operators and add new operators to any group. [SHORTCODE_4]

## Access rights
There are four level of access rights that you can set to each operator and/or operator groups;
- None: No specific permission set to an operator and/or operator group. To restrict the visibility of operator (groups) to others, the default visibility of the *Everyone group* itself must be removed first.
- See operators: Allow operators to see the operator group and the operators within the group.
- Edit settings: Allow operators to edit the settings of each operator within the group.
- Create and Delete: Allow operators to create and delete operators within the group.

### To set permissions via Operators

1. Go to [SHORTCODE_6] Account setup > Operators and groups [SHORTCODE_7].
2. Click [SHORTCODE_8] View all operators [SHORTCODE_9] button.
3. Select the operator name you want to grant permission.
4. Under [SHORTCODE_10] Permissions [SHORTCODE_11] tab, you will see the *Operator permissions* container. Add your operators by selecting them in the dropdown menu and set permission rights accordingly using the slider. To remove any settings or delete the entire row, click the *X* icon.
![Operator permission settings]([LINK_URL_3])
5. Click [SHORTCODE_12] Save [SHORTCODE_13] at the bottom left of the screen to confirm changes.

### To set permissions via Operator groups

1. Go to [SHORTCODE_14] Account setup > Operators and groups [SHORTCODE_15].
2. Click [SHORTCODE_16] View all operator groups [SHORTCODE_17] button.
3. Select the operator group you want to grant permission. 
4. Under [SHORTCODE_18] Permissions [SHORTCODE_19] tab, you will see the *Operator permissions* container. Add your operator groups by selecting them in the dropdown menu and set permission rights accordingly using the slider. To remove any settings or delete the entire row, click the *X* icon.
![Operator group permission settings]([LINK_URL_4])
5. Click [SHORTCODE_20] Save [SHORTCODE_21] at the bottom left of the screen to confirm changes.

[SHORTCODE_5] **Note:** The level of permissions configured using the **Operator permissions** would also take effect and be reflected on other locations where operators can be selected, take for example, *Alert definitions* and *Scheduled reports*. Therefore, the visibility of each operator or operator groups would vary depending on the settings given to them.
