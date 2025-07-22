{
  "hero": {
    "title": "Monitor Notes"
  },
  "title": "Monitor Notes",
  "summary": "Adding and editing notes in your monitors and using them to make communication easier.",
  "url": "/support/kb/synthetic-monitoring/monitor-settings/monitor-notes",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/monitor-notes"
}

 Uptrends' monitor notes can be used for internal communication between operators. It's an easy way to quickly discuss issues concerning (settings of) the monitor. The **Monitor status** dashboard will show which monitors have a note and give easy access to read that note without having to leave the screen. This allows operators to get easy access to internal status information left by another operator, like: 

- Monitor status 
- Frequent errors and instructions on how to solve when the error occurs  
- Quick view on who is working on it so other team members can focus on other issues 

For example, an _SSL Certificate_ monitor. The monitor warns the certificate will expire in advance. Next, an operator takes action to renew the certificate and records in the note that action is taken. After renewal of the certificate the text in the **Notes** field can be cleared.  
 
## How to add monitor notes 
Every monitor's edit screen contains a free-form text format **Notes** field. 
To access your monitor settings:
1. Go to the menu {{< AppElement type="menuitem" >}} Monitors > Monitor Setup {{< /AppElement >}}. 
2. Click on {{< AppElement type="menuitem" >}} Monitor Setup {{< /AppElement >}}.
3. Look for the name of the monitor you want to access the settings for. Click on its corresponding link under the **Monitor Name** column. Or, you can filter the results by entering (a portion of) the monitor’s name, type, group, or URL in the search box and press Enter. 
4. The monitor configuration screen will open on the {{< AppElement type="tab" >}} Main {{< /AppElement >}} tab. 
![Entering a note in the free-form text-field](/img/content/scr-monitor-settings-notes.min.png)
5. Enter notes in the **Notes** field, under **Meta data**.  
6. If you have entered notes you wish to keep, make sure to click the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button. 

## Where are notes displayed? 
Notes are shown on the **Monitor status** dashboard. (Go to menu {{< AppElement type="menuitem" >}} Monitoring > Status details {{< /AppElement >}}). The second dashboard column will show which monitors have a note. If so, a dark note icon will be displayed. If there is no text to show, the icon will be light gray. An operator can read the note's text by hovering over it.

![Notes in monitor status dashboard](/img/content/scr-monitor-status-show-notes.min.png)

Notes are also visible on a monitor's quick-info panel:

![Notes in quick-info panel status dashboard](/img/content/scr-monitor-notes-q-inf-pan.min.png)
## Who has access to monitor notes? 
Go to {{< AppElement type="menuitem" >}} Account setup > Account settings {{< /AppElement >}}. On the {{< AppElement type="tab" >}} Settings {{< /AppElement >}} tab under Access to monitor notes you configure the right to view notes for operators.
![Access to monitor notes](/img/content/scr-monitor-notes-permissions.min.png)
Note: The access setting is available for Enterprise accounts only. 