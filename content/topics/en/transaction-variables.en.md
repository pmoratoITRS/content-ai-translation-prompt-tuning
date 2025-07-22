{
  "hero": {
    "title": "Using variables in transactions"
  },
  "title": "Using variables in transactions",
  "summary": "A guide on how to use variables in transactions.",
  "url": "/support/kb/synthetic-monitoring/transactions/transaction-variables",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-variables",
  "tableofcontents": true
}

In some cases, you may have to save and reuse a value your transaction monitor will encounter over the course of running its script. In such cases, you can configure your transaction to save the value as a **variable**, and make use of it again later on in the script. For example, if your transaction goes through a funnel that generates an order number, you can have the transaction save it in a variable, and then check it against an order number listed on a confirmation page later on in the process, to ensure that your backend has done its job correctly. 

## Creating a variable

To create a variable, make use of the ['Test element content' action]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks#test-element-content" lang="en" >}}). Variables will be created based on the complete content of one of the elements on the page. To specify the element you wish to save, you'll need to use either [a CSS selector or XPath query]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="en" >}}). 

1. [Add a 'Test element content' action]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#adding-action" lang="en" >}}) in the right place in the transaction script. The element content you wish to save as a variable must be present on the page at that point in the transaction.
2. Point the content check to the correct element on the page using [a CSS selector or XPath query]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor#css-selectors-and-xpath-queries" lang="en" >}}). If you need help with this, please [contact the support team]({{< ref path="/contact" lang="en" >}}). 
3. The [content check]({{< ref path="support/kb/synthetic-monitoring/transactions/content-checks" lang="en" >}}) will test for the presence of the specified element, and also verify that its content matches a certain value (you can make use of regular expressions). 
4. For the **Assign variable** option, fill in the variable name wrapped in double curly brackets: `{{variableName}}`

In the example below, the second step of a transaction places an order (by clicking on an element with identifier `#confirmPurchase` in step 2.1), checks for the presence of an element `#orderNumber` and verifies that its content matches a regular expression (in step 2.2). Finally, it saves a variable `{{orderNumberLong}}` by making use of the **Assign variable** option. The variable contains the entire value of the element (which in this case would be *"Your order number is: 1234"*).

![Creating a transaction variable](/img/content/scr-transaction-variable-creation.min.png)

## Adjusting a variable

In cases such as the example above, the content captured in the variable may contain unnecessary text. In this case, the interesting part of the string in the variable would likely be only the order number itself. The variable content can be adjusted by applying a regular expression to it, to keep or remove specific parts of it. For more information, see the knowledge base article on [the 'Adjust variable content' action]({{< ref path="support/kb/synthetic-monitoring/transactions/action-adjust-variable-content" lang="en" >}}).

1. After the variable has been created in the transaction script, add an **Adjust variable content** action.
2. Add the variable name defined earlier (`{{orderNumberLong}}` in the example above).
3. Choose to **keep** or **remove** everything that matches the regular expression pattern.
4. Add the regular expression.

![Transforming a variable](/img/content/scr-transform-trn-variable.min.png)

The result of this action, as applied to the example above, would be the isolated order number: *1234*. Keep in mind that this will overwrite the existing variable.

## Using variables

Now that a variable has been defined and optionally adjusted, it can be used elsewhere in the transaction. Variables can be referred to at any point after their creation by their name. For example, the order number isolated in the example above can be reused as the value in a **Set** action, and filled in to a search box to confirm that the order was successfully created. Simply refer to the variable by its name (`{{orderNumberLong}}` in this case).


![Using a transaction variable](/img/content/scr-trn-variable-use.min.png)



