{
  "hero": {
    "title": "Database server monitors"
  },
  "title": "Database server monitors",
  "summary": "Uptrends supports two types of database server monitors: MySQL and Microsoft SQL Server.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/database-server-monitors",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Unless you're serving up a static brochure website, your website or web service depends on a database to retrieve content, manage users, or process orders. Knowing your database response times can help you avoid catastrophe. Using Uptrends' database server monitors, you can always know when your database is in trouble.

Uptrends will use its {{% Features/Variable variable="CheckpointCount" %}} checkpoints to monitor your database server externally.

[SHORTCODE_1]
**Note**: If your database doesn't have Internet exposure, you can't use this monitor type. However, you can monitor servers behind your firewall with [Uptrends Infra]([LINK_URL_1]).
[SHORTCODE_2]

## How does database monitoring work?

With Uptrends' database monitoring, you can monitor Microsoft SQL Server or MySQL. The Uptrends checkpoints will attempt to establish a connection to the IP address and database you specify on the [SHORTCODE_5]Advanced[SHORTCODE_6] tab, and if you provide login credentials, the checkpoint will attempt a successful login. Besides the response times you specify on the [SHORTCODE_7]Error conditions[SHORTCODE_8] tab, Uptrends will trigger an alert for failed or lost connections.

[SHORTCODE_3]
**Note:** Concerned about security and sharing your database authentication information? Read up on how Uptrends keeps your login credentials safe: [Encryption and your website's security]([LINK_URL_2]).
[SHORTCODE_4]

A database monitor type will send you alerts based on response time and connectivity issues. You will find the database server monitor setup similar to setting up an HTTPS monitor type with just a couple special fields. For information about setting up monitors and error conditions, visit the [knowledge base]([LINK_URL_3]). For a database monitor you will need to know:

- Database name
- Database URL or IP
- Database login credentials (if needed)

## Setting up a database monitor

To set up a database monitor

1. Click the + button in the menu [SHORTCODE_9] Monitoring > Monitor setup [SHORTCODE_10]. 
2. Select either **Microsoft SQL Server** or **MySQL** under **Database Servers** in the **Type** box.
3. Type the domain name or IP address for the database server in the **Network Address** box.
4. Complete the other fields on the [SHORTCODE_11]Main[SHORTCODE_12] tab.
5. Set your expected response times on the [SHORTCODE_13]Error conditions[SHORTCODE_14] tab.
6. Click the [SHORTCODE_15]Advanced[SHORTCODE_16] tab.
7. Provide a **Username** and **Password** if necessary.
8. Provide the **Database name**.
9. Choose your checkpoints on the [SHORTCODE_17]Checkpoints[SHORTCODE_18] tab.
10. Click [SHORTCODE_19]Save[SHORTCODE_20].
