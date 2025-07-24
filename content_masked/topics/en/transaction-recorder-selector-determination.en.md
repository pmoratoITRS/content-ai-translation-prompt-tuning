{
  "hero": {
    "title": "Transaction Recorder selector determination"
  },
  "title": "Transaction Recorder selector determination",
  "summary": "When you use the Transaction Recorder, the recorder makes the decsision of about how to identify the individual elements on the page based on several factors. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/transaction-recorder-selector-determination",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When you use the Transaction Recorder, the recorder returns a long list of possible selectors that Uptrends uses in your Self-Service Transaction steps to identify a page element. Each step or action will only use one of these selectors in your script. Therefore, Uptrends uses an algorithm to determine the best selector.

## Selectors

While recording your transaction using the Transaction Recorder, as you interact with the various page elements, the recorder generates a list of possible selectors to identify each element. The list of possible selectors contains various text, ID, CSS, and XPath selectors. The Transaction Recorder generates a list of the possible selectors for each element. The recorder itself does not contain any logic to choose one selector over another, so the Uptrends servers make the determination during the conversion process.

To select the best selectors, Uptrends looks at the value of the selectors and chooses a selector value and type that is not too vague, too complicated, nor frequently appears on the page.

[SHORTCODE_1]
**Note**: You can view the other selectors by clicking the ellipsis [SHORTCODE_3]...[SHORTCODE_4] in the selector value field.
[SHORTCODE_2]

## Selection process

The following steps are executed to find the best selector:

1.  **Normalization**: The normalization process filters out any selectors that have the same value and select on the same attributes.
2.  **The removal of unsupported locators**: The process  removes any selectors that Self-Service Transactions don't support (text selectors).
3.  **Prioritization of the element types**: The process gives priority to selectors based on type (in order of priority): text, id, name, CSS, XPath (text), XPath (attributes), XPath (index), XPath (node).
4.  **Prioritization of shorter selectors over longer ones**: Uptrends prioritizes the selector based on the number of characters in the string giving priority to the shortest selector.
5.  **Prioritization of the matched elements count**: each selector may have multiple elements on the page that match the same description, so this process gives priority to selectors based on uniqueness.
6.  **Prioritization of single match selectors**: Uptrends gives the highest priority to selectors that only match one element on the page.
7.  **Final selection**: The resulting list has the selectors prioritized, and Uptrends chooses the first selector in the list for the action.
