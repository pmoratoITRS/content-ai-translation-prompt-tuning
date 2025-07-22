{
  "hero": {
    "title": "Multi-step monitoring sources"
  },
  "title": "Multi-step monitoring sources",
  "summary": "How to extract values for assertions or variable assignment when setting up Multi-step API Monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-sources",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "TableOfContents": true
}

To set up a [content check assertion]([LINK_URL_1]) or extract a [value to be stored as a variable]([LINK_URL_2]) as part of your multi-step API monitor, you'll need to specify which value we should look at. The following options are available as sources:

## Response body as JSON
Choose this option if the body content of your response contains JSON data, and you want to inspect or capture a certain element in the JSON structure. In the property field for the assertion or variable, specify which JSON element we should inspect.

### Examples
Suppose your JSON response has the following content:

[CODE_BLOCK_1]
      

To capture the value of the **access_token** attribute, fill in [SHORTCODE_5]access\_token[SHORTCODE_6] as the property value.

If the object containing the **access_token** key is the **child** of another JSON object, specify the complete 'path'. For example:

[CODE_BLOCK_2]

Here, the access token can be grabbed by filling in [SHORTCODE_7]response.access\_token[SHORTCODE_8] as the property value.


Another JSON example: suppose your JSON data contains an **array** of one or more elements, in this case an array of three products:

[CODE_BLOCK_3]

To get to an attribute of one of those products, we'll first need to point to one particular element in the array by providing an index. The index of the first element in a JSON array is always zero: [INLINE_CODE_1]. So, to capture the Price attribute of the first product in our array, we would specify [SHORTCODE_9]\[0\].Price[SHORTCODE_10] which results in a value of "20000".

If your JSON contains an array as the child of another object, you'll need to specify each 'step', including the index for the element in the array. Suppose your JSON contains something similar to:

[CODE_BLOCK_4]

In this case, the value for the first [INLINE_CODE_2] can be captured as [SHORTCODE_11]Destinations.\[0\].Name[SHORTCODE_12] (the value for **Name** in the first element in the **Destinations** array), which would yield "Alpha Cygnus IX". 


[SHORTCODE_1]**Note**: If the response body cannot be parsed as JSON, this function will generate an error.[SHORTCODE_2] 

## Response body as XML
If your response contains an XML document, choose this option and specify an XPath query to narrow down which piece of content should be inspected or captured.

### Example

Suppose your XML response has the following content:

[CODE_BLOCK_5]

      

To capture the inner value of the **access\_token** node, use the XPath query [SHORTCODE_13]/AuthInfo/access\_token/text()[SHORTCODE_14] as the property value.

For more information, please look at [more XPath examples, including SOAP XML]([LINK_URL_3]).

If the response body cannot be parsed as a standalone XML document, if the XPath query is invalid or does not select an actual value from the document, an error will be generated.

## Response body as text

If your response content is not JSON or XML (e.g. plain text, HTML or a proprietary format) you can still use this option to search that content. By default, we'll consider the entire content of the response. This works fine if you only want to perform a simple Contains-operation (for example: the response body must contain the phrase "Price"; that check will be satisfied as long as the word Price appears somewhere in the content). To use the entire content for your assertion or variable definition, leave the property field empty.

However, if you're looking to inspect or extract content from a very specific location in the document, you'll need a way to define which part of the content we should use for that. To do this, specify a regular expression in the property field. Using the pattern matching capabilities of regular expressions, we'll try to match the regex and use the first match to capture that value from your content.

If the regular expression contains a so-called capturing group (which allows you to define an inner pattern inside the regular expression), we'll use the first match for that capturing group.

Please note that these options apply to text content only (although it may be applied to responses containing JSON or XML as well, since those are still just text); searching binary content is not supported.

## Status code

This option inspects the numeric HTTP status code that is part of every HTTP response. In most cases, you'll just want to check that the status is 200 (which means OK), or at least does not represent a failure. In fact, we'll do this for you by default: if you don't specify a Status code assertion, we will automatically perform the following assertion, since 4xx and 5xx codes are generally error codes:

[INLINE_CODE_3] [SHORTCODE_15]Is less than[SHORTCODE_16] [SHORTCODE_17]400[SHORTCODE_18] 

However, if you define a Status code assertion yourself, it will overrule our default check. For example, if you define

[INLINE_CODE_4] [SHORTCODE_19]Is equal to[SHORTCODE_20] [SHORTCODE_21]200[SHORTCODE_22] 

we will check exactly that condition.

[SHORTCODE_3]**Note**: There is a special case when you add a status code assertion for code 301, 302, 303, 307 or 308 (i.e. a redirect code). For more information, see the section [Handling redirects]([LINK_URL_4]).[SHORTCODE_4] 

## Status description

This option looks at the textual description of the HTTP status code (formally called the Reason-Phrase). This can be useful when you're checking the behavior of certain error conditions in your API: you may want to verify that when you feed incorrect input into your API, a useful Status description is returned.

## Response completed

This option always returns a Boolean value related to whether the HTTP request could be completed successfully. It returns false if we could not determine which server to connect to, if no connection could be established, or if the server did not respond with an HTTP response in a timely fashion. In all other cases, it returns true.

You won't need to specify this option for most cases, because we'll check it for you automatically: based on this assertion type, we will report an error whenever we cannot retrieve an HTTP response from your server:

[INLINE_CODE_5] [SHORTCODE_23]Is equal to[SHORTCODE_24] [SHORTCODE_25]true[SHORTCODE_26] 

For some special cases, it is possible to turn this check around: if you specify false instead, we will check that getting a successful response is NOT possible. This may be useful if you have a web application or API that should only be available inside your network, even though the corresponding domain name is publicly available. Using this check, we will verify that we cannot reach your API or web app.

## Response header 

This option allows you to inspect a specific HTTP response header. You must specify the name of that header in the property field.

## Cookie

This option returns the current value of a cookie. You must specify the name of that cookie in the property field. Please note that cookies returned by your server are treated as session cookies: cookie values are retained, updated and sent back to your server during execution of the entire scenario, up until the last step. Afterwards, all cookies are removed, regardless of any expiration directives. This means that permanent cookies are essentially treated as session cookies.

## Content length

This option returns the size (in bytes) of the response body. Please note that this is the actual content length after the response body has been decompressed (if your server previously compressed it).

## Duration
This option returns the total amount of time (in milliseconds) it took to execute the request and receive the response. This allows you to monitor performance times for individual steps.
