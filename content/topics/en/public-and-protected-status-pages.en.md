{
  "hero": {
    "title": "Public and protected status pages"
  },
  "title": "Public and protected status pages",
  "summary": "Public status page overview and setting up a protected status page for when you want to limit visibility.",
  "url": "/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages",
  "translationKey": "https://www.uptrends.com/support/kb/dashboards-and-reporting/status-pages/public-and-protected-status-pages"
}

## Public status pages

A public status page lets you publish uptime information for your monitors, so the general public has up to date information about the availability of your sites and services. You can control which monitors you want to include in your status page, and you can change the look and feel of the page so it fits in with the style of your brand. 
Technically spoken, a public status page is a specialized website monitoring dashboard designed to publicly showcase the availability status of a website, web service, or server being monitored.

The public status page shows the current status of the monitor (color code at the start of each row) and the SLA status (icons in the table):

![screenshot public status page overview](/img/content/scr_public-status-page-overview.min.png)

If you want to go into detail and see the uptime data for a monitor, click on the row of the corresponding monitor:

![screenshot public status page details](/img/content/scr_public-status-page-monitor-details.min.png)

### Reasons for using a public status page

Check out the page [What are public status pages used for?]({{< ref path="support/kb/dashboards-and-reporting/status-pages/why-use-public-status-pages" lang="en" >}}) to find out whether a public status page is a good fit for you.

### Setting up a public status page

Learn how to set up and configure public status pages in the knowledge base article [Public status page configuration]({{< ref path="support/kb/dashboards-and-reporting/status-pages/public-status-page-configuration" lang="en" >}}).

## Protected status pages

{{< callout >}} **Note**: Protected status pages are a feature of the Enterprise subscription plan. {{< /callout >}}

Perhaps you want to share the status of your sites and services to someone outside your organization, without exposing it to the rest of the world. To do this, you can use the public status page function to create a protected status page. A protected status page means that a login name and password is needed to access that page. When a person outside your organization uses that login, they will only see that status page; they will not see any other dashboard and won't be able to make any changes. Since the status page is protected, it will remain completely invisible to the outside world.

### Creating a protected status page and setting up operators

Read the knowledge base article [Protected status page configuration]({{< ref path="support/kb/dashboards-and-reporting/status-pages/protected-status-page-configuration" lang="en" >}}) for instructions on how to set up a new protected status page.

### Accessing a protected status page

Once you've had confirmation of Support that the permissions have been granted, you can go ahead and instruct the people outside your organization to start using the protected status page. There are two ways for them to navigate to it: 

- They can go to the [Uptrends app](https://app.uptrends.com) and enter the login credentials you created for them. A list of protected status pages they have access to will be displayed. 
- You can give them the *Preview* link (URL) of the protected status page. To find the URL, go to {{< AppElement type="menuitem" >}} Account setup > Public status pages {{< /AppElement >}} and check out the *Preview* next to the page. This URL can be bookmarked for easy reference. When someone first visits it, they'll have to log in.

Please note that a protected status page is always accessible to administrators (operators who are members of the *Administrator* operator group) and regular operators when they are logged in.
