{
  "hero": {
    "title": "Selector alternatives"
  },
  "title": "Finding selector alternatives",
  "summary": "Sometimes selectors don't work, or they only work some of the time. In this article we step you through some of the common selector problems and suggested fixes.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/selector-alternatives",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When you need to identify a specific page element in your transaction script, you use either an XPath or CSS selector. You may have multiple selector choices to specify a typical element, but some selectors are more problematic than others. So, finding the right one may take some clever applications of XPath or CSS selectors.

When you use the Transaction Recorder to capture your user click path, the [recorder applies algorithms]([LINK_URL_1]) to pick what it thinks is your best selector option. Because the Transaction Recorder only gets a single snapshot of what your page structure looks like, the selector it chooses may not be your best choice. In this article, we cover some situations and solutions for you to consider when searching out alternative selectors.

## Common causes of poor selector determination

Numerous factors may come into play that cause your selector not to perform the way you expect. For example, your tests may result in errors such as "Element not found." Bad selector choices may be the cause of your problems. Let's take a look at a few of the reasons for script errors.

### Dynamic IDs

Some elements get a new ID every time the server sends the page, so if your selector references the dynamic ID, the selector will fail when your script tries to find the element. There are a few different ways to fix these problems.  
  
For the following examples, we'll use an input element for selecting the item quantity in the HTML snippet.

    [HTML_TAG_1] 
      [HTML_TAG_2] 
    [HTML_TAG_3]

The ID for the input is partly fixed and partly generated causing errors when referencing the ID as captured by the Transaction Recorder. The Transaction Recorder recommends:  
XPath: [INLINE_CODE_1] CSS selector: [INLINE_CODE_2]  
Both fail when used in the transaction. You have several options for fixing the problem.

-   **Use an element attribute that doesn’t change**. By referencing a different element attribute such as an element name, you may establish a stable selector.  
    [INLINE_CODE_3]
-   **Use a relative path to navigate the DOM.** The HTML node above is nested in a parent [INLINE_CODE_4] node. We can reference the input element inside the parent using XPath. The code below locates the parent followed by the child input element.  
    //div\[@class="quantity"\]/input
-   **Use a relative XPath using** [INLINE_CODE_5] or [INLINE_CODE_6]. If the ID is partly fixed and partly dynamic such as [INLINE_CODE_7] where the "[INLINE_CODE_8]" portion changes but the "[INLINE_CODE_9]" portion of the ID remains the same, you can reference the portion that doesn't change. For example,  
    [INLINE_CODE_10]  
    or  
    [INLINE_CODE_11]
-   **Add element attributes for your transaction tests**. Have your developers help you out by adding special element attributes for testing that don’t change. For example, let's say you have an element with a dynamic ID such as  
    [INLINE_CODE_12]  
    In this case, you don’t have anything concrete to identify the element such as a name attribute. If you add another attribute such as “data-test-id,” with a static value, you can always find the element. An added attribute may look something like  
    [INLINE_CODE_13]
-   **Identify elements by using multiple element attributes**. If your [INLINE_CODE_14] or [INLINE_CODE_15] options for identifying an element doesn't work because the other elements on the page use the same prefix or suffix with the dynamic portion, sometimes you can use multiple attributes to identify the element using XPath.  
    [INLINE_CODE_16]`[INLINE_CODE_17][SYSTEM_VAR_1]` automatic variable.

### Get help from Support

Self-Service Transactions doesn’t mean we’ve left you to fend for yourself. Our support staff is ready to help you. Our experienced transaction team has seen it all, and they are great at finding alternative selectors. Just open a [support ticket]([LINK_URL_8]) and tell them about the challenge you’re having.
