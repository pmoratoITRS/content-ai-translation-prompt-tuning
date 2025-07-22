{
  "hero": {
    "title": "DNS servers overview"
  },
  "title": "DNS servers overview",
  "summary": "Find out why you would use a DNS monitor and how you set it up in Uptrends.",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/dns/dns-overview",
  "translationKey": "https://www.uptrends.com/support/kb/dns/dns-overview",
  "sectionlist": false
}

Monitoring your DNS is a great way of ensuring that your users can easily access your website and services quickly, and securely.

## Why use a DNS monitor?

This check allows you to perform various queries on a DNS name server. The most common thing to check, is whether your domain name (www\.yourcompany.com) is still pointing to the IP address of your web server. Your provider’s name server is the primary, first-hand source of this information. By monitoring this DNS query directly, Uptrends will detect any DNS problems, even before your website becomes unavailable for your visitors and customers.

Uptrends' DNS monitor lets you do extensive DNS health checks: verify your web site domain names (A and CNAME records), mail server domain name mappings (MX records), DNS zone delegates (NS records), authoritative information about DNS zones (SOA records) and other DNS information, contained in TXT records (including SPF information for e-mail authentication).

A specific case for using a DNS monitor is [Checking a serial number in an SOA record]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/dns/checking-a-serial-number-in-an-soa-record" lang="en" >}}).

## Setting up a DNS monitor

1. Navigate to the menu {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}} and click the + button to the right.
2. Set your monitor type to **DNS**.
3. Enter the **Name**, and **check interval** that best suits your DNS monitoring needs.
4. Select your **IP version**. If testing using IPv6, you have the option to use only those checkpoints that have native IPV6; if left unchecked, checks will originate from all selected checkpoints using IPV6 when native and IPV6 emulation on IPV4 checkpoints.
5. Fill in the **DNS server** information, specifying the *domain name* or *IP address* of the DNS server you’d like to test, for example `n1s.yourprovider.com`.
6. It is important to check the **Port** for your DNS server, to confirm if the default value of 53 applies.
7. Select your **DNS query** type. Uptrends supports *A Record*, *AAAA Record*, *CNAME Record*, *MX Record*, *NS Record*, *SOA Record*, *TXT Record*, or *Root Server*.
8. Specify the domain name that you would like to query in the **Test Value** field, for example `www.yourdomain.com`.
9. Provide the **Expected result** in the field with the same name.
    For example: If you are testing the domain name of your website (an A Record query), fill in the IP address of your domain name. The Uptrends service will then verify that the response from the DNS query matches the IP address.

    {{< callout >}}**Tip**: If your domain name has multiple IP addresses, you can use a regular expression to match multiple values.
    Example: 1.2.3.4|5.6.7.8{{< /callout >}}
10.  Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button when you're done.

