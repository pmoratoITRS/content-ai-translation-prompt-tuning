{
  "hero": {
    "title": "Using wait conditions"
  },
  "title": "Using wait conditions",
  "summary": "When scripting your transactions, sometimes you need to instruct the monitor it needs to wait for a specific element to load before proceeding. Transaction monitoring supports three types of wait conditions",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/using-wait-conditions",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Loading a page takes time. Just like when you have to wait for a page to load, the transaction script sometimes also needs to wait for the page to finish loading before it can continue with the next action.

The loading of a page is a little chaotic because the browser divides the process into phases with some elements loading simultaneously while other elements wait until later. Therefore, it can be difficult for a script to keep track of when it can perform which action. The script needs to wait for the browser to load the page elements and for those elements to become interactive before the script can proceed with the next action.

Because of the chaotic load process, Uptrends' transaction monitors have a **Wait until** option available for all actions that interact with a specific element. With the **Wait until** option, you can define which condition the indicated element needs to meet before the transaction executes an action.

Currently, you have the option of three different **Wait until** conditions.

![]([LINK_URL_1])

## The element exists

**The element exists** option checks if the indicated element exists in the page's DOM. Just because an element exists does not necessarily mean you can interact with the element, nor does it mean that the element is visible on the page. Quite often, a page's DOM contains elements that the browser doesn't render for a multitude of possible reasons. **The element exists** option allows the transaction to attempt to proceed as soon as it finds the indicated element in the DOM Document node.

## The element is visible

**The element is visible** option checks if the element exists in the DOM document node and that the element is visible on the page. For example, a drop-down menu may contain several links that don't become visible until you hover the cursor over a specific page element. Since these links exist in the DOM before the hover action is available, you need to tell the transaction monitor to wait before interacting with the links until the browser renders the links.

## The element is both visible and enabled

**The element is both visible and enabled** option behaves the same as **The element is visible** option, with one important difference—not only must the element be visible on the page, the element must also be enabled. For example, the browser disables (often grayed out) certain buttons on some pages until the page meets a specific requirement. The requirement may be that the user must fill out a form before using the button. Therefore, the element is visible on the page, but you must also tell the transaction monitor to wait until the button is enabled before it attempts an interaction.

## What is a reasonable wait duration?

The wait time you set is the maximum amount of time your monitor waits for an element. The default wait times, unless otherwise specified, are 60 seconds for navigation and 30 seconds for all other action types. Those defaults are usually plenty of time, so unless you need to, it is generally not necessary to change from the default. If you do need to extend these timeout values, you can extend them using the **Wait timeout** field. The maximum timeout value for any action type is 60 seconds. Things to consider with long wait times:

-   Don't make your timeouts too short. Short timeouts can and do cause your monitor to generate errors. We recommend leaving the timeouts set to the default to avoid unwanted errors.
-   The maximum runtime Uptrends allows for a transaction monitor is four minutes. After four minutes the transaction times out. Although the monitor only waits as long as it needs to up to the timeout you've set, extended wait times can cause your monitor to error due to hitting the four-minute maximum run time.

[SHORTCODE_1]
**Note**: Generally, it's not necessary to change the default settings for the wait conditions. If you feel you need to adjust the wait conditions, [reach out to support]([LINK_URL_2]) to help you optimize your monitor's wait options.
[SHORTCODE_2]
