{
  "hero": {
    "title": "Encryption and your website's security"
  },
  "title": "Encryption and your website's security",
  "summary": "Uptrends uses advanced encryption standards to protect your sites usernames and passwords. ",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/encryption-and-your-websites-security",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/encryption-and-your-websites-security"
}

Your website's security is important, and Uptrends doesn’t take security lightly. We handle the usernames and passwords you provide carefully. We encrypt sensitive data right away before we store your data in our database, and we tightly control the access to the encrypted version of the data within our organization.

## How we protect your data

Our system uses the [Rijndael](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) (also known as **Advanced Encryption Standard**) algorithm for encrypting sensitive data. In doing so, we use [PBKDF2](https://en.wikipedia.org/wiki/PBKDF2) (following RFC 2898) to generate the encryption key we need to perform the encryption. We use 256-bit cryptographically secure random values to generate the salt- and IV-values that we need to generate the encryption key and perform the encryption. Lastly, all communication between Uptrends’ subsystems happens over encrypted and authenticated connections.

## What you can do

Besides encryption and access policies on our side, we also encourage our customers to take security measures on their side.

### Limit access rights

Limit any access rights you provide us through the login credentials. Ideally, the login accounts specified in transactions and other monitor types should have minimal access rights. Give these logins just enough privileges to perform the required checks.

### Use separate Login accounts

We also advise you to create separate login accounts in your system with the only purpose of performing monitoring tasks. You may want to whitelist those accounts with respect to the locations ([IP addresses]({{< ref path="checkpoints" lang="en" >}}), i.e. the addresses of Uptrends' checkpoint servers) that you allow to use those credentials.

### Monitor login behavior

If your systems use logging to track the behavior of each logged in account, it's generally a good practice to monitor that behavior. Observe the behavior to ensure that the test accounts don’t do anything you didn't intend.

### Remember to update passwords

Lastly, remember to update the passwords in your monitoring setup and transaction monitoring scripts (see [Changing Transaction Values]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="en" >}})) if your security policy forces them to expire on your own backend. Keeping your passwords updated prevents your monitors from reporting unnecessary errors.

## Partners in security

With our ongoing commitment to security and your active participation in using these security measures, we’re working together in the best possible way to keep vulnerabilities to a minimum.
