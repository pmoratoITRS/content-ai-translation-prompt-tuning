{
  "hero": {
    "title": "Two-factor authentication setup"
  },
  "title": "Two-factor authentication setup",
  "summary": "How to setup two-factor authentication (2FA) with time-based one-time passwords (TOTP) for Uptrends.",
  "url": "/support/kb/account/settings/2fa-setup",
  "translationKey": "https://www.uptrends.com/support/kb/account/2fa-setup"
}

For setting up two-factor authentication in Uptrends an account administrator first needs to configure the account-wide default setting. After that the operator main settings can be overridden individually if so configured. An authenticator app of choice can be used.  

## Enabling account-wide default login options 
This setting can only be configured by account administrators. 

In Uptrends, go to {{< AppElement type="menuitem" >}} Account setup > Account settings {{< /AppElement >}} and check one of the options at **Two-factor authentication setting**. 

![screenshot 2FA account setting](/img/content/scr_2fa-authentication-setting.min.png)
  - **Required** - [Basic operators]({{< ref path="/support/kb/account/users/operators/permissions#basic-operator" lang="en" >}}) are required to use two-factor authentication using a time-based one-time password.
  - **Optional** - Basic operators can choose whether to use two-factor authentication using a time-based one-time password.
  - **Disabled** - Two-factor authentication using a time-based one-time password cannot be used within the whole account.

## Two-factor authentication settings for operators
After configuring the default login options for operators, choose a login option on the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab of the operator page, in the section **Login options for this operator**. Here the default status of two-factor authentication in your account is displayed and the option of overriding the default account-wide settings for two-factor authentication for this specific operator. (Still, this setting can only be configured by account administrators.)

![screenshot 2FA operator login options](/img/content/scr_2fa-operator-login-options.min.png)
At **Two-factor authentication setting** check the **Override two-factor authentication settings** to override the settings if needed. 
-	**Required** - Two-factor authentication must be used. The setup will be triggered during the operator's next login. 
-	**Optional** - Two-factor authentication can be set up manually on this screen.
-	**Disabled** - Two-factor authentication cannot be used.

To clear the two-factor authentication configuration and set it up again click the {{< AppElement type="deletebutton" >}} Reset two-factor authentication {{< /AppElement >}} button.

{{< callout >}}
**Note:** Two-factor authentication with time-based one-time passwords does not work in combination with [Single Sign-on (SSO) in Uptrends]({{< ref path="support/kb/account/settings/single-sign-on-overview" lang="en" >}}). 
{{< /callout >}}

There are several ways for an administrator or operator to enable or trigger setting up two-factor authentication:

### Operator settings
In Uptrends, navigate to the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab of the operator page. You can do this by clicking on the operator’s name located at the bottom of the main menu and selecting  {{< AppElement type="menuitem" >}} User Settings {{< /AppElement >}}. Next, click {{< AppElement type="editbutton" >}}  Scan QR code {{< /AppElement >}} to set up two-factor authentication. A popup window will open.

Use an authenticator app of your choice to scan the QR code. If you can't scan it, switch to manual input by clicking the link under the code. Click {{< AppElement type="buttonPrimary" >}} Next {{< /AppElement >}} and fill in the 6-digit code provided. After clicking {{< AppElement type="buttonPrimary" >}} Finish {{< /AppElement >}} the two-factor authentication has successfully been set up. 

### By operator invitation
When an operator required to use two-factor authentication is [invited to Uptrends]({{< ref path="support/kb/account/users/operators/add-or-delete-operator#by-invitation" lang="en" >}}) the process to set up two-factor authentication will be part of accepting the operator's invitation. The authentication process is the same, with an authenticator app of choice providing a time-based one-time password. 

### By email link
After logging in, an operator required to use two-factor authentication will be presented with a page notifying them of an email. That email message contains a link to a page within Uptrends where two-factor authentication can be enabled. After that the operator will be logged in. The operator will need to login with a time-based one-time password from that moment on.