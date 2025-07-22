{
  "hero": {
    "title": "Errors and alerting for concurrent monitors"
  },
  "title": "Errors and alerting for concurrent monitors",
  "summary": "How does error generation and alerting work for concurrent monitors?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/concurrent-monitoring/errors-and-alerting-for-concurrent-monitors",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Compared to standard monitoring, the way errors are generated for concurrent monitors works slightly differently. Standard monitoring typically follows a sequence of *[Ok (green) - Unconfirmed error (yellow) - Confirmed error (red)]([LINK_URL_1])* for the generation of errors, with alerts being generated after a specified number of confirmed errors for any given monitor. For concurrent monitors, however, errors are generated differently. In this article, we'll take a deep-dive into how a concurrent monitors generates errors. Keep in mind that once the errors have been generated, the alerting works [the same way as for standard monitoring]([LINK_URL_2]).

## Concurrent error thresholds

When creating a concurrent monitor (or setting an existing monitor to concurrent mode), you'll be required to fill out two new fields: **Unconfirmed error threshold** and **Confirmed error threshold**. Additionally, a concurrent monitor requires a minimum of 3 high-availability checkpoints, or 5 checkpoints from the complete set to be selected. Together, those settings determine the circumstances under which the monitor check receives an Ok, unconfirmed error, or confirmed error status. In short, a concurrent monitor will report errors if the number of checkpoints that individually detect an error exceeds the set thresholds.

As an example, let's look at an Https monitor, which has an unconfirmed error threshold of 30%, a confirmed error threshold of 50%, and 10 checkpoints selected.

-   Under normal circumstances, each of the selected checkpoints individually would return an ok result - none of the checkpoints that execute the test concurrently detect an error, meaning the error percentage is 0%. In such cases, the concurrent monitor overall result is *Ok*.
-   If two of the selected checkpoints detect something wrong, the error percentage is 20% (since 2/10 selected checkpoints detected an error). Since neither error threshold is met, the overall check result is still reported as *Ok*.
-   In the case that four of the selected checkpoints detect errors, the error percentage becomes 40%. This exceeds the unconfirmed error threshold (at 30%), but not the confirmed error threshold (50%). The overall check result will be *unconfirmed*, and therefore will not trigger any alerting under any circumstances.
-   When five (or more) checkpoints individually detect an error, the error percentage starts matching or exceeding the confirmed error threshold. In this case, the overall result will immediately registered as a *confirmed* error. That means that such errors can trigger alerting, depending on the settings in your alert definitions.

In the example image below, you can see that two of the six selected checkpoints (or \~33%) have reported an error. That exceeds the threshold for *unconfirmed* errors (25% in this example), but not the threshold for *confirmed* errors (set to 50%). That means that the overall check result is *unconfirmed*, and will not generate any alerts. ![]([LINK_URL_3])

In other words, concurrent monitoring does not double-check its errors in the same way standard monitors do. A standard monitor, upon detecting an error, will immediately perform the test again from a different checkpoint location to confirm the error. For concurrent monitoring, we exceed that robustness by performing the check from multiple locations at the same time. If a certain amount of them come up as errors, it's safe to assume that the error is genuine.

[SHORTCODE_1]
**Note:** the individual monitor checks do not follow the regular *Ok - Unconfirmed - Confirmed* scheme of errors. Instead, individual checks will be either *Ok* (green) or *Confirmed* (red). Since the status of your monitor is decided based on the error thresholds you've set, an individual confirmed error will not cause any alerting by itself.
[SHORTCODE_2]

## Considering checkpoint downtime

Since our [global network of checkpoints]([LINK_URL_4]) is quite expansive, some downtime is unavoidable. Primarily due to regular maintenance, but sometimes for other reasons, certain checkpoints may be unavailable for executing your monitor check. In the event this happens for one of the checkpoints you have selected for your concurrent monitor while a check is running, the overall check result will display a gray **?** icon for that specific checkpoint. The individual check for that checkpoint will be *inconclusive*, and we will not take it into account when calculating whether the number of errors from the individual checks exceeds the error thresholds. ![]([LINK_URL_5])
