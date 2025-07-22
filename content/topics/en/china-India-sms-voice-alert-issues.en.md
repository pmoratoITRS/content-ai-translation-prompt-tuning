{
  "hero": {
    "title": "China and India SMS and voice alert issues"
  },
  "title": "China and India SMS and voice alert issues",
  "summary": "Spam filters and do-not-call registries may block alert messages to some regions, so consider these other options for your operators in China or India.  ",
  "url": "/support/kb/alerting/china-india-sms-voice-alert-issues",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/china-india-sms-voice-alert-issues"
}

Are your operators in China or India not getting their alerts or only getting some of their alerts? Government regulations in China and India's National Customer Preference Register (also known as Do Not Disturb Registry) effectively block some phone calls and text messages.

## Spam filtering in China

China scrutinizes calls and texts originating from outside the country and blocks calls and SMS messages considered as spam as summarized by [Twilio.](https://support.twilio.com/hc/en-us/articles/360016488474-Calling-Limitations-to-China)

"Our network and operating partners must meet rigid standards for terminating calls in China. These standards make call traffic shorter than two minutes and high volumes of calls using the same caller ID undesirable, and non-conforming entities risks a complete and permanent shut-off without warning. To remain in compliance with our partners, Twilio can no longer support low-ACD calling use cases to China going forward. This is a universal behavior for all international traffic terminating to China and is not something unique to Twilio's platform. Additional details are outlined in our FAQ Calling limitations to China."

Several factors to meet China's tough calling and SMS requirements prevent our alert messages from getting through:

- Average call length of two minutes or longer — voice messages coming from Uptrends phone or voice alerting will never meet this requirement.
- Frequent calls that originate from the same number.
- Three text messages sent with the same message constitutes a block. Depending on your escalation settings, reminder messages may exceed the three-message limit.
- Five different messages from the same originating number to a number in China trigger a manual review and 24-hour block of all messages.

As you can see, **SMS messages to numbers terminating in China will not work reliably and possibly not at all, and voice or phone alerts will not work at all.** We strongly recommended that you consider some of our other alerting methods described below.

## India's call and SMS blocking

If your operator in India isn't receiving voice or SMS alert messages from Uptrends, they probably have their number listed on the [National Customer Preference Register](https://www.trai.gov.in/faqcategory/unsolicited-commercial-communicationsucc) (NCPR). The NCPR allows consumers to have calls and SMS blocked based on market sector or block all market sectors. If the operator has registered the number, the operator must wait three months after registering their number to remove the number from the block list.

## Alternatives to SMS and voice alerting in China and India

Uptrends has multiple options beyond SMS and voice alerts for alerting your operators in China and India.

- **Email** — email is an effective alerting tool for on-duty operators.
- [**Integrations**]({{< ref path="/integrations" lang="en" >}}) — if you use Slack, PagerDuty, StatusHub, Splunk On-Call, or ServiceNow you can quickly integrate them with your Uptrends account to send messages to your operators in China and India.
- [**Webhooks**]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="en" >}}) — 
if your third-party service or app can receive and process API message requests, you can get alerting from Uptrends through those services.
- **Push notifications using the Uptrends App** — the [Uptrends App]({{< ref path="/mobile-apps" lang="en" >}}) for iPhone and Android can send push notifications to your operators.
