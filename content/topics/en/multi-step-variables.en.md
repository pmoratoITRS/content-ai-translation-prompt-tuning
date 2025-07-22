{
  "hero": {
    "title": "Multi-step monitoring Variables"
  },
  "title": "Multi-step monitoring Variables",
  "summary": "How to use variables for storage of values extracted from your API responses for use in later steps.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-variables"
}


In a [multi-step API monitoring setup]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="en" >}}), variables are typically used to extract values from your HTTP responses and temporarily store them, so you can use them again in a later step. This essentially lets you link steps together: every time you want to take a piece of information from an HTTP response and use that information to execute the next HTTP request, you'll need a variable. Simply put: Step 1 receives a value from your server and stores it in a variable. Step 2 then takes the value we just stored and uses it to build up a new request. You can use as many variables as you want, and use them in as many steps as you need.

A second reason to use variables is to define certain values just once, and re-use them in several steps. You will typically add those values in the Predefined variables section: those variables are available in any step throughout the entire multi-step scenario. See the [Predefined variables](#predefined-variables) section for more information.

All variables you define in a step are evaluated as soon as the HTTP request has been executed and the response has been processed. At that point, if a variable already existed (either through a previous step, or because you predefined it), its existing value will be overwritten. Otherwise, a new variable is created and added to the list. This list of variables and corresponding values will then be carried across to the next step.

## Defining variables

If you want to use variables, you'll need to tell us which value we should store in that variable. Similar to the pattern used to define assertions, variables are defined in the following way:

{{< Code/Symbol type="source" >}}Source{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}property{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}variable name{{< /Code/Symbol >}} 

for example:

{{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}access\_token{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}access\_token{{< /Code/Symbol >}} 

-   The **variable source**: this field defines which attribute of the HTTP response you want to extract. [Each available option is outlined in this article]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="en" >}}).
-   The **variable property**: some source options (in particular the content extraction and header related options) require you to further specify which content or header to check. This is [explained in more detail]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="en" >}}) for each appropriate source type.
-   The **variable name**: this is the identifier that will be used in subsequent steps to refer back to this variable, using a special notation.

If a problem occurs during the evaluation of a variable (for example, because you're trying to extract a value that is not present in the response content), the step will fail and an error will be reported.

## Referring to variables in other steps

Once a variable has been evaluated successfully, its value can be re-used in the request definition of subsequent steps, and inside assertions (response content checks). Always refer to a variable by enclosing the variable name in double curly braces: {{< Code/Symbol type="variable" >}}{{variable-name}}{{< /Code/Symbol >}}.

-   In the URL of a step: `https://myapi.customer.com/ProductInfo/{{ProductId}}`

-   In a Request header: `"Authorization": Bearer {{access_token}}`

-   In Request Body content:

    `{ "ProductId": "{{ProductId}}", "Code": "P123456" }`

-   In the target value of an assertion. For example, if you have a variable {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}} (populated in a previous step, or as a predefined variable), you can use it to verify that a response contains the actual value contained in that variable:

    {{< Code/Symbol type="source" >}}Response body as JSON{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}Products\[0\].Id{{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Equals{{< /Code/Symbol >}} {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}

-   In the property value of an assertion. If you have a variable {{< Code/Symbol type="variable" >}}{{ProductId}}{{< /Code/Symbol >}}, you can refer to that variable in a JSON expression or XPath query to select the content you're looking to verify:

    {{< Code/Symbol type="source" >}}Response body as XML{{< /Code/Symbol >}} {{< Code/Symbol type="property" >}}//Product\[@Id="{{ProductId}}"\]/Name/text(){{< /Code/Symbol >}} {{< Code/Symbol type="comparison" >}}Equals{{< /Code/Symbol >}} `Chocolate chip cookie`

## Predefined variables

Below the step editor, you'll find an additional section where you can specify more variables. These variables are available right at the beginning of the entire scenario. If you need a particular value several times, you can define that value in advance and use it in different steps. This could be a product Id you want to use throughout your scenario, an API key, or other special values your API needs.One special case is to use a variable that holds the domain name for each API. By using that variable as part of each URL, you don't have to repeat it in each step, allowing you to change it very easily for the entire scenario. To add a predefined variable, click {{< AppElement type="button" >}}\+ Add variable{{< /AppElement >}} in the monitor settings, under the *Predefined variables* section.  Then, create a variable named `BaseUrl` with value `https://test.yourapi.com`. Using a reference to that variable, the URL for each API step could then take the form `{{BaseURL}}/UserService/GetUserInfo`. This approach allows you to change your multi-step scenario to point to a different environment (e.g. staging environment vs. production environment) without having to change each step. 

Predefined variables can also be used in case sensitive data needs to be sent at any point during the monitor run. For example, if your API requires authenticated access, you may need to log in or retrieve an access token by adding credentials to one of your requests. Sensitive data is stored [in the vault]({{< ref path="/support/kb/account/vault" lang="en" >}}). To set up vault credentials for use in a Multi-Step API monitor, do the following:

1. First, make sure you've [added them to the vault]({{< ref path="/support/kb/account/vault#adding-a-new-item-to-the-vault" lang="en" >}}).
2. Create the predefined variable as you normally would, described above. 
3. To reference a vault item, click the [...] icon under **value**, which opens the value picker.

![MSA vault value picker](/img/content/scr_MSA_predefined_variables_1.min.png)

4. Select the appropriate credential set from the list, and select the value from either the username or password field.
5. Give your variable an appropriate **Name**, which you will use to refer to it during the monitor run as described in this article. In the example below, we'd refer to the *examplePassword* variable as `{{examplePassword}}`. 

![MSA vault value picker](/img/content/scr-MSA-predefined-variables-example.min.png)

In the monitor log, values taken from the *password* field in the vault item will be shown as asterisks, to keep the sensitive data hidden.

![MSA vault value picker](/img/content/MSA_predefined_variables_result.png)

## Encoding of variable values

Depending on where you use your variables, it's sometimes necessary to encode the values. Encoding means that we'll convert special characters to a format that is suitable for an HTTP request. Typically, variables that are used in a URL need to be encoded.For example, imagine you're building a URL that takes a name parameter, and you want to use a variable called {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} to specify a value for that parameter. Without considering encoding, you would use it like this:

`https://my.api.com/GetCompanyInfo?name={{CompanyName}}`

Now, suppose that the {{< Code/Symbol type="variable" >}}CompanyName{{< /Code/Symbol >}} variable contains the value `Ben & Jerry's`. That value contains spaces and an ampersand character, which have a special meaning in a URL. Without applying any encoding, you wouldn't get the correct value across to the server. If you apply encoding first, the value will be converted to `Ben\+%26\+Jerry's`, which will be interpreted by the server as the original value. To apply encoding to your variables, use the {{< Code/Symbol type="variable" >}}{{@UrlEncode(...)}}{{< /Code/Symbol >}} function. Inside the parentheses, include the full variable name, e.g. {{< Code/Symbol type="variable" >}}{{CompanyName}}{{< /Code/Symbol >}}. Used in a URL, it would look like this:

`https://my.api.com/GetCompanyInfo?name={{@UrlEncode({{CompanyName}})}}`

If a variable will never contain any special characters (for example, only numeric values), it's not necessary to use the @UrlEncode function.We'll automatically URL-encode variables used in the Request Body field of a step, but only if a Content-Type header has been specified with the value application/x-www-form-urlencoded. Other content types don't usually require URL encoding.

## Automatic variables

Aside from variables you define in your monitor setup, you also have access to a number of automatic variables that we create for you. Most of them are actually functions that generate a value you can use in your HTTP requests, and during the evaluation of your HTTP responses using assertions. If you wish to use any automatic variables in your Multi-Step API monitoring, please refer to our [complete list of available automatic variables]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="en" >}}).

## User-defined functions

In certain cases, the incoming data will need its values transformed or mapped, to make sense of it more easily. Uptrends allows you to set User-defined functions, which can be used to convert variable values (acquired in a previous step, or from a system variable provided by Uptrends) to a new value. For more information on how to set up and use user-defined functions, see [this Knowledge Base article]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="en" >}}).

## Custom metric variables

Whenever your MSA monitor captures data from your APIs, there may be instances wherein you want to track specific numerical data that are not part of the standard metrics, such as response status code and response duration, in evaluating your API's behavior.

In such cases, the Custom metric variable allows you to create a user-defined variable to store any numerical data captured from the API's response. To set up the Custom metric variable, refer to the [Custom API scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup#how-to-set-up-custom-api-monitoring" lang="en" >}}) knowledge base article.