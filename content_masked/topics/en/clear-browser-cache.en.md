{
  "hero": {
    "title": "Clear browser cache"
  },
  "title": "Clear browser cache",
  "summary": "When your transaction needs to reload page elements directly from the server instead of the stored cache, clearing the browser cache helps.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/clear-browser-cache",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends [transaction monitors]([LINK_URL_1]) always open a browser to simulate user activities to check your website performance. The browser starts without any cached data. As it performs user activities (such as logging in, scrolling through products, and adding to cart) on your website, it temporarily stores cache to recognize all your website resources. This speeds up the browser's loading process the next time it visits the same page.

There are cases where you want to monitor different page behaviors when visiting a page. If you want to compare the behavior of your e-commerce site when loading items in the shopping cart for existing users (with cached data) compared to new visitors (without cached data), we recommend you clear the browser cache.

## Clear browser cache action

The **Clear browser cache** action in your transaction steps empties the browser cache to reload page elements directly from the server instead of the browser cache. This feature helps you check the website's first-time visit performance and ensures that UI elements (such as images, text, and other front-end elements) are loaded correctly.

[SHORTCODE_1] **Note:** This action doesn't cost any transaction credits. Use it to enhance your monitoring needs. For more information, refer to [Understanding transaction monitor credit calculations]([LINK_URL_2]). [SHORTCODE_2]

## Add Clear browser cache action

There are two ways to add the **Clear browser cache** action in your transaction steps: the [Transaction step editor]([LINK_URL_3]) or the [Transaction script editor]([LINK_URL_4]).

### Using the Transaction step editor

To add the **Clear browser cache** in the **Transaction step editor**:

1. Go to [SHORTCODE_3] Transactions > Transactions setup [SHORTCODE_4].
2. Click the transaction monitor to which you want to add the clear browser cache action.
3. Go to the [SHORTCODE_5] Steps [SHORTCODE_6] tab.
4. Go to the **Step** section you want to add the clear browser cache action.
5. Click the [SHORTCODE_7] Add Action [SHORTCODE_8] button.
6. In the **Add action** popup, select **Clear browser cache**.
7. Click [SHORTCODE_9] Select [SHORTCODE_10].
8. In the **Settings > Description field**, provide a detailed description of the added action.
9. Click the [SHORTCODE_11] Save [SHORTCODE_12] button to confirm the monitor changes.

![Clear Browser Cache GIF]([LINK_URL_5])

### Using the Transaction script editor

To add the **Clear browser cache** in the **Transaction script** editor:

1. Go to [SHORTCODE_13] Transactions > Transactions setup [SHORTCODE_14].
2. Click the transaction monitor to which you want to add the clear browser cache action.
3. Go to the [SHORTCODE_15] Steps [SHORTCODE_16] tab.
4. In the right corner of your screen, click the [SHORTCODE_17] Switch to Script [SHORTCODE_18] button.
5. In the **Transaction script**, add the following [INLINE_CODE_1] snippet to the [INLINE_CODE_2] array:

[CODE_BLOCK_1]

6. Click the [SHORTCODE_19] Save [SHORTCODE_20] button to confirm monitor changes.

The **Clear browser cache** is now part of your steps and executes every time your transaction monitor runs.
