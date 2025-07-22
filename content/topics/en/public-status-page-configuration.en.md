{
  "hero": {
    "title": "Setting up public status pages"
  },
  "title": "Setting up public status pages",
  "summary": "This article describes how you create a new public status page and configure it.",
  "url": "/support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration"
}


## Creating a public status page

1. Go to {{< AppElement type="menuitem" >}} Account setup > Public status pages {{< /AppElement >}}.
2. You will see a list of your current public status pages. By default, your account comes with one pre-configured status page. 
3. Click the {{< AppElement type="button" >}}Add public status page{{< /AppElement >}} button at the top right.
4. Enter a descriptive *Name* for the new status page.
5. The *URL* will be generated and visible once you save the status page. This URL is needed to [embed the status page]({{< ref path="#embedding-status-page" lang="en" >}}) in a web page.
6. Select the *Publish* option to make your public status page available at the URL shown in the *URL* field. The page can then be accessed without any Uptrends login credentials. 
7. Next, go to the {{< AppElement type="tab" >}}Data{{< /AppElement >}} tab.
8. Configure the **Period** for which you would like data to be pulled and displayed publicly.
9. Set the **SLA** ([service level agreement]({{< ref path="support/kb/dashboards-and-reporting/sla/setting-up-an-sla" lang="en" >}})). The data in your public status page is based on the selected SLA.
10. Add the monitors or monitor groups for which you would like to display data on the status page. 
11. Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button at the bottom.

You have now successfully configured your public status page and are brought to the main public status pages list, where you will see your new public status page. To see the preview of published pages, click on the preview links. 

If you find yourself needing additional assistance, please do not hesitate to [file a support ticket]({{< ref path="contact" lang="en" >}}).

## Embedding your public status page into a webpage {id="embedding-status-page"}

Embedding a public status page on your website is easy.
1. Go to the {{< AppElement type="tab" >}}Customization{{< /AppElement >}} tab of the public status page.
2. Copy the value of the *Embed code*, looking similar to `<iframe src=”your public status page URL here”>  </iframe>`.
3. Paste the *Embed code* into the source of your web page.
4. Save and refresh the page to see the result.

## Customizing your public status page {id="customize"}

There are a number of things you can do to customize the appearance of your public status page.
Go to the {{< AppElement type="tab" >}} Customization {{< /AppElement >}} tab of your public status page to change settings like the color, logo, title, comments, sorting order, etc.

![screenshot customization tab of public status page](/img/content/scr_public-status-pages-customization.min.png)

### Using comments {id="comments"}

If you would like to inform your clients about ongoing incidents and display those on your public status pages, you can enter a status report or message in the comment fields.

You can find the **Comment title** and **Comment text** fields in the {{< AppElement type="tab" >}} Customization {{< /AppElement >}} tab.

Once you've entered a title and text, these will display between the title bar and the content of your public status page.

![](/img/content/scr-public-status-pages-comments-front.min.png)

{{< callout >}}**Tip:** If you want to highlight the message, copy an emoji like 'warning', 'exclamation mark', or 'alert' and paste it in your message in the text field.{{< /callout >}}

### Automatically refreshing the page

When you want the page to automatically refresh, enable the **Auto refresh** setting on the {{< AppElement type="tab" >}} Customization {{< /AppElement >}} tab of your public status page. The page will be refreshed every 30 seconds. The auto refreshing is turned off by default. 

### Changing the logo 

To change your page's logo, you first need to open a [Support ticket]({{< ref path="contact" lang="en" >}}) and include a 210 X 40 pixel PNG or JPG image file. Note that larger images will be resized. Support then adds the file to your account so that you can replace the existing Uptrends logo on your page. 

### Alternative monitor names {id="alternative-monitor-names"}

The monitor names you are using internally can be less meaningful to your external audience or maybe you simply don't want to share the monitor names that are used inside your company. In that case you can use alternative monitor names. These are set by using a custom field with an identical name in both the public status page and the monitors. 

To define alternative monitor names:

1. Go to {{< AppElement type="menuitem" >}} Account setup > Public status pages {{< /AppElement >}}.
2. Open the public status page for which you want to set alternative monitor names.
3. Go to the {{< AppElement type="tab" >}}Customization{{< /AppElement >}} tab of a public status page.
4. Enter a *Custom name field*, e.g. `MyMonitorName`.
5. Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button at the bottom.
6. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
7. Open the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab.
8. In the **Meta data** section, add a custom field with the name you have used in the public status page, e.g. `MyMonitorName` and add a value. This value is the alternative monitor name that will be shown on the public status page.
9. Click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button.
10. Repeat steps 6 to 9 for all monitors that should show up with alternative names on the public status page.

If you have several public status pages where alternative monitor names should be shown, repeat steps 1 to 5 for those pages. 
