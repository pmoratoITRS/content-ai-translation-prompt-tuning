{
  "hero": {
    "title": "Private locations troubleshooting"
  },
  "title": "Private locations troubleshooting",
  "summary": "Troubleshooting guidelines and examples for troubleshooting your private locations.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting"
}

The installation of a private location is fully automated and will leave you with an active container checkpoint that will keep itself up-to-date and is able to run measurements for monitors. This guide provides steps to help you [verify your private location installation](#verify-private-location-installation), [smoke test your setup](#smoke-test-your-setup) and [how to troubleshoot](#how-to-troubleshoot) any issues during or after the installation of a private location. 

## Verify private location installation

The first step is to verify if your private location is [installed and set up]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-steps" lang="en" >}}) correctly. The automated installation package is pre-configured and consists of three steps.

- Installation of prerequisites (including a reboot if required).
- Pulling the Uptrends container images from Azure.
- Installation of the auto-run & auto-update tasks.


### Installation of prerequisites
Three prerequisites for running the Uptrends container images are installed: the ‘Containers’ Windows feature, the Docker engine and Docker Compose. The installation of the Containers Windows feature may require a reboot for which a prompt will appear. The installation will continue automatically after this reboot (using a Scheduled Task).

If you want to check if these three items are installed correctly there are three commands to execute. 

First, list all Windows features and check if this list includes 'Containers':
1. Open a PowerShell console in admin mode. 
2. Go to the folder where the docker-compose.yml file lives and execute the following command ``Get-WindowsFeature | Where-Object {$_. installstate -eq "installed"}``. 
3. Check if this list includes 'Containers'

Second, check the output of the version of Docker:
1. Open a PowerShell console in admin mode. 
2. Go to the folder where the docker-compose.yml file lives and execute the following command ``Docker -v``. 
3. The result should read something like 'Docker version 23.0.3, build 3e7cbfd'

Thirdly, check the output of the version of Docker Compose:
1. Open a PowerShell console in admin mode. 
2. Go to the folder where the docker-compose.yml file lives and execute the following command ``Docker-compose -v``. 
3. The result should read something like 'Docker Compose version v2.17.2'

If you think anything is out of order you can refer to the installation script, install-checkpoint.ps1, and manually run the individual parts for the components above and examine the output.
 
### Container images
If all three prerequisites above are in place the [installation script]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-script" lang="en" >}}) will start to pull the Uptrends container images from Azure. These images are large since each includes a compressed installation of Windows Server. The download can take at least several minutes (20 minutes is common) depending on the network throughput. Parts of the images are re-used when updating so subsequent downloads will be faster. Once the downloading is done, you can verify this by [running](#managing-running-containers): ``docker images`` and expect to see three entries.

Pulling the images relies on the inner workings of Docker and is a robust process which can handle connections dropping. If downloading fails altogether the most expected cause is a (local) firewall preventing Docker from accessing the Azure Container Repository via azurecr.io, hosted by Microsoft.

To authenticate when pulling the images, the installation script will register credentials via Docker login. In case of issues with authentication you can navigate to the installation directory (the folder that contains install-checkpoint.ps1) and run these commands in powershell to:

Clear existing credentials, use the following command:
``Docker logout``

Re-run registry-login.ps1 and examine the output of this command use the following command:
``.\registry-login.ps1``

### Auto-run and auto-updates
To keep the container checkpoints running a scheduled task is created to run the script start-containers.ps1 after startup of the server. To keep the container checkpoint Docker images [up to date]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-update-containers" lang="en" >}})  a second Scheduled Task is created to check for image updates on a regular interval. Check the output of the powershell command ``Get-ScheduledTask`` to verify if these tasks exist. They are called 'Start Checkpoint Containers' and 'Update Checkpoint Images'. 

You can use the Windows Scheduled Task user interface to further examine the tasks, run history and failures or manually trigger the task to troubleshoot. Again, in case of issues, use the installation script (install-checkpoint.ps1) to manually re-run this part of the installation if needed.

### Configuration
All server-specific configuration will be in the Docker-compose.yml config file. This file lists all three container images and their individual settings. This configuration file comes pre-filled with all necessary settings when it is being downloaded. Most important is the ``ServerId/Password`` combination that should be configured for all three of the container images listed in the file (meaning the same combination of credentials will be in the yml file thrice with the same values). 

{{< callout >}} The *ServerId* and *Password* are unique to the container checkpoint. Multiple container checkpoint servers should never have the same *ServerId*.
{{< /callout >}} 

The Docker Compose file can be used to configure checkpoint specific [data protection]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="en" >}}) policies and [environment specific DNS rules](#dns-issues).
 
### Current status
After installation, the containers for all three images are started and these containers are expected to always be running. You can verify their status with the command ``docker ps`` and check the right-most column to see if the containers are indeed running. In case of issues use these commands to obtain log files for further diagnosis:


- Get the current status for all containers
``Docker ps``

- Get the logs for the checkpoint Agent container and write to file
``Docker logs Checkpoint | Out-File Docker_CS.txt``

- Get the logs for the transaction processor container and write to file
``Docker logs TransactionProcessor | Out-File Docker_TP.txt``

- Alternatively, get combined logs for all containers
``Docker-compose logs -t -n 5000 | Out-File Docker.txt``

## Smoke test your setup

Once container checkpoints are installed, they are immediately ready to run measurements. Uptrends' internal processes will automatically switch the maintenance status of a container checkpoint based on its health. A healthy checkpoint is switched to active, an unhealthy checkpoint to maintenance. 

Checkpoints update their health each minute. Also, you can enable or [disable]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-how-to-use#disable-a-private-checkpoint" lang="en" >}}) checkpoints (for instance when doing maintenance or testing their setup) from the private locations UI in the Uptrends web application. The default state is 'enabled'. 

To smoke test a container checkpoint the most convenient way is by using the {{< AppElement type="buttonSecondary" >}} Test now {{< /AppElement >}} button. Ideally you would do this for each monitor type you intend to run on it. 

You can use the private locations' [Checkpoint health]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-checkpoint-health" lang="en" >}}) to diagnose the status of unhealthy checkpoints. 

Note that all measurements run ‘inside’ a container, you will not see a browser being started on the host machine when using the {{< AppElement type="buttonSecondary" >}} Test now {{< /AppElement >}} button for an FPC or transaction.

Also note that when adding a checkpoint to an existing private location that is part of the checkpoint selection of active monitors, the new checkpoint will start doing measurements after the installation finishes. If that is undesired (for instance if you want to test first) you should disable the checkpoint in the Uptrends private locations section.


## How to troubleshoot

### Stop, start, or restart a set of containers
Restart containers associated with the Docker-compose.yaml file in the current directory. This often is the C:\uptrends\ folder:

1. Open a PowerShell console in admin mode. 
2. Go to the folder where the docker-compose.yml file lives and execute one or all of the following commands.
- To start type `docker-compose up -d` in the command-line. 
- To stop type `docker-compose down` in the command-line. 
- To restart type `docker-compose restart` in the command-line.


{{< callout >}} **Tip,** use the Docker help. For any of the commands you can learn more by using the *docker - -help* command. This command will display all commands with generic help for all the different commands. You can request help on a certain command, as well, by typing *docker image - -help*.{{< /callout >}}


### Managing running containers
To get a list of running containers execute the ``docker ps`` command. Here a containerId will be listed that can be used in other commands regarding this container. 

To get a list of all local images run the command ``docker images`` Note the plural images, all commands targeting an image are ran against image (singular)

Images can get quite large, to free up some space you can use ``docker image prune`` to remove images no longer used by active containers. Or use ``docker image rm <containerid>`` to remove a specific container.

### Removing unused Docker objects

The [Uptrends installation script for Private locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}) does not include a setup for automatically cleaning up unused Docker objects. To remove unused Docker objects, refer to the [Prune unused Docker objects](https://docs.docker.com/engine/manage-resources/pruning) documentation. If you are using other platforms, such as Kubernetes, please refer to their official documentation.

### Getting cmd/shell access inside a container
Run this command to start a powershell or cmd process inside the container. This can be used to quickly read the file system inside the containers. Use commands ```Docker exec -i checkpoint powershell``` or```Docker exec -i checkpoint cmd```.

Are you not sure if you are inside or outside a container? Type ``winver`` in the Windows Command Prompt. If you are inside a container it will look like this: 

```winver : The term 'winver' is not recognized``` 

If you are on the host the **About Windows** pop-up will show.
If you want to exit the powershell or cmd session in the container, to get back to the host, use Ctrl+C.

### Reading log output

1. Open a PowerShell console in admin mode. 
2. Go to the folder where the docker-compose.yml file lives and execute one of the following commands.
- Log output type `Docker-compose logs -t -n 5000` in the command-line. 
- Or when you want to output this to a file containerlogs.log type ``Docker-compose logs -t -n 5000 > containerlogs.log``

### Network
On startup Docker will create a virtual network on the host to which the containers are attached and get an IP address. 
You can view existing networks in powershell with ``docker network ls`` and a specific network with ``docker network inspect <<network name>>``. To find the network a container is in use ``docker inspect <<container name>>`` (and ``docker ps`` to find container names).

All three Uptrends Docker containers (Checkpoint, CheckpointRelay, TransactionProcessor) need to be able to connect to Uptrends via probemaster1.uptrends.com and probemaster2.uptrends.com. Both the Checkpoint and CheckpointRelay containers need to be able to connect to the customers applications under test.

### DNS issues

A common cause of connectivity issues is DNS resolving. For troubleshooting you can follow these steps:

1. On the host, ``nslookup probemaster1.uptrends.com`` should return 95.211.70.204. If it doesn't the containers will not be able to connect to Uptrends.

2. Given that the containers are running (check with ``docker ps``), enter a powershell session in a container: ``docker exec -i Checkpoint powershell.exe``.

3. Once inside the container, ``nslookup probemaster1.uptrends.com`` should again return 95.211.70.204. If that succeeds the container should be able to reach the Uptrends cloud platform.

4. Try the same for a hostname of an internal application, like ``nslookup <<name application>>``, and verify the returned IP. If this times out, the application will not be reachable from the container (and thus cannot be monitored).

If any of these steps fail, you can try:

- Compare ipconfig from the host and from inside a container (``docker exec -i Checkpoint powershell.exe`` to get a powershell session inside the Checkpoint container) and verify the configured DNS server(s).

Try specifying a public DNS like 8.8.8.8 (Google) when doing a nslookup like so: ``nslookup probemaster1.uptrends.com 8.8.8.8``, if it functions correctly when not using the public DNS' IP address, but encounters issues when it is absent, there may be a problem with DNS resolving. Do note that using 8.8.8.8 as DNS server in production is not desired since that will not be able to resolve internal applications.

Specify specific DNS server(s) in the compose file as shown in the code below. Remember to do this for both containers in the yaml file.

```yaml
TransactionProcessor:
    container_name: TransactionProcessor
    image: uptrends.azurecr.io/win2022/transaction-processor
    deploy:
      restart_policy:
        condition: always
    volumes:
      - .\Certificates:C:\Uptrends\Certificates:ro
    logging:
      driver: local
    environment:
      - ServerId=
      - Password=
    dns:
      - 1.2.3.4
      - 2.3.4.5
```

Fill in the IP addresses of the DNS servers you wish to use. You can test these against probemaster1.uptrends.com as well as the hostname using nslookup. Remember to do so from within a container.

You may need to allow DNS requests originating from the Docker containers in case your DNS servers make use of an allow-list. If you are running container checkpoints on a cloud platform such as Google Cloud, AWS or Azure, additional configuration may be required to ensure connectivity from within the Docker containers. 

## Still not working? 

If at any time during the troubleshooting process you don't understand something or have a question, please communicate your questions or concerns to Uptrends by [opening a support ticket]({{< ref path="contact" lang="en" >}}). We will get back to you quickly. 