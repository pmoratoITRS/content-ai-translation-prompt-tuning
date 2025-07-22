{
  "hero": {
    "title": "Monitor templates"
  },
  "title": "Monitor templates",
  "url": "/support/kb/synthetic-monitoring/monitor-management/monitor-templates",
  "summary":"With a monitor template you can apply certain settings to multiple monitors at once.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-management/monitor-templates"
}

With Uptrends it has never been easier to monitor the uptime or performance status of any website, server, or web service. But what if you want to monitor a series of services, and set them up quickly? Enter: **Monitor templates**.

A monitor template is a tool that can be used to add certain settings, like *error conditions*, *checkpoints*, and *maintenance periods*, to groups of monitors. Think of them as a way of duplicating monitor configurations, rapid-fire.

## Why are monitor templates useful?

If you are creating a series of monitors that follow the same error condition ruleset, checkpoints for monitoring, or maintenance periods, manual configuration can take quite a lot of time and effort. By using a monitor template, you can minimize the time and effort it takes to add specific settings to monitors, and get back to what you do best.

{{< callout >}} **Note**: You need to be an administrator or have the [Manage monitor templates permission]({{< ref path="/support/kb/account/users/operators/permissions#manage-monitor-templates" lang="en" >}}) to be able to create, edit and apply templates. {{< /callout >}}

## How do I create a monitor template?

1.  Go to  {{< AppElement type="menuitem" >}}Account setup > Monitor templates{{< /AppElement >}}. 
2.  At the top right corner of the screen, click the {{< AppElement type="button" >}}Add Monitor Template{{< /AppElement >}} button.   
3. You can now customize your template settings:
- Set a name for your monitor template.
- Under monitor settings, you have an option to input [load time limits]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="en" >}}) to generate an error when the server's response is slower than this duration.
Likewise, you can select a [user agent]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks" lang="en" >}}) to identify the user's  browser type and operating system which will be sent to the server during HTTPS requests. By default, the user agent is set to *Keep unchanged*.
- Under [checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="en" >}}), use the checkboxes to determine the locations you want to monitor from. 
- You may also add [maintenance periods]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="en" >}}) and setup its recurrence.

{{< callout >}} **Note**: When applying a monitor template, we’ll only apply the settings you’ve made changes to upon template creation. If you wish to use a template to apply only a maintenance period, for example, make sure you only adjust that setting when creating the monitor template. The same goes for applying a certain checkpoint selection or error condition. {{< /callout >}}

4.  When you’re done, click the green {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button.

You can now apply your saved monitor templates to any existing monitor using two options. The first option is to update a single monitor or perform bulk updates to multiple monitors via the {{< AppElement type="menuitem" >}}Monitor templates{{< /AppElement >}} menu. The second option allows you to directly apply a template from your current monitor via the {{< AppElement type="menuitem" >}}monitor editor {{< /AppElement >}}screen. See step-by-step instructions below to know more about applying monitor templates.

## Applying a monitor template
To generally apply a template to a single monitor, or make bulk updates to multiple monitors at once;

1. Go to  {{< AppElement type="menuitem" >}}Account setup > Monitor templates{{< /AppElement >}}. 
2. Find the right monitor template in the list, and click **Apply**. 
3. Select the individual monitor(s) or monitor group(s) to which you wish to apply the template.
4. Click the {{< AppElement type="button" >}} Apply {{< /AppElement >}} button. 

This will apply the specified settings to the selected monitor(s)/monitor group(s).

## Applying a monitor template using the monitor editor screen
To apply a template directly from your current monitor;

1. Go to {{< AppElement type="menuitem" >}}Monitoring > Monitor setup{{< /AppElement >}}.
2. Click the monitor name you wish to apply the template to.
3. At the bottom part of the monitor editor page, click the {{< AppElement type="button" >}} Apply Template {{< /AppElement >}} button.
4. In the Apply template dialog, select which monitor template you want to apply from the dropdown menu. All the available sections from your chosen template will then be displayed. You can use the checkboxes to either apply or skip individual sections. Disabled checkboxes indicate that the template does not contain any settings for that section.

![A screenshot displaying a popup on how to apply monitor templates in a monitor editor window](/img/content/scr-apply-monitor-template-monitor-editor-page.min.png)

5. Click the {{< AppElement type="button" >}} Apply {{< /AppElement >}} button to confirm changes to your current monitor. 
