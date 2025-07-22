{
  "hero": {
    "title": "Error handling in Multi-step APIs"
  },
  "title": "Error handling in Multi-step APIs",
  "summary":"Know how to handle and ignore errors in a Multi-step API monitor.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-error-handling",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-error-handling"
}

There might be situations where you encounter unexpected and dynamic web server behaviors when testing your Multi-Step API (MSA) monitors or when a monitor runs checks. Some of these behaviors are request timeouts and failed assertions that stop your monitors from getting other requests.

For example, you've set up an MSA monitor to retrieve information from an e-commerce platform. This monitor includes four /GET request steps arranged as follows:

1. GET /product — returns all products and their information.
2. GET /products/{productID} — returns a specific product and its information.
3. GET /users — returns all users and their information.
4. GET /users/{userID} — returns a specific user and its information.

Above configuration shows that steps one and two retrieves product details, while steps three and four retrieves user details. If you run this monitor and Step 2 fails because of an error, such as request timeout or a change in the endpoint name, the error blocks the monitor from executing the next steps.

This is where the **Error handling** feature becomes useful. Even if Step 2 caused an error, you can still retrieve details from Steps three and four, as these are independent from the previous /GET requests. The error shouldn't prevent your monitor from running the remaining steps.

## Error handling

The MSA **Error handling** feature lets you control and handle API errors with flexibility. For each MSA step in your monitor, you have the option to select the **Continue execution after an error** checkbox to ignore errors that occurred in that step:

![MSA Error handling checkbox](/img/content/scr-error-handling-checkbox.min.png)

By enabling this option, if a particular step encounters any form of errors, your monitor automatically skips that step and jumps to the next steps. Your monitor ignores errors, meaning these errors will not be recorded or reflected in any of your [Errors overview dashboards]({{< ref path="/support/kb/alerting/errors/errors-overview" lang="en" >}}) or [reports]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/exporting-dashboard-data" lang="en" >}}). All ignored errors only shows in the **Check details** popup once you perform the **Test Now** and in the monitor logs.

To further understand this concept, the image below shows the monitor result of our previous example. Check how Step two failed due to a 404 Not Found status. If the **Continue execution after an error** checkbox is unchecked, the monitor fails at a certain point where it encounters an error (Step two). This error blocks the monitor execution, and the remaining steps will not be executed:

![MSA Disabled Error handling](/img/content/scr-disabled-error-handling.min.png)

Alternatively, if you check the **Continue execution after an error** in Step two, the monitor ignores this step and continues checking the remaining steps:

![MSA Enabled Error handling](/img/content/scr-enabled-error-handling.min.png)

## Related articles

To know about Error handling in Transaction monitors, refer to [Using ignore errors for optional steps and actions]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions#how-is-ignore-errors-like-making-a-conditional-statement" lang="en" >}}) knowledge base article.
