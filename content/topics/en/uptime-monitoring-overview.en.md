{
  "hero": {
    "title": "Uptime Monitoring overview"
  },
  "title": "Uptime Monitoring overview",

  "summary": "Which kind of uptime monitors does Uptrends provide and how can you set them up?",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview",
  "tableofcontents": true,
  "sectionlist": true
}

**Uptime monitors** are one of the several [monitor types]({{< ref path="support/kb/basics/monitor-types" lang="en" >}}) Uptrends offers. Uptime monitors do basic checks such as checking the website's availability, page content, and load time.

In the background process, this monitor gets your website's URL and sends a request to that URL. This monitor expects a response, retrieving all your website's page source (HTML document) and a response status code 200. Once these requirements are satisfied, your website is considered reachable and running as expected.

## Uptime monitor types

There are several Uptime monitor types that you can choose from:

### HTTP and HTTPS monitors

An **HTTP** monitor type checks the Uptime of HTTP websites, while the **HTTPS** monitor checks both the Uptime of HTTP and HTTPS (websites secured with an SSL certificate) websites. 

Recently, the **HTTP** monitor type is no longer available for new users. Uptrends extended the functionality of **HTTPS** monitors to cater to and check the availability of HTTP websites. For more information, see [HTTP and HTTPS Monitors Overview]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/http-and-https/http-and-https-overview" lang="en" >}}).

### Network server monitors {id="network-server-monitors"}

There are two main network server monitors that you can choose from:

- **Ping**  — checks the availability and uptime of any IP address reachable outside your firewall.  
- **Connect**  — checks the availability and uptime of your network by performing a low-level TCP connection to a specific port.

For more information, see [Network checks overview]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/network-checks" lang="en" >}}) and [Setting up a network check monitor]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/network-checks" lang="en" >}}).

### Database server monitors

Uptrends offers two main monitor types, **Microsoft SQL** and **MySQL**, to check the availability and uptime of specific databases. For more information, see [Database server monitors]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/database-server-monitors" lang="en" >}}).

### Mail server monitors

Uptrends offers three main mail server monitors that you can choose from:

- Simple Mail Transfer Protocol (SMTP)
- Post Office Protocol (POP3)
- Internet Message Access Protocol (IMAP)

For more information, see [Mail server monitors]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/mail-server-monitors" lang="en" >}}).

### Advanced availability monitors

Uptrends offers more advanced availability monitors used for data transfers:

- File Transfer Protocol (FTP) and Secure File Transfer Protocol (SFTP) — checks the availability and uptime of your [FTP and SFTP monitors]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/ftp-and-sftp" lang="en" >}}).
- A Domain Name System (DNS) — checks if the DNS configuration runs and is available as expected.
- A Secure Sockets Layer (SSL) certificate — checks if your SSL certificates are always valid and not expired.

## Credits

Uptime monitors use Uptime credits to let you create and schedule monitors for execution. Uptrends uses credits to calculate the pricing for different monitoring services. For more information, refer to the [credits]({{< ref path="/support/kb/account/payments-and-subscriptions/adding-extra-monitors-and-sms" lang="en" >}}) knowledge base article.