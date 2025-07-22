{
  "hero": {
    "title": "Private locations overview"
  },
  "title": "Private locations overview",
  "summary": "Use private locations to manage your checkpoints.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations/private-locations-overview",
  "sectionlist": false
}

{{< callout >}} **Announcement:** Uptrends is offering a 30-day trial for Private locations! For more details, refer to the [Private locations trial]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-overview#private-locations-trial" lang="en" >}}) section. {{< /callout >}} 

In general, Uptrends monitors your websites, applications, and APIs using its global network of [public checkpoint locations](/checkpoints). However, there are times when you may need to conduct monitoring activities internally. For these situations, Uptrends provides the **Private locations**, allowing you to perform monitor checks within your own server and firewall.

**Private locations** allow you to create, define, and group your checkpoints based on a specific purpose, use, or physical location (such as city, country, and continent). To give you full control, Uptrends will provide the necessary software installation instructions, and you will be responsible for managing all the internal hardware infrastructure, installation, updates, and other [setup requirements]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="en" >}}).

To access the **Private locations** in the Uptrends web application, go to {{< AppElement type="menuitem" >}} Private locations {{< /AppElement >}}.

![screenshot of private locations](/img/content/scr_private-locations-v3.min.png)

## Add Private locations

To add a new location:

1. Go to {{< AppElement type="menuitem" >}} Private locations {{< /AppElement >}}.
2. Click the {{< AppElement type="buttonPrimary" >}} Add location {{< /AppElement >}} button.
3. Provide the name of the location from which you want to monitor.
4. Choose a [monitor group]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/monitor-groups#permission-types" lang="en" >}}) with permission to create monitors. The health monitors for the location will be created in this group. Monitor groups with the permissions needed will be listed in the drop-down menu.
5. Click the {{< AppElement type="savebutton" >}} Add private location {{< /AppElement >}} button.

 The new location is created and added to the list of private locations. Two unconfigured and uninstalled checkpoints are added by default. See the [FAQs]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq#two-default-private-checkpoints" lang="en" >}}) for an explanation why two checkpoints are added (and not just one).

To rename a private location, click the {{< AppElement type="iconSettings" >}} {{< /AppElement >}} button before the name.

## Add a Checkpoint

Note that a new private location comes with two checkpoints added to it automatically. You can start by installing those or add (now or later) more checkpoints.

To add a **Checkpoint**:

1. Go to {{< AppElement type="menuitem" >}} Private locations {{< /AppElement >}} in the menu.
2. Click the {{< AppElement type="buttonSecondary" >}} Add checkpoint {{< /AppElement >}} button in the location where you want to add a checkpoint.
3. Choose a monitor group with permission to create monitors. The health monitor for the checkpoint will be created in this group.
4. Click the {{< AppElement type="savebutton" >}} Add checkpoint {{< /AppElement >}} button.

To rename a **Checkpoint**:

Click on the checkpoint to open its page and click the edit {{< AppElement type="iconSettings" >}} {{< /AppElement >}} button behind the name and enter a new name.

The checkpoint you add will exist only as a digital representation in the Uptrends web application. The checkpoint that will carry out monitoring checks must also be installed.

To install a Checkpoint, refer to the [Install a Docker checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="en" >}}) instructions. To know more about Private locations, refer to [How to use Private locations checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="en" >}}).

## Private locations trial

The Uptrends **Private locations trial** is available for all account users. This trial allows you to create and set up your **Private locations** to test and use it to your existing monitors.

To give you enough time to prepare, the trial remains open-ended until you've successfully finished installing your first private location on the Uptrends platform. That said, you've already completed all the necessary [requirements]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="en" >}}) and [set up and installed a containerized Docker private checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="en" >}}).

Once your first private location is up and running, your 30-day trial will start free of charge. Note that the trial end date will be set regardless of whether the **Private locations** are selected in any monitor checkpoint.

To extend the trial or convert to a paid subscription, please reach out to your Account manager or the [Support team](/contact).
