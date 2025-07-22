{
  "hero": {
    "title": "Multi-step monitoring Client certificates"
  },
  "title": "Multi-step monitoring Client certificate authentication",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-client-certificate-authentication"
}

Many APIs require that the caller specifies authentication information to verify their identity, and possibly the access rights of that caller. Authentication information can be passed along using HTTP headers (Basic/NTLM/Digest authentication), by exchanging access tokens (OAuth), by requiring the client to include a client certificate in the request, or a combination.

This article discusses the options for **client certificates**. To set up traditional authentication methods, please [read the article on authentication types](/support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication).

## Client certificate types

The *Client certificate* section on the {{< AppElement type="tab" >}} Request {{< /AppElement >}} tab of a Multi-step API step offers the following options. If you're using multiple steps in your step definition, please ensure you have the desired settings for each step.

-   **Uptrends client certificate**: This option is useful if you require your API users to generate and include their own client certificate to prove their identity. If you choose this option, a certificate owned by Uptrends will be included when the HTTP request is sent. Your API can verify that incoming request using the corresponding public key. If it matches, you can be sure that the request is coming from someone who owns the original certificate (i.e. Uptrends), and no-one else. The certificate is not available on (containerized) [private checkpoints.](/support/kb/synthetic-monitoring/checkpoints/private-locations) 
For more information, please read the article about [Uptrends' public key information](/support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information). 
-   **Custom client certificate**: Use this option when you own or control the client certificate that should be included in the request. Once you've uploaded the certificate file to Uptrends, you can include it in your Multi-step API monitors. Since you own that certificate, your API will be able to verify incoming requests that use it. Please read the next section for setting this up.
-   **None**: Choose *None* if you don't want to include any client certificate in your HTTP request.

## Setting up a user-defined or individual client certificate

To include a client certificate into the Multi-step monitor, you first have to upload it to Uptrends. Certificates (and other sensitive information) are uploaded to and saved inside the vault. Once you have added a certificate file to the vault, you can use it when setting up monitoring.

### Uploading a client certificate

When choosing the option of an individual client certificate for the first time, you'll see that there are no certificates available yet. To add a certificate, click *Add item* to switch to the vault. Alternatively, go to the menu {{< AppElement type="menuitem" >}}Account setup > Vault{{< /AppElement >}} , open a vault section and click {{< AppElement type="button" >}}Add vault item{{< /AppElement >}}.

On the page *New vault item* enter a unique name for the certificate, so that you can find it back later. Make sure that the Type of the new vault item is set to **Certificate archive**. Enter all information that you regard important into the *Description*.

Finally, choose a certificate file that you want to upload. The file must have the PKCS \#12 format or must be a certificate archive that includes both the private and the public key. Files with the PKCS \#12 format have the extension .pfx or .p12.

A certificate archive file is encrypted in most cases. Therefore we'll need the corresponding password to use the archive. Please enter the password in the *Archive password* field and click {{< AppElement type="savebutton" >}}Save{{< /AppElement >}}.

### Using client certificates in Multi-step monitor

As soon as you've saved an appropriate client certificate in the vault, you can use it for Multi-step API monitoring. In the section **Client certificate** of a step, click **Refresh** to update the list of available certificates. Then, for each step that requires a certificate choose the corresponding certificate.
