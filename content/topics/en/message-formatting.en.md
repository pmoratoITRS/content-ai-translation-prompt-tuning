{
  "hero": {
    "title": "Message formatting"
  },
  "title": "Message formatting",
  "summary": "Custom integrations - how to correctly format your message",
  "url": "/support/kb/alerting/integrations/custom-integrations/message-formatting",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/custom-integrations/message-formatting" 
}

Since the outgoing alert message will most often be JSON formatted, we need to adhere to rules to keep this JSON valid. To do so, certain characters (such as line breaks or quotation marks) will need to be encoded before they can be included in the outgoing, JSON-formatted alert message. If not, they would invalidate the JSON structure of the outgoing message, which could lead to the receiving endpoint to throw an error and not handle the incoming alert correctly. This article will go over the built-in functions for automatic message formatting.

## Applying automatic formatting {id="applying-automatic-formatting"}

For example, if a monitor ‘Notes’-field (which you can add to the alert message using the @monitor.notes system variable) contains such characters (line breaks, quotation marks, …), it would be resolved in such a way that would break the JSON structure of the outgoing message.  
  
As an example:  
`{ "notes": "{{@monitor.notes}}" }`  

Could resolve to:  
```json
{ "notes": "Monitor notes that include 
 a line break or "a quote"" }
 ```
  
This breaks valid JSON structure, and will likely lead to incorrect handling of the alert at the receiving end. To resolve this issue, we've included the option to encode (or decode) bits of text to correctly fit into a JSON- or XML-formatted message. When using this function, any characters that must be escaped in order to keep the JSON valid will automatically be encoded.  
  
To use this function, wrap the desired system variable or text in the following syntax:  
`{{@JsonEncode(your-variable-here)}}`  
  
For example, the previously mentioned monitor notes system variable should be wrapped as follows:  
`{ "Notes": "{{@JsonEncode({{@monitor.notes}})}}"}`  
  
Using the `@JsonEncode` function, the previously mentioned bit of JSON containing reference to the monitor notes now resolves to:  
`{ "notes": "Monitor notes that include\na line break or \"a quote\"" }`  
  
As you can see, we've now correctly included the monitor notes, encoded in such a way that it doesn't break the JSON structure.  
  
If you're using XML instead of JSON, have no fear - we support a similar function for XML encoding! You can use this function by wrapping your desired system variables in `{{@XmlEncode()}}`.
