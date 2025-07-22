{
  "title": "Support for the Multi-part form is now available on MSA monitors",
  "date": "2025-01-08",
  "url": "[URL_BASE_CHANGELOG]january-2025-msa-multi-part-form",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When [setting up a Multi-step API monitor,]([LINK_URL_1]) you can specify a payload (data being sent) as part of a request definition. Before, Uptrends only supported sending one type of content at the same time, even though the HTTP protocol does allow multiple parts to be sent. For example, sending some raw text as well as a binary file as part of a single API call.

With the new **Multi-part form** option, you can now include multiple types of content in the request body of your MSA steps. This option automatically sets the [INLINE_CODE_1] request header to [INLINE_CODE_2] and lets you specify multiple contents in different types. These types can be plain texts entries or files retrieved from the [Vault]([LINK_URL_2]).

![MSA Multi-part form]([LINK_URL_3])