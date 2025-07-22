{
  "hero": {
    "title": "Multi-step API script editor"
  },
  "title": "Multi-step API script editor",
  "summary": "An overview of the Multi-step API monitor script editor",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/msa-script-editor",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Like for [transaction monitors]([LINK_URL_1]), the Multi-step API monitor type comes with a script view editor as an alternative to the default visual editor. The script editor allows you to make changes to the steps of your monitor, much like the visual editor, but in a JSON script instead of the UI. 

## Advantages of the script editor

There are several advantages to using a script editor rather than making changes to the monitor through the UI:

- Power users may find making edits directly in a script easier than navigating through a UI. Some users prefer an experience similar to using a command line. 
- Having a script available enables automation, for example to accomodate your [CI/CD process]([LINK_URL_2]). Using the [Uptrends API]([LINK_URL_3]), you can update the steps of the monitor at the same time as you're updating the API it checks. 
- The script editor allows you to make a local copy of the steps in your monitor, by simply copying the script and pasting it into a local file. Keeping a local copy allows for version control, backups of your multi-step API monitors, and easy replication of complicated setups.

## Switching to the script editor

You can switch to the script editor for any Multi-step API monitor by navigating to the monitor options, going to the [SHORTCODE_1] Steps [SHORTCODE_2] tab, and clicking the [SHORTCODE_3] SWITCH TO SCRIPT [SHORTCODE_4] button in the top right. Switching to and from the script editor will trigger validation, so make sure that the JSON in the script view remains valid. The script will look as follows:

![The script editor]([LINK_URL_4])

## Understanding the script

As you can see, the script is essentially a JSON formatted array of individual steps, containing their request method, URL, any headers and request body you've configured, and the authentication options. Furthermore, each step entry contains the definitions for any variables created from or assertions on the response. Any necessary changes can be made directly in the script editor.

An individual step will look roughly like this:

[CODE_BLOCK_1]

Adding extra steps is as simple as adding extra entries into the array, using the complete step definition as outlined above. 

After the array containing the steps, the step definition will also contain information about any [predefined variables]([LINK_URL_5]) or [user-defined functions]([LINK_URL_6]) you have set up:

[CODE_BLOCK_2]