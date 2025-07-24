{
  "hero": {
    "title": "Private location data protection"
  },
  "title": "Private location data protection",
  "summary": "What are the data protection safeguards for private locations?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In this knowledge base article, you will find an explanation on how to implement data protection on your private locations. One of the safeguards implemented in Uptrends' private locations is preventing snapshots from being uploaded to the cloud. You can also disable page content, hide HTTP request and response headers and resolved IP addresses in check results.

## Editing the Docker Compose file

First, if you have not already done so, install your checkpoint by following the steps explained in [Install a Docker checkpoint]([LINK_URL_1]).

1. Make a backup of the extracted Docker Compose file. Please be aware that if you make changes to the provided compose file this is at your own risk. Contact [Support]([LINK_URL_2]) if you are not sure. 
2. Open the docker-compose.yml file and remove the comment tag `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4]- AllowScreenshotsInResults=false[INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7]- AllowPageContentInResults=false[INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10]- AllowHttpHeadersInResults=false[INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13]- AllowResolvedIpAddressesInResults=false[INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16]- AllowResolvedIpAddressesInResults=false` in the list of Checkpoint environment variables. Save the file and manually restart the Docker container, as described in the last step of the editing instructions above, to reflect the changes in the data protection settings in the Uptrends app.

DNS monitors will be blocked from executing on checkpoint servers in your private location if this value is set to false.

[SHORTCODE_3] **Please note**: Not all settings cover every monitor type, e.g., for basic HTTP(S) monitors only error screenshots will work, the resolved IP settings are not applicable to this type of monitor. 
[SHORTCODE_4]

## Data protection settings status 

The [Checkpoint health]([LINK_URL_9]) tab in the Uptrends app shows the status of the data protection settings. A red cross means data will not be displayed, so data protection is enabled. Please note that this is a read-only display, the settings can only be adjusted in the Docker file. 

![Data protection settings on Checkpoint Health tab]([LINK_URL_10])