{
  "hero": {
    "title": "Mail server monitors"
  },
  "title": "Mail server monitors",
  "summary": "With Uptrends' SMTP and POP3 monitors, you will be the first to know about problems with your email servers.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/mail-server-monitors",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

You have heard the the old postal system saying, "Neither snow nor rain nor heat nor gloom of night stays these couriers from the swift completion of their appointed rounds." Mail is important to you and your business, but equally important is the health and availability of your email servers. If your email server goes down for even a short amount of time, the outage could cost your business in productivity, reputation, and lost revenue. With Uptrends, you can monitor SMTP, POP3, or IMAP mail servers and make sure your team knows the instant your mail servers experience problems.

## Availability monitoring

Besides server crashes, DNS issues or other configuration issues may cause your mail servers to stop functioning properly. With mail server monitors, you will know instantly when a problem has occurred.

## Performance monitoring

Many things can affect performance including network traffic and failing hardware. By setting up response time alerts, you can know exactly when your mail servers start to experience problems.

## Setting up a mail server monitor

Setting up your mail server monitors isn't much different than setting up your other monitor types. For a review on how to set up a new monitor, visit the article [Adding monitors]([LINK_URL_1]). To set up a mail server monitor:

1.  Click the + button in the menu [SHORTCODE_1] Monitoring > Monitor setup [SHORTCODE_2]. 
2.  Select either SMTP, IMAP, or POP3 from the **Type** box.
3.  Give your monitor a **Name**.
4.  Set the **Check interval**.
5.  Select the **Enabled** and **Generate alerts** check boxes, if not already selected.
6.  Provide either the IP address or the domain name for your mail server in the **Network address** box.
7.  Verify that the **Port** number is correct.
8.  Click [SHORTCODE_3]Save[SHORTCODE_4].

With this basic setup, Uptrends will generate alerts if your server ever becomes unavailable. You can also use the [SHORTCODE_5] Error conditions [SHORTCODE_6] tab to set alerts for response time, and you can provide authentication information on the [SHORTCODE_7]Advanced[SHORTCODE_8] tab if you would like Uptrends to attempt to log into the server (learn how [Uptrends protects your authentication information]([LINK_URL_2])).
