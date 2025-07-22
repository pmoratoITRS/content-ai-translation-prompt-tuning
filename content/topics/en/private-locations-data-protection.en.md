{
  "hero": {
    "title": "Private location data protection"
  },
  "title": "Private location data protection",
  "summary": "What are the data protection safeguards for private locations?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-locations-data-protection"
}

In this knowledge base article, you will find an explanation on how to implement data protection on your private locations. One of the safeguards implemented in Uptrends' private locations is preventing snapshots from being uploaded to the cloud. You can also disable page content, hide HTTP request and response headers and resolved IP addresses in check results.

## Editing the Docker Compose file

First, if you have not already done so, install your checkpoint by following the steps explained in [Install a Docker checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}).

1. Make a backup of the extracted Docker Compose file. Please be aware that if you make changes to the provided compose file this is at your own risk. Contact [Support]({{< ref path="/contact" lang="en" >}}) if you are not sure. 
2. Open the docker-compose.yml file and remove the comment tag ``#`` before the data protection variable(s) in the Checkpoint service you want to enable. By deleting the tag, data protection will be set up for the selected environment list item. 


 ```
 Checkpoint:
    container_name: Checkpoint
    image: uptrends.azurecr.io/win2022/checkpoint
    depends_on:
      - TransactionProcessor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: "json-file"
      options:
        max-size: 10m
        max-file: "3"
    environment:
     - ServerId=
     - Password=
     - HasIpv6Support=false
#    - AllowScreenshotsInResults=false
#    - AllowPageContentInResults=false
#    - AllowHttpHeadersInResults=false
#    - AllowResolvedIpAddressesInResults=false
  
 ```    
3. Save your file. 
4. Restart the container manually by executing the command ```docker-compose down```, and then executing ```docker-compose up``` in the command-line of the folder where the edited Compose file lives. In the Uptrends app, check the changed settings in the [data protection settings](#data-protection-settings-status) section on the {{< AppElement type="tab" >}} Checkpoint health {{< /AppElement >}} tab.
 
### Prevent (error) screenshots and filmstrips from uploading to the cloud
After the setting is active, the **check details** in Uptrends will display a text to inform you that screenshots are not collected due to your company's data protection policy. 

This holds true for all screenshots, including [timeline screenshots]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/timeline-screenshots" lang="en" >}}) (also called filmstrips) and the [error screenshot]({{< ref path="support/kb/alerting/errors/working-with-error-snapshots" lang="en" >}}) for an HTTP(S) monitor.

To disable screenshots in results, remove the ``#`` tag before `- AllowScreenshotsInResults=false` in the list of Checkpoint environment variables. Save the file and manually restart the Docker container, as described in the last step of the editing instructions above, to reflect the changes in the data protection settings in the Uptrends app.

{{< callout >}} **Important**: Disabling screenshots means just that. No screenshots will be made. So, when [troubleshooting]({{< ref path="support/kb/synthetic-monitoring/monitoring-results#further-troubleshooting" lang="en" >}}) an error, this source of information will not be available.
 {{< /callout >}}

### Disable page content 
This setting will make sure no content is being shown in the [page source and console log]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/page-source-and-console-log" lang="en">}}). Data URLs will always be displayed without data in the results. 

To disable page content in results, remove the ``#`` tag before `- AllowPageContentInResults=false` in the list of Checkpoint environment variables. Save the file and manually restart the Docker container, as described in the last step of the editing instructions above, to reflect the changes in the data protection settings in the Uptrends app.

### Hide HTTP request and response headers
After this setting is active, the check details waterfall chart will not show any HTTP request and response headers.

To hide HTTP request and response headers, remove the ``#`` tag before `- AllowHttpHeadersInResults=false` in the list of Checkpoint environment variables. Save the file and manually restart the Docker container, as described in the last step of the editing instructions above, to reflect the changes in the data protection settings in the Uptrends app.
![Data protection hidden HTTP request and response headers in Waterfall Chart](/img/content/scr-data-protection-waterfall-headers.min.png)

### Disable resolved IP addresses for request and response headers
This setting makes sure that the report headers in a check result do not show any resolved IP addresses. Please note this will not work if there is a literal IP address instead of a domain value in the URL field of your monitor(s). 

To hide resolved IP addresses, remove the ``#`` tag before `- AllowResolvedIpAddressesInResults=false` in the list of Checkpoint environment variables. Save the file and manually restart the Docker container, as described in the last step of the editing instructions above, to reflect the changes in the data protection settings in the Uptrends app.

### Disable resolved IP addresses in check details 
This setting controls that anywhere an IP address has been resolved, it does not show at **Resolved IP address**.   

To hide resolved IP addresses, remove the ``#`` tag before `- AllowResolvedIpAddressesInResults=false` in the list of Checkpoint environment variables. Save the file and manually restart the Docker container, as described in the last step of the editing instructions above, to reflect the changes in the data protection settings in the Uptrends app.

DNS monitors will be blocked from executing on checkpoint servers in your private location if this value is set to false.

{{< callout >}} **Please note**: Not all settings cover every monitor type, e.g., for basic HTTP(S) monitors only error screenshots will work, the resolved IP settings are not applicable to this type of monitor. 
{{< /callout >}}

## Data protection settings status 

The [Checkpoint health]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="en" >}}) tab in the Uptrends app shows the status of the data protection settings. A red cross means data will not be displayed, so data protection is enabled. Please note that this is a read-only display, the settings can only be adjusted in the Docker file. 

![Data protection settings on Checkpoint Health tab](/img/content/scr_private-location-checkpoint-health-data-protected.min.png)