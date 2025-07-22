{
  "hero": {
    "title": "Monitor types"
  },
  "title": "Monitor types",
  "summary": "Get an overview on all the monitor types that Uptrends has to offer, from plain availability to complex transactions.",
  "url": "[URL_BASE_TOPICS]basics/monitor-types",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Uptrends offers a wide range of monitor types, each targeted to your specific monitoring needs. Every synthetic monitor uses [credits]([LINK_URL_1]) to calculate the pricing for different monitoring services.

This article provides an overview of how each monitor type checks your website's performance to help you get started.

[SHORTCODE_1] **Note:** You can use multiple monitor types along with [Real User Monitoring]([LINK_URL_2]) to measure your website's actual performance based on user's experience from their own network, actual browsers, and other activities. [SHORTCODE_2]

## Uptime monitors (Basic checks)

An Uptime monitor does basic checks on your websites. It checks the page's availability, expecting a 200 response status code. This monitor only sees your website's initial response and doesn't completely scan page elements or other specific website components. 

An uptime monitor checks as often as once per minute, giving a more accurate report of the page's uptime compared to Browser or Full Page Check monitors.

### Types of Uptime monitors

Several types of Uptime monitors are as follows:

- Webpage checks — **HTTP** and **HTTPS** (more advisable to use than HTTP) monitors
- Advanced checks — **DNS**, **SSL Certificate**, **SFTP**, and **FTP** monitors
- Mail servers — **SMTP**, **POP3**, and **IMAP** monitors
- Database servers — **Microsoft SQL servers** and **MySQL** monitors
- Network checks — **Ping** and **Connect** monitors

[SHORTCODE_3] **Note:** The **HTTP** monitor type is no longer available for new users. Uptrends extended the functionality of **HTTPS** monitors to cater to and check the availability of HTTP websites. [SHORTCODE_4]

For more information about uptime monitors and their types, refer to [Uptime monitors]([LINK_URL_3]).

## Browser monitors (Full Page Check)

A Browser monitor, also known as a Full Page Check (FPC) or Real browser monitor, completely checks your website's page load performance on an element-by-element basis. This monitor opens an actual (real) browser to simulate what users see upon visiting your website.

It examines how your website loads from start to finish, taking into account how each page elements (such as scripts, CSS files, images and third party contents) behaves. Also, browser monitors provide information about your website's [Core Web Vitals]([LINK_URL_4]),[W3C Navigation Timings]([LINK_URL_5]) and a [Waterfall chart]([LINK_URL_6])metrics.

This monitor checks as often as once every five minutes and gives you an idea about uptime, but with less accuracy than an uptime monitor. To know the difference between basic checks and real browser checks, refer to [Basic webpage checks versus real browser checks]([LINK_URL_7]). To learn more information, refer to [Browser monitoring]([LINK_URL_8]).

## API monitors

An API monitor is a powerful monitor that performs checks on a single-step API call or complex multi-step API calls. This monitor features a no-code (UI-based) solution and [custom scripting]([LINK_URL_9]) to test HTTP requests and responses easily while considering your monitoring needs.

You can also add custom logic or [user-defined functions]([LINK_URL_10]), define [custom variables]([LINK_URL_11]), use [assertions]([LINK_URL_12]), and more API related capabilities.  

### Types of API monitors

Several types of API monitors are as follows:

- [Multi-step API (MSA) monitor]([LINK_URL_13]) — the primary API monitoring type with more advanced and powerful features compared to Webservice HTTP and HTTPS monitors.  
- [Postman API monitor]([LINK_URL_14]) — a monitor that allows you to maximize API checks by running a Postman workspace collection on the Uptrends checkpoint network. 
- [Webservice HTTP and HTTPS monitors]([LINK_URL_15]) — a classic type of HTTP monitor that only does basic checks on the API's uptime and availability.

[SHORTCODE_5] **Note:** For API monitoring, the **Webservice HTTP and Webservice HTTPS** monitor types are no longer available for new users. Uptrends recommends using the Multi-step API monitor instead to maximize checking your API behaviors. [SHORTCODE_6]

For more information about API monitors, refer to [API monitoring]([LINK_URL_16]).

## Transaction monitors

A Transaction monitor, also known as a Web application or User journey monitor, simulates user activities through an actual (real) browser to check the performance of your website.

Imagine a real user interacting with your website using a browser window. They fill out forms, click buttons, and make selections as they navigate through your site. Now, transaction monitors let you replace that user with a robot doing the exact same thing. This robot is an Uptrends checkpoint computer that opens a Chrome browser and uses a script to navigate and test your site. These scripts are run to do the same interactions your users do every day.

Transaction monitors feature the [ITRS Uptrends Transaction Recorder]([LINK_URL_17]) to help you start automating your transactions. This is a Chrome extension that records your screen as you click through your transactions. Once your transactions are successfully recorded, you can save this as a monitor and scripts will be generated from the recording.

To begin setting up a transaction monitor, you can do any of the following:

- Create a transaction monitor from scratch using the [transaction step editor]([LINK_URL_18]).
- [Download and use the transaction recorder]([LINK_URL_19]) to initially create scripts that you can also edit and manage later.
- Have the Uptrends Support team  use your recording to write and test your script for you.

For more information about transaction monitors, see the following:

- [Transaction monitor overview]([LINK_URL_20])
- [Understanding transaction monitoring]([LINK_URL_21])
- [How to use the ITRS Uptrends Transaction Recorder: User journey in a shop tutorial]([LINK_URL_22]) — step-by-step guide on how to use the transaction recorder.