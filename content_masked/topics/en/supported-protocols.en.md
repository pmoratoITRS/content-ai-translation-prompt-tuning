{
  "hero": {
    "title": "Supported protocols"
  },
  "title": "Supported Protocols",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/supported-protocols",
  "summary": "A list of protocols supported by Uptrends.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Supported Protocols

Are you wondering if Uptrends supports the protocols you need to monitor your websites, servers, web applications, and other web services? **Answer**: You bet we do!

**Uptrends supports**: *HTTP*, *HTTPS*, *SMTP*, *POP3*, IMAP, *Ping*, *DNS*, *FTP*, *Connect*, *SQL*, *MySQL*, and more.

## HTTP

#### What is the HTTP protocol?

The **HTTP protocol** is used to view and interact with unsecured web pages. It is the default monitor type in Uptrends, and should be chosen when you need to check a webpage.

#### How does the HTTP protocol work?

First, you will need to [Add a New Monitor]([LINK_URL_1]) (complete with URL for monitoring).

Then, when the monitor executes, the Uptrends service contacts the web address. It checks for common network and HTTP errors, and attempts to download the content of the webpage.

[SHORTCODE_1]
**Note**: This monitor type will only download the HTML content of a page. It does not include any images, scripts, or interactive elements that may be a part of the page. If you are looking to check the complete content of a webpage, we suggest you consider the Full Page Check monitor type.
[SHORTCODE_2]

#### Can I monitor more with the HTTP protocol?

Yes! In addition to the simple checks listed above, you can also check for:

**Load times**:

When you set time limits, we will check that the total amount of time it takes to load the web page, is within those limits. In other words: we can check that your web page loads as quickly as you expect.

**Size**:

We can test that the downloaded content is larger than the minimum number of bytes or characters you specify. This is useful when you want to make sure that a particular file on your web server (a generated image, for example) is not broken or empty.

**Content**:

Uptrends can verify that a particular word or phrase is actually present in the content of the page. This is a powerful way to check that your web page is showing the correct content.

Choose a word or phrase that is an essential part of your page; something that won't be shown in case there is an error. Simply fill in your word or phrase in the Page content match field.

In some cases you might want to check for the absence of a word. You can do this by starting with an exclamation mark. For example, if you want us to verify that the word "error" is NOT present in the content, fill in !error.

## HTTPS

#### What is the HTTPS protocol, and how does it work?

The **HTTPS protocol** is and works exactly the same as HTTP (listed above), except that it can be used for checking a web page secured by an SSL Certificate.

## SMTP, POP3, and IMAP

#### What are the SMTP, POP3, and IMAP protocols?

The **SMTP, POP3, and IMAP protocols** are used for connecting to mail servers to test outgoing e-mail.

#### How do the SMTP, POP3, and IMAP protocols work?

First, you will need to Add a New Monitor, selecting either the SMTP, POP3, or IMAP protocol and filling in the appropriate IP and port information.

As the monitor executes, the Uptrends monitoring service will attempt to reach the IP address. If Uptrends can reach the address, uptime is registered.

[SHORTCODE_3]
**Note**: If you choose to add in the optional username and password (login credentials to your email server), the Uptrends service will also attempt to log in as part of its check test.
[SHORTCODE_4]

## Ping

#### What is the Ping protocol?

**Ping** (or ICMP) is a very simple way to see if a server is still running and reachable.

#### How does the Ping protocol work?

The ping protocol works by sending so-called ICMP Echo requests to see how long it takes for that request to reach the server. You can choose this option if you do not have any other services (web, database or mail) running on that server that are accessible through the internet.

[SHORTCODE_5]
**Note**: Your network or server settings must explicitly allow ICMP requests.
[SHORTCODE_6]

## DNS

#### What is the DNS protocol?

The **DNS protocol** allows for you to monitor the uptime status of the infrastructure that provides your users with a simple way of navigating to your website address. (For example: www.uptrends.com rather than an IP address)

Uptrends is able to monitor local, primary and specific DNS.

#### How does the DNS protocol work?

First, log in, Add a Monitor (DNS), and configure it using the DNS server address (domain name or IP), port number, DNS query type, test value, and expected result.

The most common thing to check is whether your domain name (www\.yourcompany.com) is still pointing to the IP address of your web server. If it fails to do so, your users will likely be unable to find your website. By monitoring this DNS query directly, the Uptrends service will detect any DNS problems, even before your website becomes unavailable to users.

Uptrends' DNS monitor lets you do extensive DNS health checks: verify your web site domain names (A and CNAME records), mail server domain name mappings (MX records), DNS zone delegates (NS records), authoritative information about DNS zones (SOA records) and other DNS information, contained in TXT records (including SPF information for e-mail authentication).

## FTP

#### What is the FTP protocol?

The **FTP protocol** enables you to monitor the availability of your FTP server through the port of your choosing.

#### How does the FTP protocol work?

In order for the FTP protocol to work, you will first need to log in and Add a Monitor (FTP) using the appropriate details.

The Uptrends service will then monitor its status by regularly contacting the FTP server through the appropriate port to ensure that it is operational.

[SHORTCODE_7]
**Note**: It is possible to add login credentials to the monitor, so that you can know that the FTP login functions are working. However, you cannot currently retrieve files from said server with the Uptrends service.
[SHORTCODE_8]

## Connect

If no other protocol is suitable for your situation, you can use the **Connect protocol** to do a very simple test. If you specify a domain name or IP address of your server or firewall, and a port, we will attempt to open a simple connection to that combination of address and port.

## SQL

#### What is the SQL protocol?

The **SQL protocol** allows you to monitor the uptime of your Microsoft SQL server database.

[SHORTCODE_9]
**Note:** SQL servers can only be monitored if they are directly (and regularly) accessible through the internet.
[SHORTCODE_10]

#### How does the SQL protocol work?

In order to run an SQL monitoring monitor, you will need to first log in and Add a Monitor (SQL) to your account. At a minimum, you will need to specify the IP address of the server and a port (default 1433).

The Uptrends service will then attempt to contact the server in question, reporting back positive if everything is OK, and triggering an unconfirmed (and possibly later confirmed) error if it is unreachable.

[SHORTCODE_11]
**Note**: You can specify a username and password to test your login, as well as a database name so that we can check if the database can be accessed.
[SHORTCODE_12]

## MySQL

#### What is the MySQL protocol?

The **MySQL protocol** enables the Uptrends application to monitor the availability of MySQL databases.

#### How does the MySQL protocol work?

The MySQL protocol works very much in the same way as the SQL protocol, but with MySQL databases! (The default port for connecting to MySQL databases is 3306.)
