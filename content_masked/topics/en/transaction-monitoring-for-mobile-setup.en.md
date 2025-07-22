{
  "hero": {
    "title": "Transaction monitoring for mobile setup"
  },
  "title": "Transaction monitoring for mobile setup",
  "summary": "Using Uptrends' transaction recorder, you can also test transactions for your mobile site. Learn how.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/transaction-monitoring-for-mobile-setup",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mobile is everywhere, and testing transactions for desktop alone may not guarantee that your transactions work correctly for your mobile users. With Uptrends, you can use the transaction recorder to set up scripts for monitoring the mobile or responsive design version of your website by simulating a device's viewport. You simulate the device's viewport by using the mobile simulation mode in Chrome's developer tools. Here’s how.

## Use the Chrome Device Mode when recording a transaction

1.  [Start the Uptrends transaction recorder (Chrome extension)]([LINK_URL_1]) as you normally would, and a new browser window opens.
2.  Press the F12 key to open the Chrome Developer tools.
3.  Locate the Toggle device toolbar icon and click to enter device simulation mode.  
    ![screenshot transaction recorder toggle device toolbar]([LINK_URL_2])  
4.  Adjust the device settings if necessary.
5.  Navigate to your mobile site.
6.  Click through your transaction.
7.  Upload the transaction to your account for scripting and testing yourself, or upload the script for Support to handle the scripting for you.
8.  Adjust the mobile monitoring settings in your new transaction monitor.

Learn more about [using Device Mode]([LINK_URL_3]) in your Chrome browser.

## Adjust the monitor settings for mobile monitoring 

Now that you've recorded your transaction using the Device Mode from Chrome DevTools, you need to finish the mobile setup in your monitor settings.

1. Go to [SHORTCODE_1] Transactions > Transaction setup [SHORTCODE_2] and open the new transaction monitor.
2. Switch to the [SHORTCODE_3] Advanced [SHORTCODE_4] tab.
3. In the *Browser section* under *Device / screen* adjust your **Screen size** and choose a **User agent** (with the option to choose a custom user agent), or select **Mobile simulation** and choose one of the popular devices.
  ![screenshot Advanced tab of transaction monitor]([LINK_URL_4])
4. Set **Bandwidth throttling** if you want to simulate the end-user experience fully. Read more about [bandwidth throttling]([LINK_URL_5]) in the knowledge base.
5. Click the [SHORTCODE_5] Save [SHORTCODE_6] button to save your changes.
