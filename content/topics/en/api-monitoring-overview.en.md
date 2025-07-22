{
  "hero": {
    "title": "API Monitoring overview"
  },
  "title": "API Monitoring overview",
  "summary": "What is API monitoring and how can you use it?",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/api-monitoring-overview",
  "sectionlist": false
}

An API (Application Programming Interface) is software that enables the communication between applications. Maybe you are using your own APIs and/or you rely on third-party APIs. Either way, the correct functioning of the APIs is crucial to the operation of your website and services, therefore you should monitor them.

API monitoring checks whether the APIs that you rely on are available, function correctly and perform well. More information can be found in the article [What is API monitoring?]({{< ref path="/what-is/api-monitoring" lang="en" >}}).

Uptrends API monitoring offers different types of monitors to set up API monitoring. The choice of type depends on whether you have to deal with a single step or with a chain of requests consisting of multiple steps. The single-step monitor is defined using the Webservice HTTP or Webservice HTTPS monitor type. The monitor for a sequence of steps is defined using the Multi-step API monitor (MSA monitor) type.

The Uptrends app has a [Multi-step API monitor hub]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-hub" lang="en" >}}) where knowledge about these monitors and the current status can be found in one place.

## Setting up API monitors

The setup of the different types of monitors is documented in these articles:

-   [Setting up Web Services monitoring]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-monitor-add" lang="en" >}})
-   [Setting up Web Services monitoring (SOAP)]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/setting-up-a-soap-web-service-probe" lang="en" >}})
-   [Setting up Multi-step API monitoring]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="en" >}})
-   [Setting up Postman API monitoring]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/postman-api-monitoring" lang="en" >}})

## Defining Multi-step API monitor steps

When setting up a Multi-step API monitor, you define a step for each HTTP request that is part of the scenario you want to monitor. For each step, you will look at two parts: First, you will specify the details for the Request part, defining what needs to be executed and sent to your API. And second, you will specify the Response part, defining what needs to be checked in the response of our API.

Both the Request and Response parts for each step can optionally be extended using [Custom scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}}), written in Javascript. You can add your custom scripts for authentication and perform calculations and custom logic to verify correct functionality and content of your API steps.

There are also some definitions for [user-defined functions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="en" >}}), [variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="en" >}}) and [custom metrics]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="en" >}}). These are set globally (available to all steps). Check out the articles in the sections below to learn more about setting up the HTTP steps.

### Request

The HTTP step request is set up by providing a method and a URL and the request body, then specifying further details like the authentication. The Request definition can also be further modified using custom scripting. See the articles below for more information.

-   [Authentication]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="en" >}})
-   [Client certificates]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication" lang="en" >}})
-   [Uptrends' client certificate]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information" lang="en" >}})
-   [File uploads in Multi-Step API]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step#configuring-file-uploads" lang="en" >}})
- [Custom scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}})

### Response

Within the response of the step you should define assertions. Assertions are checks that go one step beyond the question if there is a response to the request. An assertion will also check if the response is valid or arrives in time. For each step you can define a number of assertions. In addition to defining Assertions in the Response tab, it is possible to set up completely custom checks and logic using the Custom Scripting feature. Find more information about assertions in these articles:

-   [Assertions - Introduction]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="en" >}})
-   [Assertions - Sources]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-sources" lang="en" >}})
-   [Assertions - Comparison operators]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-comparison-operations" lang="en" >}})
-   [Assertions - Examples using XPath]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-xpath-examples" lang="en" >}})
-   [Variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables" lang="en" >}})
-   [Handling redirects]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-redirects" lang="en" >}})
- [Custom scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}})

### Global definitions

There are a number of things that you can define for all steps and both the request and response part of them. This comes in handy if you want to use a certain value or function across different steps. Read on in the following articles to find out more:

-   [Predefined variables]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-variables#predefined" lang="en" >}})
-   [User-defined functions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/user-defined-functions" lang="en" >}})
-   [Custom metrics]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/custom-api-metrics-setup" lang="en" >}})
-   [Hashing and encoding]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/hashing-and-encoding" lang="en" >}})

### Script view

You can also edit Multi-step API monitor step definitions directly in the *script view*. This script contains the entire definition of your Multi-step API definition, that you can copy and paste to other places. See our article on the [MSA script editor]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/msa-script-editor" lang="en" >}})for more information.

Note that the *script view* is not the same as the [Custom scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}}) feature that allows you to add custom logic to your scripts.

## Credits

API monitors use API credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="en" >}}) knowledge base article.