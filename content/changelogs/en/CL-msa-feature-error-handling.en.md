{
  "title": "New MSA feature: Error handling",
  "date": "2024-12-18",
  "url": "/changelog/december-2024-msa-error-handling-feature",
  "translationKey": "https://www.uptrends.com/changelog/december-2024-msa-error-handling-feature"
}

We've added a new `Error handling` section in the MSA Visual step editor UI. This feature gives you more flexibility in handling MSA step errors, allowing better control and adaptability to dynamic web server behaviors.

![MSA Error handling checkbox](/img/content/scr-error-handling-checkbox.min.png)

Selecting the **Continue execution after an error** checkbox enables you to ignore errors that occurred in an MSA monitor step. This means that if a certain step encounters any errors (such as a bad request, request timeout, or failed assertion), the monitor will continue checking the remaining steps. Such errors will only be visible in the **Step results** and displayed as `An error occurred during this step`. These will not be reflected in any of your **Errors overview** dashboards or reports.  

This error-handling behavior is similar to that of the Transaction monitors. For more information, refer to the [Using ignore errors for optional steps and actions]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions#how-is-ignore-errors-like-making-a-conditional-statement" lang="en" >}}) knowledge base article.

