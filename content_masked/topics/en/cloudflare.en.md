{
  "hero": {
    "title": "Using Uptrends and Cloudflare together for maximum security"
  },
  "title": "Using Uptrends and Cloudflare together for maximum security",
  "summary": "Find out how Cloudflare and Uptrends work in general and what you need to consider when using both. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/cloudflare",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

You may be using the services of Cloudflare to secure and protect your websites and APIs. As part of those services, Cloudflare will block any incoming traffic from malicious users who are using automated tools or bots (sometimes as part of a bot network) to gain access to resources provided by your sites and APIs. 

Cloudflare uses various technologies such as Rate Limiting, IP and Country blocking, Anti-DDoS technology, and CAPTCHA to help verify requests from legitimate users and block those from automated bots. 

Cloudflare also provides a Verified Bot service that allows you to designate specific bots that should be granted access to your websites and APIs. This service will ensure that requests from the designated bots are verified and allowed through, while all other bots will be blocked, providing additional security for your sites.

## Uptrends is a verified bot

The monitoring activities performed by Uptrends to test the availability and performance of your web pages, user journeys and APIs are in fact bot activity: Automated processes are used to continually access your web servers. 

Uptrends is one of Cloudflare’s verified bot partners. Cloudflare is aware of Uptrends’ public monitoring locations — the checkpoint network — and they regularly refresh the list of IP addresses (IPv4 and IPv6) from which monitoring on your sites takes place.

This means that by configuring Cloudflare and Uptrends together, your website and API resources are protected from malicious bots while monitoring traffic from Uptrends is allowed through the Cloudflare firewall.

## The verified bots list

As part of Cloudflare Radar, a curated list of bots is published as the [Verified bots list]([LINK_URL_1]). All legitimate services may apply to be included in the list of bots that are trusted by Cloudflare. 

Uptrends went through the application process and Cloudflare has confirmed that Uptrends is a fully verified bot. Unfortunately, Cloudflare only publishes a part of their verified bots on their verified bots list and while Uptrends is a fully verified bot, you won't find it on that list.

## Troubleshooting

Despite Cloudflare’s confirmation that Uptrends is a verified bot, and that the checkpoint servers’ IP addresses are whitelisted at Cloudflare, some Uptrends users are still reporting problems from time to time. 

When Cloudflare happens to block incoming traffic that originates from one of the checkpoint locations, it will appear as though your site is not available — from a monitoring perspective. 

When you encounter unexpected outages that may be caused by Cloudflare blocking incoming traffic from Uptrends, please follow these steps:

- Review the Cloudflare documentation on [How to manage good bots]([LINK_URL_2]). This article explains allowlists, blocklists, and how to set up rules for bots accessing a website or application.

- Take note of checkpoint locations that are having trouble accessing your site or API, and which aren’t. Then, submit a ticket to [Uptrends Support]([LINK_URL_3]) with this information. This will help us identify if the issue is related to Cloudflare whitelisting or from a different cause.

- Reach out to [Cloudflare Support]([LINK_URL_4]) if you are trying to make configuration changes to your Cloudflare firewall rules. Ensure that you read the Cloudflare documentation on [Firewall rules actions]([LINK_URL_5]).

We are actively working with Cloudflare to resolve these issues, and your input is needed to help us understand more the root cause.