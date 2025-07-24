{
  "hero": {
    "title": "Setting up a SOAP web service monitor"
  },
  "title": "SOAP Setup",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/api-monitoring/setting-up-a-soap-web-service-probe",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

If you’re looking to add a **SOAP monitor** to your Uptrends account, you'll find the instructions in this article.

## Setting up a SOAP Web Service monitor

To test a SOAP service, you typically want to call a method of that web service, by posting input data to it in the form of a SOAP envelope and then verifying that the response is correct.

1.  Get to the Add Monitor configuration screen. (If you need a refresh on how to do this, please refer to the [Add a monitor]([LINK_URL_1]) article) Set your monitor type to Web Service HTTP or Web Service HTTPS.  
      
    [SHORTCODE_1]**Note**: Using the Web Service monitor type ensures that we’re using Content-Type: text/xml when sending requests to your server. Since SOAP envelopes are in XML format, this should work for most web services.[SHORTCODE_2] 
2.  Fill in the appropriate name, check interval, URL, and port information.  
3.  Navigate to the [SHORTCODE_5]Advanced[SHORTCODE_6] tab, and set the HTTP method to POST.  
4.  Specify your SOAP request (the entire SOAP envelope) in the Post Data field.  
      
    Typically it will look like this:  
    *…Message information goes here…*  
5.  Your web server likely expects a SOAPAction HTTP header, which tells the server which method your web service should execute.  
      
    In the HTTP headers field, specify the header in the following format:  
      
    [INLINE_CODE_1]
      
    [SHORTCODE_3]**Note**: If your web server expects a different content type, you can specify a different Content-Type in the HTTP headers field. For example: Content-Type: application/xml[SHORTCODE_4] 
6.  It is likely useful to verify that your web service comes back with the appropriate content.  
      
    You can look for a specific piece of content by specifying it in the *Page Content Match* field, located in the [SHORTCODE_7]Error conditions[SHORTCODE_8] tab.  
      
    The Uptrends service will then look for that content in the HTTP response every time it performs a check.

## Can't get your SOAP monitor to work?

If you can’t get your SOAP monitor to work, please contact support by [filing a support ticket]([LINK_URL_2]).

If possible, please provide a screen capture of an HTTP request that is known to work. Usually you will have a working setup in your own web service test tool, which you can use to provide a Fiddler capture, or a cURL command which contains all the necessary data (URL/POST data/HTTP headers.)
