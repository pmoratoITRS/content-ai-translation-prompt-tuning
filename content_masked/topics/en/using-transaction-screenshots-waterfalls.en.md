{
  "hero": {
    "title": "Using transaction screenshots and waterfalls"
  },
  "title": "Using transaction screenshots and waterfalls",
  "summary": "For thorough testing of your transaction scripts and later for troubleshoot, you need to review the waterfall reports and screenshots to identify the source of errors and the health of your transaction monitoring script. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends' [transaction monitors]([LINK_URL_1]) come with several options for analysis and debugging. Two of those tools are screenshots and waterfall reports. The tools are an essential part of your transaction monitoring toolkit, and are essential for root-cause or performance analysis. 

[SHORTCODE_1]
**Note**: Screenshots and waterfall reports are available to all users when using the [SHORTCODE_3] Test now [SHORTCODE_4] button. However, only **Enterprise-** and **Business**-level accounts may add them for use in staging and production modes.
[SHORTCODE_2]

## Enabling waterfall reports and screenshots

1.   Navigate to the settings of the transaction monitor you'd like to enable waterfalls/screenshots for (for example, via [SHORTCODE_5] Monitoring > Monitor setup [SHORTCODE_6] in the sidebar menu).
2.   In the [SHORTCODE_7]Steps[SHORTCODE_8] tab, select the step you want to activate a waterfall/screenshot for.
3.   Check the appropriate checkbox to enable a waterfall or screenshot for that step. 

  -  Note that you can also add screenshots halfway through steps by [adding them as an action]([LINK_URL_2]).

  - In order to view the [page source and console log data]([LINK_URL_3]), the waterfall option must be enabled.

Keep in mind that waterfalls and screenshots will cost a [transaction monitor credit]([LINK_URL_4]) for each one you add.



Uptrends generates a waterfall or screenshot in the following situations:

-   **In case of errors:** when a confirmed error occurs during a transaction, a screenshot (but **not** a waterfall) will be generated. You don't have to set anything up, this happens automatically for the first confirmed error.
-   **Every monitor check result:** When you have enabled a waterfall or screenshot in a specific step, after the step completes.

## Finding your waterfall reports and screenshots

Screenshots and waterfalls are indispensable when it comes to troubleshooting and debugging transaction errors. You get them automatically when you use the [SHORTCODE_9] Test now [SHORTCODE_10] button, and Enterprise and Business users get a screenshot on the first confirmed error.

### Where are my screenshots and waterfalls while debugging?

You use the Test now button a lot when you're testing your transaction in development mode. An important feature of the Test now results are the waterfall reports and screenshots. To access these, click the **Test results available** button located at the top of each step after running a manual test.

![]([LINK_URL_5])

After clicking the **Test results available** button, scroll down the page to the **Debug information**. The report automatically includes the debug details during manual tests.

Click the graphic to access the screenshot or waterfall.

![Screenshot and waterfall after test now]([LINK_URL_6])

### Where are my screenshots and waterfall charts in my reports?

Enterprise and Business users can find their staging and production screenshots in their check detail reports. Navigate to [SHORTCODE_11]Monitoring > Monitor log [SHORTCODE_12] on the Uptrends menu to see your monitor log.

**Screenshots**: You know if a detail has a screenshot when you see a camera icon in your monitor log.

**Waterfalls**: If you've added waterfall charts to your transaction scripts, each check will include the chart(s). The Monitor log doesn't show an indicator.

![]([LINK_URL_7])

To view the screenshot or waterfall charts:

1. Click to open the Check detail report.
2. Locate the **Check details** section.
3. Click the camera or waterfall icon in your step results.

![]([LINK_URL_8])

## Using screenshots for debugging

So that you can see the on-screen result of a step, your test generates a screenshot. The screenshot shows you what the viewport looked like after a successful step or page error. If the action occurs further down the page, you can add a scroll action before the click event.

Study the screenshot to verify:

-   **Expected content loaded.** After a page navigation check for correct content.
-   **Dynamic content resulting from user input** works well. For example, if item selection requires the user to select a color before size options become available to verify that the element populated properly.
-   **Masked fields work as expected**. Is the character formatted correctly?
-   **Responsive design changes**. If your site uses responsive design, you may need to adjust the browser resolution in your monitor settings. By adjusting your browser resolution, you can ensure that you’re getting the correct page layout. For example, if your menu reduces down to a hamburger icon when the browser window gets smaller, you may need to add additional click or hover actions. Check under the monitor's [SHORTCODE_13]Advanced[SHORTCODE_14] tab adjust your browser resolution.

## Using waterfall charts for debugging

The waterfall report gives you detailed information about the initial page’s load time. It tells you exactly how long it took to retrieve and process each page element along with the request and response headers. Your waterfall will help you quickly identify problems on the page. See our article on the [waterfall chart]([LINK_URL_9]) for a more in-depth look at what is presented in the waterfall chart and how it can be used for debugging. 

![]([LINK_URL_10])


