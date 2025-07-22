{
  "hero": {
    "title": "Bandwidth throttling"
  },
  "title": "Bandwidth throttling",
  "summary": "FPC's and transaction monitors allow you two different methods for throttling your connection speeds: Simulated and browser-based throttling using Chrome.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/bandwidth-throttling",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

To fine-tune your synthetic monitoring for a closer match to your users' actual connection speeds, we recommend that you use bandwidth throttling with your Full Page Check (FPC) and transaction monitors.

## Why use bandwidth throttling?

Uptrends' checkpoint computers operate within data centers. Their native speeds reflect that of a typical user working over a high-speed network much like the one you use in your office. If your user base consists primarily of desktop users, you will probably find our native speeds on Uptrends' checkpoints represent your users just fine. If your users access your site or service using mobile devices or use slower DSL connections, you should consider setting up a monitor that mirrors those users' experiences. That's where bandwidth throttling comes in.

## Bandwidth throttling types

Uptrends offers you two types of bandwidth throttling: Simulated and browser-based throttling. You have the same connection speed options for either type. Browser-based throttling is only available for Chrome and simulated bandwidth throttling is available for other browser types.

### Browser-based

You can use browser-based bandwidth throttling when you choose to use a Chrome browser for your FPC monitor. The preferred option by most, browser-based bandwidth throttling uses the same bandwidth throttling available to you in the Chrome Developer Tools. Chrome differs from simulated throttling in that Chrome applies latency in addition to simulating a lower bandwidth. Browser-based throttling gives a more precise measurement especially on web pages that use very few or lots of connections. In addition, Chrome tracks the number of connections and throttles them together, which is more accurate on websites with a lower or higher than average amount of resources. 

To enable browser-based throttling:

1.  Create a new or open an existing FPC monitor.
2.  Open the [SHORTCODE_1]Advanced[SHORTCODE_2] tab.
3.  Select **Browser** in the [SHORTCODE_3]Bandwidth throttling[SHORTCODE_4] section along with the connection speed you would like to use (see below).
4.  Click [SHORTCODE_5]Save[SHORTCODE_6].

### Simulated

You can set up simulated throttling with any of your browser picks, except for Chrome. Simulated throttling uses a proxy to give you a reasonable simulation of the various connection speeds your users may have.

The checkpoint throttles each connection the browser makes, simulating the average amount of bandwidth available for the chosen connection type. The checkpoint does not take network latency into account and makes calculations based on an average number of connections.

1.  Create a new or open an existing FPC monitor.
2.  Open the [SHORTCODE_7]Advanced[SHORTCODE_8] tab.
3.  Select your [SHORTCODE_9]Browser type[SHORTCODE_10].
![Bandwidth Throttling Simulated]([LINK_URL_1])
4.  Select **Simulated** in the [SHORTCODE_11]Bandwidth throttling[SHORTCODE_12] section along with the connection speed you would like to use (see below).
5.  Click [SHORTCODE_13]Save[SHORTCODE_14].


## Connection types

We base the various connection types that you can choose from when applying bandwidth throttling on real usage scenarios and not the theoretical maximum speeds these technologies can provide. Browser-based throttling applies network latency to your results.

**ADSL**: 4 Mbit down, 0.5 Mbit up, 80 ms round trip time  
**Cable**: 5 Mbit down, 1 Mbit up, 50 ms round trip time  
**Fiber**: 15 Mbit down, 3 Mbit up, 10 ms round trip time  
  
**2G**: 200 Kbit down, 200 Kbit up, 1000 ms round trip time  
**3G**: 1 Mbit down, 500 Kbit up, 300 ms round trip time  
**4G**: 4 Mbit down, 4 Mbit up, 230 ms round trip time
