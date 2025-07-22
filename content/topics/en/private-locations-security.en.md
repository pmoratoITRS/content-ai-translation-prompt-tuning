{
  "hero": {
    "title": "Private locations and security"
  },
  "title": "Private locations and security",
  "summary": "What should be considered to ensure secure operations of checkpoints in private locations?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-security",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-security"
}

If you are wondering about the security of the installation of private location checkpoints and what you should do yourself to protect your data, please read on. This article explains the main security measures that are taken by Uptrends or are your responsibility. 

## Containers 

The installation of a private location checkpoint is based on Docker containers. There are some 'built-in' security features as well as some measurements taken by Uptrends:

- Uptrends is using its own container repository on Microsoft Azure. This allows you to work with a small repository, containing only the trusted containers that you are looking for. 
- Docker takes care of container verification.
- Uptrends scans the contents of the container images, using security scanning software, prior to uploading them to the container repository. This helps ensure Uptrends catches known vulnerabilities before shipping new versions of containerized software. In addition, we suggest that you also scan the container packages (updates) after downloading them and before installing them.
- By design Docker containers are restricted in the incoming communication from the outside world and communication on the host where they are located. You do not need to open incoming firewall ports. 
- The standard private location installation installs a script that will auto-update the Docker containers. This ensures that the private locations will always run based on the latest security updates. 

## Software (other than Docker containers installation)

The operation of checkpoints requires the checkpoint software but it also involves some supporting software. Think about the following topics:

- [Updates]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-docker#security-considerations" lang="en" >}}) of Windows, browsers, etc are necessary to get any bug fixes as soon as they are available and that way fix possible security problems.
- Uptrends is ISO 27001 certified. This certification handles information security and development practices like:
  - Changes to Uptrends' software are peer reviewed.
  - There are tools and procedures in place to defend against vulnerabilities in software dependencies.
  - There is a formal security officer and Uptrends has procedures in place for security incidents. 
  - Check out Uptrends' [ISO 27001 certificate](https://www.uptrends.com/downloads/uptrends-iso-certificate-2022.pdf).
- For a Windows host, an anti-virus scanner on the host is sufficient. Most anti-virus scanners are able to scan the processes and traffic inside the container. However, you should check this for the anti-virus scanner you are using.

## Network traffic 

The monitor checks involve some network traffic where data and requests are travelling inside and sometimes outside your network. Check out the following situations:

- You should always restrict network access to the necessary minimum. 
- The private locations do not require incoming connections, and we recommend that those are disabled completely. Any connections to the outside will be outgoing, and will always be initiated by the host. 
- The instructions that a checkpoint receives from the Uptrends Cloud are signed with a secret key. The checkpoint validates incoming instructions using the corresponding public key (known at the checkpoint) and that way ensures that the instruction is genuinely sent by Uptrends.

## Data privacy / protection

Monitoring is all about data ranging from simple information if a check was "OK" or produced an error to more in-depth information like screenshots of your website at a certain transaction step. You may want to know what kind of information is sent to the Uptrends cloud environment and which information you can restrict from leaving your site.

- Health data of the checkpoint is sent to the Uptrends cloud application. This is needed to determine if the checkpoint is working and working correctly. An outdated or incompatible checkpoint can be spotted with the health information. A non-working checkpoint may lead to wrong monitoring results. 
- The health data is visible on the health tab of the private locations.
- Other than checkpoint health info only the measurements information is sent to the Uptrends cloud.
- If you are concerned about sending measurement information outside your company, please check the knowledge base article [Data protection]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) to find out how to disable collecting certain information, e.g. screenshots, IP addresses, etc.

Another topic that should be considered carefully when it comes to data and privacy is login credentials. Uptrends strongly advises you to be careful about which credentials you use as part of your monitoring. You should never use a really powerful user in a system to do basic tasks. Keep the permissions/rights assigned to a user to the minimum that is needed to carry out their tasks. Any rights that go beyond this, may give access to assets or tasks that the user should not be able to access. Please see  [Login credentials]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#login-credentials" lang="en" >}}) for more information on this topic. 
