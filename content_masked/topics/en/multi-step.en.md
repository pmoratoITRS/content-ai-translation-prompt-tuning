{
  "hero": {
    "title": "Setting up Multi-step API Monitoring"
  },
  "title": "Setting up Multi-step API Monitoring",
  "summary": "Step-by-step instructions for setting up Multi-step API Monitoring.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

To effectively monitor your API, you often need to create a sequence of HTTP requests, where each request retrieves data from a previous request to perform the next set of tasks. With the **Multi-step API monitor**, you can set up multiple HTTP requests, define [variables]([LINK_URL_1]), create [user-defined functions]([LINK_URL_2]), set up [custom scripting]([LINK_URL_3]), and many more.

Here are some possible scenarios why you should run a sequence of HTTP requests:

- Your API requires authenticated access — an API client must verify their login credentials first to access HTTP methods (for example, using the OAuth authentication).
- You want to test a functional scenario in your API consisting of multiple steps that are typically executed in a particular sequence by your end users.
- Your HTTP request returns a redirect to a different URL, and you want to inspect that response's behavior before following the redirect.

## Features of the Multi-step API monitor

The **Multi-step API monitor** gives you full control over the complete HTTP request content. Its features include:

- Set the HTTP method, URL, request headers, and request body for each request.
- [Add authentication (Basic/NTLM/Digest/OAuth)]([LINK_URL_4]) or [including client certificates]([LINK_URL_5]) to gain access to protected APIs.
- [Define assertions (checks) for each response]([LINK_URL_6]) to verify the HTTP status code, content checks (based on plain text, JSON content, or XML content), request duration, and more.
- Extract contents from the response body, response headers, cookies and [store them in variables]([LINK_URL_7]). Such variables can be used in later steps to build new URLs, request headers, and others.
- Use global definitions such as [pre-defined variables]([LINK_URL_8]), [user-defined functions]([LINK_URL_9]), [custom API metrics]([LINK_URL_10]), and [hashing and encoding]([LINK_URL_11]).

These features help you ensure that your API behaves correctly and performs within the limits you specify. The step-by-step approach allows you to set up very powerful scenarios without adding complexity. As long as you know how your API should behave, you don't need to have any programming skills to get started with API monitoring.

## Create a Multi-step API monitor

To add a multi-step API monitor:

1. Go to [SHORTCODE_7] API > API monitors setup [SHORTCODE_8] and click the [SHORTCODE_9][SHORTCODE_10] button.
2. In the *Select a monitor type* popup, click *Multi-step API* and click the [SHORTCODE_11] Choose [SHORTCODE_12] button.  
3. Once the monitor is created, give your monitor a *Name*.  
4. Set the *Check interval*. Your [check interval]([LINK_URL_12]) is the time between the end of one check and the start of the next.
5. Switch to the [SHORTCODE_13] Steps [SHORTCODE_14] tab to input the details for each step.

Your new monitor starts out with one (empty) step. You can do any of the following:
- Click [SHORTCODE_15] Add request step [SHORTCODE_16] to add additional steps.
- Click the **>** icon beside each step to expand and edit step details.
- Click the **copy** icon to duplicate and create a copy of an existing step. 
- Click the **X** icon to delete a step.
- Use the *Move step up* and *Move step down* buttons to move the position of the steps.

![Example MSA steps]([LINK_URL_13])

## Configure a Request step

Looking at the Visual step editor, you'll see the [SHORTCODE_17] Request [SHORTCODE_18] tab. A step in Multi-step API monitoring consists of one round-trip call to the API (for example, one request and one response). Within each step, you can define your request and tell Uptrends how to handle the response. Each Multi-step API starts with one empty step.

### Request

![Request tab details]([LINK_URL_14])

The **Request** tab contains all of the data needed to perform the actual HTTP request in the step. At a minimum:

1. Choose the appropriate HTTP method, either **GET**, **POST**, **PUT**, **PATCH**, **DELETE**, **HEAD** or **OPTIONS**. If you need a different method, [contact us]([LINK_URL_15]).
2. Fill in the URL for the request. Use a fully qualified URL, including the schema ("[URL_1] or "[URL_2]), the domain name and path for your API, and any query string parameters you want to include.

#### Request body

When specifying a POST, PUT, PATCH, HEAD, OPTIONS, or DELETE request, the **Request body** field lets you send specific data (payload) as part of the request definition. For example, sending a specific username and password to create a new user account.

The following are the request body data formats that you can choose from:

- Raw text — allows you to send plain texts without any formatting.
- Upload a file (as form-data) — allows you to send a file (such as images and documents from the [Vault]([LINK_URL_16])) in form-data format.
- Upload a file (as binary) — allows you to send a file (such as images and documents from the [Vault]([LINK_URL_17])) in a raw binary data format.
- Multi-part form — allows you to send multiple types of content in different formats (such as plain text entries or files retrieved from the [Vault]([LINK_URL_18])) all at once.

In most cases and depending on the chosen data format, the correct [INLINE_CODE_1] request header value is automatically set (such as [INLINE_CODE_2]) to let the server identify, read, and process your data correctly. You can also specify the [INLINE_CODE_3] request header which will be discussed in the next section of this article.

#### Request headers [ANCHOR_1]

An HTTP request usually contains some request headers to specify the format of the data that's being sent, or to further describe what kind of response is expected. When setting up a request step, you'll notice that certain headers are added automatically. These headers consist of a default set, depending on the type of request you're making (for example, GET requests will have a different set of headers than POST requests). To override a default header, simply add a new header and name it exactly as the existing one, but with a different value.

[SHORTCODE_1] **Note:** For optimization purposes, **Connection: Keep-Alive** was removed from the list of default request headers. In the background process, the request header is already the default behavior for HTTP/1.1 and is no longer supported for HTTP/2 and HTTP/3. [SHORTCODE_2]

You can also add new headers by following these steps:

1. Click the [SHORTCODE_19]Add request header[SHORTCODE_20] button to add a request header key and value.
2. Fill in Content-Type as the header key.
3. The appropriate header value depends on the data you're sending. The most common content types are [INLINE_CODE_4] for JSON data, [INLINE_CODE_5] for XML data, and [INLINE_CODE_6] for webform data.

Similarly, if your API requires you to include authentication, include a header [INLINE_CODE_7] along with the appropriate data in the Value field.

![Examples of request headers]([LINK_URL_19])

The image above shows an example of a request step. Notice the following:

- It is a POST request to [INLINE_CODE_8]
- The default headers set for this request are:
  - [INLINE_CODE_9]
  - [INLINE_CODE_10]
- The values for the [INLINE_CODE_11] header will be determined upon sending the request.
- Manual headers [INLINE_CODE_12] and [INLINE_CODE_13] have been added, to specify the data format and provide the necessary credentials, respectively.
- Default [INLINE_CODE_14] has been overridden.
- The request body contains some [INLINE_CODE_15] content, referencing some [variables]([LINK_URL_20]).

#### Authentication

A lot of APIs are protected and can only be accessed by supplying login credentials. If your API uses authentication on the HTTP protocol level, choose your type of authentication (Basic, NTLM or Digest) and fill in the corresponding username and password. Alternatively, you can set up OAuth based authentication using separate steps. [More information on setting up built-in or custom authentication]([LINK_URL_21]).

#### Use of credential set from the vault

It is possible to use [vault credential set]([LINK_URL_22]) references at any point as part of the request body, request headers, or as the value for your username/password under *Authentication*. To refer to a vault item, use the following syntax: [INLINE_CODE_16] or [INLINE_CODE_17] depending on which value is required. To find the [INLINE_CODE_18], navigate to the vault item with the credential set, then copy the last part of the URL in the URL bar of your browser.

![Examples of vault item references]([LINK_URL_23])

#### Set the TLS versions

The Transport Layer Security (TLS) is a security protocol that authenticates, encrypts, and protects connections between websites and servers. By ticking the *Only allow specific TLS versions* checkbox in your MSA monitor, you can select specific TLS versions during the TLS handshake for HTTP connection. You can also uncheck the checkbox if no restrictions are needed.

All [Uptrends checkpoints]([LINK_URL_24]) support TLS 1.1 and TLS 1.2. Selecting the TLS 1.3 option limits Checkpoint selection to those with TLS 1.3 capability. While TLS 1.1 is still available, it is not recommended.

![TLS versions checkbox in MSA monitors]([LINK_URL_25])

#### Set the HTTP version

The **HTTP version** option allows you to control which HTTP version the checkpoint servers use when making requests. Use this option to ensure that the servers communicate effectively with the API in terms of compatibility, performance, and security.

![HTTP version]([LINK_URL_26])

By default, the **HTTP version** option is unchecked, meaning the server will automatically use the highest supported HTTP version available, with a fallback back no lower than HTTP/1.1.

Currently, HTTP/3 is available at selected checkpoint locations, and support will soon be expanded to additional locations.

[SHORTCODE_3] **Note:** The HTTP version allows you to select only one version, while the **TLS version(s)** support selecting multiple versions.
[SHORTCODE_4]

### Import cURL requests [ANCHOR_2]

It is also possible to directly import cURL requests to create your steps, without having to manually recreate them. To do so:

1. In the **Visual step editor** (in the [SHORTCODE_21]Steps[SHORTCODE_22] tab of the monitor settings) of the Multi-step API monitor in which you wish to import a step based on a curl command click the [SHORTCODE_23]cURL import[SHORTCODE_24] button to open the import wizard.
2. Click the [SHORTCODE_25]Next[SHORTCODE_26] button.
3. Paste your cURL command line statement(s). For example, let's say we want to create a step based on cURL statement:

[CODE_BLOCK_1]

This is a request to create a reservation on our fake holiday booking testing site, [GalacticResorts.com]([LINK_URL_27]).

You can add multiple steps at once, by pasting multiple cURL commands.

4. If necessary, specify the command format. In most cases, however, 'Auto-Detect' will suffice.
5. Click the [SHORTCODE_27]Next[SHORTCODE_28] button.
6. In the final step of the wizard, click the [SHORTCODE_29]Generate steps[SHORTCODE_30] button.

The result for the cURL command mentioned in this example would be as follows:

![cURL import result]([LINK_URL_28])

The Multi-step API monitor type doesn't support all the options included in the cURL command line. Unsupported options will be automatically discarded, so make sure to try out the step to verify that it works as expected.

### Response

The response tab contains all options for performing checks on response data (using Assertions) and processing that data in preparation for the next step (using Variables).

![Response tab]([LINK_URL_29])

#### Assertions

Defining your steps and feeding the correct data into those steps is the ground layer for a useful setup. However, it's also important to look at the results of each step. Just calling a series of URLs is no good if they're not returning the right results. Assertions help you with those health checks.

Assertions are checks you can execute to verify that the response in a particular step behaved as expected, for example, by checking its content or verifying that it was retrieved within a certain amount of time. Like with variables, you specify the source for the check, e.g., a JSON property from the JSON response body, an XPath query on the XML response body, or even just the status code of the response, its duration or content length.

**More examples of Assertions**: read our [extensive guide for defining assertions]([LINK_URL_30]).

#### Variables

When you're setting up multi-step scenarios, it's likely that at least one of those steps depends on some input retrieved during a previous step. By capturing that input, storing it temporarily and taking it across to the next steps, you're creating a natural progression of connected steps, without the need to write any code.

Variables let you do exactly that! Each step can create new variables and has access to variables created by other steps, so you can re-use data that was captured previously in the scenario.

You can define where a variable should come from: probably a particular value from JSON or XML data, but capturing response headers or even data from a redirect is also possible. After a variable has defined, you can use it anywhere in your multi-step setup simply by referring to it by name: [SHORTCODE_37]{{my-variable}}[SHORTCODE_38].

**More examples of Variables**: [How to define and use variables]([LINK_URL_31]).

#### Maximum number of attempts [ANCHOR_3]

In some cases, it may be that your API needs some time to process an incoming request before it can respond indicating a success. For example, let's say you upload a file to your API for processing. While it's processing, the API responds to requests regarding the status with [INLINE_CODE_19] in a JSON body. Once processing finishes, the API starts responding with [INLINE_CODE_20] instead. In such cases, you can configure the monitor to keep polling the API until it responds with a success by using the **Maximum number of attempts** setting.

This function will set the monitor to retry the step if one or more of the assertions in the step (such as [SHORTCODE_39]Response body as JSON[SHORTCODE_40] [SHORTCODE_41]result[SHORTCODE_42] [SHORTCODE_43]Is equal to[SHORTCODE_44] [SHORTCODE_45]success[SHORTCODE_46] for the example mentioned above) fails. You can set how many retries the monitor should attempt, up to a maximum of 50 retries. Note that the minimum number of attempts is two, since the initial request already counts as the first attempt.

In addition to the number of retries you can set the wait time between those attempts. The wait time between attempts should be between 500 and 30000 ms and is set to 1000 ms by default. 

For each step, you can configure a maximum number of attempts in combination with a minimum wait time in between.

The monitor will continue retrying the step until either the maximum number of retries is reached or every assertion passes. At that point, the monitor will proceed as normal, executing the rest of the steps in order. If the maximum number of retries is reached, and still at least one assertion fails, the monitor will report an error in the monitor log.

The cost of the MSA monitor remains the same, regardless of the number of retries it uses.

## Configure file uploads

Multi-step API monitors allow you to upload files from [your vault]([LINK_URL_32]) as part of one of your request steps. Any HTTP steps you configure in the Multi-step API monitor that contains a request body may be either a form-data or binary file upload or a regular plain text request. Files will be sent as [INLINE_CODE_21] or binary content. To add a file as form-data, follow these steps:

1. [Upload the file in question]([LINK_URL_33]) to your vault. The maximum file size is 2 MB. 
2. In the settings of your Multi-Step API monitor, add a request step or use an existing step to execute the file upload. 
3. In the **Request** tab of the step that should execute the file upload, set the request method to *POST*, *PUT*, or *PATCH* (depending on which you require) and fill in the request URL.
4. Under **Request body**, select option *Upload a file (as form-data)*. 
5. Click the [SHORTCODE_31]Add file from vault[SHORTCODE_32] button that appears.
6. Choose the appropriate file from the Vault file upload list and click the [SHORTCODE_33]Select[SHORTCODE_34] button.
![File upload picker]([LINK_URL_34])
7. It is not necessary to add any specific request headers. We will automatically set a request header for [INLINE_CODE_22] and set [INLINE_CODE_23] with the correct boundary.
![Example headers for file upload]([LINK_URL_35])

If you want to upload a file without Uptrends adding [INLINE_CODE_24] metadata to the request body, you can select *Upload a file (as binary)* under **Request body** at step 4 above. We’ll still automatically generate the appropriate headers listed at **Request headers**, but without adding this specific metadata to the request. This way, if your API expects files uploaded as raw binary data, you still will be able to test it.

Keep in mind that your API may be expecting a specific value for the file name. The request will include an automatically constructed header **Content-Disposition**, containing some metadata. The value for this header contains a *name* parameter. By default, we'll use the file name as specified by you in the vault. Please make sure the file name you specify when adding the file to the vault matches the value expected by your API. For example, if your API expects the uploaded file to be named "image", make sure you specify "image" (without a file extension) as the file name in the appropriate vault item.

## Configure a Wait step

When you've added a sequence of Request steps to your monitor, each step will be executed as soon as the previous step finishes, without any delay. However, this immediate execution may be a bit too quick for some scenarios.

Consider an API method that acts as a request for a report file to be generated. The API kicks off a backend process that will generate the file, and instructs the caller to send a second request in order to download the new file. Generating that file may take a second or two, so the caller should wait for a few seconds before sending the second request. If the second request is sent too soon, it will fail since the generated file isn't ready yet.

For this scenario, it's important to wait before the second request is executed. To do this, you can insert a separate Wait step. This type of step allows you to specify the number of milliseconds to wait. For example, to wait 3 seconds, specify 3000 milliseconds as the wait time. This wait time will be included in the total time metric for this monitor.

To add a wait step, simply click the [SHORTCODE_35] Add wait step [SHORTCODE_36] button and specify the number of milliseconds you want to wait. If necessary, you can move the wait step to the right spot in your scenario using the Move step up/down buttons.

The wait time for a wait step is limited to 60 seconds: a wait step is not intended to monitor a long-running task that takes several minutes or hours. If the monitor exceeds the maximum total running time, the check will stop running and a failure will be reported.

Adding a wait step to your monitor doesn't cost you anything. The cost of a Multi-step API monitor is only based on the number of Request steps.

[SHORTCODE_5] **Note:** The duration of the execution of all the steps in your monitor may not exceed 4 minutes in total. If the monitor takes longer than 4 minutes to execute from beginning to end, the monitor check result will be an error. In such cases, please consider spreading out your requests over multiple monitors, if possible. [SHORTCODE_6]

## Multi-step monitor results, errors and alerting

Multi-step API monitors behave in the same way as any other monitor. Each check appears in the monitor log, and displays extensive information for each individual step. For each step, this information consists of the following:

- **Total duration** of the step (in milliseconds).
- **URL** that was executed during that step.
- **HTTP status code** that was returned.
- Result for each **assertion** (pass or fail).
- **Request headers and content** that we sent.
- **Response headers and content** that we received.

If a problem occurs during one of the steps, or if one of the assertions you defined does not pass, the monitor will fail and report an error. As usual, these errors can generate alerts based on your alert definitions.