{
  "hero": {
    "title": "Multi-step monitoring comparison operators"
  },
  "title": "Multi-step monitoring comparison operators",
  "summary": "Learn about the comparison operators available to you when setting up Multi-Step API Monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-comparison-operations",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": false
}

When you're creating an assertion for one of the steps in a [multi-step monitor setup]([LINK_URL_1]), you'll need to define what kind of check operation we need to perform. Choose one of the options mentioned below. In the description for each option, *source* refers to the value of the HTTP response attribute you want to inspect; *target value* is the fixed value we're comparing against.

-   **Is equal to**: the source must be equal to the target value. We'll perform a case insensitive comparison.

-   **Is not equal to**: the source must NOT be equal to the target value. We'll perform a case insensitive comparison.

-   **Contains**: the source must contain the target value. The source and target values are both interpreted as text (even if they just contain a number), and the target value must appear somewhere in the text of the source value.

-   **Does not contain**: the source must NOT contain the target value.

-   **Is less than**: source and target value must both be a number, and the condition source [HTML_TAG_1] target must be true.

-   **Is greater than or equal to**: source and target value must both be a number, and the condition source >= target must be true.

-   **Is empty**: source must contain an empty string (e.g. [INLINE_CODE_1]).

-   **Is not empty**: source must contain some text or number.

-   **Is null**: source must have value [INLINE_CODE_2] (e.g. [INLINE_CODE_3]).

-   **Is not null**: source must NOT have value [INLINE_CODE_4].

-   **Exists**: source must exist in the response.

-   **Does not exist**: source must NOT exist in the response.

-   **Should be ignored**: indicates that no automatic check should be performed on the source value. This option can be used to cancel out the automatic assertions on the Status code and Response complete fields. (see [Source types and properties]([LINK_URL_2]))
