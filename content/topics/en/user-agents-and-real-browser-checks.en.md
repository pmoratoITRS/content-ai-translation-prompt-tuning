{
  "hero": {
    "title": "User agents and real browser checks"
  },
  "title": "User agents and real browser checks",
  "summary": "User agents are a great way to conduct synthetic tests for specific user environments like mobile. In this article learn how real browser checks and user agents can work for you.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/user-agents-and-real-browser-checks"
}

If you find the topic of user agents and real browser monitoring confusing, relax; you aren’t alone. Confusion about user agents and their application with real browser monitoring is one of our support team’s most frequently asked questions. The short answer is:

Real browser checks (Full Page Check and transaction monitoring) use an actual browser (just like your site’s visitors) to get and load your website's content. The browser generates a user agent that tells your servers about your user’s environment. The user agent allows the server to return optimized content for the specific environment defined by the user agent. You can manipulate the user agent on your monitors to test content meant for other browsers, operating systems, and devices like mobile phones and tablets.

Maybe not so short, but if the short answer works for you—great! For the rest of us, let’s dig a little deeper into the topic. First, let’s look at the three main components of HTTP communications.

## The players

Communication is a two way street between two parties; one asking for information and the other giving information. What facilitates that information is language, and for both parties to understand each other, they need to share a language. Let’s take a look at the players:

-   **Client**: The client asks for something from a resource. The client may be an Internet browser or another type of software application like a web crawler.
-   **HTTP**: The mutual language. The Hypertext Transfer Protocol clearly states the semantics of the communication.
-   **Server**: The server sends the information back to the client customized for that client based on the user agent.

A client uses an HTTP request to ask for information from the server, and the server sends back the information as an HTTP response. So where does this all fit in with real browser checks and user agents? Let’s start with the user agent.

## What is a user agent?

A user agent is a specific field in the HTTP request that contains information about the client. The server looks for specific words within the text and ignores everything else, so based on what the server does or doesn’t find in the user agent text, the server builds out the content optimized for the client. The user agent includes:

-   Browser type and version
-   Operating system and version
-   Rendering engine

To confuse things, you will see that user agents include pieces of information like the text “Mozilla/5.0” (found in most browser user agents) that just signals the server that this client is compatible with that browser. 

The Chrome user agent tells the server that it is a Mozilla/5.0 browser, a Safari browser, and a Chrome browser as you can see in the user agent below.

`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36`

## What is a real browser check?

As described above, a client can be any software application capable of communicating over the Internet, and an Internet browser is just one type of client. Software applications are perfectly happy just looking at the communications in the raw format, but your end-users wouldn’t like that much. Instead, for end users, the browser takes all of the returned content, parses it, and displays it visually on the screen.

You can test your site using a [basic monitor type or a real browser check](/support/kb/synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks). Uptrends' checkpoints can either use a browser or do without depending on the type of monitor you’ve selected. The basic HTTP and HTTPS monitors generate a request and send it to the server (no browser used). When the checkpoint computer receives the response, it looks for a result code, maybe some specified content, and a few other basics. The response is never processed, images never downloaded, and script files never ran. This process tells you if your site is up or down.

When you choose to monitor with a real browser, Uptrends' checkpoint computers open a browser window and send a request to your server just like your site visitors do using the browser. The response is received, processed, images downloaded, script files executed, and CSS files applied and the page appears in the browser window. A real browser check such as the [Full Page Check](/support/kb/synthetic-monitoring/browser-monitoring) can tell you about connection times and load times for every element on the page along with any failing content. We can even capture a screenshot when the page errors.

## So what is the crossover between user agents and Real Browser Monitoring?

You can change the user agent for both non-browser based monitors and for browser based monitors. You may want to modify the user agent for basic monitors just so that you can do content checks specific to certain user environments. You will find the real power is in using a real browser. By modifying the user agent, you can test the performance and contents of the page for most any user environment. Let’s look at a few examples:

### It’s a mobile-centric world out there

Mobile is quickly surpassing the desktop in user preference, so knowing that your servers respond quickly with your working mobile specific content is extremely important. Short of manual testing, you may think there just isn’t much you can do in the way of testing your mobile site. Not true. Using user agents for a real browser check can emulate any device, screen size, and mobile browser. Your servers will respond with your mobile content, and our real browser checks will load the content. Below you’ll find some user agents for popular devices, operating systems, and browsers.

**Android Chrome**

`Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36`

**iPhone Safari**

`Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_4 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B350 Safari/8536.25`

**Amazon Fire**

`Mozilla/5.0 (Linux; U; Android 5.1; locale; device Build/build) AppleWebKit/webkit (KHTML, like Gecko) Version/4.0 Chrome/chrome Safari/safari`

### Test for non-supported browsers

Currently you can test natively with Chrome and we have others in our pipeline to include soon. Using the current native browser is great for testing your users that update their browsers regularly, but a large percentage of users don’t. So although your site may work well in the current Chrome browser, how does it work on a release 5 updates ago? By modifying the user agent, you can test any version of the browser.

### Test other operating systems

A Chrome browser running on Mac OSX may have a very different experience than the same Chrome browser running on Windows 10. The only way you can know for sure is to adjust your user agent to specify other operating systems and versions. If you use the native browser on the checkpoint, the user agent defaults to the checkpoint operating system and current browser version.
