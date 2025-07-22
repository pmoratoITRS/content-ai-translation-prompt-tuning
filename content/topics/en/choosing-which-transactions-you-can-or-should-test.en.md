{
  "hero": {
    "title": "Choosing which transactions you can or should test"
  },
  "title": "Choosing which transactions you can or should test",
  "url": "/support/kb/synthetic-monitoring/transactions/choosing-which-transactions-you-can-or-should-test",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/choosing-which-transactions-you-can-or-should-test"
}

Determining which transactions you need to test with Web Application Monitoring is an important first step when it comes to setting up a successful transaction monitoring strategy.

## What transactions can I monitor?

A better question to ask is, "What kind of transactions CAN'T I monitor with Web Application Monitoring." Using Web Application Monitoring, you can test almost any task a user may need to perform on your website or service. That leaves you with a lot of monitoring options. Some common transactions you may want to verify with Web Application Monitoring include

-   Log in and log off function,
-   Search functions,
-   Scheduling or making a reservation,
-   Shopping cart transactions: adding, removing, and selecting product options,
-   Form completion and submission especially those that connect with other services such as address verification or shipping calculators, and
-   Financial transactions

## How to pick the best transactions to monitor

Your site is probably loaded with possible user scenarios. But you can't test every scenario, so how do you choose? Well, of course, **you want to test the transactions that are critical to the success of your site and that your users rely on** (you can find many of them mentioned above). You will want to [map out your user scenarios]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="en" >}})  and break them down to specific tasks such as logging in or adding an item to a shopping cart. You'll want to create monitors that touch on distinct parts of your system.  Setting up separate monitors to check each aspect of a user scenario makes for better reporting and alerting. For example, to test a shopping cart, navigate to the page, add an item to the shopping cart, verify the cart, and exit the transaction. With this monitor, you test page availability, the databases associated with product and user data, and transaction speed. You'll want to test transactions that

-   Access servers to check on the site availability, accuracy of response, and response times.
-   Require database access and responses. If your system uses more than one database, set up monitors to hit them all.
-   Use external service availability and function. For example, if your transaction uses third-party services such as location and address verification services, you may want to verify them all.

**Note**: The transactions you choose to monitor may have unexpected side effects. Be sure to read our [Transaction monitoring caveats, tips, and tricks]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks" lang="en" >}})  article before moving any monitor into production or staging mode.

## A note about choosing testing locations

As you probably know, user location can have a huge impact on transaction performance and success. Carefully consider your checkpoint location choices. We do not recommend choosing the entire set of available checkpoints for a single monitor. Making broad choices can make identifying performance issues and errors affecting a specific area more difficult to catch. Here's why.

1.  When you have chosen a large testing area, one failing check at a single checkpoint may not make it to the alert stage. After a checkpoint detects an error condition, Uptrends chooses another random checkpoint from your designated test locations to verify the error. Because the verifying check may come from an entirely different region, Uptrends can't verify the error, so an alert doesn't go out. Therefore, a location-based error condition can persist until you recognize a pattern in your monitor logs, or the verifying check occurs in the same region experiencing the problem.

    **Note**: Choosing too few checkpoints can also reduce the effectiveness of your monitoring. You need to choose a minimum of three checkpoints for any monitor, but we recommend more. Consider each transaction carefully when making your checkpoint choices.

2.  Performance is very much a product of the user's location due to network latency and quality. Some locations may experience slow response times that go unnoticed because they barely exceed the minimum response time, or the poor response time goes unverified meaning an alert doesn't go out. The infrequency of the checks means that the slow response times do not have enough impact on performance reports for you to notice easily.

**Solution**: Duplicate your monitor. Set the copies to check specific regions. You'll get reports that more closely represent your user's experience within the region. With the smaller number of checkpoints, Uptrends can capture and let you know about localized issues that may go unnoticed using a broader checkpoint area.
