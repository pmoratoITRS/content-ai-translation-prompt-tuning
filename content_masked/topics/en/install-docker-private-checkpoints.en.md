{
  "hero": {
    "title": "Install a Docker checkpoint"
  },
  "title": "Install a Docker checkpoint",
  "summary": "Implement a Docker host and checkpoint containers for internal monitoring of your network infrastructure.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

This knowledge base article provides a setup guide to configure Windows Server 2022 or 2019 as a host operating system. It also explains how to set up and start a containerized [Docker private checkpoint]([LINK_URL_1]).

Before installation, ensure that all the [requirements and settings]([LINK_URL_2]) are met. Uptrends will provide you with all the necessary files to get started.

## Installation script

Uptrends provides an installation script that you can download as a .zip file from the [SHORTCODE_5] Private locations [SHORTCODE_6] menu of the [Uptrends app]([LINK_URL_3]). This script is available for each of your [Private locations]([LINK_URL_4]) and performs the main installation steps. These steps include installing Docker and Docker Compose, pulling the Uptrends container images, performing a startup and update task, and starting the containerized checkpoint.

## Installation steps

**To install a checkpoint using the script:**

1. Go to the [SHORTCODE_7] Private locations [SHORTCODE_8] menu.
2. If you haven't added any [Private locations]([LINK_URL_5]), click the [SHORTCODE_9] Add location [SHORTCODE_10] button. Once added, two checkpoints will be included by default.
3. Click the Private locations' checkpoint name.
4. Select the required operating system from the **Host Operating System** dropdown.
5. Click the [SHORTCODE_11] Download installation zip file [SHORTCODE_12] button.

[SHORTCODE_1] **Important:** Keep in mind that the downloaded .zip file only contains the specific Private locations checkpoint you selected from the two default options. Your .zip file has a file name UptrendsCheckpoints\[HTML_TAG_1].zip, where \[HTML_TAG_2] is the name of your checkpoint. [SHORTCODE_2]

5. Unzip the downloaded file in the place where you want to install the private checkpoint.
6. To prevent screenshots from uploading to the cloud, [edit the docker-compose file]([LINK_URL_6]) after downloading and extracting the files.

[SHORTCODE_3] **Important:** Depending on your company's policies, you might need to unblock all the Powershell script files (*.ps1) in the zip folder before running them. For more information, see the [instructions]([LINK_URL_7]) on how to unblock files. [SHORTCODE_4]

7. Open a PowerShell console and run it as Administrator. Run the script [INLINE_CODE_1] in the Uptrends (unzip) directory. This will restart the server once. Note that the script will configure a task that runs once every hour to check the Uptrends containers for updates.

The checkpoints are now available and can be selected on the monitor's [SHORTCODE_13] Checkpoints [SHORTCODE_14] tab. You can also see the checkpoints in the *Check details* dialog when running a quick test directly from the monitor using the [SHORTCODE_15] Test now [SHORTCODE_16] button.

To install certificates in Private locations, see [Install certificates in Private locations]([LINK_URL_8]).

## Monitoring your private checkpoint

Uptrends will make changes to your account to better assist you in monitoring your private checkpoints. Please ensure that all your private checkpoint's servers, firewall, internet connection, and other supporting systems remain accessible.

During the private checkpoint setup, Uptrends will add additional monitors and configurations. Please do not delete or modify anything in your account.

For more information, refer to the [How to use Private locations]([LINK_URL_9]) knowledge base article.