{
  "title": "Introducing Clear browser cache in transaction monitors",
  "date": "2025-01-29",
  "url": "[URL_BASE_CHANGELOG]january-2025-clear-browser-cache-transaction-monitors",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends [transaction monitors]([LINK_URL_1]) always open a browser to simulate user activities to check the performance of your website. The browser starts without cached data, and later stores cache to temporarily store website resources to speed up the loading process.

If you want to compare the behavior of your e-commerce site when loading items in the shopping cart for existing users (with cached data) compared to new visitors (without cached data), we recommend clearing the browser cache.

With the new **Clear browser cache** action in transaction monitors, you can now empty the browser cache to reload page elements directly from the server instead of the browser cache. This feature helps you check the website's first-time visit performance and ensures that UI displays (such as images, text, and other front-end elements) are loaded correctly. This action doesn't cost any transaction credits. Use this to enhance your monitoring needs. For more information, refer to the [Transaction step editor]([LINK_URL_2]).

![Clear Browser Cache GIF]([LINK_URL_3])