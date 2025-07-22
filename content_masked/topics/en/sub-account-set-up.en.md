{
  "hero": {
    "title": "Sub account set up"
  },
  "title": "Sub account set up",
  "summary": "In this article we step through the process of setting up a new sub account.",
  "url": "[URL_BASE_TOPICS]account/users/sub-accounts/sub-account-set-up",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Create a sub account

To create a new sub account:

1.  Open the operator hub by going to ([SHORTCODE_5]Account setup > Operators, groups and sub accounts[SHORTCODE_6]).
2.  Click the [SHORTCODE_7]Add sub account[SHORTCODE_8] button in the sub accounts section.

Now, on the tabs on the *New sub account* page you have to add some information for the sub account.

## Main
### Sub account info

1.  Provide a **Sub account name**. On save, this name will also be used to generate a monitor group and operator group.
2.  Include a **Custom reference** (optional).

### Permission

In this section, you decide on whether the sub account operators can modify or add monitors.

1.  Check the **Allow changing monitors** box to allow the operators to adjust monitor settings. Enabling this feature also allows the sub account holders to add additional operators, but they can't delete operators.
2.  Check the **Allow adding monitors** box if you want to allow the sub account operators to set up their own monitors. If allowing them to set up monitors, indicate how many they may add in the **Maximum number of monitors** box.

[SHORTCODE_1]
**Note**: When a sub account adds a monitor, the new monitor is subject to the availability of unused monitors in the primary account. If the primary account doesn't have enough monitors available, the sub account cannot add new monitors even if they haven't reached their maximum number of monitors.
[SHORTCODE_2]

### New monitor info

Creating a sub account requires that you provide information for an HTTP/HTTPS monitor. Select the **Monitor type** and provide a **Monitor URL** for the new monitor. Uptrends will add this monitor to a monitor group with the same name as the sub account.

## SLA

If you have an SLA with the new sub account holder, set the SLA requirements up on the [SHORTCODE_9]SLA[SHORTCODE_10] tab. If you need a refresher on SLA setup, our [SLA section]([LINK_URL_1]) can step you through it.

## Extra monitors

Using the [SHORTCODE_11]Extra monitors[SHORTCODE_12] tab, you can add pre-existing monitors to the sub-account, and you can come back later to add new monitors you may add in the future for the sub account.

## Operators

On this tab you add existing operators to the sub account by selecting them from the list. Sub account operators can only belong to the *Everyone* group and their sub account group.

## Save

Click [SHORTCODE_13]Save[SHORTCODE_14] to create the sub account and the new monitor.

[SHORTCODE_3]
**Note**: If you plan for your sub-account operators to receive alerts, you need to set up a new [alert definition]([LINK_URL_2]), and if you plan on using SMS or phone/voice alerting, you will need to make sure to add mobile phone numbers in their [operator settings]([LINK_URL_3]).
[SHORTCODE_4]
