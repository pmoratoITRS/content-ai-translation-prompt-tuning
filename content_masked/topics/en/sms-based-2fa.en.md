{
  "hero": {
    "title": "SMS-based 2FA"
  },
  "title": "Working with SMS-based 2FA in transactions",
  "summary": "Learn how to set up SMS-based 2FA for your transaction monitors.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/sms-based-2fa",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In a world where security and personal data protection are becoming increasingly more important, many organizations no longer want to rely on just one single login action for securing access to web applications. To increase the chance that a genuine user can be safely identified during a login process, web applications now use multi-factor authentication (MFA), often implemented as 2-factor authentication (2FA) by asking the user to provide two proofs of identity. 

The most common ways for proof of identity, alongside the normal username/password combination, are based on sending a unique code through email, SMS (mobile text) or a mobile authenticator app.

This additional human interaction offers an extra challenge for automated testing of the web application. This article discusses the approach that Uptrends currently supports for SMS-based 2FA as part of the Uptrends transaction monitoring. 

[SHORTCODE_1] **Note**: MFA implementations that rely on authenticator apps are [also supported]([LINK_URL_1]). [SHORTCODE_2]

## Normal flow of an SMS-based 2FA scenario
The flow we expect to see during the 2-factor authentication procedure using an SMS message in a web application is as follows:

1. After navigating to the login page of the application, a user types their login credentials into the text fields of the login page. This part is the first identification step of 2FA.
2. This login attempt should trigger the underlying system to send an SMS message to the mobile phone number that has been preconfigured for the user.
3. While the SMS message is being sent, the web application navigates to a new page containing a text field, awaiting further user input.
4. When the user receives the SMS message on their mobile phone, they will see a unique code that should be typed into that new web page. This part is the second identification step of 2FA.
5. When everything matches correctly, the user will be allowed to enter the web application.
6. Once logged in fully, the user completes their task in the web application.

## Overview of the Uptrends solution for SMS-based 2FA
Rather than using a physical mobile phone, Uptrends will arrange a virtual phone number that will be used to receive SMS messages. A few simple manual steps are required at the Uptrends side to set up the SMS component of the 2FA process. 

One of the actions in the transaction script will be to wait for the incoming SMS message. Once received, the unique code (usually a 6-digit numeric code, but other formats are supported too) will be extracted and can be used to enter in the appropriate text field. This entire process is an exact simulation of what a normal user would do, making it a very good solution for end user testing.

## Steps for setting up SMS-based 2FA in a transaction
1. During the setup stage for creating the transaction, some initial discussion and manual preparation is needed. [Contact support]([LINK_URL_2]) to get started.
2. No physical mobile phone is used. Instead, a new virtual phone number is requested from our partner, Twilio. To do this, we need to determine in which country that phone number should be registered.
3. Once registered, the new mobile phone number needs to be preconfigured in the user profile in the target application. Additionally, the user profile may need to be marked as requiring SMS-based 2-factor authentication.
4. Before Uptrends starts working on building the transaction, it makes sense to perform a manual test first to see whether the setup works correctly and actually triggers an SMS message that can be received by the Uptrends system.
5. When we have established that the SMS communication works reliably, Uptrends Support will build a transaction (typically based on a transaction recording created by using our [Transaction Recorder browser plugin]([LINK_URL_3])).

![An SMS-based 2FA action in a transaction script]([LINK_URL_4])

6. Once the transaction has been tested and put into production, the transaction can be maintained and updated freely without outside help from Uptrends Support, even though the Support team is always happy to help.



## Cost
The [normal cost for a transaction]([LINK_URL_5]) applies; this cost is based on the number of actions that will cause the browser to navigate to a new page. On top of the normal cost, one additional transaction credit will be counted for the wait-for-SMS action. 

## Caveats
Some 2FA systems don't fire an SMS message on every login attempt. Our advice is to use a configuration that shows consistent behavior for every check. This makes the transaction script more predictable, and greatly increases the chance that a problem in the 2FA system is spotted as quickly as possible.

When a dedicated phone number is registered, it is always meant to work for **one single transaction**. If 2FA needs to be used in multiple transactions, a separate phone number will be required for each transaction. The reason for this is that the transactions will be executed in parallel, possibly simultaneously, and it's impossible to determine which SMS message is related to which transaction, if they were all sent to the same phone number.