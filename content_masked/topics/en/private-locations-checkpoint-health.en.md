{
  "hero": {
    "title": "Checkpoint health"
  },
  "title": "Checkpoint health",
  "summary": "Get an overview of how your private location checkpoints are doing. Are they operating well or do they need attention?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Your checkpoints in [private locations]([LINK_URL_1]) can do their monitoring work only if they are in good condition. The [SHORTCODE_1] Checkpoint Health [SHORTCODE_2] tab gives you an insight in the important facts that impact the condition of the checkpoint. This includes information on the installed software as well as some metrics about the host. Please see below for more detail on the provided information.

## How do I get to the checkpoint health information?

1. Go to [SHORTCODE_3] Private locations [SHORTCODE_4].
2. In the list of private locations, expand the location with the checkpoint you want to look at.
3. Click on the checkpoint and select the [SHORTCODE_5] Checkpoint Health [SHORTCODE_6] tab.

![screenshot of the checkpoint's health tab]([LINK_URL_2])

Note that you'll see this tab only when the checkpoint was fully installed. Otherwise you'll see the [SHORTCODE_7] Installation [SHORTCODE_8] tab only and will have to install your checkpoint first. Please follow the instructions in [Install a Docker checkpoint]([LINK_URL_3]) to get your checkpoint up and running.

## Uptrends software

This section shows you if the Uptrends software was installed correctly and if the various services that are needed to make monitoring available are up and running. Each part of the **Uptrends software** section can have a status of active or inactive. They all should show the status of 'active' for the checkpoint to be able to run monitoring tasks.

The checkpoint container is used to perform all non-browser based checks. 
The transaction processor container is used to perform the real browser checks ([Full Page Checks]([LINK_URL_4]), [transaction monitors]([LINK_URL_5])). 
The relay container is used as a communication relay between the other containers and the Uptrends cloud services.

Please note that Uptrends releases container images with matching version numbers, and only tests those combination of releases. It is not recommended to use non-matching versions together. 

## Browsers

The checkpoint needs to have the browsers installed that you want to use for doing real browser checks ([Full Page Checks]([LINK_URL_6]), [transaction monitors]([LINK_URL_7])). 

In this section you can see the installed browsers with their versions and check those against the latest versions. 
Uptrends will provide container images containing the most recent browsers. Please make sure that you are always updating your containers when available. 

## Host details

The (virtual) machine that hosts your checkpoint needs to be in good condition and have enough memory available to carry out monitoring tasks.

Please check the info on your system here to detect possible bottlenecks.

## Host configuration

In this section you'll find the configuration details of the private location's host, like DNS servers, time zone and language settings.

## Data protection settings

This section shows if data protection is enabled. A green check mark means data will be displayed, so data protection is not enabled. Read more info on how to implement data protection on your private checkpoints in this article about [Data protection]([LINK_URL_8]).

