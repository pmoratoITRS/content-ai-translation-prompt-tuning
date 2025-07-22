{
  "hero": {
    "title": "Working with domain groups"
  },
  "title": "Working with domain groups",
  "summary": "Understand and learn how to set up your domain groups for Full Page Check Plus.",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/working-with-domain-groups",
  "translationKey": "https://www.uptrends.com/support/kb/full-page-check/working-with-domain-groups"
}

The Full Page Check \+ (FPC\+) allows you to identify the source of page elements quickly. The typical page has many elements that come from different providers; for example, you may have content coming from a CDN, ads coming from Google, and social media plugins bringing your most recent posts to your page. With domain groups you'll find that you can quickly identify the problem sources. A great way to learn about managing domain groups is to look at the **Default set**.

{{< callout >}}
**Note**: You will find the information about viewing your page elements by domain groups in the Knowledge Base: [Interpreting the results of the waterfall report]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="en" >}}).
{{< /callout >}}

## The Default set

Uptrends created a set of default domains. They included the most common domains, so you may not need to do anything more. Of course, we don't live in a cookie-cutter world, and the default set may not fit your needs. Uptrends gives you several options; you can

-   Modify the default set directly (not recommended),
-   Copy the default set and then modify it, or
-   Create a brand new domain group from scratch.

Before you start hacking and slashing your way through the domain group settings, let's make sure that you understand the parts that define a domain group.

{{< callout >}}
**Note**: After you open the Default Set (in the next step), you will notice the {{< AppElement type="button" >}}Copy this domain group{{< /AppElement >}} button on the top right of the page. We recommend that you use the button to duplicate the Default Set rather than edit the Default Set directly.
{{< /callout >}}

### Opening Domain Groups and the Default Set

When you open *Domain Groups* for the first time, you will have one domain group in the list called, **Default Set**.

To open the Domain Groups page

1.  Hover over **Account** on the **Main** menu,
2.  Click **Domain Groups** in the **Account** options section, and
3.  Click the name **Default Set** to open the editor.

![](/img/content/6cb4c7fd-a9b3-4496-934f-34210abf3009.png)

### The defined groups

Once you open the Default Set, you will see five domain groups defined in the **Groups** section of the page. In each section, you can add additional domains using the {{< AppElement type="button" >}}Add Rule{{< /AppElement >}} button. You can also exclude or remove a rule by selecting "exclude" in the rules definition or clicking the minus button to the right of the rule to delete the rule.

#### 1st party

When you expand the group (click the triangle next to **Name**), you'll notice that, by default, the developers selected the **Automatically include all content from the monitor's URL** and the **This is first party content** check boxes. Selecting these check boxes tells the system to include all the content that comes from the URL provided for the monitor. First party content is your content; i.e., you control the content. You may also have other domains that you control that contribute to the content on the page. Make sure you add them by using the {{< AppElement type="button" >}}Add rule{{< /AppElement >}} button.

#### Statistics

Analytic content runs in the background, and analytic services often contribute to poor performance on pages. You can add the URLs for any third party analytic tool you might use. If you want to monitor Google Analytics, make sure you do not select the **Block Google Analytics** check box on the monitor definition page.

#### CDN

Sometimes content delivery networks (CDN) fail or have performance issues. By defining the URLs and rules for your CDNs, you can monitor the performance of your CDNs.

#### Social

Social media plugins seem benign enough, but frequently your social media content and action buttons can cause havoc for your web performance. Include the URLs for your social media elements here. Uptrends has already included six of the most frequently used social media URLs for you.

#### Ads

We have all seen the click-bait sites that have so much advertising on the page that you simply give up waiting to see the top five cat pictures on the internet. Don't let your ad providers make your page sluggish; monitor your add providers by including the URLs in the **Ads** section.

#### Add your own

Of course, you can add rules to the predefined groups, but the default set leaves you room to add up to three more groups at the bottom of the page. Remember, to click the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button before you leave the page.
