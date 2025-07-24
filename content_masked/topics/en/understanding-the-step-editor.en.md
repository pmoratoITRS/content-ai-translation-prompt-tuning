{
  "hero": {
    "title": "Understanding the step editor"
  },
  "title": "Understanding the step editor",
  "summary": "The step editor is used to edit the steps and actions of a transaction script.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transactions/understanding-the-step-editor",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The transaction step editor is needed to edit the steps and actions of a transaction script and can be used as the visual editor that has a UI allowing you to add and edit steps or the script editor that that is a plain text editor. 

If you feel comfortable with writing your own script, check out [Scripting source code directly]([LINK_URL_1]) to learn more about the script editor.

In most cases you won't write a script, but rather [use the transaction recorder]([LINK_URL_2]) to make a first set-up of your script and then use the step editor to fine-tune the transaction.

[SHORTCODE_1]
**Note**: Uptrends uses transaction credits to price your transaction monitors. The number of credits used for a monitor is shown after the monitor name in the *Monitor* overview (go to [SHORTCODE_3] Transactions > Transactions setup [SHORTCODE_4]). You can find a full explanation on credits in the knowledge base article [Understanding transaction monitor credit calculations]([LINK_URL_3]).
[SHORTCODE_2]

## Steps and actions

The script of a transaction monitor contains steps (of the transaction you want to monitor). Inside the steps you find actions, which are the micro-steps in your transaction.

To edit the steps and actions:

1. Go to [SHORTCODE_5] Transactions > Transactions setup [SHORTCODE_6].
2. Open the [SHORTCODE_7]Steps[SHORTCODE_8] tab.

![screenshot transaction step editor]([LINK_URL_4])

 You refine and test your transaction script in the  [SHORTCODE_9]Steps[SHORTCODE_10]  tab, or you can write your script from scratch here as well. Notice the [SHORTCODE_11] SWITCH TO SCRIPT [SHORTCODE_12] button at the top right of the editor for this purpose.

If you uploaded your script from the [transaction recorder]([LINK_URL_5]), you should see one or more steps with actions already defined. If you're creating your script from scratch, you will build out each step in your transaction using the step editor. It is recommended to use the transaction recorder to give you a good basis to start from.

Your transaction script is made up of *steps* and *actions*. Let's take a closer look at what we mean by steps and actions.

## What is a step?

When you upload your script from the transaction recorder, Uptrends automatically defines your steps for you, but what is a step? A step is an arbitrary grouping of actions in your transaction script. Typically, you want to group user interactions with your page into steps that end with a server request such as a form submit. Grouping actions by server submits/requests helps with troubleshooting and performance reporting.

You could also think of a step as a state transition in the browser, i.e., an action that results in a new page or refreshes the page with new content. But really, you can set up your steps to reflect whatever grouping makes sense to your use case and your reporting needs.

### Step settings [ANCHOR_1]

Click the arrow **>** icon beside the step name to access the step actions and settings.

![screenshot single step in script]([LINK_URL_6])

Within each step, several settings are shown:

- **Waterfall** - You can add an optional [Waterfall]([LINK_URL_7]) report to show the page load, **Core Web Vitals**, and **W3C Performance metrics** of any transaction step. Each Waterfall report uses one [transaction step credit]([LINK_URL_8]). To enable this setting, check the **Waterfall checkbox** and adjust the following according to your needs:

  1. **Name** — specify a descriptive name for each step. For example, *Add to cart*, *Login*, or *Request appointment time*.

  2. **Error handling** — if you wish to continue executing your transaction steps or scripts with page errors, you can do so by checking the **Ignore all errors that occur in this step** option. Uptrends continues to the next step regardless of the result from the current step. Your **Check details** screen shows the error, but the Transaction monitor continues despite the error. For more details, refer to [Using ignore errors for optional steps and actions]([LINK_URL_9]).

  3. **Performance metrics** - check this option to enable and **Store Core Web Vitals and W3C scores as separate metrics** in your Transaction monitors. This option allows you to display such [metrics]([LINK_URL_10]) in your [Simple data or list custom report tiles]([LINK_URL_11]) when you click the [SHORTCODE_13] [SHORTCODE_14] icon.


- **Filmstrip** - You can add optional [Timeline screenshots]([LINK_URL_12]) (also known as a filmstrip) on a per-step basis. A filmstrip uses one [transaction step credit]([LINK_URL_13]) unless there is already one screenshot in the step. In that case, the filmstrip is provided free of charge.

- **Screenshot** - An optional [screenshot]([LINK_URL_14]) lets you see the screen as experienced by your user at the end of the step. You can enable a single screenshot by adding the *Control* [action]([LINK_URL_15]) **Screenshot**. A screenshot uses one [transaction step credit]([LINK_URL_16]).

- **Page source** - Choose this option to get the page source information and any console log data that was generated during the execution of that step. Note that the page source is available only in combination with the waterfall.


### Adding steps

To add a new step to your script:

1. Scroll to the bottom of the  [SHORTCODE_15]Steps[SHORTCODE_16]  tab.
2. Click the [SHORTCODE_17]ADD STEP[SHORTCODE_18] button.
3. Name the new and currently empty step.
4. (Optional) Grab the step by clicking on the handle (dotted vertical lines at the top left of the step) and drag the step to the desired location in the sequence within the script. 
5. Add actions. You find more information on actions in the next paragraph.
6. Click the [SHORTCODE_19] Save [SHORTCODE_20] button to save your changes.

## What is an action?

Actions are your user interactions, content checks, and browser interactions that happen within a step. They are divided into the categories Interaction, Test, and Control.

#### Interaction

The actions of type *Interaction* are in short:

- **Navigate** — go to a specific URL
- **Click** — locate a page element like (radio) buttons or checkboxes and perform a mouse click 
- **Set** — locate and fill a text field, text area, password field, etc. 
- **Hover** — find an element and hover the cursor over the element to reveal other hidden page elements 
- **Key event** — perform a single key press, e.g. an element does not have a clickable button

These are described in detail in the knowledge base article [Page interactions]([LINK_URL_17]).


#### Test

The *Test* type actions are either content checks or enter a wait action. 

- **Element content** — find and check an element for specific content 
- **Document content** — check the entire page document for specified content 
- **Wait for element** — look for and wait for a specified page element 
- **Wait a fixed time** — add a custom wait time 

Refer to the the knowledge base articles [Content checks]([LINK_URL_18]) in transaction monitoring and [Using wait conditions]([LINK_URL_19]) to learn what they do actually.

#### Control

The action category *Control* contains the following options:

- **Screenshot** — take a screenshot of the current screen 
- **Switch browser tab** — give focus to the new window/tab, if your page opened another browser window
- **Switch frame** — allows you to [switch between iFrames]([LINK_URL_20]) on your page 
- **Scroll** — find a page element and scroll to the position on the page (especially helpful when using screenshots)
- **Adjust variable content** — change an existing variable with the [Adjust variable content]([LINK_URL_21]) action
- **Clear browser cache** — [clears the browser cache]([LINK_URL_22]) to reload page elements directly from the server instead of the browser cache

### Adding an action [ANCHOR_2]

To add a new action to one of the steps in your transaction monitor:

1. Open the step that you want to add an action to.
2. Click the [SHORTCODE_21]ADD ACTION[SHORTCODE_22] button. 
   The *Add action* pop-up opens:
   ![screenshot add action pop-up]([LINK_URL_23])
   Hovering over the action option gives you more information about that action. 
3. Click the action that you want to add to your step. 
4. (Optional) Reorder the actions, if necessary. Grab the action by clicking on the handle (dotted vertical lines at the top left of the action) and drag the action to the desired location in the actions sequence. You can also drag the action to another step, if needed.
5. Click the [SHORTCODE_23] Save [SHORTCODE_24] button to save your changes.

### CSS selectors and XPath queries [ANCHOR_3]

You may have noticed that some of the actions show CSS selectors or XPath queries. These tell the transaction monitor exactly which screen element it needs to interact with to complete the action. If you used the transaction recorder, it has already picked what it thinks is the best method for locating an element on your page as described in the knowledge base article [Transaction recorder selector determination]([LINK_URL_24]). 

However, the algorithm doesn't always pick the best option in all cases, but you can find the other options the recorder chose by clicking the [SHORTCODE_25]\[...\][SHORTCODE_26] button in the selector value field. 

Another option is to write your own selectors or queries. Learn more about [CSS selectors]([LINK_URL_25]) or [XPath queries]([LINK_URL_26]). When defining the selectors manually you can make use of [automatic variables]([LINK_URL_27]). This gives you even more flexibility in the selector choice. 

If you're not comfortable with CSS selectors and XPath queries, we suggest that you contact [Uptrends Support]([LINK_URL_28]) to have them make the needed changes.

### Action Settings

Your actions have different settings based on the action type. Please check out the knowledge base article [Page interactions]([LINK_URL_29]) to learn about all settings for each of those actions.


## Scripting source code directly [ANCHOR_4]

You can always write your scripts in a different editor or environment and cut and paste the script (or write the script directly in our text editor). Use the [SHORTCODE_27]Switch to script[SHORTCODE_28] button at the top of the [SHORTCODE_29]Steps[SHORTCODE_30] tab to open the text editor. Once in the text editor, click the [SHORTCODE_31]Switch to visual editor [SHORTCODE_32] to get back. When switching between these modes, the script is validated.

![screenshot visual and script editor view]([LINK_URL_30])

## Use the transaction API

You may wish to use the Uptrends' API to create monitors, upload scripts, alter scripts, and check your monitor's status. To learn about all of the available methods, please see the [API]([LINK_URL_31]) documentation.
