{
  "hero": {
    "title": "Understanding your transactions"
  },
  "title": "Understanding your transactions",
  "summary": "Understanding your transactions, the many paths they may take, and being aware of the transaction monitoring caveats, leads to better monitoring and results. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/understanding-your-transactions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Before you can jump into recording or scripting your transactions, you need to have a plan and a good understanding of your transactions. Having a good plan before you start recording your transactions can help you with the recording and testing process and help you avoid other problems later.

## Know your transactions and map them

Not all transactions are built the same. A good way to get a deeper understanding of your transactions is to map them out. To get started

- List the key tasks your users need to do on your website or app.
- Generate flow charts of the key tasks. Think about the different paths the user may take to achieve different goals on your site (there may be multiple paths to the same goal).
- Make sure you’re mapping out both your happy paths (the all-goes-as-planned path) and the unhappy paths (user errors and system failures). Examples of unhappy paths include difficulties such as failed user authentication, out of stock inventory, invalid credit card information, failing supporting systems like merchant services, or database errors. You may want to test these common problems to ensure your system responds appropriately.

Below, you find the key functions and user journeys for a simple e-commerce site. The diagram describes several happy paths a user may take. Some tasks depend on the successful completion of other tasks, and you could break down some tasks further.

![]([LINK_URL_1])

To simplify things moving forward, let's consider the shopping cart functionality only. The shopping cart functionality is the simple task of selecting an item, adding it to the cart, and editing the cart.

The temptation is to expand the shopping cart functionality to include testing for the search or the checkout process. It is recommended to keep the functionality compartmentalized so that you’re testing one key task at a time.

![]([LINK_URL_2])

## Other things that you need to consider

Before you start recording your transactions, you need to consider several things:

-   Please review the article on [Choosing which transactions you can or should test]([LINK_URL_3]) to help you learn more about the types of transactions you can and should monitor with transaction monitoring. The article also includes a note about selecting the checkpoints for monitoring your transactions.
-   Transaction monitoring can have real-world consequences for a business from consuming item inventory to racking up merchant fees. Please read through the [Transaction monitoring caveats, tips, and tricks]([LINK_URL_4]) article before you put any transaction monitor into [staging or production mode]([LINK_URL_5]).

If all of this seems overwhelming to you, don't worry, the [Support team]([LINK_URL_6]) is ready to help you get over any hurdles you may experience.
