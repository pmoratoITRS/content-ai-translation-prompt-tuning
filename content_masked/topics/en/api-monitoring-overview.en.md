{
  "hero": {
    "title": "API Monitoring overview"
  },
  "title": "API Monitoring overview",
  "summary": "What is API monitoring and how can you use it?",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/api-monitoring-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

An API (Application Programming Interface) is software that enables the communication between applications. Maybe you are using your own APIs and/or you rely on third-party APIs. Either way, the correct functioning of the APIs is crucial to the operation of your website and services, therefore you should monitor them.

API monitoring checks whether the APIs that you rely on are available, function correctly and perform well. More information can be found in the article [What is API monitoring?]([LINK_URL_1]).

Uptrends API monitoring offers different types of monitors to set up API monitoring. The choice of type depends on whether you have to deal with a single step or with a chain of requests consisting of multiple steps. The single-step monitor is defined using the Webservice HTTP or Webservice HTTPS monitor type. The monitor for a sequence of steps is defined using the Multi-step API monitor (MSA monitor) type.

The Uptrends app has a [Multi-step API monitor hub]([LINK_URL_2]) where knowledge about these monitors and the current status can be found in one place.

## Setting up API monitors

The setup of the different types of monitors is documented in these articles:

-   [Setting up Web Services monitoring]([LINK_URL_3])
-   [Setting up Web Services monitoring (SOAP)]([LINK_URL_4])
-   [Setting up Multi-step API monitoring]([LINK_URL_5])
-   [Setting up Postman API monitoring]([LINK_URL_6])

## Defining Multi-step API monitor steps

When setting up a Multi-step API monitor, you define a step for each HTTP request that is part of the scenario you want to monitor. For each step, you will look at two parts: First, you will specify the details for the Request part, defining what needs to be executed and sent to your API. And second, you will specify the Response part, defining what needs to be checked in the response of our API.

Both the Request and Response parts for each step can optionally be extended using [Custom scripting]([LINK_URL_7]), written in Javascript. You can add your custom scripts for authentication and perform calculations and custom logic to verify correct functionality and content of your API steps.

There are also some definitions for [user-defined functions]([LINK_URL_8]), [variables]([LINK_URL_9]) and [custom metrics]([LINK_URL_10]). These are set globally (available to all steps). Check out the articles in the sections below to learn more about setting up the HTTP steps.

### Request

The HTTP step request is set up by providing a method and a URL and the request body, then specifying further details like the authentication. The Request definition can also be further modified using custom scripting. See the articles below for more information.

-   [Authentication]([LINK_URL_11])
-   [Client certificates]([LINK_URL_12])
-   [Uptrends' client certificate]([LINK_URL_13])
-   [File uploads in Multi-Step API]([LINK_URL_14])
- [Custom scripting]([LINK_URL_15])

### Response

Within the response of the step you should define assertions. Assertions are checks that go one step beyond the question if there is a response to the request. An assertion will also check if the response is valid or arrives in time. For each step you can define a number of assertions. In addition to defining Assertions in the Response tab, it is possible to set up completely custom checks and logic using the Custom Scripting feature. Find more information about assertions in these articles:

-   [Assertions - Introduction]([LINK_URL_16])
-   [Assertions - Sources]([LINK_URL_17])
-   [Assertions - Comparison operators]([LINK_URL_18])
-   [Assertions - Examples using XPath]([LINK_URL_19])
-   [Variables]([LINK_URL_20])
-   [Handling redirects]([LINK_URL_21])
- [Custom scripting]([LINK_URL_22])

### Global definitions

There are a number of things that you can define for all steps and both the request and response part of them. This comes in handy if you want to use a certain value or function across different steps. Read on in the following articles to find out more:

-   [Predefined variables]([LINK_URL_23])
-   [User-defined functions]([LINK_URL_24])
-   [Custom metrics]([LINK_URL_25])
-   [Hashing and encoding]([LINK_URL_26])

### Script view

You can also edit Multi-step API monitor step definitions directly in the *script view*. This script contains the entire definition of your Multi-step API definition, that you can copy and paste to other places. See our article on the [MSA script editor]([LINK_URL_27])for more information.

Note that the *script view* is not the same as the [Custom scripting]([LINK_URL_28]) feature that allows you to add custom logic to your scripts.

## Credits

API monitors use API credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]([LINK_URL_29]) knowledge base article.