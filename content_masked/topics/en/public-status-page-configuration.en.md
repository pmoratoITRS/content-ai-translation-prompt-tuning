{
  "hero": {
    "title": "Setting up public status pages"
  },
  "title": "Setting up public status pages",
  "summary": "This article describes how you create a new public status page and configure it.",
  "url": "[URL_BASE_TOPICS]dashboards-and-reporting/status-pages/public-status-page-configuration",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Creating a public status page

1. Go to [SHORTCODE_3] Account setup > Public status pages [SHORTCODE_4].
2. You will see a list of your current public status pages. By default, your account comes with one pre-configured status page. 
3. Click the [SHORTCODE_5]Add public status page[SHORTCODE_6] button at the top right.
4. Enter a descriptive *Name* for the new status page.
5. The *URL* will be generated and visible once you save the status page. This URL is needed to [embed the status page]([LINK_URL_1]) in a web page.
6. Select the *Publish* option to make your public status page available at the URL shown in the *URL* field. The page can then be accessed without any Uptrends login credentials. 
7. Next, go to the [SHORTCODE_7]Data[SHORTCODE_8] tab.
8. Configure the **Period** for which you would like data to be pulled and displayed publicly.
9. Set the **SLA** ([service level agreement]([LINK_URL_2])). The data in your public status page is based on the selected SLA.
10. Add the monitors or monitor groups for which you would like to display data on the status page. 
11. Click the [SHORTCODE_9]Save[SHORTCODE_10] button at the bottom.

You have now successfully configured your public status page and are brought to the main public status pages list, where you will see your new public status page. To see the preview of published pages, click on the preview links. 

If you find yourself needing additional assistance, please do not hesitate to [file a support ticket]([LINK_URL_3]).

## Embedding your public status page into a webpage [ANCHOR_1]

Embedding a public status page on your website is easy.
1. Go to the [SHORTCODE_11]Customization[SHORTCODE_12] tab of the public status page.
2. Copy the value of the *Embed code*, looking similar to [INLINE_CODE_1].
3. Paste the *Embed code* into the source of your web page.
4. Save and refresh the page to see the result.

## Customizing your public status page [ANCHOR_2]

There are a number of things you can do to customize the appearance of your public status page.
Go to the [SHORTCODE_13] Customization [SHORTCODE_14] tab of your public status page to change settings like the color, logo, title, comments, sorting order, etc.

![screenshot customization tab of public status page]([LINK_URL_4])

### Using comments [ANCHOR_3]

If you would like to inform your clients about ongoing incidents and display those on your public status pages, you can enter a status report or message in the comment fields.

You can find the **Comment title** and **Comment text** fields in the [SHORTCODE_15] Customization [SHORTCODE_16] tab.

Once you've entered a title and text, these will display between the title bar and the content of your public status page.

![]([LINK_URL_5])

[SHORTCODE_1]**Tip:** If you want to highlight the message, copy an emoji like 'warning', 'exclamation mark', or 'alert' and paste it in your message in the text field.[SHORTCODE_2]

### Automatically refreshing the page

When you want the page to automatically refresh, enable the **Auto refresh** setting on the [SHORTCODE_17] Customization [SHORTCODE_18] tab of your public status page. The page will be refreshed every 30 seconds. The auto refreshing is turned off by default. 

### Changing the logo 

To change your page's logo, you first need to open a [Support ticket]([LINK_URL_6]) and include a 210 X 40 pixel PNG or JPG image file. Note that larger images will be resized. Support then adds the file to your account so that you can replace the existing Uptrends logo on your page. 

### Alternative monitor names [ANCHOR_4]

The monitor names you are using internally can be less meaningful to your external audience or maybe you simply don't want to share the monitor names that are used inside your company. In that case you can use alternative monitor names. These are set by using a custom field with an identical name in both the public status page and the monitors. 

To define alternative monitor names:

1. Go to [SHORTCODE_19] Account setup > Public status pages [SHORTCODE_20].
2. Open the public status page for which you want to set alternative monitor names.
3. Go to the [SHORTCODE_21]Customization[SHORTCODE_22] tab of a public status page.
4. Enter a *Custom name field*, e.g. [INLINE_CODE_2].
5. Click the [SHORTCODE_23]Save[SHORTCODE_24] button at the bottom.
6. Go to [SHORTCODE_25] Monitoring > Monitor setup [SHORTCODE_26].
7. Open the [SHORTCODE_27] Main [SHORTCODE_28] tab.
8. In the **Meta data** section, add a custom field with the name you have used in the public status page, e.g. [INLINE_CODE_3] and add a value. This value is the alternative monitor name that will be shown on the public status page.
9. Click the [SHORTCODE_29]Save[SHORTCODE_30] button.
10. Repeat steps 6 to 9 for all monitors that should show up with alternative names on the public status page.

If you have several public status pages where alternative monitor names should be shown, repeat steps 1 to 5 for those pages. 
