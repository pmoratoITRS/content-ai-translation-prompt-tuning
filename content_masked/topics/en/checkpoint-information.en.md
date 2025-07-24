{
  "hero": {
    "title": "Checkpoint information"
  },
  "title": "Checkpoint information",
  "summary": "What is a checkpoint and how do you choose the right ones from the many checkpoints that Uptrends offers for monitoring?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/checkpoint-information",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends features a vast network of over {{% Features/Variable variable="CheckpointCount" %}} global monitoring checkpoints that you can configure to monitor your websites, servers, and web services to determine the origin of an issue.

## What is a Checkpoint?

A checkpoint is a geographical location where your monitors' uptime and performance are checked periodically. Each checkpoint has one or more servers located in data centers to perform tests. These checkpoints mainly use the Domain Name System (DNS) servers provided by local Internet Service Providers (ISP), when available, to guarantee actual measurements and results.

## List of Uptrends Checkpoints' IP addresses

See the full and updated [list of Uptrends global monitoring checkpoints]([LINK_URL_1]), including IPv4 and IPv6 IP addresses.

See the list of [IPv4 addresses]([LINK_URL_2]) and [IPv6 addresses]([LINK_URL_3]). To download the IP addresses in JSON or XML format, refer to the [Get checkpoint data in JSON or XML format]([LINK_URL_4]) knowledge base article.

## Multiple Checkpoints

With the vast number of Checkpoints available in Uptrends, you can flexibly choose different locations to run tests and verify the behavior of your monitor results.

Checkpoints can also be an excellent tool to:

- Test the Content Delivery Network (CDN) with many endpoints.
- Test the global DNS network. Many of Uptrends' checkpoints are using a local DNS, allowing you to test that your DNS changes propagate across the globe in a correct manner.
- Test if the latency introduced by distance or by backbone providers is within the acceptable parameters.

## Choosing the right set of checkpoints

Selecting multiple checkpoints is already included in your subscription and has no additional cost. Uptrends recommends selecting as many checkpoints as possible, as this will better evaluate the performance of your monitor and provide alternative locations during checkpoint maintenance and downtime.

By default, Uptrends selects checkpoint locations worldwide, including Europe, North America, Africa, Asia, Australia, South America, and the Middle East. It is helpful to have a checkpoint selection that is carefully targeted at a specific region.

It is mandatory to select at least three checkpoints. If, for any reason, one of these checkpoints is for maintenance, at least two checkpoints can perform checks and verify errors from another checkpoint.

In the [SHORTCODE_5]Checkpoints[SHORTCODE_6] tab of a monitor, you can activate individual checkpoints, but also entire countries and continents. If you select a country or continent, you'll immediately benefit from new checkpoints when we add additional locations to that region. Your coverage grows automatically whenever our network grows! Even if you want to skip individual checkpoints, you can still benefit from this auto-growth function: rather than selecting individual checkpoints in a country and leaving one out, you can use the [Checkpoint Exclusions]([LINK_URL_5]) function instead to have fine-grained control over your checkpoint sets.

[SHORTCODE_1]
**Note:** The options you have differ per account type. Users on the Starter, Premium or Professional version can select fixed sets of checkpoints. Users on the Business or Enterprise version can select up to every available individual checkpoint.
[SHORTCODE_2]

## Checkpoint downtime

Due to local network problems or maintenance, checkpoint locations might be temporarily out of service. In scenarios where all of your checkpoint selections are unavailable, Uptrends ensures that checks will still be executed on a fallback location outside of your configured checkpoint selection. If only some of the selected checkpoints are unavailable, Uptrends will still check your monitors from your other selected checkpoints.

The fallback location is enabled by default in the [SHORTCODE_7] Account Settings [SHORTCODE_8] > **Checkpoint fallback**. This ensures that tests will still run in other locations and will not be compromised. Once checkpoints become available, Uptrends will automatically switch back to your monitor's checkpoint settings.

There are certain scenarios where fallback locations might not work well. For instance, if you use a whitelisting policy wherein only specific [Uptrends IP addresses]([LINK_URL_6]) are whitelisted. In cases like this, do the following options to resolve the issue:

- Increase the number of selected checkpoints to reduce the chance of monitoring from unavailable checkpoint locations.

- Go to [SHORTCODE_9] Account Settings [SHORTCODE_10] and uncheck the **Checkpoint fallback** option. Disabling the **Checkpoint fallback** means that no alternative locations will be available to check your monitor. If your monitor starts running a test and detects a checkpoint downtime, automatically, the monitor will skip the current check. Then, the monitor will start another check at the next monitor [interval]([LINK_URL_7]). Note that disabling this option might cause some gaps in your monitoring results.

## Checkpoint issues?

Having issues with a certain checkpoint? [Contact us]([LINK_URL_8])!

[SHORTCODE_3]
**Note:** Some Internet IP geographic locator tools misrepresent the physical location of our data centers. [Learn more]([LINK_URL_9]). 
[SHORTCODE_4]
