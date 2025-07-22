{
  "hero": {
    "title": "Integrate Uptrends with Zapier"
  }, 
  "title": "Zapier",
  "summary": "Guide on how to integrate your Uptrends alerting into Zapier",
  "url": "/support/kb/alerting/integrations/zapier",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/zapier" 
}

**Zapier** is an online automation tool that connects your apps and services. It allows you to connect your Uptrends alerting to virtually any other application out there. In this guide we'll help you set up your Uptrends integration with Zapier, and where to take your Uptrends data next.

1.  Set up a *When this happens...* action in Zapier
2.  Set up the integration in Uptrends
3.  Test the webhook in Zapier
4.  Set up a *Do This...* action in Zapier
5.  Add the integration to an alert definition in Uptrends

Read on for detailed instructions on how to set up this integration!

## 1. Set up a When this happens... action in Zapier

1.  In Zapier, automated workflows are called *Zaps*. Go to *Zaps* and click *Create Zap.* Alternatively, click the *MAKE A ZAP* button in the top left of the screen.
2.  Give your new Zap an appropriate name.
3.  Select *Webhooks by Zapier*.
4.  Select *Catch hook* and click *Continue*.
5.  Take note of the **Custom Webhook URL** as you will need it to set up the integration on the Uptrends end later.
6.  Click *Continue*.

At this point, Zapier will ask you to test the webhook by sending data to it. In order to do this, we'll first need to set up the Uptrends integration.

## 2. Set up the integration in Uptrends

1.  Go to {{< AppElement type="menuitem" >}}Alerts > Integrations{{< /AppElement >}}.
2.  Click {{< AppElement type="button" >}}Add integration{{< /AppElement >}} at the top right.
3.  Choose Zapier as the integration type.
4.  Specify a name for this integration.
5.  Paste the **Custom Webhook URL** you saved earlier in the corresponding {{< AppElement type="menuitem" >}}Predefined variables{{< /AppElement >}} field.
6.  Click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} to store your settings. The new Zapier integration will appear on the Integrations page.

## 3. Test the webhook in Zapier

1.  Go to the newly created **Zapier** integration in Uptrends.
2.  In the {{< AppElement type="tab" >}}Customizations{{< /AppElement >}} tab, click the {{< AppElement type="button" >}}Send test alert{{< /AppElement >}} button.
3.  Click {{< AppElement type="button" >}}Start test{{< /AppElement >}} to send a test alert to the Zapier webhook. It doesn't matter which *Alert type* you select.
4.  On the Zapier end of things, click the *Test trigger* button. This will prompt Zapier to look at the incoming data we've sent in the previous step, and parse its JSON body. We'll be able to refer to the individual fields in the outgoing message later on.![](/img/content/5386ad32-943e-41ff-9533-abcb03c30fc5.png)
5.  Click the *Continue* button in Zapier.

## 4. Set up a Do This... action in Zapier

### Example 1: email integration through Zapier

As an example, let's set up a simple email integration through Zapier first.

1.  In Zapier, find and select the *Email by Zapier* Built-in App.
2.  Click *Continue*.
3.  Add your email address in the **To**-field.
4.  The **Subject** and **Body** fields may be customized using the incoming Uptrends data. Since Zapier has received and parsed a test alert in step 3, it is already aware of the data contained in incoming Uptrends alerts. When you click either field, a list labeled **Insert data** appears, from which you can select references to values included in an Uptrends alert. When Zapier sends the outgoing message, it will automatically fill out the correct values.![](/img/content/af300fe7-01dd-4e58-b2fe-afa99b1125ff.png)
5.  After customizing the outbound message to your liking, click the *Continue* button.
6.  If you wish, you can test the outgoing message in this screen. It should send you an email with fictitious data right away.![](/img/content/8a4e2e5e-2288-4a6d-91c4-d9f64c54b6f0.png)
7.  Finish setting up the integration on the Zapier end by clicking **TURN ON ZAP**.

### Example 2: Trello integration through Zapier

Your Zapier integration can do so much more. As a second example, let's look at setting up an integration with Trello. You'll need to have your Trello account connected to Zapier. You can find the option to do this under *My Apps* in the Zapier sidebar menu.

1.  Add a new Zap by following the same steps outlined in section 1 ( *Set up a When this happens... action in Zapier*) of this guide.
2.  You'll get a new **Custom Webhook URL**. This new Webhook URL should be added to a separate integration in Uptrends. Follow the actions in step 2 to set up a new integration in Uptrends, but make sure you use this new Webhook URL.
3.  Repeat the actions outlined in Step 3 to send test data to this new webhook, so that Zapier can parse the incoming data. In short: in the {{< AppElement type="tab" >}}Customizations{{< /AppElement >}} tab, click the {{< AppElement type="button" >}}Send test alert{{< /AppElement >}} button. In Zapier, click the *Test trigger* button. Finish by clicking *CONTINUE*.
4.  To set up the integration with Trello, select the *Trello* app under **Your Apps**.
5.  You can select the exact action to take in Trello when an Uptrends alert is sent out. For this example, let's choose *Create Card*. Click *CONTINUE* in the following screen.
6.  Select the connected Trello account and click *CONTINUE*.
7.  Choose the appropriate **Board** and **List**. Set the **Description** for the to-be-created card. Once again you can fully customize the content here, making use of the Uptrends alerting data as previously parsed by Zapier. Set any other options you might wish, and finish by clicking *CONTINUE*.![](/img/content/52217609-6954-4819-8bc1-9195a448ff72.png)
8.  If you wish, you can test the outgoing message in this screen.![](/img/content/4cea7e0f-e577-4250-aec5-ab31d000935d.png)
9.  Finish setting up the integration on the Zapier end by clicking **TURN ON ZAP**.

{{< callout >}}
**Tip:** These are just 2 examples, but Zapier will allow you to forward your Uptrends alerts to virtually any external platform.
{{< /callout >}}

## 5. Add the integration to an alert definition in Uptrends

An integration definition on its own does nothing. You need to attach it to an escalation level in an alert definition in order to receive messages through it.

1.  Go to {{< AppElement type="menuitem" >}}Alerts > Alert definitions{{< /AppElement >}} and open the one that you want to attach the integration to.
2.  Each {{< AppElement type="tab" >}}Escalation level{{< /AppElement >}} tab contains a section **Alerting by integrations** with a list of available integrations. Read the knowledge base article [Alert escalation levels]({{< ref path="support/kb/alerting/alert-escalation-levels" lang="en" >}}) to learn how escalations work.
3.  Select the integration(s) that you would like to attach to this escalation level. In this case the **Custom integration** for Zapier.
4.  Make sure to hit the {{< AppElement type="savebutton" >}}Save{{< /AppElement >}} button to save your changes.

**And that's it!** You've successfully set up the Zapier integration.

As always, if you have any questions, please [reach out to our support team](/contact).
