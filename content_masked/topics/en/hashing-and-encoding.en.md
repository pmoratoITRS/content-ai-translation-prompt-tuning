{
  "hero": {
    "title": "Hashing and encoding"
  },
  "title": "Hashing and/or encoding values",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/hashing-and-encoding",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

For certain use-cases of [API monitoring]([LINK_URL_1]), it may be necessary to hash or encode variables or values. For example, authorization setups might require Base64 encoding or HMAC-SHA256 hashing in order to work correctly, or you might need to include encoded JSON in your request body. To this end, Uptrends offers several encoding and hashing options, which will be described in this article.

## Encoding and decoding

Encoding is a process to ensure data can be sent in a reliable way, in a particular form. A string or file can be encoded to ensure that the receiving side understands its format, after which it can be decoded again.

### Base64 
Base64 is an encoding scheme, typically used to transport binary data as text. It is commonly used in protocols such as [Basic Authentication]([LINK_URL_2]). To apply Base64 encoding within your Multi-step API monitor, use the [INLINE_CODE_1] function. 

The Base64Encode-function also accepts [(predefined) variables]([LINK_URL_3]), by simply filling in the variable reference (wrapped in curly brackets) in the function: [INLINE_CODE_2].

Decoding is also supported, by using the [INLINE_CODE_3] function. 

The Base64Encode and -Decode functions can be used at any point in the Multi-step API monitor configuration, meaning you can refer to it directly when creating a request header, or in your request body content, for example. 

![Base64Encode function used in an Auth header]([LINK_URL_4])

### JSON and XML

JSON and XML are common data interchange formats, that typically adhere to rather strict formatting in order to remain valid. In some cases, JSON or XML content will need to be encoded before they can be sent. For example, JSON cannot be embedded in itself (you can't send JSON-formatted content within JSON-formatted content) without breaking its structure, unless it is encoded. Another example: if your plaintext content contains quotation marks, those have a specific meaning in the JSON format, and cannot be sent in a JSON-structured message without encoding them first. 

Similar to the Base64Encoding and -Decoding functionality described above, there are JsonEncode(), JsonDecode(), XmlEncode(), and XmlDecode() functions. More information on their implementation can be found in our documentation on [applying message formatting in a custom integration]([LINK_URL_5]).

## Hashing

Unlike encoding, which can be decoded, hashing is a one-way process where an algorithm takes a message of any length, and maps it to a fixed-length value using a mathematical function. A hashed value cannot practically be reverted, and any given input should always lead to the same result. Hashing is commonly used in authentication, since it is a secure method to exchange and compare secret information, such as passwords or signatures. 

Uptrends supports the following hashing algorithms:

- MD5
- SHA1
- SHA256
- SHA512
- HMAC-SHA1
- HMAC-SHA256
- HMAC-SHA512

Hashing functions are implemented through the [User-defined functions]([LINK_URL_6]) system, and the implementation of a hashing function follows the same steps outlined in that article. You can apply a hashing function to any plain text string, any [variables]([LINK_URL_7]) that were created as a result of one of the steps in your monitor, or any [predefined variables]([LINK_URL_8]).

The HMAC-based hashing functions require you to supply a **secret key** as a static input, which they will combine with the message to generate a secure consistent output. This can also be a value from a [vault]([LINK_URL_9]) credential set.

![A hashing function example]([LINK_URL_10])


### Base64 encoding for hashed data

Certain methods of authentication may require a hashed value, which must then be Base64 encoded. The [INLINE_CODE_4] function mentioned above is intended to encode the *string* data type. However, these hashing functions result in *hexadecimal* data. That means that encoding them using the default Base64 function can lead to incorrect results, since we're working with different data types. 

In order to correctly encode the *hexadecimal* value that is the result of a hashing function, use the [INLINE_CODE_5] rather than the standard [INLINE_CODE_6] function.