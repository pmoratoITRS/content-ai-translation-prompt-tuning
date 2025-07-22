{
  "hero": {
    "title": "Updating a Docker container"
  },
  "title": "Updating a Docker container",
  "summary": "How does updating a private locations' checkpoint Docker container work?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-update-containers",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-update-containers"
}

When you [install a user-managed checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#script-content" lang="en" >}}) a script is created and a scheduled task is setup that will update the checkpoint container every hour. If you need to update outside of this schedule, a manual update can be performed.

## How to update manually?

First, make sure that the steps explained in [Install a Docker checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="en" >}}) have been executed earlier.

1. Open a PowerShell console **in admin mode**. 
2. Go to the folder where the docker-compose.yml file lives and execute the following commands.
3. Type `docker-compose pull` in the command-line. 
4. Type `docker-compose down` in the command-line. 
5. Type `docker-compose up` in the command-line.

During the update, your other private checkpoints will take over doing checks. The soon to be updated checkpoint does not need to be disabled for a successful update. As you should have at least [one other checkpoint instance]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-faq#two-default-private-checkpoints" lang="en" >}}) (again this is strongly recommended) you can update without having to make any other changes like disabling checkpoints, stopping monitors, etc.

{{< callout >}}
It is important to keep your Docker containers up to date. The containers have a built-in Chrome and Edge browser that must be kept up to date to not become a security liability.
Uptrends will show a warning or error if we consider your containers to be out of date.  
{{< /callout >}}
