{
  "hero": {
    "title": "Private locations overview"
  },
  "title": "Private locations overview",
  "summary": "Use private locations to manage your checkpoints.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

[SHORTCODE_1] **Announcement:** Uptrends is offering a 30-day trial for Private locations! For more details, refer to the [Private locations trial]([LINK_URL_1]) section. [SHORTCODE_2] 

In general, Uptrends monitors your websites, applications, and APIs using its global network of [public checkpoint locations]([LINK_URL_2]). However, there are times when you may need to conduct monitoring activities internally. For these situations, Uptrends provides the **Private locations**, allowing you to perform monitor checks within your own server and firewall.

**Private locations** allow you to create, define, and group your checkpoints based on a specific purpose, use, or physical location (such as city, country, and continent). To give you full control, Uptrends will provide the necessary software installation instructions, and you will be responsible for managing all the internal hardware infrastructure, installation, updates, and other [setup requirements]([LINK_URL_3]).

To access the **Private locations** in the Uptrends web application, go to [SHORTCODE_3] Private locations [SHORTCODE_4].

![screenshot of private locations]([LINK_URL_4])

## Add Private locations

To add a new location:

1. Go to [SHORTCODE_5] Private locations [SHORTCODE_6].
2. Click the [SHORTCODE_7] Add location [SHORTCODE_8] button.
3. Provide the name of the location from which you want to monitor.
4. Choose a [monitor group]([LINK_URL_5]) with permission to create monitors. The health monitors for the location will be created in this group. Monitor groups with the permissions needed will be listed in the drop-down menu.
5. Click the [SHORTCODE_9] Add private location [SHORTCODE_10] button.

 The new location is created and added to the list of private locations. Two unconfigured and uninstalled checkpoints are added by default. See the [FAQs]([LINK_URL_6]) for an explanation why two checkpoints are added (and not just one).

To rename a private location, click the [SHORTCODE_11] [SHORTCODE_12] button before the name.

## Add a Checkpoint

Note that a new private location comes with two checkpoints added to it automatically. You can start by installing those or add (now or later) more checkpoints.

To add a **Checkpoint**:

1. Go to [SHORTCODE_13] Private locations [SHORTCODE_14] in the menu.
2. Click the [SHORTCODE_15] Add checkpoint [SHORTCODE_16] button in the location where you want to add a checkpoint.
3. Choose a monitor group with permission to create monitors. The health monitor for the checkpoint will be created in this group.
4. Click the [SHORTCODE_17] Add checkpoint [SHORTCODE_18] button.

To rename a **Checkpoint**:

Click on the checkpoint to open its page and click the edit [SHORTCODE_19] [SHORTCODE_20] button behind the name and enter a new name.

The checkpoint you add will exist only as a digital representation in the Uptrends web application. The checkpoint that will carry out monitoring checks must also be installed.

To install a Checkpoint, refer to the [Install a Docker checkpoint]([LINK_URL_7]) instructions. To know more about Private locations, refer to [How to use Private locations checkpoints]([LINK_URL_8]).

## Private locations trial

The Uptrends **Private locations trial** is available for all account users. This trial allows you to create and set up your **Private locations** to test and use it to your existing monitors.

To give you enough time to prepare, the trial remains open-ended until you've successfully finished installing your first private location on the Uptrends platform. That said, you've already completed all the necessary [requirements]([LINK_URL_9]) and [set up and installed a containerized Docker private checkpoint]([LINK_URL_10]).

Once your first private location is up and running, your 30-day trial will start free of charge. Note that the trial end date will be set regardless of whether the **Private locations** are selected in any monitor checkpoint.

To extend the trial or convert to a paid subscription, please reach out to your Account manager or the [Support team]([LINK_URL_11]).
