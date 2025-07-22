{
  "title": "Introducing new alerting variables",
  "date": "2025-02-19",
  "url": "[URL_BASE_CHANGELOG]february-2025-alert-variable-updates",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The following alerting variables are now available for use:

- **@alert.numberOfConsecutiveErrors** — contains the total number of consecutive errors (confirmed errors) of the alert. This returns [INLINE_CODE_1] when the API response is  [INLINE_CODE_2].
- **@alert.checkpointName** — contains the checkpoint's name or location where the alert was last checked. This returns [INLINE_CODE_3] when the API response is  [INLINE_CODE_4].
- **@‌alert.responseHeaders** — contains the response headers of the alert in key-value pairs. For example, this returns [INLINE_CODE_5] from the API response header, similar to how the values are returned for [INLINE_CODE_6].

Note that the value of the [INLINE_CODE_7] can be empty if the [Private location data protection]([LINK_URL_1]) is enabled on a private checkpoint location performing the alert check. For more information, see [Alerting system variables]([LINK_URL_2]).