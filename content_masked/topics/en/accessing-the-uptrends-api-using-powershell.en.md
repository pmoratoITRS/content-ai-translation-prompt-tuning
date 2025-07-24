{
  "hero": {
    "title": "Accessing the Uptrends API using Powershell"
  },
  "title": "Accessing the Uptrends API using Powershell",
  "summary": "Learn how to setup a PowerShell Uptrends' API connection. ",
  "url": "[URL_BASE_TOPICS]api/accessing-the-uptrends-api-using-powershell",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

The following example accesses the Uptrends API and fetches the list of Uptrends monitors in your account. Keep in mind that in order to access our API, you'll need to [register for a set of API-specific credentials]([LINK_URL_1]), and make sure to use those rather than your regular Uptrends credentials.

[CODE_BLOCK_1]

That final statement puts the result in the \[INLINE_CODE_1] variable. You can then continue working with that content. For example, to retrieve the check URL for a specific monitor:

[INLINE_CODE_2]
