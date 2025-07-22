{
  "hero": {
    "title": "Analyzing Transaction Errors"
  },
  "title": "Analyzing Transaction Errors",
  "url": "/support/kb/synthetic-monitoring/transactions/analyzing-transaction-errors",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/analyzing-transaction-errors"
}

Sometimes things don’t work the way that we’d like or expect them to – and that includes your monitored transactions!

Below you’ll learn about transaction errors and how to analyze them, so you can get everything up and running again.

## Check the HTML output

In the event of a transaction error, the Uptrends service grabs a copy of the HTML output seen when the error was detected. This data can be a powerful tool to learn what a page looked like at the moment a problem occurred.

**To check the HTML output**:

1.  Log into your Uptrends account, and navigate to the {{< AppElement type="menuitem" >}}Probe log{{< /AppElement >}} dashboard, located within the {{< AppElement type="menuitem" >}}Probes{{< /AppElement >}} dropdown menu.
2.  Click on a listed transaction error *(either unconfirmed or confirmed)*. {{< callout >}}**Note**: We cannot deliver the HTML output for transactions with a “Navigate” error, as it means we were unable to reach your website.{{< /callout >}} 
3.  Under {{< AppElement type="menuitem" >}}Page Content{{< /AppElement >}} , and next to the {{< AppElement type="menuitem" >}}HTML Result{{< /AppElement >}} prompt, you can see the HTML output.
4.  To see roughly how the page looked, select the piece of HTML code, and save it (using Notepad, for example) as an HTML file.
5.  Open the file up in a browser to view the page.

## Is the error detected by only one checkpoint?

If an error is only being detected by a single checkpoint, it typically means that there may be a connection issue for users in that region, or a specific technical issue for that checkpoint.

In this situation, we advise that you [file a support ticket](/contact) so that we can help investigate the issue.

## Are your login credentials still valid?

Sometimes the login credentials needed to perform a step of a multi-step transaction can change. If this happens, please [change the transaction's credentials](/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction) using the transaction step editor.
