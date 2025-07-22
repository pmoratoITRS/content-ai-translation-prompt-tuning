{
  "title": "Updates to the transaction recorder",
  "date": "2024-06-12",
  "url": "/changelog/june-2024-transaction-recorder-updates",
  "translationKey": "https://www.uptrends.com/changelog/june-2024-transaction-recorder-updates"
}

We have updated our [transaction recorder]({{< ref path="/features/transaction-recorder" lang="en" >}}), including a graphical overhaul, and several new features. These new features include:

- A new context-sensitive right-click menu in the recorder browser allowing users to add [Hover]({{< ref path="/support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="en" >}}), [Wait for element]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks#wait-for-element" lang="en" >}}), and [Test document content]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks#test-document-content" lang="en" >}}) (when text on the page is highlighted) actions, while making the recording. These actions will no longer need to be added afterwards!
- The ability to add [Key event]({{< ref path="/support/kb/synthetic-monitoring/transactions/page-interactions#key-event" lang="en" >}}) actions directly from the recorder interface. The recorder can not record actions such as pressing the enter key after filling in credentials, but such an action can now be added using the **'+ Add keyboard action'** button in the recorder.

![Right-click menu in recorder](/img/content/scr-recorder-context-menu.min.png)