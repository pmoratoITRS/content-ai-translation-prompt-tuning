{
  "hero": {
    "title": "Monitor templates"
  },
  "title": "Monitor templates",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-management/monitor-templates",
  "summary": "With a monitor template you can apply certain settings to multiple monitors at once.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

With Uptrends it has never been easier to monitor the uptime or performance status of any website, server, or web service. But what if you want to monitor a series of services, and set them up quickly? Enter: **Monitor templates**.

A monitor template is a tool that can be used to add certain settings, like *error conditions*, *checkpoints*, and *maintenance periods*, to groups of monitors. Think of them as a way of duplicating monitor configurations, rapid-fire.

## Why are monitor templates useful?

If you are creating a series of monitors that follow the same error condition ruleset, checkpoints for monitoring, or maintenance periods, manual configuration can take quite a lot of time and effort. By using a monitor template, you can minimize the time and effort it takes to add specific settings to monitors, and get back to what you do best.

[SHORTCODE_1] **Note**: You need to be an administrator or have the [Manage monitor templates permission]([LINK_URL_1]) to be able to create, edit and apply templates. [SHORTCODE_2]

## How do I create a monitor template?

1.  Go to  [SHORTCODE_5]Account setup > Monitor templates[SHORTCODE_6]. 
2.  At the top right corner of the screen, click the [SHORTCODE_7]Add Monitor Template[SHORTCODE_8] button.   
3. You can now customize your template settings:
- Set a name for your monitor template.
- Under monitor settings, you have an option to input [load time limits]([LINK_URL_2]) to generate an error when the server's response is slower than this duration.
Likewise, you can select a [user agent]([LINK_URL_3]) to identify the user's  browser type and operating system which will be sent to the server during HTTPS requests. By default, the user agent is set to *Keep unchanged*.
- Under [checkpoints]([LINK_URL_4]), use the checkboxes to determine the locations you want to monitor from. 
- You may also add [maintenance periods]([LINK_URL_5]) and setup its recurrence.

[SHORTCODE_3] **Note**: When applying a monitor template, we’ll only apply the settings you’ve made changes to upon template creation. If you wish to use a template to apply only a maintenance period, for example, make sure you only adjust that setting when creating the monitor template. The same goes for applying a certain checkpoint selection or error condition. [SHORTCODE_4]

4.  When you’re done, click the green [SHORTCODE_9]Save[SHORTCODE_10] button.

You can now apply your saved monitor templates to any existing monitor using two options. The first option is to update a single monitor or perform bulk updates to multiple monitors via the [SHORTCODE_11]Monitor templates[SHORTCODE_12] menu. The second option allows you to directly apply a template from your current monitor via the [SHORTCODE_13]monitor editor [SHORTCODE_14]screen. See step-by-step instructions below to know more about applying monitor templates.

## Applying a monitor template
To generally apply a template to a single monitor, or make bulk updates to multiple monitors at once;

1. Go to  [SHORTCODE_15]Account setup > Monitor templates[SHORTCODE_16]. 
2. Find the right monitor template in the list, and click **Apply**. 
3. Select the individual monitor(s) or monitor group(s) to which you wish to apply the template.
4. Click the [SHORTCODE_17] Apply [SHORTCODE_18] button. 

This will apply the specified settings to the selected monitor(s)/monitor group(s).

## Applying a monitor template using the monitor editor screen
To apply a template directly from your current monitor;

1. Go to [SHORTCODE_19]Monitoring > Monitor setup[SHORTCODE_20].
2. Click the monitor name you wish to apply the template to.
3. At the bottom part of the monitor editor page, click the [SHORTCODE_21] Apply Template [SHORTCODE_22] button.
4. In the Apply template dialog, select which monitor template you want to apply from the dropdown menu. All the available sections from your chosen template will then be displayed. You can use the checkboxes to either apply or skip individual sections. Disabled checkboxes indicate that the template does not contain any settings for that section.

![A screenshot displaying a popup on how to apply monitor templates in a monitor editor window]([LINK_URL_6])

5. Click the [SHORTCODE_23] Apply [SHORTCODE_24] button to confirm changes to your current monitor. 
