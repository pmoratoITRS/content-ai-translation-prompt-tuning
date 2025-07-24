{
  "hero": {
    "title": "Multi-step monitoring Variables"
  },
  "title": "Multi-step monitoring Variables",
  "summary": "How to use variables for storage of values extracted from your API responses for use in later steps.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/multi-step-variables",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In a [multi-step API monitoring setup]([LINK_URL_1]), variables are typically used to extract values from your HTTP responses and temporarily store them, so you can use them again in a later step. This essentially lets you link steps together: every time you want to take a piece of information from an HTTP response and use that information to execute the next HTTP request, you'll need a variable. Simply put: Step 1 receives a value from your server and stores it in a variable. Step 2 then takes the value we just stored and uses it to build up a new request. You can use as many variables as you want, and use them in as many steps as you need.

A second reason to use variables is to define certain values just once, and re-use them in several steps. You will typically add those values in the Predefined variables section: those variables are available in any step throughout the entire multi-step scenario. See the [Predefined variables]([LINK_URL_2]) section for more information.

All variables you define in a step are evaluated as soon as the HTTP request has been executed and the response has been processed. At that point, if a variable already existed (either through a previous step, or because you predefined it), its existing value will be overwritten. Otherwise, a new variable is created and added to the list. This list of variables and corresponding values will then be carried across to the next step.

## Defining variables

If you want to use variables, you'll need to tell us which value we should store in that variable. Similar to the pattern used to define assertions, variables are defined in the following way:

[SHORTCODE_3]Source[SHORTCODE_4] [SHORTCODE_5]property[SHORTCODE_6] [SHORTCODE_7]variable name[SHORTCODE_8] 

for example:

[SHORTCODE_9]Response body as JSON[SHORTCODE_10] [SHORTCODE_11]access\_token[SHORTCODE_12] [SHORTCODE_13]access\_token[SHORTCODE_14] 

-   The **variable source**: this field defines which attribute of the HTTP response you want to extract. [Each available option is outlined in this article]([LINK_URL_3]).
-   The **variable property**: some source options (in particular the content extraction and header related options) require you to further specify which content or header to check. This is [explained in more detail]([LINK_URL_4]) for each appropriate source type.
-   The **variable name**: this is the identifier that will be used in subsequent steps to refer back to this variable, using a special notation.

If a problem occurs during the evaluation of a variable (for example, because you're trying to extract a value that is not present in the response content), the step will fail and an error will be reported.

## Referring to variables in other steps

Once a variable has been evaluated successfully, its value can be re-used in the request definition of subsequent steps, and inside assertions (response content checks). Always refer to a variable by enclosing the variable name in double curly braces: [SHORTCODE_15]{{variable-name}}[SHORTCODE_16].

-   In the URL of a step: [INLINE_CODE_1]

-   In a Request header: [INLINE_CODE_2]

-   In Request Body content:

    [INLINE_CODE_3]

-   In the target value of an assertion. For example, if you have a variable [SHORTCODE_17]{{ProductId}}[SHORTCODE_18] (populated in a previous step, or as a predefined variable), you can use it to verify that a response contains the actual value contained in that variable:

    [SHORTCODE_19]Response body as JSON[SHORTCODE_20] [SHORTCODE_21]Products\[0\].Id[SHORTCODE_22] [SHORTCODE_23]Equals[SHORTCODE_24] [SHORTCODE_25]{{ProductId}}[SHORTCODE_26]

-   In the property value of an assertion. If you have a variable [SHORTCODE_27]{{ProductId}}[SHORTCODE_28], you can refer to that variable in a JSON expression or XPath query to select the content you're looking to verify:

    [SHORTCODE_29]Response body as XML[SHORTCODE_30] [SHORTCODE_31]//Product\[@Id="{{ProductId}}"\]/Name/text()[SHORTCODE_32] [SHORTCODE_33]Equals[SHORTCODE_34] [INLINE_CODE_4]

## Predefined variables

Below the step editor, you'll find an additional section where you can specify more variables. These variables are available right at the beginning of the entire scenario. If you need a particular value several times, you can define that value in advance and use it in different steps. This could be a product Id you want to use throughout your scenario, an API key, or other special values your API needs.One special case is to use a variable that holds the domain name for each API. By using that variable as part of each URL, you don't have to repeat it in each step, allowing you to change it very easily for the entire scenario. To add a predefined variable, click [SHORTCODE_1]\+ Add variable[SHORTCODE_2] in the monitor settings, under the *Predefined variables* section.  Then, create a variable named [INLINE_CODE_5] with value [INLINE_CODE_6]. Using a reference to that variable, the URL for each API step could then take the form [INLINE_CODE_7]. This approach allows you to change your multi-step scenario to point to a different environment (e.g. staging environment vs. production environment) without having to change each step. 

Predefined variables can also be used in case sensitive data needs to be sent at any point during the monitor run. For example, if your API requires authenticated access, you may need to log in or retrieve an access token by adding credentials to one of your requests. Sensitive data is stored [in the vault]([LINK_URL_5]). To set up vault credentials for use in a Multi-Step API monitor, do the following:

1. First, make sure you've [added them to the vault]([LINK_URL_6]).
2. Create the predefined variable as you normally would, described above. 
3. To reference a vault item, click the [...] icon under **value**, which opens the value picker.

![MSA vault value picker]([LINK_URL_7])

4. Select the appropriate credential set from the list, and select the value from either the username or password field.
5. Give your variable an appropriate **Name**, which you will use to refer to it during the monitor run as described in this article. In the example below, we'd refer to the *examplePassword* variable as [INLINE_CODE_8]. 

![MSA vault value picker]([LINK_URL_8])

In the monitor log, values taken from the *password* field in the vault item will be shown as asterisks, to keep the sensitive data hidden.

![MSA vault value picker]([LINK_URL_9])

## Encoding of variable values

Depending on where you use your variables, it's sometimes necessary to encode the values. Encoding means that we'll convert special characters to a format that is suitable for an HTTP request. Typically, variables that are used in a URL need to be encoded.For example, imagine you're building a URL that takes a name parameter, and you want to use a variable called [SHORTCODE_35]CompanyName[SHORTCODE_36] to specify a value for that parameter. Without considering encoding, you would use it like this:

[INLINE_CODE_9]

Now, suppose that the [SHORTCODE_37]CompanyName[SHORTCODE_38] variable contains the value [INLINE_CODE_10]. That value contains spaces and an ampersand character, which have a special meaning in a URL. Without applying any encoding, you wouldn't get the correct value across to the server. If you apply encoding first, the value will be converted to [INLINE_CODE_11], which will be interpreted by the server as the original value. To apply encoding to your variables, use the [SHORTCODE_39][SYSTEM_VAR_1][SHORTCODE_40] function. Inside the parentheses, include the full variable name, e.g. [SHORTCODE_41]{{CompanyName}}[SHORTCODE_42]. Used in a URL, it would look like this:

[INLINE_CODE_12]

If a variable will never contain any special characters (for example, only numeric values), it's not necessary to use the @UrlEncode function.We'll automatically URL-encode variables used in the Request Body field of a step, but only if a Content-Type header has been specified with the value application/x-www-form-urlencoded. Other content types don't usually require URL encoding.

## Automatic variables

Aside from variables you define in your monitor setup, you also have access to a number of automatic variables that we create for you. Most of them are actually functions that generate a value you can use in your HTTP requests, and during the evaluation of your HTTP responses using assertions. If you wish to use any automatic variables in your Multi-Step API monitoring, please refer to our [complete list of available automatic variables]([LINK_URL_10]).

## User-defined functions

In certain cases, the incoming data will need its values transformed or mapped, to make sense of it more easily. Uptrends allows you to set User-defined functions, which can be used to convert variable values (acquired in a previous step, or from a system variable provided by Uptrends) to a new value. For more information on how to set up and use user-defined functions, see [this Knowledge Base article]([LINK_URL_11]).

## Custom metric variables

Whenever your MSA monitor captures data from your APIs, there may be instances wherein you want to track specific numerical data that are not part of the standard metrics, such as response status code and response duration, in evaluating your API's behavior.

In such cases, the Custom metric variable allows you to create a user-defined variable to store any numerical data captured from the API's response. To set up the Custom metric variable, refer to the [Custom API scripting]([LINK_URL_12]) knowledge base article.