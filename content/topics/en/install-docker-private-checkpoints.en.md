{
  "hero": {
    "title": "Install a Docker checkpoint"
  },
  "title": "Install a Docker checkpoint",
  "summary": "Implement a Docker host and checkpoint containers for internal monitoring of your network infrastructure.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/install-docker-private-checkpoints"
}

This knowledge base article provides a setup guide to configure Windows Server 2022 or 2019 as a host operating system. It also explains how to set up and start a containerized [Docker private checkpoint]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-docker#how-do-i-get-a-private-checkpoint" lang="en" >}}).

Before installation, ensure that all the [requirements and settings]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements" lang="en" >}}) are met. Uptrends will provide you with all the necessary files to get started.

## Installation script

Uptrends provides an installation script that you can download as a .zip file from the {{< AppElement type="menuitem" >}} Private locations {{< /AppElement >}} menu of the [Uptrends app](https://app.uptrends.com/PrivateLocations). This script is available for each of your [Private locations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="en" >}}) and performs the main installation steps. These steps include installing Docker and Docker Compose, pulling the Uptrends container images, performing a startup and update task, and starting the containerized checkpoint.

## Installation steps

**To install a checkpoint using the script:**

1. Go to the {{< AppElement type="menuitem" >}} Private locations {{< /AppElement >}} menu.
2. If you haven't added any [Private locations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="en" >}}), click the {{< AppElement type="buttonPrimary" >}} Add location {{< /AppElement >}} button. Once added, two checkpoints will be included by default.
3. Click the Private locations' checkpoint name.
4. Select the required operating system from the **Host Operating System** dropdown.
5. Click the {{< AppElement type="buttonPrimary" >}} Download installation zip file {{< /AppElement >}} button.

{{< callout >}} **Important:** Keep in mind that the downloaded .zip file only contains the specific Private locations checkpoint you selected from the two default options. Your .zip file has a file name UptrendsCheckpoints\<checkpoint-name\>.zip, where \<checkpoint-name\> is the name of your checkpoint. {{< /callout >}}

5. Unzip the downloaded file in the place where you want to install the private checkpoint.
6. To prevent screenshots from uploading to the cloud, [edit the docker-compose file]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection#disable-screenshots-in-docker-compose-file" lang="en" >}}) after downloading and extracting the files.

{{< callout >}} **Important:** Depending on your company's policies, you might need to unblock all the Powershell script files (*.ps1) in the zip folder before running them. For more information, see the [instructions](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/unblock-file?view=powershell-5.1) on how to unblock files. {{< /callout >}}

7. Open a PowerShell console and run it as Administrator. Run the script `./install-checkpoint.ps1` in the Uptrends (unzip) directory. This will restart the server once. Note that the script will configure a task that runs once every hour to check the Uptrends containers for updates.

The checkpoints are now available and can be selected on the monitor's {{< AppElement type="tab" >}} Checkpoints {{< /AppElement >}} tab. You can also see the checkpoints in the *Check details* dialog when running a quick test directly from the monitor using the {{< AppElement type="buttonSecondary" >}} Test now {{< /AppElement >}} button.

To install certificates in Private locations, see [Install certificates in Private locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-certificates-private-locations" lang="en" >}}).

## Monitoring your private checkpoint

Uptrends will make changes to your account to better assist you in monitoring your private checkpoints. Please ensure that all your private checkpoint's servers, firewall, internet connection, and other supporting systems remain accessible.

During the private checkpoint setup, Uptrends will add additional monitors and configurations. Please do not delete or modify anything in your account.

For more information, refer to the [How to use Private locations]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use" lang="en" >}}) knowledge base article.