{
  "hero": {
    "title": "Operator groups"
  },
  "title": "Operator groups",
  "summary": "Having trouble setting up your operator groups? Learn how other Uptrends users have organized their groups.",
  "url": "[URL_BASE_TOPICS]account/users/operators/operator-groups",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When setting up your [operators]([LINK_URL_1]) in your Uptrends account, you may find it useful to create custom operator groups. Operator groups make it easier for you to assign access to custom reports and comes in handy when [setting up your alert definitions]([LINK_URL_2]). In this article, you will find information about the two operator groups already included in your account and some examples of how to organize your operator groups.

Operator groups are the place where you grant permissions to users within the Uptrends app. Check out the article [Permissions]([LINK_URL_3]) to learn more.

## Adding an operator group

To add a new operator group:

1. Go to [SHORTCODE_1] Account setup > Operators, groups (and sub accounts) [SHORTCODE_2] to open the User management hub]([SHORTCODE_7]).
2. Click the [SHORTCODE_3] Add operator group[SHORTCODE_4] button.
3. Enter a name for the operator group in the **Description**.
4. Use the tree view **Operators contained in this group** to add or remove operators by (de)selecting the box in front of the name. Note that an operator can be member of several groups.
5. When you are done with adding operators to the group, click the [SHORTCODE_5] Save [SHORTCODE_6] button.

## The Everyone and Administrators operator groups

You start out with two operator groups: Everyone and Administrators. These two special groups serve two very different functions.

### Everyone

The Everyone group is just what it says, everyone. All operators set up on your account will appear in this group. You cannot edit the Everyone operator group. Use this group when you want to set access rights across all of your operator groups.

### Administrators

If you add an operator to this group, you give the operator full rights to access every aspect of your Uptrends account. These operators can modify monitors and dashboards, add and remove operators, define and alter alert definitions, adjust account settings, and they can see billing and request quotes for additional SMS credits and monitors. Add users to this very exclusive group with care.

## Custom Groups

If you're stuck, and you just can't think of a way to organize your operators, take a look at how some of our other Uptrends users have used groups in their accounts.

### Using your org chart

You probably have a great example of how to define your operator groups using your company’s org charts. We frequently see operator groups based on department or teams. For example, you may want to create an operator group for your DevOps team, support team, or management team. You may want to break those department-based groups into teams, for example, support: first shift, support: second shift, and support: third shift.

### By operator function

You may find it useful (especially for alerting) to create operator groups based on the operator’s function. For example, it doesn’t do you much good to assign API related issues to your web designer, so instead, you can create an API operators group so that you can send alerts relating to your API directly to the team that can fix them. The same goes for database issues, performance issues, and network infrastructure issues.

### Response/support level

When setting up your alert definitions, you may want to create groups based on response levels. For example, set up first, second, and third level support operator groups. Coupled with off-duty schedules and alert escalations, your on-call support person at each level will receive the alert as the issue escalates.

### Vendors and Customers

You may want to create groups based on vendors and customers you have given access to your Uptrends reports. Perhaps you have an agreement with your CDN provider to respond directly to CDN related issues. Also, customers that rely on your services may require insight into your availability and performance by having direct access to your reports. Placing these special operators into their own operator groups can make managing access easier.
