{
  "title": "Pre-request and post-response scripting in Multi-step API monitors",
  "date": "2024-07-03",
  "url": "/changelog/july-2024-msa-scripting",
  "translationKey": "https://www.uptrends.com/changelog/july-2024-msa-scripting"
}

We have enabled [custom pre-request and post-response scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting" lang="en" >}}) for steps in [Multi-step API monitors]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step" lang="en" >}}). The Multi-step API monitor type supports many built-in options to configure requests and handle the response, but for some use cases, extra flexibility or functionality may be required. The new scripting tabs allow users to apply and execute Javascript code to the request and the response for each step, including special functions to interact with the rest of the monitor settings.

![MSA pre-request script example](/img/content/scr-msa-prerequest-script.min.png)

With some scripting, this will allow for maximum flexibility to configure the request or response handling in exactly the way you require.