{
  "hero": {
    "title": "Data protection in Multi-step APIs"
  },
  "title": "Data protection in Multi-step APIs",
  "summary": "Know how your Multi-step API monitoring information is protected.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-data-protection",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": false,
  "sectionlist": "true"
}

Whenever you run any synthetic monitor in Uptrends, the server from that checkpoint location performs monitoring tests. At the Checkpoint server level, Uptrends retrieves all the monitoring results and directly stores them on the Uptrends platform.

Most organizations have strict regulations concerning data privacy and prefer to exclude sensitive information from being retrieved or sent in any form. With the **Data protection** feature, you can exclude specific monitoring details from being collected and stored in Uptrends. This feature provides an added layer of security, ensuring that any sensitive information are not transmitted externally (or leave the Checkpoint server).

![MSA Data protection checkbox]([LINK_URL_1])

By default, the following information are collected and displayed as part of your MSA monitoring results:

- HTTP Request and Response headers of your website
- HTTP Response content of your website
- Resolved IP address connection details of your website

Unchecking any of the checkboxes will prevent the associated information from being sent to the Uptrends platform. Instead, a message will be displayed indicating that such data is not collected because of your company's data protection policy.

![Disabled MSA Data protection]([LINK_URL_2])

## Related articles

To know about Data protection in Private locations, refer to [this knowledge base article]([LINK_URL_3]).
