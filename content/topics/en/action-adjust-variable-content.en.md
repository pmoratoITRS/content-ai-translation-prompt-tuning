{
  "hero": {
    "title": "Adjust a transaction variable"
  },
  "title": "Adjust a transaction variable",
  "summary": "When setting up transaction monitors, you may want to extract and adjust values. The control action *Adjust a variable* allows you to change previously extracted content. ",
  "url": "/support/kb/synthetic-monitoring/transactions/action-adjust-variable-content",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/action-adjust-variable-content"
}

The transaction action of type **Adjust variable content** allows you to change the value of a variable that was set in a [**Test element content**]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks#test-element-content" lang="en" >}}) action within a transaction monitor's step. The adjustment is done using regular expressions (RegEx). Changing a variable value could be handy if you want to use only part of or a adjusted part of the value that was derived from a page element. 

{{< callout >}} **Note**: The adjustment of a variable will replace the original value of the variable. A (adjusted) variable is available starting with the action where it was defined/adjusted, in all following actions and steps until the transaction's end. {{< /callout >}}

## Defining the variable {id="defining-the-variable"}

For more information on how to set up a transaction variable, please see our knowledge base article on [Using transaction variables]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-variables" lang="en" >}}).

## Adjusting the variable {id="adjust-variable"}

The second part is to add an *Adjust variable content* action to the step:

1. Open the transaction monitor that you want to change.
2. Go to the {{< AppElement type="tab" >}} Steps {{< /AppElement >}} tab.
3. Open the step where you want to change a variable.
4. Click the {{< AppElement type="buttonPrimary" >}} Add action {{< /AppElement >}} button. 
5. From the list of **Control** actions, choose the *Adjust variable content* action and click the {{< AppElement type="button" >}} Select {{< /AppElement >}} button to add the action to the step.

   ![screenshot transaction action adjust a variable](/img/content/scr_transaction-action-transform-variable.min.png)

   The values for *Variable*, *Adjustment type*, and *Regular expression pattern* are mandatory. The other settings are optional.

6. Fill in the variable name using the format `{{name}}`. The name has to be spelled exactly as when you were [Defining the variable](#defining-the-variable). The name is case sensitive.
7. Choose the *Adjustment type*, which can be  
   \- **Keep everything that matches a pattern** — to extract a value from the variable that matches the *Regular expression pattern* value  
   \- **Remove everything that matches a pattern** — to extract everything but the part that matches the *Regular expression pattern* value
8. Enter the regular expression (RegEx) that should be used to adjust the variable.
   As an example, if the value of the variable originally is "Your order number is 12345" and given that your order number is always five digits long, you could change the variable to the order number only by using the *Keep everything that matches a pattern* setting in combination with the regular expression `\d{5}` as the *Regular expression pattern* which will find five digits in a row. 
9. Make sure that the adjustment of the variable happens after setting the variable. You can drag and drop the actions within a step, should this be necessary. 
10. Click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button to save all changes.

 The adjusted variable value is now available in all consecutive actions and steps until the end of the transaction. To refer to the variable, use the original name ({{name}}) that you have given when defining the variable. Check out the information about the [Set action]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#set" lang="en" >}}) to learn how to use the variable for setting a value in another step or action.
