{
  "title": "Additional conditions for Check URLs loaded by the page",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]february-2025-additional-conditions-check-urls-loaded-by-the-page-error-condition",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The [Check URLs loaded by the page]([LINK_URL_1]) is an error condition that checks if specific page elements are loaded on your website. These page elements are the URLs displayed in your [Waterfall chart]([LINK_URL_2]), including images, files, and other website resources.

This error condition now allows you to set extra criteria for checking each page element's metrics. By clicking the new [SHORTCODE_1] +Add additional condition[SHORTCODE_2] button, you can now specify the page element's response size in bytes (B), total time in milliseconds (ms), and status code:

![Additional conditions for Check URLs loaded by the page]([LINK_URL_3])

If you want to get errors when your image loads longer than 2 seconds or if a file results in a status code higher than 400, you can add specific criteria for each.

The Check URLs loaded by the page error condition are available for [Browser or Full-Page checks]([LINK_URL_4]) and [Transaction]([LINK_URL_5]) monitors. Note that for transaction monitors, you need to select the [Waterfall option in a step]([LINK_URL_6]) to set the additional conditions.