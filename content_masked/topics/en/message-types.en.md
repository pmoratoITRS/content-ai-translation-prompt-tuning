{
  "hero": {
    "title": "Message types"
  },
  "title": "Message types",
  "summary": "Custom integrations - descriptions of the various message types",
  "url": "[URL_BASE_TOPICS]alerting/integrations/custom-integrations/message-types",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Alerting messages come in different types. Uptrends makes the distinction between **Error** messages, **Reminder** messages, and **Ok** messages. By default, all these message types are created with the same setup. However, when setting up a custom integration or customizing an existing integration, you can create different sets of actions for each individual message type.

## Error messages, OK messages, and Reminders

When you create a message definition in the [SHORTCODE_1]Customizations[SHORTCODE_2] tab, Uptrends uses that message definition for all error types: an Error alert when the check first generated the alert, an OK alert when the check resolves the alert, and Reminder alerts (depending on your escalation level settings) in between.

The message contents are practically the same for all alert types, except for any timestamp values, and the [SYSTEM_VAR_1] variable, which outputs the alert type itself.

Although fine for a lot of situations, using the same message content is not sufficient if you need different content for different alert types, or if you need to create a new incident in your system (based on an Error alert) requiring a different URL than resolving that same incident (based on an OK alert).

### Separate messages for different alert types

To create separate message definitions for alert types, click the "Add steps" button at the bottom of the [SHORTCODE_3]Customizations[SHORTCODE_4] tab. The "Add steps" button creates an additional message definition which you can configure, for example, to only apply to OK alerts. For each alert type, you can now specify the appropriate HTTP method (GET/POST/PUT/PATCH/DELETE), URL, headers, and request body.

Click the *Error alert*, *OK alert* and *Reminder alert* checkboxes at the top of each step definition to create the desired setup. You can only check each alert type once, but OK alerts and Reminder alerts are optional. If you don't want to send OK alerts or Reminders at all, simply leave those checkboxes unchecked.

### Error alerts and OK alerts belong together

Whether you're using separate messages for Error and OK alerts or not, it's probably useful for the external system to know which alerts belong together. After all, each incident starts with an Error alert and ends with an OK alert. To help the external system understand this, you can use the [SYSTEM_VAR_2] variable in your messages. Error and OK alerts share the same incident key, but each new incident has a unique key. In some systems, the incident key is called a deduplication key or incident Id.
