{
  "hero": {
    "title": "Understanding transaction monitor credit calculations"
  },
  "title": "Understanding transaction monitor credit calculations",
  "summary": "Learn how we determine the number of transaction credits set for your transaction.",
  "url": "/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/Understanding-transaction-monitor-count-calculations"
}

If you're wondering how Uptrends determines the cost of a particular transaction monitor, you're in the right place. Before we get into the credit calculation, let's review some terms frequently used when discussing transaction monitors.

**Transaction**: A transaction is a user’s journey to complete a task on your website. Transactions include tasks like logging in, making a purchase, submitting a form, requesting a document, setting up an account, requesting a password reset, and more. A single transaction consists of two or more steps.

**Transaction credit**: Think of a transaction credit like cash. You have an allotted number of transaction credits based on your plan (You can always buy more.). A transaction monitor carries a "costs" of a certain number of credits based on multiple factors that we discuss in a moment. While your monitor is in development mode, no credits are used or needed. You use the credits by putting the monitor in staging or production mode (Learn more about [monitor modes](/support/kb/synthetic-monitoring/monitor-settings/monitor-mode).). You can find the number of credits available to you in your account settings.

**User actions**: A user action is a user's interaction with the page. Examples of user actions include clicks, text input, hover actions, and content checks.  

**Step**: A step is an arbitrary grouping of user actions. You can group your actions into steps that make the most sense to you and help you with troubleshooting and reporting. Uptrends reports durations on a step-by-step basis (something to consider when setting up your steps). Our recommendation is to end each step with an action that prompts the next page to load, and a content check.

## How does Uptrends determine the number of credits a transaction monitor uses?

We determine how many transaction credits a transaction uses based on a couple of different factors:

**The number of user actions resulting in a server request**. Each user action (see the definition above) in a transaction monitor that results in a server request uses one transaction credit. Navigation actions, file uploads and clicks that load new pages in the browser use a credit. Text input, hover actions and content checks are free.  
  
**Transaction waterfalls, filmstrips and screenshots**: Each transaction waterfall or screenshot used in your transaction uses a transaction credit. Filmstrips are priced at one transaction credit, except when there is already one screenshot in the step, in which case the filmstrip is provided free of charge. Two screenshots and one filmstrip will cost two transaction credits.

## The transaction monitor calculation

If you want a formula for calculating the number of credits required for a single transaction, try this:

**Number of actions with server requests** \+ **number of waterfall charts** \+ **number of screenshots** = **total number of transaction credits used**

**Note**: When you add a new monitor or modify a monitor, the monitor count in your Monitor list will show the number followed by the word "calculating" or "calculated". The system needs a few moments to analyze your transaction steps to determine the right cost. In specific cases, our support team reviews the changed or new monitor to ensure that the number of monitor credits applied to the monitor remains accurate.

## Conclusion

If you find yourself scratching your head wondering how we made the transaction credit use calculation, [contact support](/contact). Our support team reviews the transaction with you to clear up any confusion.
