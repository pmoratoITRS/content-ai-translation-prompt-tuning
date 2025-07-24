{
  "hero": {
    "title": "Monitor Notes"
  },
  "title": "Monitor Notes",
  "summary": "Adding and editing notes in your monitors and using them to make communication easier.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/monitor-settings/monitor-notes",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

 Uptrends' monitor notes can be used for internal communication between operators. It's an easy way to quickly discuss issues concerning (settings of) the monitor. The **Monitor status** dashboard will show which monitors have a note and give easy access to read that note without having to leave the screen. This allows operators to get easy access to internal status information left by another operator, like: 

- Monitor status 
- Frequent errors and instructions on how to solve when the error occurs  
- Quick view on who is working on it so other team members can focus on other issues 

For example, an _SSL Certificate_ monitor. The monitor warns the certificate will expire in advance. Next, an operator takes action to renew the certificate and records in the note that action is taken. After renewal of the certificate the text in the **Notes** field can be cleared.  
 
## How to add monitor notes 
Every monitor's edit screen contains a free-form text format **Notes** field. 
To access your monitor settings:
1. Go to the menu [SHORTCODE_1] Monitors > Monitor Setup [SHORTCODE_2]. 
2. Click on [SHORTCODE_3] Monitor Setup [SHORTCODE_4].
3. Look for the name of the monitor you want to access the settings for. Click on its corresponding link under the **Monitor Name** column. Or, you can filter the results by entering (a portion of) the monitor’s name, type, group, or URL in the search box and press Enter. 
4. The monitor configuration screen will open on the [SHORTCODE_5] Main [SHORTCODE_6] tab. 
![Entering a note in the free-form text-field]([LINK_URL_1])
5. Enter notes in the **Notes** field, under **Meta data**.  
6. If you have entered notes you wish to keep, make sure to click the [SHORTCODE_7] Save [SHORTCODE_8] button. 

## Where are notes displayed? 
Notes are shown on the **Monitor status** dashboard. (Go to menu [SHORTCODE_9] Monitoring > Status details [SHORTCODE_10]). The second dashboard column will show which monitors have a note. If so, a dark note icon will be displayed. If there is no text to show, the icon will be light gray. An operator can read the note's text by hovering over it.

![Notes in monitor status dashboard]([LINK_URL_2])

Notes are also visible on a monitor's quick-info panel:

![Notes in quick-info panel status dashboard]([LINK_URL_3])
## Who has access to monitor notes? 
Go to [SHORTCODE_11] Account setup > Account settings [SHORTCODE_12]. On the [SHORTCODE_13] Settings [SHORTCODE_14] tab under Access to monitor notes you configure the right to view notes for operators.
![Access to monitor notes]([LINK_URL_4])
Note: The access setting is available for Enterprise accounts only. 