{
  "hero": {
    "title": "Main settings for operators"
  },
  "title": "Main settings for operators",
  "summary": "Each operator needs to be set up properly with contact, login information and access rights or time and language settings.",
  "url": "[URL_BASE_TOPICS]account/users/operators/main-settings",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When you have [added an operator]([LINK_URL_1]) you have to configure a few settings, starting with settings on the [SHORTCODE_1] Main [SHORTCODE_2] tab of the operator page. The options are described in this article. You have to have administrator rights to add and configure operators.

## Login information [ANCHOR_1]
Login information is provided during operator setup. Learn more in our KB article [Add or delete an operator]([LINK_URL_2]).

## Language settings [ANCHOR_2]
The **Language** is configured during account setup. The language, as specified in the account settings, will be displayed, and used by default. If you want to override the account language, select **Override account language** and choose another language in the pull-down menu.

## Operator role [ANCHOR_3]
The **Operator role** setting can be used to indicate the role that specific operators have within the company, for internal reference. A special role is the *User for alert routing*, which can be used as a flag to indicate that that particular operator is to be used only to receive, parse, and process alerting emails. 

## Newsletter subscription settings [ANCHOR_4]
The **Newsletter subscription** options allow operators (and administrators) to configure which types of emails are to be received. The individual options are to enable the receiving of *feature updates*, which are general messages regarding newly released or updated features, and *checkpoint updates*, which contain updates regarding our [checkpoint network]([LINK_URL_3]) (new checkpoints added, old ones removed, changes in IP addresses, etc). 

By default, operators will receive feature update emails, while the checkpoint updates are only sent to [account administrators]([LINK_URL_4]) and operators marked as [technical contact]([LINK_URL_5]).

## Default dashboard [ANCHOR_5]
The **Default dashboard** is configured as [SHORTCODE_3] as specified by your administrator [SHORTCODE_4] during account setup but can be changed by choosing another dashboard in the pull-down menu.

Learn more about dashboards in our KB article [Dashboards and public status pages]([LINK_URL_6]).

## Time zone settings [ANCHOR_6]
During the Uptrends account setup (when logging in for the first time) the [time zone]([LINK_URL_7]) has been set for the entire account. This setting applies to all operators that are added to the Uptrends account. You can find the time zone setting in [SHORTCODE_5] Account setup > Account settings [SHORTCODE_6]. 


If you have an [Enterprise account]([LINK_URL_8]), you have the option to introduce an additional time zone to individual operators. This is handy for operators that work in a different time zone than the default time zone in your Uptrends account.

In the **Timezone settings** choose the option *Additional timezone* and choose the appropriate time zone from the list. Then click the [SHORTCODE_7] Save [SHORTCODE_8] button to activate this option.

Now the operator can see this extra information for timestamps:

- Within any monitor check detail, both timestamps based on the default and additional time zone will be shown.
- In the **Monitor log** dashboard (go to [SHORTCODE_9] Monitoring > Monitor log [SHORTCODE_10]), when you hover over the timestamp of a log entry, the timestamp in the additional time zone will be shown.

## Phone settings [ANCHOR_7]
A mobile phone number is provided during operator setup. Read more in our KB article [Add or delete an operator]([LINK_URL_9]).  