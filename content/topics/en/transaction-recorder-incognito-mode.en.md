{
  "hero": {
    "title": "Transaction Recorder incognito mode"
  },
  "title": "Transaction Recorder incognito mode",
  "url": "/support/kb/synthetic-monitoring/transactions/transaction-recorder-incognito-mode",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-recorder-incognito-mode",
  "tableofcontents": false,
  "sectionlist": true
}

{{< callout >}} **Note**: It's always recommended to use the Transaction Recorder in incognito mode to achieve a seamless recording experience. Simply toggle a button to prevent the recorder from using  cookies, saved information, and cached data. {{< /callout >}}

The **Uptrends Transaction Recorder** is a helpful tool for monitoring user interactions and the overall flow of activities performed on your website. These include activities such as logging in, filling out forms, and adding items in a shopping cart. Monitoring such activities entails recording your transaction flows as smoothly as possible, without adding any type of saved information from your website that may add confusion to your desired flow.

Uptrends can definitely help you achieve a seamless recording experience! By running the recorder in incognito mode, you can prevent cookies, site data, and cache used from previous sessions to keep popping up in your recordings.

Using incognito mode improves the quality of your transaction recordings. Here are some common scenarios:

- Testing multiple login sessions — using incognito mode is recommended if you're testing a website that needs access to different user accounts (for example, testing an account as a default user versus a user with admin access). Running the recorder in incognito mode prevents issues such as incorrect user interface (UI) displays, overlapping user features, and authentication errors.

- Auto-populating data forms —
in cases where you want to fill out forms from scratch, incognito mode allows all your cookies (a piece of data saved from your web browser) and other saved information to be ignored when the recording starts. If you want to test an error message when inputting an incorrect email, you may do so without having a suggested list of texts from your previous browser sessions. Running in incognito mode will give you a smoother and easier experience to validate and test form scenarios.

- Testing translated or personalized websites —
use the recorder in incognito mode to efficiently test websites with personalization settings and translated contents. This allows you to easily redirect from one page to another without opening and closing multiple windows, navigating through different web browsers, and resetting cache manually.

- Forgetting to record the user's flow of interaction in the website —
there are also cases where you quickly navigate to a website > click the *Accept cookies* option > log your credentials and perform normal user activities. However, you realized you haven't pressed the *Start recording* button in the Transaction Recorder.
    - If your recorder runs in a normal browser and you just started recording after all those steps, your recorder will recognize you as a logged-in user and you need to adjust and start everything again. 
    - But if your recorder runs in incognito mode, your recorder will not recognize you as a logged-in user. It will not track cookies, allowing you to start the recording from where you left off.

### Enable the incognito mode option

As a prerequisite, ensure you have successfully [set up]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}}) the *ITRS Uptrends Transaction Recorder* browser extension.

To run the Transaction Recorder in incognito mode:

1. Open Chrome.
2. Navigate to *chrome://extensions/*.
3. Search for *ITRS Uptrends Transaction Recorder*.
4. Click the {{< AppElement type="buttonSecondary" >}}Details{{< /AppElement >}} button.
5. Scroll until you see the *Allow in Incognito* option, then toggle the switch button to enable the Transaction Recorder to run in incognito mode.

### Helpful links

To learn more:

- [What are Transaction monitors?]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="en" >}})
- [How to download and use the Transaction Recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="en" >}})
- [Step-by-step instructions to use the Transaction Recorder]({{< ref path="/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction" lang="en" >}})