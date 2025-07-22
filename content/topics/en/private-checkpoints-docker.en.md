{
  "hero": {
    "title": "User-managed checkpoints (Docker containers)"
  },
  "title": "User-managed checkpoints (Docker containers)",
  "summary": "What is a user-managed checkpoint and how do you implement Uptrends monitoring behind your company's firewall in Docker containers.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-docker",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-docker"
}

Uptrends provides a Docker container to run an Uptrends checkpoint on your network (behind your firewall). You get full Uptrends functionality on the private checkpoint and can conduct tests of your private infrastructure. Using the Uptrends application, you choose where your monitors' tests run: internal on your private checkpoint, external using Uptrends' [global network of checkpoints]({{< ref path="checkpoints" lang="en" >}}), or on both.

![](/img/content/private-checkpoint-overview.min.png)

While the tests take place on your network, all other activity such as scheduling, alerting, and reporting happens in the Uptrends cloud application, and Uptrends stores your monitor definitions and test data in their data centers.

Your private checkpoint is exclusive to your Uptrends account and for your use only. You can run monitors internally to check your non-Internet facing infrastructure such as:

- Intranet
- Internal web-enabled business applications
- Web services (APIs)
- Acceptance and other preproduction environments
- Basic infrastructure uptime monitoring for servers including database servers, email servers, and SFTP servers

## How does a private checkpoint work?

The setup works as follows: Uptrends' private checkpoint software is packaged in Docker containers. Those containers are hosted in your own network on a container platform. The platform can be your own host or virtual machine and other options like Azure are available as well. The instructions in [Install a Docker private checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}) focus on the setup using a virtual machine.

A private checkpoint uses at least two Windows Docker container instances running on your container platform connected to your network. These instances only have access to the monitored infrastructure on your network, and you'll need to isolate the Docker apps from the rest of your network. Uptrends provides the software running on these containerized checkpoints, while you keep the supporting hardware and infrastructure running.

The Uptrends monitoring system uses a central command and control system, the cloud platform. The cloud platform has your monitoring definitions, and it decides where and when the next monitor check should take place based on your checkpoint selection. When you configure a monitor to use a private checkpoint, Uptrends picks one of the container instances to conduct the monitor check. The container instance runs the tests and reports back to Uptrends. Uptrends processes and stores the resulting data from the test ran on your private checkpoint. If Uptrends detects an error, it immediately tests again on the other container instance. If the monitor detects an error the second time, Uptrends issues an alert from the cloud, see "Private checkpoint architecture" below.

If your checkpoint becomes completely unavailable for any reason, Uptrends issues an error to let you know that your private checkpoint has gone down. Some reasons downtime may happen include:

- The private checkpoint loses its internet connection.
- All your container instances use the same hosting platform, and that platform experiences an outage.

![](/img/content/private-checkpoint-architecture.min.png)

1. Outbound HTTPS (including WebSockets) connectivity to the Uptrends cloud platform for command and control, to retrieve monitor definitions and sending back results. The outbound WebSockets connection will be used to receive commands and will be open for a long period of time. Whitelisted for four Uptrends locations.
2. Outbound HTTPS connectivity to retrieve container updates with checkpoint and browser updates
3. Outbound internet connectivity to validate the revocation status of used certificates
4. Connectivity from the Uptrends private checkpoint to the monitored infrastructure, with blocked connectivity to all other parts of the platform

## How do I get a private checkpoint? 

Once you've decided to monitor your internal infrastructure with a Docker private checkpoint you need to prepare the infrastructure: set up (preferably 2) Windows Server based hosts as explained in the installation steps in [Install a Docker private checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}).

If you have any questions along the way, please don't hesitate to ask using Uptrends' [ticketing system]({{< ref path="contact" lang="en" >}}). Discussions with you and the decisions made will be logged in our ticketing system. You can review the discussions, make comments, and ask questions directly to the Support engineer assigned to your ticket.

## Security considerations

Although Uptrends applies industry best practices and due diligence for security matters, the responsibility for the impact of the private checkpoint on the client's network falls on the customer. Please find some detail below on who is responsible for which part.

### Uptrends' responsibilities

- Provide private checkpoints containers with up-to-date software
- Keep all software components used in the containers up to date (i.e. the image's base and the web browsers)
- Encrypt all traffic to and from the customer's platform
- Provide information for whitelisting

### Users' responsibilities

- Apply firewall rules to allow access to the infrastructure that needs monitoring only
- Use accounts in their monitoring with limited exposure to the platform
- Use virus scanning etc. where applicable
- Apply, when needed, extra safeguards (e.g., when a transaction does a repeated money transfer)
- Update the Docker host and containers preferably every day but at least every two weeks to make sure the most recent browser versions are in use and the latest security patches have been applied
- Keep the host operating system up to date
- Consider [disabling snapshots, screenshots and filmstrips]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) in basic and browser type monitors 

{{< callout >}} If you need further information, please visit [Private checkpoints FAQ]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq" lang="en" >}}). {{< /callout >}}
