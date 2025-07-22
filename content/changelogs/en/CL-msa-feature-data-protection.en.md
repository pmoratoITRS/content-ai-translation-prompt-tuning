{
  "title": "New MSA feature: Data protection",
  "date": "2024-12-18",
  "url": "/changelog/december-2024-msa-data-protection-feature",
  "translationKey": "https://www.uptrends.com/changelog/december-2024-msa-data-protection-feature"
}

Uptrends collects all your MSA monitoring results from the Checkpoint server, which are then directly stored and retrieved on the Uptrends platform.

With the **Data protection** feature, you can exclude specific monitoring information from being collected and stored on the Uptrends platform. This feature provides an added layer of security, ensuring that any sensitive information remains within your network environment and is not transmitted externally.

![MSA Data protection checkbox](/img/content/scr-data-protection-checkbox.min.png)

By default, the following checkbox options are enabled, allowing Uptrends to store and display information as part of your MSA monitoring results:

- Collect HTTP headers — collects the HTTP Request and Response headers of your website.
- Collect response content — collects the HTTP Response content of your website.
- Collect resolved IP address — collects the Resolved IP address connection details of your website.

Unchecking any of the checkboxes will prevent the associated information from being sent to the Uptrends platform. Instead, an informational text will be displayed.

Please note that the **Data protection** feature is already available in [Private locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}). We are now extending this implementation to our public checkpoint network, such as MSA monitoring.

