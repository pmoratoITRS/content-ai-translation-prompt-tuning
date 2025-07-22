{
  "hero": {
    "title": "Options for transaction scripts"
  },
  "title": "Options for with transaction scripts",
  "summary": "You have several options when it comes to generating the final script for your transactions from full service to self service and using scripting directly.",
  "url": "/support/kb/synthetic-monitoring/transactions/self-or-full-service",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/self-or-full-service"
}

A transaction monitor needs a script to replicate the steps you want to monitor. Depending on your comfort level with scripting, there are some options on how to deal with the transaction script.

- **If you need a lot of help**, Uptrends Support can handle the scripting and testing for you with [full-service transactions](#full-service).
-   **If you're fairly comfortable with web technologies** like HTML, CSS, JSON, and XPath, the [self-service transactions](#self-service) are right for you.
-   **If you're a power user**, you can jump right from the visual to the script editor and cut and paste from your own scripting tool and source control tools, build a [script from scratch](#script-from-scratch). You can also manage your transactions and scripts with the Uptrends' [API]({{< ref path="support/kb/api" lang="en" >}}).

Before scripting your transactions, you may want to decide which method will work best for you. Just remember, [Support]({{< ref path="contact" lang="en" >}}) is always ready to help you along when and if you need it.

## Full-service transactions {id="full-service"}

You record your transactions, upload them choosing "full-service", and Uptrends' scripting pros use your recording to edit and test your scripts. The entire full-service process takes about a week from the time you submit your recording until you receive a completed monitor in your account and the [script review policy]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="en" >}}) applies.

### Who should use full-service transactions?

Anyone can and may choose the full-service option, and Support is glad to help you get your monitors up and running. You may choose full-service transactions if:

-   You're not comfortable working with scripting technologies like HTML, CSS, JSON, and XPath.
-   You simply don't have the time or resources to dedicate to the task.
-   You just don't want to do it.

### Which steps are involved?

If you choose to use full-service transactions, you need to:

1.  Practice your transactions for a cleaner recording.
2.  [Record the transaction]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}})
3.  Upload your recordings for further scripting. After stopping the recording, you will have the option to choose "full-service transactions" to submit the recording to Support.

The upload process generates a read-only monitor in your account while the monitor goes through the full-service process. Once scripted and tested, Uptrends' scripting pros notify you that the monitor is ready and unlocked for you in your account. Please review our [scripting review policy]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="en" >}}) for information about full-service transaction script completion times and limitations on the number of recordings you can have submitted at any one time.

{{< callout >}}
**Note**: If you need a little extra help understanding web application monitoring or you need a systematic approach to understanding your transactions, we've got a couple additional articles you may want to review: [Understanding web application monitoring]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="en" >}}) and [Understanding your transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="en" >}}).
{{< /callout >}}

## Self-service transactions {id="self-service"}

With self-service transactions, you have complete control of your transaction scripting. You have these options available for achieving your scripting goals:

- Use the [transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}}) to do the bulk of the work for you, and then refine and test the script using the [step editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}).
- Skip the transaction recorder and use the [step editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}) directly to create your scripts from scratch in the visual step editor.

It is recommended that you start with the recorder, as it makes life a whole lot easier.

### Who should use self-service transactions?

We encourage everyone to use or try self-service transactions. It doesn't cost anything to edit and test scripts in development mode. You may even find editing and testing your transaction scripts fun. [Support]({{< ref path="contact" lang="en" >}}) is always there to help you along or take over if you would like. You may want to try self-service transactions if:

- You're comfortable with basic web technology, and you can typically figure things out.
- You're well versed in the client-side technologies like HTML, CSS, XPath, and JSON.

### Which steps are involved?

1. [Use the transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}}) for a quick start.
2.  Open up your new monitor in your Uptrends account and [edit and test]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}) away.

## Scripting from scratch {id="scripting-from-scratch"}

There is a third option for the power user. If you choose this one, you can skip the transaction recorder and the step editor and enter your script directly in your monitor settings by using the script text editor. Just click the {{< AppElement type="button" >}}Switch to script{{< /AppElement >}} button at the top of the {{< AppElement type="tab" >}}Steps{{< /AppElement >}} tab of your monitor and edit or paste your script.

You can also use the [API]({{< ref path="support/kb/api" lang="en" >}}) to create new transaction monitors, edit, and test your monitors. 
