{
  "hero": {
    "title": "Adding extra monitors and credits"
  },
  "title": "Adding extra monitors and message credits",
  "summary": "When you need extra monitors, API credits, transaction credits, or message credits either call us or buy them from within your Uptrends account.",
  "url": "/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms",
  "translationKey": "https://www.uptrends.com/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms"
}

## Credits

Uptrends uses credits to calculate the [pricing]({{< ref path="/pricing" lang="en" >}}) for different monitoring services. Credits are needed to create, configure, and schedule monitors for execution.

Each synthetic monitor, such as [Uptime or Basic monitors]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="en" >}}), [Browser (Full-Page Checks or FPCs) monitors]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="en" >}}), [API monitors]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="en" >}}), and [Transaction monitors]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="en" >}}) has its own credit type:

- Uptime monitors use **Uptime credits**
- Browser monitors use **Browser credits**
- API monitors use **API credits**
- Transaction monitors use **Transaction credits**
- **Credits** — only applies to all existing accounts using single pricing tier

Your total credits depend on your [monitor mode]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="en" >}}) and [monitor settings]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-settings-overview" lang="en" >}}). All monitors set to **Staging** and **Production** mode use credits. Meanwhile, any monitor in **Development** mode is considered inactive and doesn't use any credits.

If you don't have enough monitor credits, you can easily [purchase more]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms#add-credits" lang="en" >}}) or just create and run your monitors in [Development mode]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-mode#development-mode" lang="en" >}}).

## Calculate credits

To view the credit status of all your Synthetic monitors, go to {{< AppElement type="menuitem" >}} Account setup > Subscription and invoices {{< /AppElement >}}. The donut chart shows your credits for each monitor type:

![Monitor credits](/img/content/scr-monitor-credits.min.png)

As shown in the image, the user purchased five **Browser credits** or monitors. Two of these are currently in use, and they can still create three more FPC monitors. Similarly, for **Uptime credits**, the user purchased 10 credits or Uptime monitors. Four of these are currently in use, and they can still create six more basic monitors.

For API and transaction monitors, calculating credits is slightly more complex. Credits are not calculated for every monitor used, but for each request or page load the monitor checks. 

If you created any API monitor (Multi-step API (MSA) or Postman), each HTTP request counts as one credit. If you created one MSA monitor with three steps, it costs three credits. If you created two MSA monitors, each with three steps, total credits will be calculated as 3 steps for MSA-A and 3 steps for MSA-B, 6 API credits in total.

This is also the case for transaction monitors: we count one credit for every new request (page load),[every waterfall, or every filmstrip]({{< ref path="/support/kb/synthetic-monitoring/transactions/using-transaction-screenshots-waterfalls" lang="en" >}}). If a transaction monitor goes through four pages (new page loads), has the waterfall and filmstrip enabled on the first step, this will be calculated as 4 page loads + 1 waterfall + 1 filmstrip, 6 Transaction credits in total. For more information about transaction credits, refer to [Understanding transaction monitor credit calculations]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="en" >}}).





## Add credits

To monitor additional websites, servers, transactions, and other web services, there are two ways to buy more credits:

1. **Contact Us**  
    If you are currently subscribed and would like to make sure that you get the appropriate number of extra monitors or credits at a competitive rate, please contact your sales representative directly, or [file a ticket](/contact).  

2. **Add through the Uptrends web application**
    1. Go to {{< AppElement type="menuitem" >}}  Account setup > Buy extras {{< /AppElement >}}.
    2. You can increase the number of Uptime, Browser, API, Transaction, and message credits for your account.
    3. Click {{< AppElement type="buttonPrimary" >}} Next {{< /AppElement >}}.
    4. Provide your billing information and select your desired **Payment method**.
    5. Click {{< AppElement type="savebutton" >}} Confirm order {{< /AppElement >}}.
