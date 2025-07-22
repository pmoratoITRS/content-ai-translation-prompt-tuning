{
  "hero": {
    "title": "Private locations API"
  },
  "title": "Private locations API",
  "summary": "The available API methods for manipulating private locations.",
  "url": "[URL_BASE_TOPICS]api/private-locations-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The Private locations API includes a set of endpoints that provide information about the health and operational status of your configured private locations. These endpoints allow you to monitor the availability, performance, and connectivity of each checkpoint.

## Private location and private checkpoint health

Private location health and private checkpoint health are two related concepts that may be used interchangeably when working with the API. The [INLINE_CODE_1] endpoint returns health-related information for a single, specific checkpoint within your private location. In contrast, the [INLINE_CODE_2] endpoint provides an overview of the health status for all individual private checkpoints associated with a given private location. This allows you to monitor each checkpoint separately or get a collective view of their overall status.

## Server information

The API provides detailed information about your server status, including the following:

- Healthy servers — the number of fully functional servers without any errors or warnings.
- Unhealthy servers — the number of servers experiencing errors, warnings, or those not properly set up.
- Number of servers — the total number of servers running in a private location or at a specific checkpoint.
- Checkpoint name — the name of the checkpoint associated with the private location.
- Status — the current status of your server: [INLINE_CODE_3], [INLINE_CODE_4], or [INLINE_CODE_5].
- Status details — the date and time when your server was last active.
- Warnings — displays the warning information, such as if the server requires an update, installation, or other attention.

## Authorization

The API allows you to manipulate private locations permissions. Using this endpoint lets you check whether your authorization type has permission to use or edit private locations. To know more about authorizations, refer to [Setting up Private locations permissions]([LINK_URL_1]).

For more information, refer to the [Uptrends Private locations API]([LINK_URL_2]).