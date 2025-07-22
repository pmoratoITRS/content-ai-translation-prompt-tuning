{
  "hero": {
    "title": "Multi-step API custom scripting"
  },
  "title": "Multi-step API custom scripting",
  "summary":"An overview of the Custom Scripting options in Multi-step API monitoring",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-custom-scripting"
}

The Multi-step API (MSA) monitor features powerful [built-in functions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}) that provide a user-friendly and no-code solution to test the behavior of your APIs.

While a no-code approach goes a long way in building proper monitoring setups, you might need a scripting language to do in-depth functional tests and completely describe what you expect from your APIs. For example, adding a custom logic or handling more advanced behaviors which cannot be achieved in a UI-based setup only.

The MSA monitor lets you handle both classic no-code features along with custom scripting. You can use built-in UI functions along with their scripting counterparts. You don't have to create your monitors from scratch if you have existing API monitors and want to add custom scripting. Simply start adding some scripts and have them work alongside your existing setup.

## Pre-Request and Post-Response scripts

An API monitor consists of a single or multiple steps executed in a sequence. For each MSA step (except Wait steps), two script editors,
{{< AppElement type="tab" >}} Pre-Request {{< /AppElement >}} and {{< AppElement type="tab" >}} Post-Response {{< /AppElement >}} tabs are available:

- The **Pre-Request script** editor lets you write scripts in preparation for sending an HTTP request. This is useful for preparing and calculating any values you want to include in the request, such as environment variables, URL parameters, request headers, or content body. The script written in this editor runs *before* the API request is sent to the server.

- The **Post-Response script** editor lets you write scripts to verify and process the HTTP response that comes back from the API. This is useful for writing custom logic to check response headers, validate the completeness and consistency of your content, and use that content data to prepare for any next steps. The script written in this editor only runs *after* the API response is successfully received from the server. If a connection error occurs, the script will not be executed, and any assertions or variables in the {{< AppElement type="tab" >}} Response {{< /AppElement >}} tab will not be validated.

These editors also includes the following features:
![Custom scripting tabs](/img/content/API-monitoring-custom-scripting-editors-min.png)

- Line numbering — displays numerical values that identifies the scripts or codes per line.
- Code highlighting — displays codes in color-coded format to easily identify syntax errors and keywords.
- Code completion — automatically suggests possible code combinations to assist script writing.
- Snippets panel — provides a list of helpful code snippets that you can automatically insert in your code editor once selected.

## Snippets

The **Pre-Request** and **Post-Response** editors allow you to insert and execute scripts written in JavaScript language. Aside from the full range of capabilities standard Javascript offers, you can also use **Snippets**.

**Snippets** are special functions that let you access data from HTTP requests (during the Pre-Request process) and HTTP responses (during Post-Response process). It also allows you to execute log statements, store calculated data as [Custom metrics]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="en" >}}), and perform tests on a step data. These special functions are accessible through a unique object called `ut`.

## General or base ut objects

In this section, the list of general `ut` objects are as follows:

- `ut.request` gives access to the API request object.
- `ut.response` gives access to the API response object.
- `ut.variables` is the collection of variables that you can use across all API steps. Use this to pass values from one step to the next. Any [Predefined variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="en" >}}) or variables you use in the {{< AppElement type="tab" >}} Response {{< /AppElement >}} tab is included in this object collection.
- `ut.log()` is a helper function that outputs the specified logs in the console log. Logs when the pre-request scripts are executed are found in the **Pre-Request script Console log** while logs for post-response scripts are found in the **Post-response script Console log**.
- `ut.test()` is the main function for capturing test outputs. Any test output you define inside each `ut.test()` call will be captured and listed as an **Assertions** result along with the assertions you define from the {{< AppElement type="tab" >}} Response {{< /AppElement >}} tab of each step.
- `ut.customMetrics` is a collection of numeric values directly from an API response. You can define your own custom metric variable to store or calculate values from an API response. This value will be displayed in the monitor check details for each measurement and can also be listed and charted in dashboards.
- `ut.crypto` allows you to generate MD5, SHA, HMAC, and RSA hashes for secure data handling, transmission and singing. It can also be used to parse Certificate Revocation Lists (CRLs).
- `ut.encoding` allows you to perform Base64 string and Base64 URL encoding and decoding.

Now that you are familiar with the general `ut` base objects. In this section, the attributes of each `ut` object will be discussed in detail.

### Request

Attributes of `ut.request`:

- `.url` — get or set of the request's URL
- `.method` — get or set the request's HTTP method (such as GET and POST)
- `.body` — get or set a raw text version of the request body

### Request headers

Functions of `ut.request.headers`:

- `.has(header, value)` — returns whether the header exists and has a specific value
- `.get(header)`— returns the value of the header. Returns an empty string if the header doesn't exist
- `.add(header, value)` — creates a new header and its specified `value` (only if the header was not already set)
- `.upsert(header, value)` — inserts the header with the specified `value` (if the header does not already exist) or updates the header with the specified value (if the header already exists)
- `.remove(header)` — removes the header

### Response

Attributes of `ut.response`:

- `.code` — gets the numeric HTTP response status code (such as 200, 404, 500)
- `.status`  — gets the HTTP status description (such as OK)
- `.responseSize` — gets the size of the response in bytes
- `.bytes` — returns a byte array containing the response body. Responses are limited to 100 MB

Functions of `ut.response`:

- `.text()` — returns a raw text version of the response body
- `.json()` — returns an object by parsing the response text as JSON

### Response headers

Functions of `ut.response.headers`:

- `.has(header)` — returns whether the header exists
- `.get(header)` — returns the value of the header. Returns an empty string if the header doesn't exist

### Variables

Functions of `ut.variables`:

- `.has(key)` — returns whether the variable exists
- `.get(key)` — returns the value of the variable. Returns an empty string if the variable doesn't exist
- `.set(key, value)` — creates the variable (if it doesn't exist) and stores the specified `value` in the `key` variable

### Custom metrics

Functions of `ut.customMetrics`:

- `.get(key)` — returns the value of the custom metric variable. Returns an empty string if the custom metric doesn't exist
- `.set(key, value)` — stores the specified `value` in the custom metric `key` variable

For more information, refer to the [Custom API metrics setup]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="en" >}}) and [Multi-step monitoring variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="en" >}}) knowledge base articles.

### Test or Assert

Uptrends supports the Expect and Should interfaces from Chai JS, see [Chai - Should](https://www.chaijs.com/guide/styles/#should "https://www.chaijs.com/guide/styles/#should") and [Chai - Expect](https://www.chaijs.com/guide/styles/#expect "https://www.chaijs.com/guide/styles/#expect") to read how to express various value tests and comparisons:

- `ut.expect(value)` + various expressions
- `ut.should(value)` + various expressions  

Any `.expect()` and `.should()` expressions (if used by themselves) will generate an error if the desired criteria are not met and will stop monitor execution. Any additional assertions defined in the remaining parts of the script will not be executed.

Use `ut.test()` to execute the full set of assertions, regardless of whether any of the earlier assertion fails:

- `ut.test(descriptionText, testFunction)` — the output (success or failure) of an `.expect` or `.should` defined inside the specified testFunction ends up in the monitor's assertions output. In addition, when an assertion fails, `ut.test()` will make sure that execution of the script is not stopped.

### Hashing

Functions of `ut.crypto`:

- `.md5(value)` — generates an MD5 hash of the specified value
- `.sha1(value)` — generates an SHA-1 hash of the specified value
- `.sha256(value)` — generates an SHA-256 hash of the specified value
- `.sha512(value)` — generates an SHA-512 hash of the specified value
The scripting methods for generating MD5 and SHA hashes enable you to store and send values securely, ensuring data protection through hashing. 

Example:

```js
var hashedMD5value = ut.crypto.md5("value here");
var hashedSHA1value = ut.crypto.sha1("value here");
```

- `.cert.parseCrl(bytes)` — parses a Certificate Revocation List (CRL) and returns its metadata. A CRL file should be provided as input to the `.cert.parseCrl(bytes)` function. For example, if you want to read the `NextUpdate` field from a CRL file or CRL URL, you can use the function as follows:

```js
  var crl = ut.crypto.cert.parseCrl(ut.response.bytes);
  var crlNextUpdate = new Date(crl.NextUpdate);
  ut.log(ut.crypto.cert.parseCrl(ut.response.bytes));

  // Assert the value of a variable
  ut.test("Variable {variable} should equal {value}", () => {
    expect(crlNextUpdate).at.least(new Date(2026, 1, 1));
  });
```

#### HMAC hashing

Functions of `ut.crypto` for HMAC hashing:

- `.hmacsha1(value, secret)` — generates an HMAC of the specified value using the SHA-1 hash function and the provided secret
- `.hmacsha256(value, secret)` — generates an HMAC of the specified value using the SHA-256 hash function and the provided secret
- `.hmacsha512(value, secret)` — generates an HMAC of the specified value using the SHA-512 hash function and the provided secret


#### RSA signing

Functions of `ut.crypto` for RSA signing:

- `.rsasha1(value, privateKey, privateKeyType)` — signs the specified value with the RSA algorithm and SHA-1 as the hash function, using the provided private key in PEM, PKCS8, or PKCS1 format.
- `.rsasha256(value, privateKey, privateKeyType)` — signs the specified value with the RSA algorithm and SHA-256 as the hash function, using the provided private key in PEM, PKCS8, or PKCS1 format.
- `.rsasha512(value, privateKey, privateKeyType)` — signs the specified value with the RSA algorithm and SHA-512 as the hash function, using the provided private key in PEM, PKCS8, or PKCS1 format.

#### Base64 and Base64 URL encoding and decoding

Functions of `ut.encoding` for Base64 and Base64 URL encoding and decoding:

- `.base64.encode(value)` — encodes the specified value as a Base64 string
- `.base64.decode(Base64-string)` — decodes the specified Base64 string into its original value
- `.base64.urlencode(value)`— encodes the specified value as a Base64 string using a URL-encoded variation for Base64 encoding, replacing certain characters with URL-safe alternatives
- `.base64.urldecode(Base64-string)` —  decodes the specified Base64 string into its original value, using a URL-encoded variation for Base64 encoding that replaces certain characters with URL-safe alternatives