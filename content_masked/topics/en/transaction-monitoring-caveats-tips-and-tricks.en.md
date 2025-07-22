{
  "hero": {
    "title": "Caveats, tips, and tricks"
  },
  "title": "Caveats, tips, and tricks",
  "summary": "When setting up transaction monitors, you may want to consider a few things.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/transaction-monitoring-caveats-tips-and-tricks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Transaction monitoring (Web Application Monitoring) can save brand reputation and revenue by capturing issues with your transactions before they impact your users. Transaction monitoring is a synthetic monitoring approach where Uptrends' checkpoints follow a script to simulate real user journeys. When setting up user journey tests, it is important to think about the short and long-term ramifications of your testing. You can avoid many problems by carefully mapping out your transaction before recording. Every use case is different, but we found some common problems you may want to think about when setting up your Transaction Monitoring.

## Avoid inventory shortages

Inventory shortages due to testing shopping carts and checkout transactions can cause problems with your inventory. The synthetic testing places orders as frequently as 288 times a day, and if not handled properly, testing can reduce your inventory making the item unavailable to your users. We've actually seen problems where the warehouse processed and readied the orders for shipping.  We’ve seen several different solutions to avoid inventory problems.

**Database solution**

Although we’ve seen some companies choose to delete test purchases and shopping carts from the database manually, a stored procedure or automated process may prove more reliable. Perhaps have your order processing system ignore orders made by the test user or orders placed from Uptrends' [checkpoint IP addresses]([LINK_URL_1]).

**Use test (virtual) items**

You may find it beneficial to create an inventory item that is used strictly for testing purposes. Using a test item keeps your actual inventory accurate and available. Test items may also help you identify test transactions when purging your databases and prevent accidental shipping of actual items.

**Dump the cart**

If testing a shopping cart transaction, build item removal into the transaction steps. Add an item and then remove the item before closing the transaction.

[SHORTCODE_1]
**Note**: Removing items from the cart can help with keeping inventory available for your users. However, when the transaction fails before the script removes the item from the cart, cart items can still accumulate. Monitor the test user's cart frequently to clear items.
[SHORTCODE_2]

**Pick an item with large quantities**

If using a real item, pick an item for testing with such large quantities that an inventory shortage becomes nearly impossible.

## Keep an eye on replenishment systems

Inventory management software often has a process that automatically reorders popular items or items low in inventory. To avoid an overabundance of the item in your inventory, check with system administrators to find out your best course of action such as using a test item or turning off automatic replenishment for the item. 

## Avoid filling up appointments and reservations

If your transaction monitor tests schedulers for things like doctor appointments, hotel rooms, flights, or dinner reservations, you can quickly find all of your time slots full or sold out. Identifying and purging appointments created by testing is crucial.

## Your transaction monitor WILL cause emails to be sent

If part of your transaction includes an email field, and your transaction sends confirmation emails for any reason such as invoices, password resets, or user ID reminders, your transaction monitor will also generate emails. To avoid a mailbox full of unwanted emails, use an email address such as a noreply@mysite.com for your transaction monitor. 

## Unexpected credit card charges

If you use a real credit card when testing the checkout processes, you can accrue charges and merchant fees, get holds placed on the available funds, and trigger fraud alerts due to the frequent transactions. Instead, use test credit card accounts. Most merchant service companies offer test account numbers that allow you to test the checkout transaction without assessing fees or putting holds on a real account.

## New account creation solutions

When testing new account setup, you can only do it once with the same username. The second time the script runs the transaction will error due to the duplicate account. We’ve seen a few solutions for testing account setup.

### Don't commit the data

Although this option doesn’t provide a complete test of the entire account setup, some Uptrends users have chosen to stop short of the final commit. The monitor tests every aspect of the account creation process except the final submit.

### Database solutions

You may want to consider using a database trigger to check for the test account id after a CREATE event that purges the test account from the database before the next test begins.

### Generate new unique logins

You can also generate new unique logins by using things like the time date stamp. Just remember to purge them on a regular basis. [Check with support]([LINK_URL_2]) to learn more.

## Account already logged in

If using the same login credentials for multiple monitors or you fail to log out after a test, you may generate errors. Best practice is to set up a different test user account for each monitor, and always log out as the final step in the test process to avoid unnecessary alerts.

## Protecting sensitive information

If a user needs to log in to perform a task, the monitor needs to log in too. Consider the authentication process and protecting logins and passwords. You can protect your authentication information in our [vault]([LINK_URL_3]), and hide them in your test results. 

Also, consider the permissions you grant the test user from a security standpoint, and keep an eye on the user to make sure there is no suspicious activity.  

## Use content checks

[Content checks]([LINK_URL_4]) are free, and you can add one to each step in your transaction. Content checks are a great way to make certain the page loaded completely and that the browser received the correct content. You can add content checks in three different ways, either via the *Add content check* button or via the context menu. You can also add content checks later on using the monitor step editor in your account. Check the [shopping cart step-by-step tutorial]([LINK_URL_5]) to know how to use content checks in actual scenarios.

## Use keyboard actions
The transaction recorder allows you to also capture keyboard actions from the user. You can choose from a variety of characters ranging from Control keys, Special keys, Digit keys, Numpad keys, Uppercase and Lowercase keys. Choose whether this key should be pressed globally or just on the currently focused element or last clicked element. 

This is useful when you encounter websites with *Press any type of key to continue* or *Press enter to confirm* instructions. Keep in mind that compared to mouse click activities (which automatically records a move), you need to manually add a keyboard action to record any keyboard event and count it as an actual activity. Check the [shopping cart step-by-step tutorial]([LINK_URL_6]) to know more about keyboard actions.

## Use hover and wait for an element to be visible actions

You can also record mouse hover actions and verify if an element is visible when you right click an element in the page and choose appropriate option in the *ITRS Uptrends Transaction Recorder* context menu. This is helpful when you wanted to verify if an element have certain hover triggers like displaying a message,  or making an element or sub menus visible later on. Check the [shopping cart step-by-step tutorial]([LINK_URL_7]) for actual examples.

[SHORTCODE_3]
**Note:** Every use case is different, so don't hesitate to reach out to our scriptwriters to help you find solutions that fit your unique situations. Either use the [ticket system]([LINK_URL_8])  or include a note on your transaction recording submission to let the writers know about any concerns.
[SHORTCODE_4]
