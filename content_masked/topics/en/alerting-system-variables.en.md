{
  "hero": {
    "title": "Alerting system variables"
  },
  "title": "Alerting system variables",
  "summary": "An overview of available system variables, for use in (custom) integrations",
  "url": "[URL_BASE_TOPICS]alerting/integrations/custom-integrations/alerting-system-variables",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false
}

This article contains an overview of all available **System variables**, which can be used to populate the outgoing alert message with relevant information about things like the monitor that caused it, what error occurred, or the alert itself. For more information on how to make use of these system variables, please read our article on [building the right message content]([LINK_URL_1]).

In short, to use the variables listed here, they will have to be included in the message content wrapped in double curly brackets. As an example: [INLINE_CODE_1].

|  Variable   | Description    |  Example value   |
| --- | --- | --- |
| [INLINE_CODE_2] | Your Uptrends account id. | [INLINE_CODE_3] |
| [INLINE_CODE_4] | Unique id of this alert. | [INLINE_CODE_5] |
| [INLINE_CODE_6] | Contains the checkpoint's name or location where the alert was last checked. | [INLINE_CODE_7] |
| [INLINE_CODE_8] | Text description of the error that triggered this alert. Will include step number if applicable. | [INLINE_CODE_9] |
| [INLINE_CODE_10] | The time between the first error and the current (OK) alert timestamp. | [INLINE_CODE_11] |
| [INLINE_CODE_12] | [SHORTCODE_1] The error type id of the error that triggered this alert, see [Error types]([LINK_URL_2]) for a list of error types. [SHORTCODE_2] | [INLINE_CODE_13] |
| [INLINE_CODE_14] | The custom failure message for the specific action in a transaction step that caused the error.  | [INLINE_CODE_15] |
| [INLINE_CODE_16] | The same date and time as @alert.firstErrorUtc, but in the timezone of your account. Also formatted as ISO 8601. | [INLINE_CODE_17] |
| [INLINE_CODE_18] | The Id of the error that triggered this alert. | [INLINE_CODE_19] |
| [INLINE_CODE_20] | The URL of a deep link that takes you to the details of the error that triggered this alert. | [INLINE_CODE_21] |
| [INLINE_CODE_22] | The error description of the first monitor check that received the error. Will include step number if applicable. | [INLINE_CODE_23] |
| [INLINE_CODE_24] | The same date and time as @alert.firstErrorUtc, but in the timezone and culture of your account. | [INLINE_CODE_25] |
| [INLINE_CODE_26] | The date and time of the original error that triggered this alert, expressed in UTC time, and formatted as ISO 8601. | [INLINE_CODE_27] |
| [INLINE_CODE_28] | The date and time of the original error that triggered this alert, expressed in UTC time, and formatted in the culture of your account. | [INLINE_CODE_29] |
| [INLINE_CODE_30] | Contains the total number of consecutive errors (confirmed errors) of the alert. | [INLINE_CODE_31] |
| [INLINE_CODE_32] | The ip address that was used to perform the check. Can be either a ipv4 or a ipv6 address. | [INLINE_CODE_33] |
| [INLINE_CODE_34] | [SHORTCODE_3] Contains the response headers of the alert in key-value pairs. Note that the value of this variable can be empty if the [Private location data protection]([LINK_URL_3]) is enabled on a private checkpoint location performing the alert check. [SHORTCODE_4] | [INLINE_CODE_35] |
| [INLINE_CODE_36] | [SHORTCODE_5] Contains the response body received when it's available. Note that the response body may contain characters that need to be encoded, e.g. [using @JsonEncode or @XmlEncode]([LINK_URL_4]). The response body will be truncated when it's larger than 1 MB. [SHORTCODE_6] | [INLINE_CODE_37] |
| [INLINE_CODE_38] | The IPv4 address of the server on which the check was performed. | [INLINE_CODE_39] |
| [INLINE_CODE_40] | The IPv6 address of the server on which the check was performed. | [INLINE_CODE_41] |
| [INLINE_CODE_42] | Contains the date and time when the SSL certificate is set to expire for SSL monitor alerts. | [INLINE_CODE_43] |
| [INLINE_CODE_44] | The same date and time as @alert.timestampUtc, but in the timezone of your account. Also formatted as ISO 8601. | [INLINE_CODE_45] |
| [INLINE_CODE_46] | The same date and time as @alert.timestampUtc, but in the timezone and culture of your account. | [INLINE_CODE_47] |
| [INLINE_CODE_48] | The date and time of the alert, expressed in UTC time, and formatted as ISO 8601. | [INLINE_CODE_49] |
| [INLINE_CODE_50] | The date and time of the alert, expressed in UTC time, and formatted in the culture of your account. | [INLINE_CODE_51] |
| [INLINE_CODE_52] | The type of this alert message:[HTML_TAG_1][HTML_TAG_2]- Alert: a new error was detected.[HTML_TAG_3]- Ok: the original error has been resolved.[HTML_TAG_4]- Reminder: the original error is still ongoing. | [INLINE_CODE_53] \| [INLINE_CODE_54] \| [INLINE_CODE_55] |
| [INLINE_CODE_56] | The unique id of the alert definition that was used to generate this alert. | [INLINE_CODE_57] |
| [INLINE_CODE_58] | The name of the alert definition that was used to generate this alert. | [INLINE_CODE_59] |
| [INLINE_CODE_60] | [SHORTCODE_7] A reference to a [custom field]([LINK_URL_5]), which can be used to include custom data for individual monitors. [SHORTCODE_8] | [INLINE_CODE_61] |
| [INLINE_CODE_62] | The id of the escalation level that was used to generate this alert. | [INLINE_CODE_63] |
| [INLINE_CODE_64] | The custom message that was specified in the escalation level. | [INLINE_CODE_65] |
| [INLINE_CODE_66] | Unique id of the incident this alert belongs to. An error alert and an Ok alert share the same incident key. | [INLINE_CODE_67] |
| [INLINE_CODE_68] | The URL of a deep link that takes you to the dashboard for this monitor. | [INLINE_CODE_69] |
| [INLINE_CODE_70] | The URL of a deep link that takes you to the settings for this monitor. | [INLINE_CODE_71] |
| [INLINE_CODE_72] | The unique id of the monitor in your account that triggered this alert. | [INLINE_CODE_73] |
| [INLINE_CODE_74] | The name of the monitor in your account that triggered this alert. | [INLINE_CODE_75] |
| [INLINE_CODE_76] | Any custom notes that were filled in the monitor settings. | [INLINE_CODE_77] |
| [INLINE_CODE_78] | Contains the type of the monitor. | [INLINE_CODE_79] |
| [INLINE_CODE_80] | The URL or network address this monitor is checking. | [INLINE_CODE_81] |