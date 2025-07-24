{
  "title": "Support for specific HTTP versions is now available in the Multi-step API (MSA) monitor steps",
  "date": "2025-04-03",
  "url": "[URL_BASE_CHANGELOG]april-2025-http-version-in-multi-step-api-monitors",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

It is now possible to specify the HTTP version for each step of an MSA monitor. This lets you control which HTTP version the checkpoint servers use when making requests:

![HTTP version]([LINK_URL_1])

By default, the **HTTP version** option is unchecked, meaning the server will automatically use the highest supported HTTP version available, with a fallback back no lower than HTTP/1.1. Currently, HTTP/3 is available at selected checkpoint locations, and support will soon be expanded to additional locations.

On a similar note, the HTTP configuration allows you to select only one version, while the TLS configuration supports selecting multiple versions. This is because TLS supports version negotiation during the connection process, whereas HTTP/3 does not and requires a specific version to be defined.