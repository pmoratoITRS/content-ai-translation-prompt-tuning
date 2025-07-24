{
  "hero": {
    "title": "Using an IPv6 address instead of a domain name"
  },
  "title": "Using an IPv6 address instead of a domain name",
  "summary": "If you need to use an IPv6 address instead of a domain name, you need to format it correctly for Uptrends to process the monitor checks correctly without generating errors. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/using-an-ipv6-address-instead-of-a-domain-name",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

You can use an IPv6 address instead of the domain name in the URL field of your monitor if you choose, but remember, you have to use square brackets around the address and select IPv6 for your monitor's IP version. If you don't indicate IPv6 your monitor will generate errors when tested from checkpoints that do not support IPv6.

For example:

[INLINE_CODE_1]

![]([LINK_URL_1])
