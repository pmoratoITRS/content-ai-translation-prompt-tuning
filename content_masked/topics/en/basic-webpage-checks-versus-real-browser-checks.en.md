{
  "hero": {
    "title": "Basic webpage checks versus real browser checks"
  },
  "title": "Basic webpage checks versus real browser checks",
  "summary": "Learn the difference between a basic webpage check and one that uses an actual browser.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/basic-webpage-checks-versus-real-browser-checks",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When it comes to [synthetic monitoring]([LINK_URL_1]), you have two choices for monitoring your webpage: basic checks and checks that use a real browser. So what’s the difference between these two types of monitors? The primary difference is how Uptrends handles the response.

#### The short answer

Basic checks only look at the initial response; page elements like scripts, CSS files, and images are never retrieved or executed. Real browser checks download and load the entire page contents (scripts, CSS files, images, and third-party content) into an actual browser window.

## Basic Checks

When a checkpoint conducts a basic check (HTTP/HTTPS), the checkpoint sends a request for the page. The checkpoint receives the response and looks at a few key components. Based on your monitor settings, a basic check may examine the:

-   Result code
-   Response time
-   Page length is bytes
-   Content match (character strings)

The monitor never loads the response content into a browser, so page elements like CSS files, script files, third-party content, and images are never downloaded, parsed, and loaded. With a basic check you don’t know about any errors or performance problems that may occur when retrieving and loading the full content. What we do know is that the site is available, returning acceptable codes, has a minimum size, and includes the content specified. A basic check may occur as frequently as once per minute giving a more accurate account of the page's availability.

## Real browser checks

When a checkpoint conducts a real browser check ([Full Page Check]([LINK_URL_2]), [Transaction Monitor]([LINK_URL_3])), the checkpoint requests the page and loads the response into a real browser. The checkpoint loads the entire page contents (CSS, script files, additional HTML files, third-party content, and images). Each request and response is checked for performance and errors. The real browser checks are scheduled as frequently as once every five minutes giving you a simulated view of an actual user’s experience with your page. A real browser check can give you an idea about uptime but with less accuracy than a basic check.
