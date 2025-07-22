{
  "hero": {
    "title": "Two-factor authentication setup"
  },
  "title": "Two-factor authentication setup",
  "summary": "How to setup two-factor authentication (2FA) with time-based one-time passwords (TOTP) for Uptrends.",
  "url": "[URL_BASE_TOPICS]account/settings/2fa-setup",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

For setting up two-factor authentication in Uptrends an account administrator first needs to configure the account-wide default setting. After that the operator main settings can be overridden individually if so configured. An authenticator app of choice can be used.  

## Enabling account-wide default login options 
This setting can only be configured by account administrators. 

In Uptrends, go to [SHORTCODE_3] Account setup > Account settings [SHORTCODE_4] and check one of the options at **Two-factor authentication setting**. 

![screenshot 2FA account setting]([LINK_URL_1])
  - **Required** - [Basic operators]([LINK_URL_2]) are required to use two-factor authentication using a time-based one-time password.
  - **Optional** - Basic operators can choose whether to use two-factor authentication using a time-based one-time password.
  - **Disabled** - Two-factor authentication using a time-based one-time password cannot be used within the whole account.

## Two-factor authentication settings for operators
After configuring the default login options for operators, choose a login option on the [SHORTCODE_5] Main [SHORTCODE_6] tab of the operator page, in the section **Login options for this operator**. Here the default status of two-factor authentication in your account is displayed and the option of overriding the default account-wide settings for two-factor authentication for this specific operator. (Still, this setting can only be configured by account administrators.)

![screenshot 2FA operator login options]([LINK_URL_3])
At **Two-factor authentication setting** check the **Override two-factor authentication settings** to override the settings if needed. 
-	**Required** - Two-factor authentication must be used. The setup will be triggered during the operator's next login. 
-	**Optional** - Two-factor authentication can be set up manually on this screen.
-	**Disabled** - Two-factor authentication cannot be used.

To clear the two-factor authentication configuration and set it up again click the [SHORTCODE_7] Reset two-factor authentication [SHORTCODE_8] button.

[SHORTCODE_1]
**Note:** Two-factor authentication with time-based one-time passwords does not work in combination with [Single Sign-on (SSO) in Uptrends]([LINK_URL_4]). 
[SHORTCODE_2]

There are several ways for an administrator or operator to enable or trigger setting up two-factor authentication:

### Operator settings
In Uptrends, navigate to the [SHORTCODE_9] Main [SHORTCODE_10] tab of the operator page. You can do this by clicking on the operator’s name located at the bottom of the main menu and selecting  [SHORTCODE_11] User Settings [SHORTCODE_12]. Next, click [SHORTCODE_13]  Scan QR code [SHORTCODE_14] to set up two-factor authentication. A popup window will open.

Use an authenticator app of your choice to scan the QR code. If you can't scan it, switch to manual input by clicking the link under the code. Click [SHORTCODE_15] Next [SHORTCODE_16] and fill in the 6-digit code provided. After clicking [SHORTCODE_17] Finish [SHORTCODE_18] the two-factor authentication has successfully been set up. 

### By operator invitation
When an operator required to use two-factor authentication is [invited to Uptrends]([LINK_URL_5]) the process to set up two-factor authentication will be part of accepting the operator's invitation. The authentication process is the same, with an authenticator app of choice providing a time-based one-time password. 

### By email link
After logging in, an operator required to use two-factor authentication will be presented with a page notifying them of an email. That email message contains a link to a page within Uptrends where two-factor authentication can be enabled. After that the operator will be logged in. The operator will need to login with a time-based one-time password from that moment on.