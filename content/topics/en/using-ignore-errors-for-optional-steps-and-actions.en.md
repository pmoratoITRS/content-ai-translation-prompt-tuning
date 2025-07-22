{
  "hero": {
    "title": "Using ignore errors for optional steps and actions"
  },
  "title": "Using ignore errors for optional steps and actions",
  "summary": "Your transaction scripts need to be able to respond to dynamic site changes. Using ignore errors gives you the control you need to insert conditional or skippable statements into your script's steps and actions.",
  "url": "/support/kb/synthetic-monitoring/transactions/using-ignore-errors-for-optional-steps-and-actions",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/using-ignore-errors-for-optional-steps-and-actions"
}

It is rare for a website not to have dynamic variations in the user click path. Your site may have dynamic variations in content for many reasons:

-   Page differences due to user location
-   A/B testing
-   Changes in input fields
-   Cookie walls
-   Temporarily inserted pages

Any variation in the click path creates challenges for your transaction scripts. Conditional statements in the form of the *ignore errors* option can help you to navigate around dynamic site changes such as those listed above.

## How is “ignore errors” like making a conditional statement?

When you choose to ignore errors, you tell the monitor to try an action, but based on whether the assertion or action fails (or succeeds), do this action next. Think of the ignore errors option as a way to insert a conditional statement. You can either set ignore errors at the step level or on individual actions.

-   **Ignore errors at the step level** By setting ignore errors at the step level, you tell the script to abandon the step and continue with the next step if the script encounters an error. If action X in step Y is successful, proceed; if action X in step Y fails, abandon the step and move to step Z.
-   **Ignore errors at the action level**  
    By setting ignore errors at the action level, you tell the script to continue to the next action even if the action fails. If action X is successful, move to action Y; if action X fails, continue to the action Y anyway.

## How do skippable steps and actions work?

Typically, when your transaction errors, execution of the script stops, and Uptrends records the error. The error may result in Uptrends sending you an alert if another checkpoint verifies the error. If you make the error skippable (ignore errors), execution continues in the next step or action depending on whether you placed the ignore errors at the step level or on the action. Uptrends notes your error in your check detail report; however, skipped errors do not affect your site’s reporting.

### Ignoring errors on steps

Enabling ignore errors on a step causes the script to stop executing the current step and skip to the next step if an action fails. For example, Figure 1 represents a transaction with a cookie wall. The cookie wall requires the user to click an accept button when the wall appears, but the wall doesn’t appear for all users.

To handle the cookie wall, we put in a skippable step. In this case, a content check determines if the site inserted a cookie wall (represented in Step X in Figure 1). If there is a cookie wall, the content check is successful, the monitor clicks the button to accept the terms, and execution continues in Step Y. If the content check doesn’t find a cookie wall, Step X fails, but the monitor continues to step Y anyway. Step Y is not set to ignore errors, so any errors that happen in Step Y cause the monitor to terminate the script, and Uptrends records the error.

![](/img/content/28f28080-958d-4d25-866e-cd73efade7d2.png)

*Figure 1*: Using ignore errors to test for and clear a cookie wall if present.

### Ignoring errors on actions

When you ignore errors on single actions, the execution continues to the next action. Figure 2 represents a transaction with an A/B test. In Step X, the script requires actions one and two to succeed, but actions three and four are only valid for version A of the page. If you don’t ignore errors for actions three and four, the script will error every time the server sends page B.

![](/img/content/8d1b26cd-3c66-4363-a82a-cdad2423b0f4.png)

Figure 2: Flow chart for a transaction with an A/B test.

## Examples

To help you out, let’s look closer at some common examples. Your specific case may require a different solution, [let us know](https://www.uptrends.com/contact) if you need help with your solution.

{{< callout >}}
**Note**: A general rule to follow is to use ignore errors on actions for a single action, and use ignore errors on the step if more than one action needs skipping based on a single conditional.
{{< /callout >}}

### Use case: Different click path due to user location

Occasionally sites behave differently based on a user’s location for various reasons, such as government regulations, availability of product in the area, or language. For example, if a user is in the EU, the site needs to get confirmation that the user understands that the website collects personal data from visitors. The site uses a popup that requires the user to check a box stating that they know the terms on which the website collects and maintains data, and the user also has to click a continue button.

#### Solution: Skippable step

This example requires the user to complete two actions to access the full site; therefore, a skippable step is a good choice.

1.  Add a step at the point in the transaction where the user may receive the prompt.
2.  Set the step to ignore errors.
3.  Insert a click action that ticks the checkbox.
4.  Insert a click action that presses the continue button.

If the click action in step three fails, the prompt wasn't displayed to the user. The script exits the step and moves to the first action in the next step; otherwise, the monitor acknowledges the terms by making the appropriate actions, and the transaction proceeds normally.

### Use case: A/B testing

An A/B test allows you to compare user interactions based on two different versions of the same page. Page A may require the user to provide more personal information than page B. The test determines which page generates more conversions. The server delivers different page versions to users randomly. The changes in the different page interactions may cause your monitor to error.

#### Solution: Skippable actions

In this situation, the monitor needs to complete some actions no matter which page is delivered and skip one or more actions specific to other page versions. To handle A/B tests:

1.  Use actions that do not ignore errors for the interactions that the two pages have in common.
2.  Set the additional fields to ignore errors.

By setting the actions to ignore errors for the additional fields, the transaction can continue no matter which version of the page the monitor receives (See Figure 2).

### Use case: Changing field options

Consider a clothing e-commerce site that has rapidly changing inventory. Your transaction picks the first item that comes up in a search, but the first item changes frequently. Although each item has a quantity field, not all items have a size (a scarf), a color (only comes in black), or neither (a handbag). The changes in available actions can cause your monitor to error when it attempts to select a color when color isn’t an option.

#### Solution: Skippable actions

Since not all selection fields show up on all pages, you want to ignore errors on the actions that set values for elements that don’t apply to the item. To handle changing field options:

1.  Add a step.
2.  Add the appropriate actions for each possible page interaction: quantity, size, and color.
3.  Leaving the ignore errors option unchecked for quantity, check the ignore errors boxes for the size and color selection actions.

The script attempts to set each value, but if the element isn’t present the action errors and the script execution moves to the next action anyway (see Figure 2).

### Use case: Inserted notification pages

From time to time, a site needs to notify its users about different things such as upcoming maintenance, changes in user terms, sales, and other promotions. The website inserts temporary pages with the notification into the regular user click path. The page often requires a user action to acknowledge the notification.

#### Solution: Skippable step or action

This use case may have one or more user interactions to move the transaction forward.

**If acknowledgment takes a single interaction, use a skippable action,** insert the action in the appropriate place, and set the action to ignore errors.

**If acknowledgment requires multiple actions, use a skippable step**. 

1.  Add a step at the point in the script where a message may appear.
2.  Set the step to ignore errors.
3.  Add the appropriate actions to close the page: accept the new terms, acknowledge the notification, and submit for the response.

If the step or action is successful, you’ve moved the transaction forward. If the step or action fails, there is no notification page, no further action is needed, and the script moves to the next action or step.
