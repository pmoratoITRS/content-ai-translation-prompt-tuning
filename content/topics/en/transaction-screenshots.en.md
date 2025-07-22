{
  "hero": {
    "title": "Working with Transaction Screenshots"
  },
  "title": "Working with Transaction Screenshots",
  "url": "/support/kb/synthetic-monitoring/transactions/transaction-screenshots",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-screenshots"
}

{{< callout >}}
**Note:** Transaction Screenshots are available in the **Enterprise version** and **Business version**.
{{< /callout >}}

When monitoring transactions it can be easy to get lost in the details of all of the data that is being communicated across a web page. To help make this task less daunting, we offer screenshots for transactions.

## Why use Transaction Screenshots?

This option is useful when trying to track down a specific error, or if you wish to see what a particular page looked like on a specific time and day. You can decide which steps you’d like a screenshot of, and we will provide the screenshot at the end of that step.

## When does Uptrends generate a Screenshot?

We generate a screenshot in the following occassions:

-   **By default:** when an error occurs during a transaction. You don't have to set anything up, this happens automatically.
-   **Ad-hoc:** When you have activated a Transaction Screenshot in a specific step, after the step completed.

## How do I set it up?

{{< callout >}}
**Just to be sure:** you'll need a transaction to start activating Transaction Screenshots.
{{< /callout >}}

-   Go to {{< AppElement type="menuitem" >}}Monitors{{< /AppElement >}} in the top menu, and select the transaction you would like to activate screenshots for.
-   In the {{< AppElement type="tab" >}}Steps{{< /AppElement >}} tab, select the step you want to activate a screenshot for.
-   Check the checkbox that says **Screenshot**, and we'll generate a screenshot every time the step has been completed.

## Where can I find Transaction Screenshots?

Transaction Screenshots are displayed in the *Monitor Log* (Monitors > Monitor Log). When you click on a specific transaction check, we'll display the steps that are executed. If a step contains a screenshot, you can click the tiny camera icon to reveal it.
