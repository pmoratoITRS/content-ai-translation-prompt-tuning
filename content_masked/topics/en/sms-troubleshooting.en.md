{
  "hero": {
    "title": "SMS troubleshooting"
  },
  "title": "SMS Troubleshooting",
  "summary": "SMS alerts are one of the best ways to stay in sync with the status of your website, servers, and web services.",
  "url": "[URL_BASE_TOPICS]alerting/sms-troubleshooting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

**SMS alerts** are one of the best ways to stay in sync with the status of your website, servers, and web services. If your SMS alerts are failing to be received, that’s a big deal!

Below you’ll find a series of SMS troubleshooting options:

## Altering Additional Senders

If you aren't able to receive test SMS messages, you can try tweaking the following in the Uptrends web application. To do so, follow these steps:

1. At the bottom left part of your screen, click  [SHORTCODE_1] Your profile name > User settings [SHORTCODE_2].
2. Under the [SHORTCODE_3] Main [SHORTCODE_4] tab, scroll to [SHORTCODE_5] Phone settings > SMS provider [SHORTCODE_6].
3. Choose the **Override SMS integration settings** option to edit the next fields.
4. Select a gateway provider from the dropdown menu. Currently, we offer 4 different providers that you can choose from:

- SMS Gateway based in Europe
- SMS Gateway 2 based in Europe
- SMS Gateway based in USA
- International based SMS Gateway

5. Tick the **Use numeric sender** option.

Some providers have issues receiving messages from numeric senders or from alphabetic senders. By default, we use an alphabetic sender.

## Unblocking Via Your Provider

### SPRINT

By default, some phone numbers from SPRINT users may be blocked. But don’t panic! There is a way to unblock your number yourself, by texting **UPTRENDS** to **46786**.

If this action is *successful*, you should start receiving SMS messages as configured in your account.

If this effort *fails*, you will need to contract your carrier directly to get the block removed from your account.

### AT&T

Some AT&T users may have difficulty receiving SMS messages by default, but you can unblock your number by texting **UPTRENDS** to **64085**.

If this *does not work*, please contact your carrier and have them remove the block from your account.

## Known SMS issues for operators

### China and India

Due to spam filters in China and do-not-call registries in India, SMS alerting may not work for operators in these countries. [Learn more]([LINK_URL_1]).

## List of supported countries and providers with Sender ID

Check the Uptrends list of supported countries and gateway providers. The *Numeric Enabled* column indicates whether the *Use numeric sender* checkbox in the Uptrends web application can be enabled or disabled.

If *Yes*, you can tick the *Use numeric sender* checkbox to receive the SMS from a mobile phone number. Otherwise, you'll receive the SMS from the contact **UPTRENDS**. If both *Yes* and *No* are options, choose the one that best suits your needs.

| Phone Code | Country | Gateway | Numeric Enabled |
|--|--|--|--|
| +1 | United States | Gateway based in USA or International | Yes and No |
| +33 | France | Gateway 2 based in Europe | Yes and No |
| +40 | Romania | Gateway 2 based in Europe | Yes |
| +44	| United Kingdom | Gateway 2 based in Europe | No |
| +45	| Denmark	| Gateway 2 based in Europe | No |
| +46 | Sweden | Gateway 2 based in Europe | No |
| +47 | Norway | Gateway 2 based in Europe | No |
| +65 |	Singapore | Gateway 2 based in Europe | No |
| +90 |	Turkey | Gateway 2 based in Europe | No |
| +91	| India	| Gateway 2 based in Europe | No |
| +358 | Finland	| Gateway 2 based in Europe	| No |
| +381 |Serbia |Gateway 2 based in Europe	| No |
| +421 | Slovakia | Gateway 2 based in Europe	| No |
| +998 | Uzbekistan | Gateway 2 based in Europe	| No |

#### Still having trouble?

If you’ve tried these SMS troubleshooting options but are still unable to receive alerts, please contact support by [filing a ticket]([LINK_URL_2]).
