{
  "hero": {
    "title": "Configuring concurrent monitoring"
  },
  "title": "Configuring concurrent monitoring",
  "summary": "A guide on how to configure Concurrent monitoring within Uptrends.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/concurrent-monitoring/configuring-concurrent-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Concurrent monitoring allows you to configure your monitors in such a way that they will run multiple checks at once, from multiple checkpoints. This means you can quickly and reliably gather information regarding your website's availability from several locations. Every monitor type can be configured as a concurrent monitor. The setup for concurrent monitoring is mostly the same as for standard monitoring, with some key differences, and some caveats to keep in mind. For some more information about how concurrent monitoring works, see [this article]([LINK_URL_1]).  
  
You can create new concurrent monitors, but it's also possible to enable the concurrent monitoring feature for existing monitors. Enabling concurrent monitoring works the same in both these cases.

## Setting up concurrent monitoring

1.  Enable concurrent monitoring. In the [SHORTCODE_3]Main[SHORTCODE_4] tab of the monitor settings / new monitor creation window, you'll find the **Concurrent monitoring** option. Enable the option by clicking the corresponding radio-button.

2.  Two new fields appear: **Unconfirmed error threshold** and **Confirmed error threshold**. These thresholds represent the percentage of checkpoints that may detect an error before the concurrent monitor result as a whole is listed as *unconfirmed* or *confirmed*, respectively. Errors work slightly differently for concurrent monitors - [see this article for a complete description]([LINK_URL_2]). We've filled out some default values, but you can tweak them as required. Keep in mind that the unconfirmed error threshold must always be lower than or equal to the confirmed error threshold.  
  
![]([LINK_URL_3])

3.  Next, please make sure to review your checkpoint settings. In the [SHORTCODE_5]Checkpoints[SHORTCODE_6] tab, select the checkpoints that will be executing the check simultaneously. We'll allow a maximum of 50 checkpoints for any concurrent monitor.

[SHORTCODE_1]
**Note:** When it comes to checkpoint selection for concurrent monitors, you have 2 options, which will be presented in the checkpoint selection screen:

1.  The first option is to have all checkpoints available. In this case, the minimum amount of checkpoints you must select for your concurrent monitor is 5.
2.  Alternatively, you can choose to use only *high availability* checkpoints. This limited set of checkpoints have an increased availability, since we operate multiple servers on those locations. This virtually eliminates the chance that, due to maintenance or downtime, one or more locations isn't available for your concurrent checks. This is important because, if a location were to drop out, it could affect your concurrent monitoring alerting rules. When choosing to use the set of *high availability* checkpoints, the minimum checkpoint selection is 3.
[SHORTCODE_2]

  

4.  If you're creating a new monitor, fill out the rest of the required fields, depending on the selected monitor type. Click [SHORTCODE_7]Save[SHORTCODE_8] in the bottom-left of the window to save the monitor.  
  
    The monitor should immediately start generating aggregate results. We have some more information on [how to interpret your concurrent monitoring results here]([LINK_URL_4]).

## Things to keep in mind

-   When setting your (un)confirmed error thresholds, keep the number of selected checkpoints in mind. It makes no sense to use values of 40% and 50% respectively, if you have only 3 checkpoints selected, since it won't be possible to get an error rate of 40-50% with such a setup.
-   Concurrent monitors do not follow the [regular pattern]([LINK_URL_5]) of *Ok-Unconfirmed-Confirmed* errors. Because of the error threshold settings, a concurrent monitor may skip directly from *Ok > confirmed*. The measurement will be more robust, because any error will have been confirmed by multiple locations simultaneously.
-   When setting up concurrent monitoring, keep in mind that a concurrent monitor is priced based on the total number of checkpoints selected. For example, if you're running a 4 credit transaction on 3 high-availability checkpoints, the total cost will be 4x3=12. You can view the total monitor cost in the [Monitors overview]([LINK_URL_6]).
