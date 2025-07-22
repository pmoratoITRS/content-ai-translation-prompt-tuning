{
  "hero": {
    "title": "Clear browser cache"
  },
  "title": "Clear browser cache",
  "summary": "When your transaction needs to reload page elements directly from the server instead of the stored cache, clearing the browser cache helps.",
  "url": "/support/kb/synthetic-monitoring/transactions/clear-browser-cache",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/clear-browser-cache"
}

Uptrends [transaction monitors]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="en" >}}) always open a browser to simulate user activities to check your website performance. The browser starts without any cached data. As it performs user activities (such as logging in, scrolling through products, and adding to cart) on your website, it temporarily stores cache to recognize all your website resources. This speeds up the browser's loading process the next time it visits the same page.

There are cases where you want to monitor different page behaviors when visiting a page. If you want to compare the behavior of your e-commerce site when loading items in the shopping cart for existing users (with cached data) compared to new visitors (without cached data), we recommend you clear the browser cache.

## Clear browser cache action

The **Clear browser cache** action in your transaction steps empties the browser cache to reload page elements directly from the server instead of the browser cache. This feature helps you check the website's first-time visit performance and ensures that UI elements (such as images, text, and other front-end elements) are loaded correctly.

{{< callout >}} **Note:** This action doesn't cost any transaction credits. Use it to enhance your monitoring needs. For more information, refer to [Understanding transaction monitor credit calculations]({{< ref path="/support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="en" >}}). {{< /callout >}}

## Add Clear browser cache action

There are two ways to add the **Clear browser cache** action in your transaction steps: the [Transaction step editor]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}) or the [Transaction script editor]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="en" >}}).

### Using the Transaction step editor

To add the **Clear browser cache** in the **Transaction step editor**:

1. Go to {{< AppElement type="menuitem" >}} Transactions > Transactions setup {{< /AppElement >}}.
2. Click the transaction monitor to which you want to add the clear browser cache action.
3. Go to the {{< AppElement type="tab" >}} Steps {{< /AppElement >}} tab.
4. Go to the **Step** section you want to add the clear browser cache action.
5. Click the {{< AppElement type="editbutton" >}} Add Action {{< /AppElement >}} button.
6. In the **Add action** popup, select **Clear browser cache**.
7. Click {{< AppElement type="buttonCta" >}} Select {{< /AppElement >}}.
8. In the **Settings > Description field**, provide a detailed description of the added action.
9. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to confirm the monitor changes.

![Clear Browser Cache GIF](/img/content/gif-transaction-clear-browser-cache.gif)

### Using the Transaction script editor

To add the **Clear browser cache** in the **Transaction script** editor:

1. Go to {{< AppElement type="menuitem" >}} Transactions > Transactions setup {{< /AppElement >}}.
2. Click the transaction monitor to which you want to add the clear browser cache action.
3. Go to the {{< AppElement type="tab" >}} Steps {{< /AppElement >}} tab.
4. In the right corner of your screen, click the {{< AppElement type="editbutton" >}} Switch to Script {{< /AppElement >}} button.
5. In the **Transaction script**, add the following `clearCache` snippet to the `actions` array:

```json
    {
      "clearCache": {
        "description": "Provide a step description here"
      }
    },
```

6. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to confirm monitor changes.

The **Clear browser cache** is now part of your steps and executes every time your transaction monitor runs.
