{
  "hero": {
    "title": "Main settings for operators"
  },
  "title": "Main settings for operators",
  "summary": "Each operator needs to be set up properly with contact, login information and access rights or time and language settings.",
  "url": "/support/kb/account/users/operators/main-settings",
  "translationKey": "https://www.uptrends.com/support/kb/account/users/operators/main-settings"
}

When you have [added an operator]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="en" >}}) you have to configure a few settings, starting with settings on the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab of the operator page. The options are described in this article. You have to have administrator rights to add and configure operators.

## Login information {id="logininfo"}
Login information is provided during operator setup. Learn more in our KB article [Add or delete an operator]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="en" >}}).

## Language settings {id="langsettings"}
The **Language** is configured during account setup. The language, as specified in the account settings, will be displayed, and used by default. If you want to override the account language, select **Override account language** and choose another language in the pull-down menu.

## Operator role {id="operatorrole"}
The **Operator role** setting can be used to indicate the role that specific operators have within the company, for internal reference. A special role is the *User for alert routing*, which can be used as a flag to indicate that that particular operator is to be used only to receive, parse, and process alerting emails. 

## Newsletter subscription settings {id="newslettersub"}
The **Newsletter subscription** options allow operators (and administrators) to configure which types of emails are to be received. The individual options are to enable the receiving of *feature updates*, which are general messages regarding newly released or updated features, and *checkpoint updates*, which contain updates regarding our [checkpoint network]({{< ref path="/checkpoints" lang="en" >}}) (new checkpoints added, old ones removed, changes in IP addresses, etc). 

By default, operators will receive feature update emails, while the checkpoint updates are only sent to [account administrators]({{< ref path="/support/kb/account/users/operators/giving-an-operator-administrator-rights" lang="en" >}}) and operators marked as [technical contact]({{< ref path="/support/kb/account/users/operators/permissions#technical-contact" lang="en" >}}).

## Default dashboard {id="defaultdash"}
The **Default dashboard** is configured as {{< AppElement type="dropdown" >}} as specified by your administrator {{< /AppElement >}} during account setup but can be changed by choosing another dashboard in the pull-down menu.

Learn more about dashboards in our KB article [Dashboards and public status pages]({{< ref path="/support/kb/dashboards-and-reporting/dashboards/" lang="en" >}}).

## Time zone settings {id="timezone"}
During the Uptrends account setup (when logging in for the first time) the [time zone]({{< ref path="support/kb/account/settings/timezones" lang="en" >}}) has been set for the entire account. This setting applies to all operators that are added to the Uptrends account. You can find the time zone setting in {{< AppElement type="menuitem" >}} Account setup > Account settings {{< /AppElement >}}. 


If you have an [Enterprise account]({{< ref path="/pricing#plans" lang="en" >}}), you have the option to introduce an additional time zone to individual operators. This is handy for operators that work in a different time zone than the default time zone in your Uptrends account.

In the **Timezone settings** choose the option *Additional timezone* and choose the appropriate time zone from the list. Then click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to activate this option.

Now the operator can see this extra information for timestamps:

- Within any monitor check detail, both timestamps based on the default and additional time zone will be shown.
- In the **Monitor log** dashboard (go to {{< AppElement type="menuitem" >}} Monitoring > Monitor log {{< /AppElement >}}), when you hover over the timestamp of a log entry, the timestamp in the additional time zone will be shown.

## Phone settings {id="phonesettings"}
A mobile phone number is provided during operator setup. Read more in our KB article [Add or delete an operator]({{< ref path="/support/kb/account/users/operators/add-or-delete-operator" lang="en" >}}).  