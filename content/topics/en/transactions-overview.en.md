{
  "hero": {
    "title": "Transaction monitoring overview"
  },
  "title": "Transaction monitoring overview",
  "url": "/support/kb/synthetic-monitoring/transactions/transactions-overview",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transactions-overview",
  "sectionlist": false
}

Transaction monitoring, also known as web application monitoring, is used to check the correct functioning of user interactions on your website. The interaction could be a simple login or all the actions that are needed to purchase a product in your webshop.

In order to monitor these user interactions you need to put them in a script that can be run again and again to check if everything still works as expected. Uptrends offers the transaction recorder (as a Chrome extension) to build a script in an easy way. Once you have recorded the script you can refine it yourself (self-service transactions) or ask Uptrends support to tune the script (full-service transactions). If you're good at scripting, you can decide to skip the recording and put your own script into a transaction monitor right away.

When you upload a transaction recording to your Uptrends account, a transaction monitor will be created with some basic information. You will have to adjust some settings to fit your needs.

Once you've tested your transaction monitor and are happy with the way it works, proceed and set up [alerting]({{< ref path="support/kb/alerting" lang="en" >}}) for it. After all, this is what it is about - to be alerted when things are not working as expected.

{{< callout >}}
We have a step-by-step tutorial [User journey in a shop]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop" lang="en" >}}) to take you through the basics and all the way to transaction monitoring and checking monitoring data.
{{< /callout >}}

## 1. Introduction

If you are new to web application/transaction monitoring, you will find some background knowledge in the following articles:

- Get an introduction in [What is web application monitoring?]({{< ref path="what-is/web-application-monitoring" lang="en" >}})
- Learn [Why you should use web application monitoring]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#why-monitor-your-web-applications" lang="en" >}})
- Check if web application monitoring is [the right solution]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#transaction-best-choice" lang="en" >}}) for you

## 2. Planning your transaction monitoring

Understanding the mechanics of your transactions, the functionality you need to test, and the impact of your monitoring on your systems is a crucial part of planning your transactions. You also may have to involve other teams at your company to set up transaction monitoring.

- [Map out possible transaction paths]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="en" >}})
- Decide [what to test]({{< ref path="support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test" lang="en" >}})
- [Caveats, tips and tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="en" >}}): things to consider and watch out for when setting up your monitoring
- [Reasons why you may need help]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#programming-skills" lang="en" >}}) from other teams at your company

## 3. Recording your transactions

Using the [transaction recorder]({{< ref path="features/transaction-recorder" lang="en" >}}) properly leads to cleaner recordings and faster monitor setup time.

- [Download and use the transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}})
- Follow the [shopping cart step-by-step tutorial]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="en" >}}) to learn how to use the transaction recorder
- Choose between [full-service and self-service transactions]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="en" >}})

## 4. Editing and testing your transaction script

Once you've recorded your transaction, and you've chosen to test the script yourself (you can also let our Support team handle your testing) you need to troubleshoot the resulting script, setup content checks if you haven't already, and adjust the vault permissions on newly created items. Finally, you need to keep an eye on the monitor in staging mode before moving your monitor to production.

- To learn about the editor, steps and actions check out [Understanding the step editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}})

- Actions are at the core of transactions. Learn more about them:
   - [Page interactions - navigate, click, set, etc.]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions" lang="en" >}})
   - [Test actions - content checks and wait]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="en" >}})
   - [Control actions - switching (inline) frames or tabs]({{< ref path="support/kb/synthetic-monitoring/transactions/Switching-between-iframes-browser-tabs" lang="en" >}})
   - [Control actions - adjust variable content]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="en" >}})
   - [Ignore errors for optional steps and actions]({{< ref path="support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions" lang="en" >}})
   - [Using selectors]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="en" >}}) and [selector alternatives]({{< ref path="support/kb/synthetic-monitoring/transactions/selector-alternatives" lang="en" >}})
   - [Transaction variables]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="en" >}}) and [adjusting variable content]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="en" >}})

- In the exercise [Testing and editing your script]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="en" >}}), find out about the *Test now* functionality, how to handle dynamic IDs and timeout errors. It also contains a [Testing checklist]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction#script-testing-checklist" lang="en" >}}).

- A few other things you may have to deal with, depending on your setup and transactions:
  - [Manage sensitive values]({{< ref path="support/kb/synthetic-monitoring/transactions/using-sensitive-transaction-data-stored-in-the-vault" lang="en" >}}) that were automatically added to the vault during recording
  - [Manage vault authorizations (automatically created sections)]({{< ref path="support/kb/synthetic-monitoring/transactions/managing-authorizations-for-automatically-created-vault-sections" lang="en" >}})
  - Transaction monitoring for [mobile setup]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-for-mobile-setup" lang="en" >}})
  - Working with a [shadow DOM]({{< ref path="support/kb/synthetic-monitoring/transactions/shadow-dom" lang="en" >}}) in your transaction
  - Working with [SMS-based 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/sms-based-2fa" lang="en" >}}) or [one-time password-based 2FA]({{< ref path="support/kb/synthetic-monitoring/transactions/otp-based-2fa" lang="en" >}}) in your transaction

  - Adding [metrics]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="en" >}}) such as [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}) and [W3C navigation timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}}) to your transaction results.

  - Bypass or override the default DNS system by using a [DNS bypass]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/dns-bypass" lang="en" >}}) in your transaction.

## 5. Results of transaction monitoring

Once your transactions are monitored, you'll receive feedback. There are a number of sources you can look into to find out what is going wrong, when things go wrong.

- [Screenshots]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-screenshots" lang="en" >}})

- [Waterfalls]({{< ref path="support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="en" >}})

- [W3C navigation timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}})

- [Core Web Vitals]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}})

- [Analyzing errors]({{< ref path="support/kb/synthetic-monitoring/transactions/analyzing-transaction-errors" lang="en" >}})

## 6. Troubleshooting

When the transaction monitoring does not work out as expected, here are a few things to check:

- [Exclude A/B tests]({{< ref path="support/kb/synthetic-monitoring/transactions/exclude-a-b-tests-from-transaction-requests" lang="en" >}})

- [Use incognito mode]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-incognito-mode" lang="en" >}})

- [Caveats, tips and tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="en" >}})

## Credits

Transaction monitors use Transaction credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="en" >}}) knowledge base article.
