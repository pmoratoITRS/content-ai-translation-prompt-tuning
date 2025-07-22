{
  "hero": {
    "title": "Setting up Private locations permissions"
  },
  "title": "Setting up Private locations permissions",
  "summary": "An overview of how to set up Private locations permissions for operators and operator groups.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-permissions",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-permissions",
  "sectionlist": false,
  "tableofcontents": false
}

[Private locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="en" >}}) allow you to perform internal monitor checks within your server and firewall instead of the default [Uptrends public checkpoints]({{< ref path="/checkpoints" lang="en" >}}). For each private location, operators can access, create, update, disable, and delete a private location checkpoint. It is essential to control the level of visibility and permission rights among operators for security and privacy reasons.

The **Private locations permissions** let you set permission rights for specific operators and operator groups.

To manage private locations permissions:

1. Go to {{< AppElement type="menuitem" >}} Account setup > Operators and groups {{< /AppElement >}}.
2. Select for which operators or operator groups you want to manage private locations permissions.
3. Go to the {{< AppElement type="tab" >}} Permissions {{< /AppElement >}} tab.
4. In the **Private location permissions**, select any of the following options:

- **Create private locations** — check this option to allow operators and operator groups to access and create private locations.
- **Use private locations** — select a Private location from the dropdown, and drag the slider to allow operators and operator groups to select the private location as a checkpoint to run monitors.
- **Edit private locations** —  select a Private location from the dropdown, and drag the slider to allow operators and operator groups to access, edit, and delete private locations. Operators with this permission can also select the private location as a checkpoint to run monitors.

By default, all administrators are granted all private location permissions with no additional setup required. Operators with **Use** or **Edit** permissions can select private locations in the monitor {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} tab. Operators with **Create** or **Edit** permissions can access private locations in the {{< AppElement type="menuitem" >}} Private locations {{< /AppElement >}} menu.

![Private Locations Permissions GIF](/img/content/gif-private-locations-permissions.gif)