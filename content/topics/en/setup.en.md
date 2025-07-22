{
  "hero": {
    "title": "Setting up Real User Monitoring"
  },
  "title": "Setting up Real User Monitoring",
  "summary": "Learn how to start with Real User Monitoring, in a few easy steps.",
  "url": "/support/kb/rum/setup",
  "translationKey": "https://www.uptrends.com/support/kb/rum/setup"
}

**Real User Monitoring** (RUM) entails collecting performance data from your actual website users. Uptrends regular synthetic monitoring runs in a predictable environment, using a fixed monitoring interval. Synthetic monitoring works well for availability monitoring and detecting performance changes of web pages. RUM, on the other hand, runs in less predictable environments (for example, on your end user's devices and computers) and as such focuses much more on measuring the actual experience of your users. We've placed your RUM-based data inside your existing Uptrends account, and you can see your RUM data and synthetic data side by side.

## Getting started with Uptrends RUM

Starting with RUM requires two actions:
- Adding a RUM website definition to your account.
- Implementing the script in your actual website.

### Adding your first RUM website to your account

1. Log into your Uptrends account. If you don't have one yet, go to the [signup page]({{< ref path="signup" lang="en" >}}) and sign up for your free trial.
2. If you're not already using the Real User Monitoring function in Uptrends, you can try it for free by starting a RUM trial. In the Apps & Extras menu, click the *Try Real User Monitoring* option.
3. On the *Start RUM trial* page, click the {{< AppElement type="button" >}}Try Real User Monitoring{{< /AppElement >}} button.
4. Fill in the URL of the website you want to monitor. Click the {{< AppElement type="button" >}} Create first RUM website{{< /AppElement >}} button.
5. Your RUM trial has now started. Click the {{< AppElement type="button" >}}Show instructions{{< /AppElement >}} button to navigate to the settings of your new RUM website.

### Adding additional RUM websites

After the initial setup is done, the *RUM* section on the menu will contain a *Real users* sub-section, where you can find the RUM-related dashboards and manage your RUM websites. To add additional RUM websites:

1. Expand the *RUM* section in the menu.
2. Click the *\+* icon next to *RUM websites*.
![Adding a RUM website](/img/content/scr-RUM-adding_a_RUM_website.png)
3. Fill out the *Name* for the website, and its *URL*.
4. If your website is a single-page application (SPA), tick the option *Use Single Page Application Tracking*.
5. In case the website uses URL fragments (for example, `#fragment` at the end), and those are a significant part of your URLs, tick the *Include URL fragment* option. Doing so will prevent Real User Monitoring from discarding everything after the # symbol.
6. After setting all options, click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button in the lower left.
7. The script will now appear in the {{< AppElement type="tab" >}}Implementation{{< /AppElement >}} tab. The next section will cover implementing the script.

### Implementing the script in your website

Unlike regular website monitoring, you need to do some work on your side. Uptrends provides you with a small piece of JavaScript that you add to the web pages you would like to measure using RUM. Uptrends designed the script to not interfere with other scripts on your website, and your end users will not notice anything once you've added the Uptrends RUM script to your pages. The [impact of having the RUM script on your site]({{< ref path="/support/kb/rum/impact-of-the-rum-script-on-your-website" lang="en" >}}) is virtually zero.

1. Please make sure you have access to the code of your website, so the content of your pages can be changed.
2. Go to {{< AppElement type="menuitem" >}} RUM > Real users > RUM websites {{< /AppElement >}}.
3. Click on the website that you want to implement.
4. Go to the {{< AppElement type="tab" >}}Implementation{{< /AppElement >}} tab.
5. Highlight and copy the [RUM script]({{< ref path="/support/kb/rum/understanding-real-user-monitoring#what-does-a-rum-script-look-like" lang="en" >}}).
6. Paste the script between the `<head>` tags of the pages you wish to monitor with RUM. Placing the script inside the `<head>` tags ensures that the script loads as early as possible. Early loading helps the monitor to capture as much of the appropriate timing data as possible.

- If your website includes a Content Security Policy (CSP) response header, ensure that the Uptrends RUM domain `https://hit.uptrendsdata.com` is [added and correctly set](https://content-security-policy.com/) up on your website. To verify if the Uptrends RUM script is working properly, inspect your website's source code and see if the Uptrends RUM script exists. Open the *Developer tools > Network tab* of your browser, check if Uptrends RUM resources are loaded without issues.

7. Relaunch your website to update it with the script included.
8. RUM data will be tracked as soon as visitors are accessing your updated site. You should see data in the [RUM overview dashboard]({{< AppUrl >}}/Report/RumOverview) right away, [in real time]({{< ref path="/support/kb/rum/real-time-data" lang="en" >}}).

{{< callout >}}
**Note:** If you are enabling the *Use Single Page Application tracking* option for an existing RUM website, keep in mind that the script will change after saving and will therefore need to be updated on your end as well.
{{< /callout >}}

## License

Uptrends makes the RUM script and the components the script uses available to you under a BSD (Berkeley Software Distribution) license. You can find the full text at <https://hit.uptrendsdata.com/license.txt>.

{{< callout >}}
**Privacy concerns?** We have a [privacy page]({{< ref path="/support/kb/rum/rum-and-user-privacy" lang="en" >}}) that explains how Uptrends protects user privacy, additional steps you can take to enhance user privacy, and a suggested addition to your privacy statement.
{{< /callout >}}

## One script per website

Keep in mind that each script is specifically for a single website since it contains a `sid` which uniquely identifies the corresponding RUM website in your account. For each page view that Uptrends registers for a particular RUM website, we'll verify that the page view is, in fact, coming from the website domain that you specified. Let's take a look at an example of what we mean.  
**Example**: Using `www.your-domain.com` as an example website, by default, we allow page views to come from both `www.your-domain.com` and `your-domain.com`. If you also include the same script on a website hosted at `test.your-domain.com` or `www.your-other-domain.com`, RUM will not work on those other domains, for RUM doesn't register page views originating from other domains. Each website needs a separate RUM instance to maintain sensible data.

Essentially, if you want to track real user monitoring data on more than one website, you need to treat them as separate RUM websites in Uptrends as well. For each website domain you wish to monitor, you'll need to set up an additional RUM website, for each domain gets a different script.

The domain verification also means that RUM will only work in your real production environment. If you have separate development and test environments running locally or under a different domain, RUM will not register page views for those sites.

{{< callout >}}
**Note:** Perhaps you have special circumstances where the exact same site does run on multiple domains, but you want to treat them as one. To set this up, please [contact Support](/contact).
{{< /callout >}}
