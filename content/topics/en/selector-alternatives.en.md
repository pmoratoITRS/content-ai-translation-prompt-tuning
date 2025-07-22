{
  "hero": {
    "title": "Selector alternatives"
  },
  "title": "Finding selector alternatives",
  "summary": "Sometimes selectors don't work, or they only work some of the time. In this article we step you through some of the common selector problems and suggested fixes.",
  "url": "/support/kb/synthetic-monitoring/transactions/selector-alternatives",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/selector-alternatives"
}

When you need to identify a specific page element in your transaction script, you use either an XPath or CSS selector. You may have multiple selector choices to specify a typical element, but some selectors are more problematic than others. So, finding the right one may take some clever applications of XPath or CSS selectors.

When you use the Transaction Recorder to capture your user click path, the [recorder applies algorithms]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-recorder-selector-determination" lang="en" >}}) to pick what it thinks is your best selector option. Because the Transaction Recorder only gets a single snapshot of what your page structure looks like, the selector it chooses may not be your best choice. In this article, we cover some situations and solutions for you to consider when searching out alternative selectors.

## Common causes of poor selector determination

Numerous factors may come into play that cause your selector not to perform the way you expect. For example, your tests may result in errors such as "Element not found." Bad selector choices may be the cause of your problems. Let's take a look at a few of the reasons for script errors.

### Dynamic IDs

Some elements get a new ID every time the server sends the page, so if your selector references the dynamic ID, the selector will fail when your script tries to find the element. There are a few different ways to fix these problems.  
  
For the following examples, we'll use an input element for selecting the item quantity in the HTML snippet.

    <div class="quantity"> 
      <input type="number" id="quantity_5e5653081acc7" class="input-text qty text"
      step="1" min="1" max="" name="quantity" value="1" title="Qty" size="4" 
      pattern="[0-9]*"inputmode="numeric"
      aria-labelledby="Suraya Bay T-Shirt quantity"> 
    </div>

The ID for the input is partly fixed and partly generated causing errors when referencing the ID as captured by the Transaction Recorder. The Transaction Recorder recommends:  
XPath: `//input[@id="quantity_5e5653081acc7"])[1] ` CSS selector: `input#quantity_5e5653081acc7`  
Both fail when used in the transaction. You have several options for fixing the problem.

-   **Use an element attribute that doesn’t change**. By referencing a different element attribute such as an element name, you may establish a stable selector.  
    `//input[@name="quantity"]`
-   **Use a relative path to navigate the DOM.** The HTML node above is nested in a parent `<div>` node. We can reference the input element inside the parent using XPath. The code below locates the parent followed by the child input element.  
    //div\[@class="quantity"\]/input
-   **Use a relative XPath using** `contains` or `starts with`. If the ID is partly fixed and partly dynamic such as `id="quantity_5e5653081acc7"` where the "`5e5653081acc7`" portion changes but the "`quantity_`" portion of the ID remains the same, you can reference the portion that doesn't change. For example,  
    `//select[starts with (@id, "quantity_")]`  
    or  
    `//select[contains(@id, "quantity")]`
-   **Add element attributes for your transaction tests**. Have your developers help you out by adding special element attributes for testing that don’t change. For example, let's say you have an element with a dynamic ID such as  
    `<button id=”i2fe4owf” class=”btn”>`  
    In this case, you don’t have anything concrete to identify the element such as a name attribute. If you add another attribute such as “data-test-id,” with a static value, you can always find the element. An added attribute may look something like  
    `<button id=”i2fe4owf” class=”btn” data-test-id =”shoppingcart-test-step2”>`
-   **Identify elements by using multiple element attributes**. If your `contains` or `starts with` options for identifying an element doesn't work because the other elements on the page use the same prefix or suffix with the dynamic portion, sometimes you can use multiple attributes to identify the element using XPath.  
    `//select[starts-with(@id, "quantity_" and contains(@class, "qty text")]```

### Multi-language sites

When you have a multilingual website, the page changes languages often based on the location of the user. If the checkpoint you’ve selected is in a region that triggers language changes, depending on how you’ve identified the element, your transaction monitor may fail. It is best to use other options other than label values or specific words found on the page in your selectors if the language affects your content.

### Dynamic content

Some sites use dynamic content based on things like seasonal promotions, holidays, user login, cookie, or location data. The shifts in data caused by variations in the dynamic content can cause transaction monitors to fail. Dynamic content is a lot like dynamic IDs, but the entire page’s elements change with each server request (think about your Amazon pages with its constantly changing product recommendations.) Although the details change, the structure typically does not. Referencing elements by where they are in the DOM rather than the current element’s attributes will give you better results.

For example, consider an e-commerce site that displays items on the page based on item popularity. The items rotate in and out almost every time the page loads. Rather than using a selector that identifies an item by its name or some other attribute specific to an item, it is probably best to use a relative path selector that chooses the first item in a list no matter what item is displayed.

### Hidden elements

Errors due to hidden elements aren't necessarily the result of a bad selector; instead, your selector may fail because you're missing a proceeding action. So, if you’re getting errors saying the script found the element, but the element isn’t visible, your script may need an additional action before you attempt the interaction.  Remember, just like your users, the script can’t interact with invisible elements.

**Missing hover action**:

A missing hover action causes errors. A menu item may not become visible until the user hovers the cursor above a menu item to generate the fly-out menu. Adding the hover interaction makes the element visible and available for interaction.

**Missing scroll action**:

Frequently pages only load elements when needed by the user to give the illusion of higher performance and to reduce data usage. As the user scrolls down the page, the contents load. Without the scroll action, the elements aren't rendered and made available for the script's interaction. Adding a scroll action solves the problem. Remember, the scroll action can only see currently visible elements. You may need to add two or more scroll actions to before the target element is visible on the page.

{{< callout >}}
**Note**: The recorder doesn’t capture scroll and [hover actions]({{< ref path="support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="en" >}}), so you need to add those actions into your script manually.
{{< /callout >}}

**Hidden in the DOM but visible on the screen**:

You may also get errors due to elements that you can plainly see on the page, but the element is hidden in the DOM. Common examples for this issue include radio buttons or checkboxes covered by labels. The recorder captures the click action on the radio button or checkbox; although those elements are not visible to the DOM, the labels are visible. To fix the problem, switch the click action to the label covering the element.

## Changing selectors

If you’ve run into problems with your selectors, you can take several different steps to solve the problem.

### Use the selector finder

When Uptrends converted your recording into a script, Uptrends decided which selector to use based on an algorithm; however, the recorder may have made a poor choice, so you need to intervene. Uptrends makes this easy by keeping your alternative selectors available to you. To access the alternative selectors,

1.  Click the gray square with an ellipsis in the selector field to open the selector dialog. 
![Selector finder button](/img/content/ed5d9588-d944-402f-9899-5ba46a574c2b.png)  

2.  Choose another selector in the list.
![Selector finder dialog](/img/content/c8a2a635-1e85-4c3b-b84b-2b1edbe4dd15.png)  

You can choose and test any of the selectors in the list. If none of them work well for you and you’re not comfortable writing your own, our [Support team](/contact) is happy to help you find a solution that works for you.

{{< callout >}}
**Note**: If you’re working with an older script, the selectors in the Selector Finder are most likely out of date, you may need to write the new selector yourself or have [Support](/contact) help you out.
{{< /callout >}}

### Write the selector yourself

If you’re comfortable working with selectors or you have development staff on hand to help you, you can write your own CSS or XPath selectors. No matter who writes your selectors, test them exhaustively. 

Note that you may use [automatic variables]({{< ref path="support/kb/synthetic-monitoring/transactions/automatic-variables" lang="en" >}}) in the selector, e.g. you could add a random number to the selector path by using the `{{@RandomInt(min,max)}}` automatic variable.

### Get help from Support

Self-Service Transactions doesn’t mean we’ve left you to fend for yourself. Our support staff is ready to help you. Our experienced transaction team has seen it all, and they are great at finding alternative selectors. Just open a [support ticket](/contact) and tell them about the challenge you’re having.
