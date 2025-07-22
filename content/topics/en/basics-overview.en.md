{
  "hero": {
    "title": "Basics of the Uptrends app"
  },
  "title": "Basics of the Uptrends app",
  "summary": "Are you completely new to Uptrends? Check out the articles here to get an introduction and have a basic understanding of what the Uptrends app can do for you.",
  "url": "/support/kb/basics/basics-overview",
  "translationKey": "https://www.uptrends.com/support/kb/basics/basics-overview",
  "sectionlist": false
}

Uptrends is a SaaS (Software as a Service) Digital Experience Monitoring tool, providing users with detailed insights into the uptime and performance of their websites and -services, from the end-user perspective. Easy to configure, Uptrends supports a wide range of [monitor types]({{< ref path="/support/kb/basics/monitor-types" lang="en" >}}) for every monitoring scenario, as well as [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="en" >}}).

## Synthetic Monitoring

With proactive [synthetic monitoring]({{< ref path="/products/synthetics/synthetic-monitoring" lang="en" >}}), Uptrends uses its worldwide [network of checkpoints]({{< ref path="/checkpoints" lang="en" >}}) to check your websites and processes for availability and performance 24/7, from locations that are relevant to your business. Various monitor types cover any use case you may have.

{{< Support/storylane url="https://app.storylane.io/demo/tqewkqp0c4ly" >}}

### Uptime monitoring {id="synthetic-monitoring"}

[Uptime monitoring]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring" lang="en" >}}) is high-frequency monitoring of the availability of your websites and -services. Monitors like the [HTTPS monitor type]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https" lang="en" >}}) check your website for availability and correct functioning, up to every minute, from anywhere in the world.

![A basic monitor log](/img/content/scr-basics-uptimelog_020224.min.png)

Other basic monitor types are available, such as the [DNS monitor]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/dns" lang="en" >}}), which checks the correctness of your DNS setup by querying any DNS server, and the [SSL certificate monitor]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ssl-monitors" lang="en" >}}) to check the validity of your SSL certificates, and send alerts as soon as it is no longer correct, or due to expire.

### Browser monitoring {id="browser-monitoring"}

In contrast with uptime monitoring, [browser monitoring]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring" lang="en" >}}) uses an actual browser to open your websites. By doing so, the Full Page Check (FPC) monitor type does a complete load of the page, in the exact same way your end-users would, generating a large set of detailed performance metrics.

Such metrics include a [waterfall chart]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}) (a detailed breakdown of technical information and performance metrics for each individual element that makes up the page load), but also key metrics such as [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="en" >}}) and [W3C navigation timings]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/w3c-navigation-timings" lang="en" >}}), which may impact your customer experience or search engine rankings.

![Full Page Check result example](/img/content/scr-fpc-result-basics.min.png)

### Transaction / Web Application monitoring {id="transaction-monitoring"}

A [transaction (or Web Application) monitor]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="en" >}}) loads your page in an actual browser, and then executes a script to interact with the page, imitating the actions of a real user. This monitor type can be used to test complete user journeys across your website, such as logins, searching for listed products, putting them in a shopping cart and proceeding through to the payment screen, filling in forms, et cetera.

A typical user flow, by which the user interacts with your website in several steps to complete a specific action, will touch multiple webservers, databases, APIs, or external resources. Transaction monitoring is the best way to check that all aspects of your critical user flows still function correctly. It is easy to set up, without any scripting experience required, by using the [transaction recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}}) plugin for Chrome.

![The transaction step editor](/img/content/scr-transaction-steps-basics_020224.min.png)

#### API monitoring

The [Multi-step API (MSA) monitor type]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring" lang="en" >}}) is to your backend/APIs what transaction monitoring is to your frontend/user journeys. APIs allow for communication between applications, and they form the backbone of the modern internet.

Your organization almost certainly relies on several APIs in one way or another, but visibility into any issues that might arise can be tricky, since API communication and interactions happen in the background. With Multi-step API monitoring, you can check your APIs directly by recreating requests and verifying the response for correctness, completeness, and timeliness.

## Real User Monitoring

In addition to supporting synthetic monitoring, Uptrends offers [Real User Monitoring (RUM)]({{< ref path="/support/kb/rum/understanding-real-user-monitoring" lang="en" >}}). RUM uses a simple script embedded in your page HTML to gather actual performance data from your real end users, in real time. Complementing synthetic data, RUM can provide you with insights about your real users' experiences, wherever they may be located, as well as providing you with data regarding your users' setups in terms of which browsers and operating systems they are using.

![An example of RUM data](/img/content/scr-rum-map-basics_020224.min.png)

## Alerting

Uptrends' monitoring comes with powerful and versatile [alerting]({{< ref path="/support/kb/alerting" lang="en" >}}). Determine when alerts should be generated and what messages should be sent using [alert definitions]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="en" >}}). Use our out-of-the-box [integrations]({{< ref path="/support/kb/alerting/integrations/what-are-integrations" lang="en" >}}) to send messages via email, SMS, phone call, or an external platform. Alternatively, build a [custom integration]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="en" >}}) to connect your Uptrends alerts with any external platform out there, even the ones that are not listed on the integrations page.

