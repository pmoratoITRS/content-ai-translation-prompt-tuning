{
  "title": "Introducing Private Locations Permissions",
  "date": "2025-01-29",
  "url": "[URL_BASE_CHANGELOG]january-2025-private-locations-permissions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[Private locations]([LINK_URL_1]) allow you to perform monitor checks (internally) within your server and firewall instead of the default [Uptrends public checkpoints]([LINK_URL_2]).

By default, all operators have access to all private checkpoint locations. Operators can create, update, disable, and delete a checkpoint anytime. It is essential to manage the level of visibility and permissions among operators.

With the new **Manage Private Locations** feature, you can set permission rights for specific operators and operator groups:

- Create — allows operators and operator groups to access and create private locations.
- Edit —  allows operators and operator groups to access, edit, and delete private locations.
- Use — allows operators and operator groups to select the private location as a checkpoint to run monitors

If an operator has any of the permissions above, the private location will be visible in the [SHORTCODE_1] Checkpoints [SHORTCODE_2] tab of a monitor and accessible in the [SHORTCODE_3]  Private locations [SHORTCODE_4] menu.

![Private Locations Permissions GIF]([LINK_URL_3])