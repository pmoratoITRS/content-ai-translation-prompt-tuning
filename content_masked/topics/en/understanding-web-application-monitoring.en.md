{
  "hero": {
    "title": "Understanding transaction monitoring"
  },
  "title": "Understanding transaction monitoring",
  "summary": "In this article you will learn what transaction monitoring (also known as web application monitoring) is, how it works, and what types of transactions you can monitor. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/understanding-web-application-monitoring",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

What is transaction monitoring, also known as web application monitoring? There is a detailed description in [Web application monitoring]([LINK_URL_1]) for you to peruse. However, in a nutshell:

*Web Application Monitoring is a synthetic monitor or bot that performs user actions on a website or web application at regularly scheduled intervals. The monitor uses a web browser (just like your users do) to verify that the site or application works properly and performs well.*

So, pretty much, any transaction a user can make on your site using a browser, a transaction monitor can do the same thing at regular intervals. Transaction monitoring checks your site around the clock seven days a week. On the chance that the transaction errors or takes too long, Uptrends' alerting system gives you a heads up.

## Why monitor your web applications? [ANCHOR_1]

Why would you want to monitor transactions, after all, you will notice if things go wrong. Sure, you will notice, eventually, but what damage is done to user confidence and reputation in the meantime?

### The high cost of slow and failing web applications

If your website or service fails to operate properly, your users just switch to your competitors.  Not only do they switch to a competitor, a lot of them never come back.

Failing web applications cost you more in future revenue than they do in immediate revenue. After all, how confident would you be to give your personal information to a brand when their application is glitchy and slow?

By watching your transactions with transaction monitoring, you immediately know when there is a problem. You can jump in and fix it before it affects your users.

### More can go wrong than you think

Some companies check their transactions sporadically throughout the workday, but what happens after your staff goes home at night? Sure, your peak hours may be over, but shouldn't your application work during non-peak hours? Your workday ends, but your site is working 24 hours a day. Many different things may go wrong that you may not notice if you're not monitoring 24/7. Checking your transactions 24 hours a day may alert you to several problems, like:

- Slow loading pages and transactions due to early morning inventory updates or other backend processes. Processes that happen when you hope your users won't notice (but they do).
- External dependencies that don't work correctly:
  -   **Business owners**: Product inventory updates, price calculations, and ordering systems.
  -   **System integrations**: Third-party payment providers, location services, SharePoint/Office365 integrations, and external calculation modules.
  -   **E-commerce and web analytics**: User behavior trackers, Google Analytics, and advertisement systems.

    Although these third-party dependencies seem like add-ons, downtime, slow performance, or bad behavior of external systems can affect your overall performance and even break the display and behaviors of your pages.

## What kind of transactions can I monitor?

A better question is, “What kind of transactions can't I monitor with transaction monitoring.” Here are a few examples of transactions you may want to consider monitoring for performance and function.

- Successful logins
- Using your site's search functionality
- Using the calendar in a reservation system
- Shopping cart functions: adding, removing, and selecting product options
- Completing forms such as order forms with connections to other services such as address verification and shipping cost calculations.
- Successful financial transactions: connecting to merchant services, validating user input, and receiving valid server responses.

## How to pick the transactions you need to monitor?

Your site is probably loaded with possible user scenarios. You can't test every scenario, so how do you choose? Of course, you want to test the transactions that are critical to the success of your site and that your users rely on (many of them are mentioned above). Also, pick transactions that require a lot of different systems and services to come together to function and perform properly. Pick transactions that hit many parts of your systems to verify:

- Supporting-server availability and response times
- Database access and responses: if more than one, choose transactions that hit them all. This may be your user database, product database, order procurement, user data, or any other database on which your system relies.
- External services availability and function: For example, location and address verification, zip code lookup, inventory management systems, logistics, merchant services, or customer relationship management systems.

## What data do I use for testing?

When choosing which data to use for testing, you may want to use test data. For example, In the case of an e-commerce site, you may want to use product IDs that are not tied to real products in the inventory to avoid unwanted consequences. We have an entire page about the pitfalls you need to avoid when monitoring your sites and services. Some of those problems are a direct result of the data you choose for testing. Be sure to read the [Caveats, tips, and tricks]([LINK_URL_2]) page for more information about possible problems and their solutions, but here are a few data-specific issues that you need to consider.

### E-commerce
When choosing products for your testing, remember that if your inventory runs out, your monitor will fail.

- Your monitor may generate orders that consume your available inventory. These orders originating from your testing may prevent users from buying product because of lack of availability.
- Orders generated due to testing may cause auto-replenishment systems to order more product.
- Generate pick-tickets and shipping labels that result in the shipping department to package and even ship test items.
- Purchase confirmation emails may go out filling up someone's inbox, if not your own.
- Testing payment systems may consume available balances and generate real merchant services fees.

### Reservation systems
Reservation systems and similar solutions have their own challenges.

- Your monitor can fill up your available reservation slots blocking real users from scheduling.
- Email confirmations fill up inboxes.
- Paid reservations may generate credit-card charges and service fees.

### Login credentials

You want to keep login information secure and not have duplicates because of automatically generated login credentials. Keep these recommendations in mind:

- Choose login credentials carefully.
- Restrict the test user's [permissions]([LINK_URL_3]), and monitor the account closely for any unusual activity.
- Protect credentials in the Uptrends [vault]([LINK_URL_4]).
- Log the user out at the end of the transaction to prevent login conflicts when the same user attempts to login on the next test.

### Analytics and Real User Monitoring

Your monitoring does affect your analytics and Real User Monitoring data. However, this can be fixed by using [URL and analytics blocking]([LINK_URL_5]).

## Is a transaction monitor always the best choice? [ANCHOR_2]

A transaction monitor is great for making sure everything is working together to create the outcome you expect. However, other monitor types may give you more information about your website's or service's overall performances and availabilities.

### Website availability

Transaction monitors check your site only on five-minute increments or more, so you can accumulate a lot of downtime between transaction checks. With availability monitors, you can check availability on webpages or web services at much shorter intervals. Also, you have options for [advanced availability monitors]([LINK_URL_6]) for databases, email servers, FTP/SFTP servers, SSL certificates, and DNS responses.

### Website performance

Transaction monitoring captures page load times, and if you choose to, you can add waterfall reports to get some additional load time data. However, performance monitoring, as it pertains to your transactions, is more about the responsiveness of your servers to your user interactions such as submits. [Web performance monitoring]([LINK_URL_7]) gives you more detailed data about a page's performance from the initial request to the completed page load. A monitor of the type [Full Page Check]([LINK_URL_8]) gives you detailed information about a single page's load time. You can see the page load progression and performance for the entire page and each element. Not only do you get more detail on each check, but Uptrends also optimized your performance dashboards for displaying the load-time data for a single page for fast comparison. 

### API monitoring

Your transaction most likely has several API calls. Where some calls are single, others may take several requests to complete a full transaction. Checking the APIs separately from your transactions with [API Monitoring]([LINK_URL_9]) can reveal API issues sooner and get you more data for root-cause analysis when your transaction errors.

To monitor the availability of your web services, use the  Webservice HTTP or Webservice HTTPS monitor type which can check the API availability every minute of every day. You can track any service level agreements associated with the API and respond to availability problems faster than with transaction monitoring.

The monitor for a sequence of steps is defined using a [Multi-step API monitor (MSA monitor)]([LINK_URL_10]). This monitor verifies responses and performance for entire API interactions (whether it takes one response or several). You get detailed information about the API responses with validation. 

Web application monitoring focuses on the complete interaction between a user and an application where Multi-step API focuses on any API interaction beyond a web application. For example, you may want to use a Multi-step API monitor to test the communication between a security system and the service provider, or to monitor transactions with your credit card processing provider.

## Do I have to be a developer to set up transaction monitors?[ANCHOR_3]

It certainly helps, but your skills and knowledge about your apps and services can take you a long way even if you're not a developer. Check out the article [Options for transaction scripts]([LINK_URL_11]) to learn more about self-service, full-service or scripting transactions. Your developers or DevOps team may need to:

- Replicate and adapt scripts for mirror sites in multiple languages or similar workflows and functionality.
- Adapting scripts for upcoming site updates for deployment simultaneously with your site update schedule triggered by your continuous integration/continuous deployment (CI/CD) system.
- Utilize the Uptrends API to leverage your monitoring setup as a valuable asset to your quality assurance system.
