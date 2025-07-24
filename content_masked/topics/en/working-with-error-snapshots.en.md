{
  "hero": {
    "title": "Working with error snapshots"
  },
  "title": "Working with Error Snapshots",
  "summary": "Error snapshots can help with troubleshooting, see when they are available",
  "url": "[URL_BASE_TOPICS]alerting/errors/working-with-error-snapshots",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

So, your website is down, but you don’t know why. You log into your Uptrends website monitoring account, and you deduce that users may be experiencing a connection error. But how? By checking your monitor error details and error snapshots.

## What is an error snapshot?

An error snapshot is a screenshot grabbed by the Uptrends service to show you what your users may be experiencing in-browser when a problem is occurring.

![screenshot of check details with error snapshot]([LINK_URL_1])

## How do error snapshots work?

Uptrends generates error snapshots in specific circumstances.

- Snapshots are available for **HTTP(S)**, **Web Service (HTTP(S))**, and **Transaction** monitors only.
- Uptrends creates snapshots for specific errors only (e.g., pattern match errors, but not for performance limit errors). In the case of an infrastructure related error, such as a TCP connection error, we don't have any content to show.  
- The Uptrends service only creates snapshots for confirmed errors that are **first** in a sequence. Consecutive errors do not receive an error snapshot. [SHORTCODE_1]**Note**: It may take a few minutes for error snapshots to appear after an error has occurred, and in some circumstances, a snapshot may be unavailable depending on the content that Uptrends receives.[SHORTCODE_2]
