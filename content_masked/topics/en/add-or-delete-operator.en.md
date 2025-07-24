{
  "hero": {
    "title": "Adding or deleting an operator"
  },
  "title": "Adding or deleting an operator",
  "summary": "Adding and setting up or deleting an operator. Each created operator needs to be set up properly with contact, login information and access rights.",
  "url": "[URL_BASE_TOPICS]account/users/operators/add-or-delete-operator",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In Uptrends the [User management hub]([LINK_URL_1]) is the place to start for managing operators (and operator groups). 

## Adding an operator

1. Navigate to the [User management hub]([LINK_URL_2]). Go to [SHORTCODE_3] Account setup > Operators, groups (and sub accounts) [SHORTCODE_4].
2. Click the [SHORTCODE_5]Add operator[SHORTCODE_6] button.
3. Under **Operator setup** you can decide, whether you set up the new operator manually (within the Uptrends app) or send an [invitation]([LINK_URL_3]) and leave it to the new operator to fill in their own credentials. 
4. If you have chosen *Manual account setup* you can now add your new operator’s e-mail address, password, full name, backup e-mail address and mobile phone number (start with a \+ sign and your country code, followed by the number with no dashes or spaces). 
5.  Once you are done configuring your operator, click the [SHORTCODE_7]Save[SHORTCODE_8] button.
6. Communicate the password to the operator afterwards. There is no email sent automatically with a manual account setup.


For more information about all the options in the operator's setup, check out the articles in [Operators and operator groups]([LINK_URL_4]). 
### By invitation  [ANCHOR_1]

The invitation is sent by email, using the *Email* setting of the **Login information** and it contains a link, which the new user can click to set their password. The invitation is valid for 21 days. After that, the link in the invitation expires. 

You can resend an invitation, for example if you want to send the new operator a reminder that they still have to activate their account or in case the invitation has expired.

On the operator settings page you can see the status of the invitation. 

Another option to check the status of the invitation is to look on the operators page, which you find by going to [SHORTCODE_9] Account setup > Operators, groups (and sub accounts) [SHORTCODE_10].  Click the [SHORTCODE_11]View all operators[SHORTCODE_12] button. The operators page has a column showing information about the user's last login and the status of (pending) invitations. It is called *Last login* and can have the values:

   - Timestamp of the last login — The account was activated and used.
   - Invited — The invitation was sent and is still valid.
   - Invitation expired — The invitation was sent but 21 days passed before the user clicked the link in the email.
   - None — The invitation was accepted by clicking the link, but the user hasn't logged in since then.


[SHORTCODE_1] **Note**: Operators that use single sign-on (SSO) can be added by invitation only if both the username/password and the SSO login options are enabled. [SHORTCODE_2]

## Deleting an operator

To remove an operator:

1. Navigate to the [User management hub]([LINK_URL_5]). Depending on your account type, the route to get there may vary slightly.
  - For **Enterprise** accounts, go to [SHORTCODE_13] Account setup > Operators, groups and sub accounts [SHORTCODE_14].
  - For all other account types, go to [SHORTCODE_15] Account setup > Operators and groups [SHORTCODE_16].

2. Click [SHORTCODE_17] View all operators [SHORTCODE_18] to open the complete overview of operators in your account.
3. Locate the operator you wish to delete in the list and click on their name. Optionally, enter (a part of) the name or email address in the filter search box to filter the results.
4. In the operator settings, click [SHORTCODE_19] Delete this operator [SHORTCODE_20] in the bottom left corner of the screen.

The operator will now be removed. Note that you can only remove an operator if they are not attached to or own any dashboards, public status pages, or scheduled reports within the account. Generally, if an operator has created such a thing, they are automatically its owner. In such cases, you can remove these objects or reassign ownership, or [contact support]([LINK_URL_6]).