{
  "title": "Automatic Content-Type header in Multi-step API monitors",
  "date": "2024-01-17",
  "url": "[URL_BASE_CHANGELOG]january-2024-msa-content-type-header",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Our [Multi-step API]([LINK_URL_1]) monitor type allows users to interact with their critical APIs directly. For some monitoring use-cases, data must be sent to the API, for example when executing POST requests to create a new object, or a PUT/PATCH request to update an existing object. In such cases, it is important to include a [INLINE_CODE_1] header to inform the receiving API of the type of data that is coming in (JSON, XML, form data, etc.) so that it knows how to parse the request. An API will commonly return errors if it receives a request body without a [INLINE_CODE_2] header.

Up until now, such headers had to be added to the Multi-step API monitor step(s) manually. As of this update, we are automatically detecting the content type, and adding the correct [INLINE_CODE_3] header, for JSON, XML, or form data request bodies. This change will help users configure POST, PUT, and PATCH requests in their Multi-step API monitors. 