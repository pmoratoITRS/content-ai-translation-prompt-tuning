{
  "hero": {
    "title": "Transaction monitoring for mobile setup"
  },
  "title": "Transaction monitoring for mobile setup",
  "summary": "Using Uptrends' transaction recorder, you can also test transactions for your mobile site. Learn how.",
  "url": "/support/kb/synthetic-monitoring/transactions/transaction-monitoring-for-mobile-setup",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-monitoring-for-mobile-setup"
}

Mobile is everywhere, and testing transactions for desktop alone may not guarantee that your transactions work correctly for your mobile users. With Uptrends, you can use the transaction recorder to set up scripts for monitoring the mobile or responsive design version of your website by simulating a device's viewport. You simulate the device's viewport by using the mobile simulation mode in Chrome's developer tools. Here’s how.

## Use the Chrome Device Mode when recording a transaction

1.  [Start the Uptrends transaction recorder (Chrome extension)]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder#using-transaction-recorder" lang="en" >}}) as you normally would, and a new browser window opens.
2.  Press the F12 key to open the Chrome Developer tools.
3.  Locate the Toggle device toolbar icon and click to enter device simulation mode.  
    ![screenshot transaction recorder toggle device toolbar](/img/content/scr_transaction-recorder-for-mobile.min.png)  
4.  Adjust the device settings if necessary.
5.  Navigate to your mobile site.
6.  Click through your transaction.
7.  Upload the transaction to your account for scripting and testing yourself, or upload the script for Support to handle the scripting for you.
8.  Adjust the mobile monitoring settings in your new transaction monitor.

Learn more about [using Device Mode](https://developer.chrome.com/docs/devtools/device-mode) in your Chrome browser.

## Adjust the monitor settings for mobile monitoring 

Now that you've recorded your transaction using the Device Mode from Chrome DevTools, you need to finish the mobile setup in your monitor settings.

1. Go to {{< AppElement type="menuitem" >}} Transactions > Transaction setup {{< /AppElement >}} and open the new transaction monitor.
2. Switch to the {{< AppElement type="tab" >}} Advanced {{< /AppElement >}} tab.
3. In the *Browser section* under *Device / screen* adjust your **Screen size** and choose a **User agent** (with the option to choose a custom user agent), or select **Mobile simulation** and choose one of the popular devices.
  ![screenshot Advanced tab of transaction monitor](/img/content/scr_mobile-simulation-devices.min.png)
4. Set **Bandwidth throttling** if you want to simulate the end-user experience fully. Read more about [bandwidth throttling](/support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling) in the knowledge base.
5. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to save your changes.
