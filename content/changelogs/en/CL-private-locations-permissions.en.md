{
  "title": "Introducing Private Locations Permissions",
  "date": "2025-01-29",
  "url": "/changelog/january-2025-private-locations-permissions",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-private-locations-permissions"
}

[Private locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview" lang="en" >}}) allow you to perform monitor checks (internally) within your server and firewall instead of the default [Uptrends public checkpoints]({{< ref path="/checkpoints" lang="en" >}}).

By default, all operators have access to all private checkpoint locations. Operators can create, update, disable, and delete a checkpoint anytime. It is essential to manage the level of visibility and permissions among operators.

With the new **Manage Private Locations** feature, you can set permission rights for specific operators and operator groups:

- Create — allows operators and operator groups to access and create private locations.
- Edit —  allows operators and operator groups to access, edit, and delete private locations.
- Use — allows operators and operator groups to select the private location as a checkpoint to run monitors

If an operator has any of the permissions above, the private location will be visible in the {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} tab of a monitor and accessible in the {{< AppElement type="menuitem" >}}  Private locations {{< /AppElement >}} menu.

![Private Locations Permissions GIF](/img/content/gif-private-locations-permissions.gif)