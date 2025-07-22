{
  "hero": {
    "title": "Setting up Private locations permissions"
  },
  "title": "Setting up Private locations permissions",
  "summary": "An overview of how to set up Private locations permissions for operators and operator groups.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-permissions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false,
  "tableofcontents": false
}

[Private locations]([LINK_URL_1]) allow you to perform internal monitor checks within your server and firewall instead of the default [Uptrends public checkpoints]([LINK_URL_2]). For each private location, operators can access, create, update, disable, and delete a private location checkpoint. It is essential to control the level of visibility and permission rights among operators for security and privacy reasons.

The **Private locations permissions** let you set permission rights for specific operators and operator groups.

To manage private locations permissions:

1. Go to [SHORTCODE_1] Account setup > Operators and groups [SHORTCODE_2].
2. Select for which operators or operator groups you want to manage private locations permissions.
3. Go to the [SHORTCODE_3] Permissions [SHORTCODE_4] tab.
4. In the **Private location permissions**, select any of the following options:

- **Create private locations** — check this option to allow operators and operator groups to access and create private locations.
- **Use private locations** — select a Private location from the dropdown, and drag the slider to allow operators and operator groups to select the private location as a checkpoint to run monitors.
- **Edit private locations** —  select a Private location from the dropdown, and drag the slider to allow operators and operator groups to access, edit, and delete private locations. Operators with this permission can also select the private location as a checkpoint to run monitors.

By default, all administrators are granted all private location permissions with no additional setup required. Operators with **Use** or **Edit** permissions can select private locations in the monitor [SHORTCODE_5] Checkpoints [SHORTCODE_6] tab. Operators with **Create** or **Edit** permissions can access private locations in the [SHORTCODE_7] Private locations [SHORTCODE_8] menu.

![Private Locations Permissions GIF]([LINK_URL_3])