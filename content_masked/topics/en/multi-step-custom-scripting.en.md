{
  "hero": {
    "title": "Multi-step API custom scripting"
  },
  "title": "Multi-step API custom scripting",
  "summary": "An overview of the Custom Scripting options in Multi-step API monitoring",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-custom-scripting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The Multi-step API (MSA) monitor features powerful [built-in functions]([LINK_URL_1]) that provide a user-friendly and no-code solution to test the behavior of your APIs.

While a no-code approach goes a long way in building proper monitoring setups, you might need a scripting language to do in-depth functional tests and completely describe what you expect from your APIs. For example, adding a custom logic or handling more advanced behaviors which cannot be achieved in a UI-based setup only.

The MSA monitor lets you handle both classic no-code features along with custom scripting. You can use built-in UI functions along with their scripting counterparts. You don't have to create your monitors from scratch if you have existing API monitors and want to add custom scripting. Simply start adding some scripts and have them work alongside your existing setup.

## Pre-Request and Post-Response scripts

An API monitor consists of a single or multiple steps executed in a sequence. For each MSA step (except Wait steps), two script editors,
[SHORTCODE_1] Pre-Request [SHORTCODE_2] and [SHORTCODE_3] Post-Response [SHORTCODE_4] tabs are available:

- The **Pre-Request script** editor lets you write scripts in preparation for sending an HTTP request. This is useful for preparing and calculating any values you want to include in the request, such as environment variables, URL parameters, request headers, or content body. The script written in this editor runs *before* the API request is sent to the server.

- The **Post-Response script** editor lets you write scripts to verify and process the HTTP response that comes back from the API. This is useful for writing custom logic to check response headers, validate the completeness and consistency of your content, and use that content data to prepare for any next steps. The script written in this editor only runs *after* the API response is successfully received from the server. If a connection error occurs, the script will not be executed, and any assertions or variables in the [SHORTCODE_5] Response [SHORTCODE_6] tab will not be validated.

These editors also includes the following features:
![Custom scripting tabs]([LINK_URL_2])

- Line numbering — displays numerical values that identifies the scripts or codes per line.
- Code highlighting — displays codes in color-coded format to easily identify syntax errors and keywords.
- Code completion — automatically suggests possible code combinations to assist script writing.
- Snippets panel — provides a list of helpful code snippets that you can automatically insert in your code editor once selected.

## Snippets

The **Pre-Request** and **Post-Response** editors allow you to insert and execute scripts written in JavaScript language. Aside from the full range of capabilities standard Javascript offers, you can also use **Snippets**.

**Snippets** are special functions that let you access data from HTTP requests (during the Pre-Request process) and HTTP responses (during Post-Response process). It also allows you to execute log statements, store calculated data as [Custom metrics]([LINK_URL_3]), and perform tests on a step data. These special functions are accessible through a unique object called [INLINE_CODE_1].

## General or base ut objects

In this section, the list of general [INLINE_CODE_2] objects are as follows:

- [INLINE_CODE_3] gives access to the API request object.
- [INLINE_CODE_4] gives access to the API response object.
- [INLINE_CODE_5] is the collection of variables that you can use across all API steps. Use this to pass values from one step to the next. Any [Predefined variables]([LINK_URL_4]) or variables you use in the [SHORTCODE_7] Response [SHORTCODE_8] tab is included in this object collection.
- [INLINE_CODE_6] is a helper function that outputs the specified logs in the console log. Logs when the pre-request scripts are executed are found in the **Pre-Request script Console log** while logs for post-response scripts are found in the **Post-response script Console log**.
- [INLINE_CODE_7] is the main function for capturing test outputs. Any test output you define inside each [INLINE_CODE_8] call will be captured and listed as an **Assertions** result along with the assertions you define from the [SHORTCODE_9] Response [SHORTCODE_10] tab of each step.
- [INLINE_CODE_9] is a collection of numeric values directly from an API response. You can define your own custom metric variable to store or calculate values from an API response. This value will be displayed in the monitor check details for each measurement and can also be listed and charted in dashboards.
- [INLINE_CODE_10] allows you to generate MD5, SHA, HMAC, and RSA hashes for secure data handling, transmission and singing. It can also be used to parse Certificate Revocation Lists (CRLs).
- [INLINE_CODE_11] allows you to perform Base64 string and Base64 URL encoding and decoding.

Now that you are familiar with the general [INLINE_CODE_12] base objects. In this section, the attributes of each [INLINE_CODE_13] object will be discussed in detail.

### Request

Attributes of [INLINE_CODE_14]:

- [INLINE_CODE_15] — get or set of the request's URL
- [INLINE_CODE_16] — get or set the request's HTTP method (such as GET and POST)
- [INLINE_CODE_17] — get or set a raw text version of the request body

### Request headers

Functions of [INLINE_CODE_18]:

- [INLINE_CODE_19] — returns whether the header exists and has a specific value
- [INLINE_CODE_20]— returns the value of the header. Returns an empty string if the header doesn't exist
- [INLINE_CODE_21] — creates a new header and its specified [INLINE_CODE_22] (only if the header was not already set)
- [INLINE_CODE_23] — inserts the header with the specified [INLINE_CODE_24] (if the header does not already exist) or updates the header with the specified value (if the header already exists)
- [INLINE_CODE_25] — removes the header

### Response

Attributes of [INLINE_CODE_26]:

- [INLINE_CODE_27] — gets the numeric HTTP response status code (such as 200, 404, 500)
- [INLINE_CODE_28]  — gets the HTTP status description (such as OK)
- [INLINE_CODE_29] — gets the size of the response in bytes
- [INLINE_CODE_30] — returns a byte array containing the response body. Responses are limited to 100 MB

Functions of [INLINE_CODE_31]:

- [INLINE_CODE_32] — returns a raw text version of the response body
- [INLINE_CODE_33] — returns an object by parsing the response text as JSON

### Response headers

Functions of [INLINE_CODE_34]:

- [INLINE_CODE_35] — returns whether the header exists
- [INLINE_CODE_36] — returns the value of the header. Returns an empty string if the header doesn't exist

### Variables

Functions of [INLINE_CODE_37]:

- [INLINE_CODE_38] — returns whether the variable exists
- [INLINE_CODE_39] — returns the value of the variable. Returns an empty string if the variable doesn't exist
- [INLINE_CODE_40] — creates the variable (if it doesn't exist) and stores the specified [INLINE_CODE_41] in the [INLINE_CODE_42] variable

### Custom metrics

Functions of [INLINE_CODE_43]:

- [INLINE_CODE_44] — returns the value of the custom metric variable. Returns an empty string if the custom metric doesn't exist
- [INLINE_CODE_45] — stores the specified [INLINE_CODE_46] in the custom metric [INLINE_CODE_47] variable

For more information, refer to the [Custom API metrics setup]([LINK_URL_5]) and [Multi-step monitoring variables]([LINK_URL_6]) knowledge base articles.

### Test or Assert

Uptrends supports the Expect and Should interfaces from Chai JS, see [Chai - Should]([LINK_URL_7]) and [Chai - Expect]([LINK_URL_8]) to read how to express various value tests and comparisons:

- [INLINE_CODE_48] + various expressions
- [INLINE_CODE_49] + various expressions  

Any [INLINE_CODE_50] and [INLINE_CODE_51] expressions (if used by themselves) will generate an error if the desired criteria are not met and will stop monitor execution. Any additional assertions defined in the remaining parts of the script will not be executed.

Use [INLINE_CODE_52] to execute the full set of assertions, regardless of whether any of the earlier assertion fails:

- [INLINE_CODE_53] — the output (success or failure) of an [INLINE_CODE_54] or [INLINE_CODE_55] defined inside the specified testFunction ends up in the monitor's assertions output. In addition, when an assertion fails, [INLINE_CODE_56] will make sure that execution of the script is not stopped.

### Hashing

Functions of [INLINE_CODE_57]:

- [INLINE_CODE_58] — generates an MD5 hash of the specified value
- [INLINE_CODE_59] — generates an SHA-1 hash of the specified value
- [INLINE_CODE_60] — generates an SHA-256 hash of the specified value
- [INLINE_CODE_61] — generates an SHA-512 hash of the specified value
The scripting methods for generating MD5 and SHA hashes enable you to store and send values securely, ensuring data protection through hashing. 

Example:

[CODE_BLOCK_1]

- [INLINE_CODE_62] — parses a Certificate Revocation List (CRL) and returns its metadata. A CRL file should be provided as input to the [INLINE_CODE_63] function. For example, if you want to read the [INLINE_CODE_64] field from a CRL file or CRL URL, you can use the function as follows:

[CODE_BLOCK_2]

#### HMAC hashing

Functions of [INLINE_CODE_65] for HMAC hashing:

- [INLINE_CODE_66] — generates an HMAC of the specified value using the SHA-1 hash function and the provided secret
- [INLINE_CODE_67] — generates an HMAC of the specified value using the SHA-256 hash function and the provided secret
- [INLINE_CODE_68] — generates an HMAC of the specified value using the SHA-512 hash function and the provided secret


#### RSA signing

Functions of [INLINE_CODE_69] for RSA signing:

- [INLINE_CODE_70] — signs the specified value with the RSA algorithm and SHA-1 as the hash function, using the provided private key in PEM, PKCS8, or PKCS1 format.
- [INLINE_CODE_71] — signs the specified value with the RSA algorithm and SHA-256 as the hash function, using the provided private key in PEM, PKCS8, or PKCS1 format.
- [INLINE_CODE_72] — signs the specified value with the RSA algorithm and SHA-512 as the hash function, using the provided private key in PEM, PKCS8, or PKCS1 format.

#### Base64 and Base64 URL encoding and decoding

Functions of [INLINE_CODE_73] for Base64 and Base64 URL encoding and decoding:

- [INLINE_CODE_74] — encodes the specified value as a Base64 string
- [INLINE_CODE_75] — decodes the specified Base64 string into its original value
- [INLINE_CODE_76]— encodes the specified value as a Base64 string using a URL-encoded variation for Base64 encoding, replacing certain characters with URL-safe alternatives
- [INLINE_CODE_77] —  decodes the specified Base64 string into its original value, using a URL-encoded variation for Base64 encoding that replaces certain characters with URL-safe alternatives