{
  "hero": {
    "title": "Exclude A/B tests from transaction requests"
  },
  "title": "Exclude A/B tests from transaction requests",
  "summary": "A/B tests can cause errors and generate needless alerts. You can prevent unwanted alerts by telling Uptrends to exclude requests to your A/B test tool's URL.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/exclude-a-b-tests-from-transaction-requests",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

A/B testing tools split the traffic to your web page by directing one group of users to version A and the other group of users to version B of your web page. Your transaction monitoring may generate errors due to your A/B testing because of the different page contents. For example, if you labeled a button in version A, "Add to cart,” and you labeled the same button in version B, "Add to shopping cart,” you will see errors if the script’s success relies on finding the text “Add to cart.” When the transaction monitoring script relies on finding an element that is only on version A of your page, the script will fail if it receives version B. You can prevent this error by excluding the URL for your A/B testing tool from the requests the Uptrends monitor performs on your site.

[SHORTCODE_1]
**Note:** Of course, this also applies to Full Page Check monitors if you're performing a check for specific content and that content changes during an A/B test.
[SHORTCODE_2]

## Excluding A/B testing tool URLs

To exclude the A/B testing tool URLs:

1.  Log into your Uptrends account.
2.  Click **Monitors** from within the [SHORTCODE_5]Monitor[SHORTCODE_6] drop-down on the main menu.
3.  Click the monitor to view the monitor's details.
4.  Click to open the [SHORTCODE_7]Advanced[SHORTCODE_8] [SHORTCODE_9]tab[SHORTCODE_10].
5.  Find the text field labeled, "**Block these (parts of) URLs**."
6.  Type the URL for your testing tool into the text field. Place each excluded URL on its own line.
7.  Click [SHORTCODE_11]Save[SHORTCODE_12].

That’s all you need to do. Once you add your excluded URLs, Uptrends doesn't send an outgoing request to your A/B testing tool when checking your site. Without the outgoing request, Uptrends never triggers the A/B testing script.

### Example

In the “Block these (parts of) URLS” provide the URL for your A/B testing tool; for example, if you use Visual Website Optimizer for your A/B testing, type visualwebsiteoptimizer.com in the field. If you use Optimizely, you need to exclude optimizely.com.

![]([LINK_URL_1])

[SHORTCODE_3]
**Note:** Although we do actively filter the request coming from the excluded URL, we do include it in the waterfall report indicated by the response header "X-Blocked-By-Uptrends: true."
[SHORTCODE_4]
