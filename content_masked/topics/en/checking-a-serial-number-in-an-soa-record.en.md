{
  "hero": {
    "title": "Checking a serial number in an SOA record"
  },
  "title": "Checking a serial number in an SOA record",
  "summary": "Verify a serial number in an SOA record using a DNS monitor. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/dns/checking-a-serial-number-in-an-soa-record",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

You may want to use a DNS monitor to check the serial number reported by a name server for a domain. The serial number is a specific property of a domain name, which the name server stores in the SOA (Start of Authority) record. The name server increments the serial number each time the DNS settings for a domain get modified, and by watching the serial number, you will know the moment your DNS entry changes and receive alerts to possible tampering. In this article, you'll step through the process of getting the serial number and how you can set up a DNS monitor to test the value.

## First, you need to get the current serial number

To get the current serial number, you need to perform an SOA query.

1.  Open a command window.
2.  Type [INLINE_CODE_1] and press \[Enter\].
3.  Switch to querying SOA records by typing [INLINE_CODE_2] and press \[Enter\].
4.  Type the name of the domain name in question and press \[Enter\].

If the current name server can respond to this query, it will give you the contents of the SOA records. One of the values returned is the serial number. In the example below, the serial number is 162337499.

![]([LINK_URL_1])

## Setting up a DNS monitor to check the SOA record

Now that you know the serial number, you need to set up a DNS monitor to check the SOA record. If you need help with setting up a DNS monitor, visit [Setting up a DNS monitor]([LINK_URL_2]).

1.  Open an existing DNS monitor or create a new DNS monitor
2.  Select **SOA Record** from the **DNS Query** dropdown
3.  Provide the IP address or domain name for the name server you want to test in the **DNS Server** box. Leave this box blank to use the local name server on the checkpoint.
4.  Fill in the domain name you would like to verify the SOA record for in the **Test Value** box.
5.  Enter the serial number you would like to test for in the **Expected result** box.

[SHORTCODE_1]
**Note**: If the name server returns a result, the result contains all the values of the SOA record, not just the serial number value. There's a trick to pull up the entire SOA record contents for your reference. The trick is to force the monitor to fail by using an invalid expected result. For example, enter "dummy test value" in the **Expected result** box. When the monitor errors, you'll get the entire contents of the SOA record in the Check Detail error report (see example below).
[SHORTCODE_2]

![]([LINK_URL_3])
