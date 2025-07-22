{
  "hero": {
    "title": "Error conditions - Console content"
  },
  "title": "Error conditions - Console content",
  "summary": "You can base monitor checks and error generation on the content of the console log of your browser.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-console-content"
}

Every monitor runs some standard checks, which depend on the monitor type. Additionally, in the error conditions of a monitor, you can define custom checks to generate alerts for specific situations. The knowledge base article [Error conditions]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) explains what they are and how to use them.

This article explains how the error conditions of the category *Console content* work. In a monitor you can find them on the tab {{< AppElement type="tab" >}}Error conditions{{< /AppElement >}} in the section *Check console content*. Note that not all monitors have all types of error conditions. Check the table in [Which error conditions are available?]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) to find out which options are available in certain monitor types.

## The browser's console log 

When loading a web page into a browser, the browser's console log will capture any log messages. You can find those messages in e.g. Chrome by pressing the "F12" key to open the DevTools and then going to the *Console* tab. The log messages can be of the type info, warning, or error (element loading failure, javascript error, etc.). Log messages can be implemented by the web developer. 

You can define error conditions that are based on the existence and optionally the content of the log messages. With these error conditions, you can check whether a log entry of the type info, warning, or error is present and also if it contains or does not contain a given text. An error is generated if the defined condition is met. 

Note that this error condition is different than the [Check page content]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="en" >}}) error condition, where you check the content of the page itself.

## Console log message exists {id="contains-content"}

Check if a console log message exists and optionally check if it contains certain content.

To define this error condition:

1. Go to {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}.
2. Click on the monitor's name to edit it.
3. Open the {{< AppElement type="tab" >}} Error conditions {{< /AppElement >}} tab.
4. In the *Check console content* section click the {{< AppElement type="buttonSecondary" >}} \+ New check {{< /AppElement >}} button to add a new check.

    ![screenshot check console content](/img/content/scr_errorconditions-console-content.min.png)

5. Select the option **Error when the console contains certain content**.  
6. Choose the message level (info, error, warning). 
7. The **Message text** works as follows: if you leave this empty, the monitor will only check if a log entry of the chosen message level exists regardless of its content. If you want to check for certain content in the log entry you have to enter the text you want to check for in the **Message text**. This can be a word, phrase, or regular expression. 
8. Add more checks, if desired.
9. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to save all changes in the monitor. 

## Console log message does not exist

Instead of checking for the existence of log messages and possibly certain content, you may (also) want to check for the non-existence of log messages and (optionally) their content.

Use the steps as described for [Console log message exists]({{< ref path="#contains-content" lang="en" >}}), but select the option **Error when the console does not contain certain content**. 

Then choose which log message level (info, error, warning) you want to check for. If you leave the **Message text** empty this condition will generate an error if no log messages of that level exist. If you fill in a **Message text** an error is generated if there is no log message of that level and with the given text.

## Results of a console content check

The monitor will run the check taking into account your settings for this error condition. You can take a look at the results by opening the [Check details]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="en" >}}). If the check returned an error instead of "OK", the information in the check detail will help you to understand which error condition caused an error and may provide information on where to start your troubleshooting.

