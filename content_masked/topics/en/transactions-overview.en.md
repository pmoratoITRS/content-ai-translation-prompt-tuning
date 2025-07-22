{
  "hero": {
    "title": "Transaction monitoring overview"
  },
  "title": "Transaction monitoring overview",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/transactions-overview",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Transaction monitoring, also known as web application monitoring, is used to check the correct functioning of user interactions on your website. The interaction could be a simple login or all the actions that are needed to purchase a product in your webshop.

In order to monitor these user interactions you need to put them in a script that can be run again and again to check if everything still works as expected. Uptrends offers the transaction recorder (as a Chrome extension) to build a script in an easy way. Once you have recorded the script you can refine it yourself (self-service transactions) or ask Uptrends support to tune the script (full-service transactions). If you're good at scripting, you can decide to skip the recording and put your own script into a transaction monitor right away.

When you upload a transaction recording to your Uptrends account, a transaction monitor will be created with some basic information. You will have to adjust some settings to fit your needs.

Once you've tested your transaction monitor and are happy with the way it works, proceed and set up [alerting]([LINK_URL_1]) for it. After all, this is what it is about - to be alerted when things are not working as expected.

[SHORTCODE_1]
We have a step-by-step tutorial [User journey in a shop]([LINK_URL_2]) to take you through the basics and all the way to transaction monitoring and checking monitoring data.
[SHORTCODE_2]

## 1. Introduction

If you are new to web application/transaction monitoring, you will find some background knowledge in the following articles:

- Get an introduction in [What is web application monitoring?]([LINK_URL_3])
- Learn [Why you should use web application monitoring]([LINK_URL_4])
- Check if web application monitoring is [the right solution]([LINK_URL_5]) for you

## 2. Planning your transaction monitoring

Understanding the mechanics of your transactions, the functionality you need to test, and the impact of your monitoring on your systems is a crucial part of planning your transactions. You also may have to involve other teams at your company to set up transaction monitoring.

- [Map out possible transaction paths]([LINK_URL_6])
- Decide [what to test]([LINK_URL_7])
- [Caveats, tips and tricks]([LINK_URL_8]): things to consider and watch out for when setting up your monitoring
- [Reasons why you may need help]([LINK_URL_9]) from other teams at your company

## 3. Recording your transactions

Using the [transaction recorder]([LINK_URL_10]) properly leads to cleaner recordings and faster monitor setup time.

- [Download and use the transaction recorder]([LINK_URL_11])
- Follow the [shopping cart step-by-step tutorial]([LINK_URL_12]) to learn how to use the transaction recorder
- Choose between [full-service and self-service transactions]([LINK_URL_13])

## 4. Editing and testing your transaction script

Once you've recorded your transaction, and you've chosen to test the script yourself (you can also let our Support team handle your testing) you need to troubleshoot the resulting script, setup content checks if you haven't already, and adjust the vault permissions on newly created items. Finally, you need to keep an eye on the monitor in staging mode before moving your monitor to production.

- To learn about the editor, steps and actions check out [Understanding the step editor]([LINK_URL_14])

- Actions are at the core of transactions. Learn more about them:
   - [Page interactions - navigate, click, set, etc.]([LINK_URL_15])
   - [Test actions - content checks and wait]([LINK_URL_16])
   - [Control actions - switching (inline) frames or tabs]([LINK_URL_17])
   - [Control actions - adjust variable content]([LINK_URL_18])
   - [Ignore errors for optional steps and actions]([LINK_URL_19])
   - [Using selectors]([LINK_URL_20]) and [selector alternatives]([LINK_URL_21])
   - [Transaction variables]([LINK_URL_22]) and [adjusting variable content]([LINK_URL_23])

- In the exercise [Testing and editing your script]([LINK_URL_24]), find out about the *Test now* functionality, how to handle dynamic IDs and timeout errors. It also contains a [Testing checklist]([LINK_URL_25]).

- A few other things you may have to deal with, depending on your setup and transactions:
  - [Manage sensitive values]([LINK_URL_26]) that were automatically added to the vault during recording
  - [Manage vault authorizations (automatically created sections)]([LINK_URL_27])
  - Transaction monitoring for [mobile setup]([LINK_URL_28])
  - Working with a [shadow DOM]([LINK_URL_29]) in your transaction
  - Working with [SMS-based 2FA]([LINK_URL_30]) or [one-time password-based 2FA]([LINK_URL_31]) in your transaction

  - Adding [metrics]([LINK_URL_32]) such as [Core Web Vitals]([LINK_URL_33]) and [W3C navigation timings]([LINK_URL_34]) to your transaction results.

  - Bypass or override the default DNS system by using a [DNS bypass]([LINK_URL_35]) in your transaction.

## 5. Results of transaction monitoring

Once your transactions are monitored, you'll receive feedback. There are a number of sources you can look into to find out what is going wrong, when things go wrong.

- [Screenshots]([LINK_URL_36])

- [Waterfalls]([LINK_URL_37])

- [W3C navigation timings]([LINK_URL_38])

- [Core Web Vitals]([LINK_URL_39])

- [Analyzing errors]([LINK_URL_40])

## 6. Troubleshooting

When the transaction monitoring does not work out as expected, here are a few things to check:

- [Exclude A/B tests]([LINK_URL_41])

- [Use incognito mode]([LINK_URL_42])

- [Caveats, tips and tricks]([LINK_URL_43])

## Credits

Transaction monitors use Transaction credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]([LINK_URL_44]) knowledge base article.
