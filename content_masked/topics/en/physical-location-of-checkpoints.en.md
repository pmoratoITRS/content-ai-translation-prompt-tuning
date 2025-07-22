{
  "hero": {
    "title": "Physical location of checkpoints"
  },
  "title": "Physical location of checkpoints",
  "summary": "Uptrends present their checkpoint locations as close to the physical location as possible, but geo-location tools may misrepresent checkpoint locations.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/physical-location-of-checkpoints",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

A single checkpoint location consists of one or more servers located at one or more data centers that we procured from both local and international providers. We label most checkpoint locations with the name of the closest city to the data center. On the [checkpoint map]([LINK_URL_1]), we point to the center of the city rather than a precise location. We want to ensure that the physical location of each server is accurate, so we actively verify the location by looking at the distance to other sites (for example by reviewing the hops in a traceroute).

## Considerations when using IP geographic locator tools

You can find tools on the Internet that let you search for the physical location of an IP address. The providers of those tools use several pieces of information to determine a geographic location but with varying degrees of accuracy. Please be aware that the information they provide may not always be 100% accurate. One of the reasons these tools may misrepresent a location is because the administrative address information of a particular Internet provider may be quite different from the physical address of our data center. In fact, it may even be in a different country. Good IP location services provide accuracy information about their [data]([LINK_URL_2]).

## Still have doubts?

When you have doubts about the location of a checkpoint, feel free to do your own network based tests. If you're getting unsatisfying results, please [contact us]([LINK_URL_3]).

[SHORTCODE_1]
**Please note:** We cannot change the information supplied by providers of geographic location information.
[SHORTCODE_2]
