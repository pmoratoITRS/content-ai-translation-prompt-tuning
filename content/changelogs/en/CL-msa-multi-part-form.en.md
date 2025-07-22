{
  "title": "Support for the Multi-part form is now available on MSA monitors",
  "date": "2025-01-08",
  "url": "/changelog/january-2025-msa-multi-part-form",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-msa-multi-part-form"
}

When [setting up a Multi-step API monitor,]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="en" >}}) you can specify a payload (data being sent) as part of a request definition. Before, Uptrends only supported sending one type of content at the same time, even though the HTTP protocol does allow multiple parts to be sent. For example, sending some raw text as well as a binary file as part of a single API call.

With the new **Multi-part form** option, you can now include multiple types of content in the request body of your MSA steps. This option automatically sets the `Content-Type` request header to `multipart/form-data` and lets you specify multiple contents in different types. These types can be plain texts entries or files retrieved from the [Vault]({{< ref path="/support/kb/account/vault" lang="en" >}}).

![MSA Multi-part form](/img/content/scr-multi-part-form-msa.min.png)