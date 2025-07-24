{
  "title": "New MSA feature: Error handling",
  "date": "2024-12-18",
  "url": "[URL_BASE_CHANGELOG]december-2024-msa-error-handling-feature",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

We've added a new [INLINE_CODE_1] section in the MSA Visual step editor UI. This feature gives you more flexibility in handling MSA step errors, allowing better control and adaptability to dynamic web server behaviors.

![MSA Error handling checkbox]([LINK_URL_1])

Selecting the **Continue execution after an error** checkbox enables you to ignore errors that occurred in an MSA monitor step. This means that if a certain step encounters any errors (such as a bad request, request timeout, or failed assertion), the monitor will continue checking the remaining steps. Such errors will only be visible in the **Step results** and displayed as [INLINE_CODE_2]. These will not be reflected in any of your **Errors overview** dashboards or reports.  

This error-handling behavior is similar to that of the Transaction monitors. For more information, refer to the [Using ignore errors for optional steps and actions]([LINK_URL_2]) knowledge base article.

