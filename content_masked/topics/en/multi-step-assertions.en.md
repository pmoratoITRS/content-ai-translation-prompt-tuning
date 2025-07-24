{
  "hero": {
    "title": "Multi-step monitoring Assertions"
  },
  "title": "Multi-step monitoring Assertions",
  "summary": "Understanding assertions in Multi-step API Monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-assertions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In the [multi-step monitoring introduction]([LINK_URL_1]), we described that assertions let you define checks on the content of your HTTP responses, which help to monitor correct behavior and performance limits of your APIs. This section describes the assertion capabilities in detail.

Each assertion is defined in the following way:

[SHORTCODE_1]Source[SHORTCODE_2] [SHORTCODE_3]property[SHORTCODE_4] [SHORTCODE_5]comparison[SHORTCODE_6] [SHORTCODE_7]target value[SHORTCODE_8] 

for example:

[SHORTCODE_9]Response body as JSON[SHORTCODE_10] [SHORTCODE_11]Products\[0\].Price[SHORTCODE_12] [SHORTCODE_13]Is greater than[SHORTCODE_14] [SHORTCODE_15]100[SHORTCODE_16] 

-   The **assertion source**: this field defines which attribute of the HTTP response you want to check. [Each available option is outlined in this article]([LINK_URL_2]).
-   The **assertion property**: some assertion source options (in particular the content check and header related options) require you to further specify which content or header to check. This is [explained in more detail]([LINK_URL_3]) for each appropriate source type.
-   The **assertion comparison**: this field expresses the type of check we should perform. By default, we'll do an *X equals Y* kind of comparison, but there are many more comparison options for text and numbers. [See the list of comparison options]([LINK_URL_4]).
-   The **assertion target value**: for most assertions, you'll want to run a comparison against a certain value you specify. That value is the target value. Depending on which assertion source you're using, and the type of comparison you're performing, this value can be a text value, a numeric value or even a boolean value (true or false). You can also enter [a reference to a variable]([LINK_URL_5]) that represents any of these values.

## What happens if an assertion condition is not met?

All assertions in a step are executed as soon as the HTTP request has been executed and the response has been processed. As a rule, each assertion for that step is evaluated, even if a previous assertion does not pass. This means that it is possible that multiple assertions can report a failure for one step.

If one or more assertions fail, execution of the monitor stops immediately. Any subsequent steps will not be executed, and the monitor check will report an error. The error code and description depend on the type of failure. If multiple assertions fail, the first one in the list is regarded as the most important one.

Sometimes it may be necessary to give the execution of an assertion another try, e.g. because you know that there could be a timing issue leading to a false negative result. Evaluating the assertion repeatedly is possible and the details are explained in [Retry until successful]([LINK_URL_6]).