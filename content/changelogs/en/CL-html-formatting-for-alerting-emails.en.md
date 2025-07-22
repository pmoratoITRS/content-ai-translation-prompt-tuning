{
  "title": "HTML formatting",
  "date": "2024-02-28",
  "url": "/changelog/february-2024-html-formatting-for-alerting-emails",
  "translationKey": "https://www.uptrends.com/changelog/february-2024-html-formatting-for-alerting-emails"
}


It is now possible to enable HTML formatting for alerting emails. You can change the outgoing email format of alerting emails to HTML, which will show a basic formatted email and replace plain text links with text with a hyperlink. 

To format outgoing alerting emails with HTML, go to the Alerting by email integration in the menu under {{< AppElement type="menuitem" >}} Alerting > Integrations {{< /AppElement >}}, select the Customize integration box, go to the {{< AppElement type="tab" >}} Customizations {{< /AppElement >}} tab, and select *Use HTML mail*.

Changing from plain text to HTML formatting in alert emails may cause issues with automated systems that use the plain text alerting emails. As a result, this option is not enabled by default for existing accounts, but it is enabled by default for new accounts.