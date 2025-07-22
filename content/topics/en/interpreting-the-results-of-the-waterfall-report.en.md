{
  "hero": {
    "title": "Interpreting the results of the waterfall report"
  },
  "title": "Interpreting the results of the waterfall report",
  "summary": "Once you have opened the report, learn how to interpret the results of the waterfall report.",
  "url": "/support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/interpreting-the-results-of-the-waterfall-report"
}

When you have opened the waterfall report (see [Where is the waterfall chart located?]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart#where-is-the-waterfall-chart-located" lang="en" >}})), you receive a large amount of data about your page and its elements. Each page element requires a request, TCP connect, HTTPS handshake, send, wait time, and receive time. The KB article [Waterfall timings]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-timings" lang="en" >}}) explains what is measured for these steps.

Once the receive time completes, the browser processes the element. A single page may have a hundred elements or more that the browser needs to process. The combined load times of the elements or just a sluggish few may cause your page to exceed your expected maximum load times. As you can see in the example below, this Full Page Check surpassed the 2.5-second maximum load time.

The report header gives general information about the check including the checkpoint used, the URL, and the browser used for the test. You will notice that the **Result** displays the specific reason for the error. This particular test failed due to exceeding the maximum load time with error code 6000. You can get explanations for other possible codes on the [Error Types](/support/kb/alerting/errors/error-types) page.

![](/img/content/8b43cd5b-e281-452e-a70d-03da8641f799.png)

## So what exactly caused the error?

As you scroll down the page, you get a list of the page elements. The report lists the page elements in the order that they load in the browser. Some portions load synchronously, and some elements have dependencies and do not load until other elements on the page finish loading. To the right of each element, you see a bar graph. Each color band on the bar graph represents a different connection state. Placing the elements on a timeline shows them in a waterfall perspective. Color bands indicate the time each element took to load. By scanning the report, you can quickly see the page elements that took the longest for the browser to receive.

In this example report, several of the handshakes (indicated in gold) took too long to complete. The elements causing the excessive handshakes and wait times could for example include a third-party analytic application and a sluggish request for a JavaScript file. Although those files took the longest, looking over the rest of the waterfall report, you will notice other elements with handshakes and wait times that, although shorter, may cumulatively affect your overall load times.

![](/img/content/2fc286e2-26d2-4b40-96f8-462734d4c509.png)

## Viewing the request and response headers

Your request and response headers give you the complete story. Viewing the request and response headers allows you to see exactly what the browser asked for and the result of the request. To open the request and response headers for an element, click the "\+" symbol to the right of the element’s name in the list. In the example below, the browser asked for a JavaScript file, but the request resulted in a lengthy delay in the handshake and response time.

![](/img/content/68f3ff2b-15a3-4f5d-b1be-233bd9ca55e2.png)

## Report summary

At the bottom of the waterfall report, you can see the report summary. The first column contains the color legend for the color bars in the waterfall portion of the report. To the right, you can see the total time and the average time for each of the connection states. The rest of the report footer gives you element type counts and page totals.

![](/img/content/eed630d9-4882-441f-a303-8bdc9fefbfc1.png)

## Find the element source using domain groups

If your monitor is an FPC\+, you can quickly see the source of your problem elements.

1.  Remember the element number you want to examine from the waterfall report.
2.  Click the Domains group button at the top right of the waterfall.  
      
    ![](/img/content/01ad49bc-cfa1-4fa1-a013-078eb3e3d53f.png)  
      
3.  Locate the element number in the list to see the domain group.  
    ![](/img/content/c3d3e95b-f9e6-448d-9fb5-2fcd628d426a.png)
