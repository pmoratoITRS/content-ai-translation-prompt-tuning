{
  "title": "Uptrends' client certificate public key information",
  "summary": "By using the Uptrends public key with your Multi-step API monitor, you ensure that API monitor requests originate from Uptrends.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/uptrends-client-certificate-public-key-information"
}

The Uptrends client certificate can be used in Multi-step API monitors to guarantee the authenticity of the HTTP requests created by your monitors: your API server can verify the identity of Uptrends' checkpoint servers, which is where the HTTP requests are sent from.

The checkpoint servers will use the certificate's private key to sign the requests. No-one else has access to that private key, so no-one can sign a request in the same way and pretend to be Uptrends. This means that you, as the receiving party, can be sure that those requests are genuinely originating from Uptrends' servers. You do this by verifying the identity of the incoming requests using Uptrends' public key. The public key information is listed below.

{{< callout >}}
**Please note:** the Uptrends client certificate is not available on (containerized) [private checkpoints.](/support/kb/synthetic-monitoring/checkpoints/private-locations) 
{{< /callout >}}


## How can I be sure this public key is genuine?

When establishing identity and authenticity, it's important to verify you're working with the correct information.

### Trusted connection and transport

-   We've made sure that you're always reading the content on this page using an HTTPS connection. Having this secure connection means that the content can never be tampered with (no content hijacking) during transport from our web server to your browser.
-   Even if a malicious person manages to present an HTTP link (i.e. a non-secure one) to the Uptrends website to you, that could subsequently be intercepted and the content be tampered with (a so-called downgrade attack), your browser will not accept that. Browsers will refuse to contact Uptrends over a non-secure connection, for the following reasons:
    -   The Uptrends website and customer app portal have a HTTP Strict Transport Security (HSTS) policy in place. This means that browsers are instructed never to follow an insecure HTTP link to the uptrends.com domain, but always use HTTPS instead.
    -   The uptrends.com domain was among the first 1,000 domains who were listed in the HSTS preload list. This preload list is hard-coded in mainstream browsers like Chrome, Edge, Opera, and Safari, which means that those browsers are hardwired to always use HTTPS for uptrends.com and its sub-domains.

### Trusted identity

If you review the TLS certificate for this site, you'll notice that this website is owned by Uptrends B.V. The certificate is signed by Sectigo Limited, one of the worldwide recognized Certificate Authorities. Your browser wouldn't even trust the connection without a CA signing it. This is the best available way to prove that the domain you’re currently visiting is in fact owned by Uptrends, and that you can trust that its content is coming from Uptrends.

## Public key information

The following information describes properties of the public key that corresponds to the client certificate used by Uptrends' checkpoint servers, when they're instructed to do so. This client certificate, just like the certificates pertaining to our web sites, have been signed by a Certificate Authority.

| Description | Value |
|--|--|
| **Issuer** |{{< tableformatter >}} 
CN = Sectigo RSA Client Authentication and Secure Email CA

O = Sectigo Limited

L = Salford

S = Greater Manchester

C = GB

{{< /tableformatter >}}|
| **Subject** |{{< tableformatter >}} 
E = certificates@uptrends.com {{< /tableformatter >}}|
| **Common name**	 | Uptrends |
| **Serial number** | 1a223e5481b066dfda30e5f35cdb3a81 |
| **Expiration date** | Sunday, 27 July 2025 01:59:59 |
| **Full public key (Base64)** | {{< tableformatter >}} —–BEGIN CERTIFICATE—– 

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

—–END CERTIFICATE—– {{< /tableformatter >}}|