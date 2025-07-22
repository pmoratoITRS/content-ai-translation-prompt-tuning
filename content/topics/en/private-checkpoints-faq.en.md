{
  "hero": {
    "title": "Private checkpoints FAQ"
  },
  "title": "Private checkpoints FAQ",
  "summary": "Frequently Asked Questions about Uptrends' private checkpoints",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-faq"
}

## Can I have multiple private checkpoints?

Yes, you can. For example, if your company has multiple hosting locations, you can have a [private checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/#user-managed" lang="en" >}}) in each relevant location.

## Can I use my private checkpoint in multiple Uptrends accounts?

Yes, you can. Tell us which accounts you want to use with your private checkpoint, and the checkpoint will be made available for those accounts. Only you will have access to use your private checkpoint.

## Why are there two private checkpoints by default? {id="two-default-private-checkpoints"}

When you create a new [private location]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="en" >}}) two private checkpoints are added to the location by default. 

This is done because in the recommended setup you need two checkpoints set up to have proper availability for your private location. With redundant checkpoints, one checkpoint can be updated while the other one still can do the monitoring for your private location. Also, should one of the checkpoints fail for any reason, the other one can still monitor your websites, services or servers. 

## Can I run transaction monitors on my internal business application?

Yes, you can do exactly that. The Uptrends functionality is available, so you can definitely run transaction monitoring on your internally hosted applications.

## Do I have to create my own transaction scripts?

No, you don't. Just record your [transactions]({{< ref path="features/transaction-recorder" lang="en" >}}) with the transaction recorder Chrome plugin as always, and you can choose if you yourself or our transaction engineers turn your recording into a stable, running transaction.

## Which monitor browser types are supported?

The [Full Page Check (FPC)]({{< ref path="/support/kb/basics/monitor-types#browser-monitors-full-page-check" lang="en" >}}) and [transaction monitors]({{< ref path="/support/kb/basics/monitor-types#transaction-monitors" lang="en" >}}) are supported in private locations.

## How do I prevent screenshots and filmstrips from uploading to the cloud?

Use [data protection]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) to disable the creation of screenshots, filmstrips and error screenshots for an HTTP(S) monitor on your private location checkpoints. 

## How do I troubleshoot?

Use the [Troubleshooting guide]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting" lang="en" >}}) in the Uptrends knowledge base.

## I want to learn more. Whom can I call?

Your Uptrends monitoring consultant is always ready to help you. If you know their number or email address, please contact them directly. If you don't know who your monitoring consultant is or don't have their contact information, please use our [Contact page]({{< ref path="contact" lang="en" >}}) to open a support ticket or call our office at one of our international locations.

## Questions or concerns?

If at any time during the setup process you don't understand something or have a question, please communicate your questions or concerns to Uptrends by [opening a support ticket]({{< ref path="contact" lang="en" >}}). We will get back to you quickly. 