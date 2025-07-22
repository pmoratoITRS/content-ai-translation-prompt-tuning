{
  "title": "Clearer DNS bypass information in check details",
  "date": "2024-03-20",
  "url": "/changelog/march-2024-dns-bypass",
  "translationKey": "https://www.uptrends.com/changelog/march-2024-dns-bypass"
}

In the latest update, we’ve improved clarity by explicitly displaying the bypass URL and resolved IP address in the [check details]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/check-details" lang="en" >}}) when a DNS bypass is set up. Previously, Uptrends only showed the separately resolved IP address, which could cause confusion. Now, you can easily differentiate between these addresses for better understanding and troubleshooting.

When creating or editing a Full Page Check or Transaction monitor, you can choose to add a [DNS bypass]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="en" >}}). The DNS bypass makes sure the webpage is resolved to the specified IP address, instead of the one used by default. This option is located within the _Connection_ information on the {{< AppElement type="tab" >}} Advanced {{< /AppElement >}} tab of the monitor. 