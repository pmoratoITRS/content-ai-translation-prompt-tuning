{
  "hero": {
    "title": "Install certificates in Private locations"
  },
  "title": "Install certificates in Private locations",
  "summary": "Install certificates in Private locations for internal monitoring of your network infrastructure.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/install-certificates-private-locations",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

When setting up your [Docker-based Private Location]([LINK_URL_1]), you may need to install certificates to establish trust and authenticate connections with the website or web service you're monitoring.

The following types of certificates are available for installation:

- Client certificates (PKCS #12)
- Intermediate Certificate Authority (CA) certificates (PKCS #7)
- Root Certificate Authority (CA) certificates (PKCS #7)

Note that the [Uptrends Docker-based installation zip file]([LINK_URL_2]) contains a **Certificates** folder. Inside, you'll find subfolders for each supported certificate type, where certificates can be installed as described below.

## Install certificates on a Docker-based Private location

This section is an optional installation guide for certificates on Docker-based Private locations. These steps are only needed if any of your applications under test require installing a certificate.

Before installing the certificates, ensure you've followed the installation steps for [Docker-based Private locations]([LINK_URL_3]).

### Install Certificate Authority (CA) certificates

**To install CA certificates:**

1. Open the folder containing your private location installation. You'll find several files included by default, such as the [INLINE_CODE_1] YAML file and Windows PowerShell scripts. These files are essential for the installation process.

2. Open the **Certificates** folder. This folder contains three subfolders and a [INLINE_CODE_2] Markdown file.

3. Place your CA certificates in the appropriate **Certificates** subfolders:

  - **Intermediate** folder — for all the Intermediate Certificate Authority (CA) certificates (PKCS #7) files.
  - **Root** folder — for all the Root Certificate Authority (CA) certificates (PKCS #7) files.
  
4. Restart the Uptrends checkpoint software by running the [INLINE_CODE_3] script from the installation root directory.

### Install Client certificates

Note that the [Client certificates in Multi-step API (MSA) monitors]([LINK_URL_4]) and Client certificates for Private locations are unrelated and serve for different purposes.

**To install Client certificates:**

1. Open the folder containing your private location installation. You'll find several files included by default, such as the [INLINE_CODE_4] YAML file and Windows PowerShell scripts. These files are essential for the installation process.

2. Open the **Certificates** folder. This folder contains three subfolders and a [INLINE_CODE_5] Markdown file.

3. Place your Client certificate in the **Client** folder.

4. In the **Client** folder, create a JSON file called [INLINE_CODE_6]. This JSON file should list all your Client certificates. Otherwise, proceed to the next step.

- Copy and edit the JSON template to get started:

[CODE_BLOCK_1]

Notice that the JSON snippet consists of two Client certificates. Each Client certificate is represented by a JSON object with three key-value pairs. The first certificate, [INLINE_CODE_7], is allowed to be used for a specific subdomain. While the second certificate, [INLINE_CODE_8], is allowed to be used for the client's subdomain of [INLINE_CODE_9] when connecting to HTTPS port 1234, or when visiting [INLINE_CODE_10] or any of its subdomains.

Edit the following values based on your requirements:

  - [INLINE_CODE_11] — the filename and file extension of your Client certificate.
  - [INLINE_CODE_12] — the password needed to access the data in the certificate archive, such as the private key.
  - [INLINE_CODE_13] — the list of allowable URL domains or subdomains that will use the Client certificate. This list can consist of multiple URL patterns which can be a single domain, subdomain, or a wildcard for a domain and all of its subdomains. To learn more, refer to [Enterprise policy URL pattern format]([LINK_URL_5]).

5. Restart the Uptrends checkpoint software by running the [INLINE_CODE_14] script from the installation root directory.

6. Verify that both the old and new certificates are recognized and installed correctly. If you encounter any issues, do a basic troubleshooting:

- Verify that the JSON filename is correct.
- Ensure that all JSON key-value pairs adhere to correct JSON syntax.
- Check for any misconfigurations or permission issues.
