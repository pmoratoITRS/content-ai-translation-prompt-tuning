{
  "hero": {
    "title": "Capturing the shopping cart user journey"
  },
  "title": "Capturing the shopping cart user journey",
  "summary": "In this tutorial, step-by-step you are taken through the recording process as you capture the shopping cart user journey.",
  "url": "/support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/recording-your-transaction",
  "tableofcontents": false
}

In this example you go through the process of capturing the user journey for a user adding to and modifying their shopping cart.

The following instructions take you through a detailed example of the transaction recording process. Once the transaction monitor is active, it will use transaction credits that you have to buy in your account. This example includes information about which steps will use credits. More details about the usage of credits can be found in the article [Transaction monitor credit calculations]({{< ref path="support/kb/synthetic-monitoring/transactions/Understanding-transaction-monitor-count-calculations" lang="en" >}}).

1. Get Uptrends' transaction recorder from the Chrome webstore and add this extension to your Chrome browser. The steps are described in [Download the transaction recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder#download-transaction-recorder" lang="en" >}}).
2. In a Chrome browser window, open the transaction recorder extension and click the {{< AppElement type="deletebutton" >}} Start Recording {{< /AppElement >}} button. The **REC start** window opens. 
3. Enter [https://galacticshirts.com](https://galacticshirts.com/) as the URL in the address bar of the **REC start** window.  
   *This is your first transition to a new page resulting in a server request (credits used = 1).*  
   The home page of the shop is shown.
   ![screenshot of galactic shirts homepage](/img/content/f0180d9f-9bf2-4947-bf11-c47c48afcd23.png)  
4. Click the image of the first shirt to open its product detail page.  
   The shirt may change, but there should always be a first shirt. In this case, the first shirt is the Suraya Bay T-Shirt.  
   *Clicking the link means transitioning to the product detail page and making a server request. This will use another credit (credits used = 2).*
   The product details for the shirt are shown.
5. Click the **Size** drop-down to select size "**L**".
6. Change the quantity to "**2**".
   ![](/img/content/e1b42b45-fb3a-4687-af3e-fba30d780986.png)
   Changing the quantity by highlighting the "1" and typing "2" or clicking the up/down arrows doesn't matter; the recorder registers the click and the change in value only.  
7.  Click **Add to cart**.  
    *Clicking the *Add to cart* button generates a server request and a page refresh using another credit (credits used = 3).* 
8.  Add a content check. For best practices, it is recommended to always add [content checks]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="en" >}}) to verify if the result of each page load turns out as expected. In this example, we want to make sure that the add-to-cart action worked properly (one of many content checks you should consider adding to your script). You can add a content check in three different ways, either via the **Add content check** button or via the context menu. You can also add content checks later on using the monitor step editor in your account.

    To add a content check via the **Add content check** button:
      
    1. Find the recorder window (often behind your browser window) and click {{< AppElement type="editbutton" >}} \+ Add content check{{< /AppElement >}} 
       ![screenshot recorder content check](/img/content/6101d30a-9158-40d0-9b28-d7422f3c94c3.png)
      
    2. Choose a part of the confirmation page that is unique to the page and least likely to change. In this case a good candidate is "added to your cart." Enter this into the **Add content check** pop up.
       ![screenshot content check pop up](/img/content/scr_transaction-recorder-add-content-check.min.png)
    3. Click {{< AppElement type="button" >}}Save{{< /AppElement >}}.
    4. Return to the recording window.

    To add a content check via the context menu:

    1. Highlight the text "added to your cart.".
    2. Right click and choose *ITRS Uptrends Transaction Recorder* option in the context menu.
    3. Select the *Create a content check* option. This content check is now recorded in the transaction recorder window.
    4. Return to the recording window.

    ![screenshot content check context menu option](/img/content/scr_transaction-recorder-content-check-hover.min.png)

The content check was now successfully recorded.

9.  Click the **View Cart** button to go to the shopping cart view.  
    *This uses another credit (credits used = 4).*
10.  Change the quantity from "2" to "1."
11. Click **Update cart**.  
    *Update cart refreshes the page which generates a server request using one credit (credits used = 5).*
    ![screenshot shopping cart update](/img/content/5ba19828-a398-41bd-b67e-e8c615442cb1.png)
12. Add a content check to verify the page loaded correctly by testing for the text "Cart updated."
13. Click the red "X" to remove the item from the shopping cart to finish our transaction.  
    *Removing the item generates a server request using one credit (total credits used = 6).*
14. Add a content check using the phrase "Your cart is currently empty.".
15. Another way to verify if your cart is empty is via hovering the basket icon at the upper right corner of your screen. Take note that the transaction recorder doesn't automatically record a step when you hover elements in the website, therefore, you need to add it manually.
    
    To add a hover action during the recording process:
    1. Right click the element in which you want to hover, in this case, the basket icon. 
    2. In the context menu, click the *ITRS Uptrends Transaction Recorder* option.
    3. Click *Create hover action*. Notice that the actual step has been recorded in the transaction recorder window.
    4. In this example, when you hover the basket icon, a message "No products in the cart." appears. In cases where a mouse hover makes an element visible, you can also track the activity of an element that needs to be visible. You can do this with the same approach as the hover action just by right clicking the visible element (*"No products in the cart" element*) > In the context menu, click *ITRS Uptrends Transaction Recorder* > *Wait for this element to be visible*. 

     ![screenshot empty cart](/img/content/scr_transaction-recorder-hover.min.png)

Both the hover action and the element that needs to be visible are now recorded.

16. Add a content check using the phrase "No products in the cart.".
17. Now that your cart is empty, you can look for another type of shirt using the search products text field at the upper right part of the screen. Type in *Summer*, notice that this field doesn't contain any search button. Instead, you can press the *Enter key* to generate search results.

    The transaction recorder can also capture such keyboard actions from the user. This is useful when you encounter websites with *Press any type of key to continue* or *Press enter to confirm* instructions. Keep in mind that compared to mouse click activities (which automatically records a move), you need to manually add a keyboard action to record any keyboard event and count it as an actual activity.

    To add a keyboard action during the recording process:
    1. Find the recorder window (often behind your browser window):
       ![screenshot of add keyboard action button](/img/content/scr_transaction-recorder-add-keyboard-action.min.png)
       Click {{< AppElement type="editbutton" >}} \+ Add keyboard action{{< /AppElement >}} 
    2. A popup will appear displaying a dropdown menu to select which key should be pressed. You can choose from a variety of characters ranging from Control keys, Special keys, Digit keys, Numpad keys, Uppercase and Lowercase keys.
        ![screenshot of add keyboard action popup](/img/content/scr_transaction-recorder-add-keyboard-action-popup.png)
    3. Choose whether this key should be pressed globally or just on the currently focused element. By choosing the *Global* option, that specific keyboard event is recognized within the entire application. While the latter option is only applied for the *last clicked element* as stated inside the parenthesis of the radio button.
    4. Click {{< AppElement type="button" >}}Save{{< /AppElement >}} and return to the recording browser window.

    *Searching a new shirt generates a server request using one credit (credits used = 7).*

18. Add a content check to verify that the shirt does not exist by testing the text "No products were found matching your selection.".
19. Click {{< AppElement type="deletebutton" >}} Stop recording{{< /AppElement >}}.
20. Click the **Upload recording** button and choose to test and optimize the transaction yourself first (self-service transaction). Check out the knowledge base article [Options for transaction scripts]({{< ref path="support/kb/synthetic-monitoring/transactions/self-or-full-service" lang="en" >}}) on the choice between full-service and self-service transactions.

You've reached the end of the shopping cart user journey recording process. The result will be a new transaction monitor in your Uptrends account. You can expect your monitor to use seven transaction credits, but other factors affect the [calculation of credits]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-transaction-monitor-count-calculations" lang="en" >}}). 

The next task is to test your transaction and make adjustments, if needed. Use the instructions in [Testing and editing your transaction script]({{< ref path="support/kb/synthetic-monitoring/transactions/tutorial-record-user-journey-in-shop/testing-your-transaction" lang="en" >}}) to guide you through the testing.
