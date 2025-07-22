{
  "hero": {
    "title": "Private location requirements"
  },
  "title": "Private location requirements",
  "summary": "What are the technical requirements for private locations?",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/private-checkpoints-requirements",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-requirements"
}

## Requirements and necessary settings

There are some requirements for hardware and network, and necessary network settings. The requirements are based on common scenarios and if you are in doubt about what you need, please check with [Uptrends' Support]({{< ref path="contact" lang="en" >}}). Make sure to adhere to the requirements and have the settings in place before you start installing the checkpoint.

## Private location capacity

Your private locations are used only for your monitors. The required capacity depends on the sort of monitoring running on the checkpoints in the private location. 

Non-browser-based monitoring, like HTTPS, connect, ping, and Multi-step API mainly have an impact on the available network capacity. Browser-based monitors mainly have an impact on server capacity (CPU, memory, disk I/O).

### Calculation of a typical capacity 

The typical capacity for a recommended private location setup, when using the recommended [hardware]({{< ref path="#hardware-requirements" lang="en" >}}) and having two checkpoints, would be:

- 2 x 10 transactions at 5-minute intervals
- 2 x 10 Full Page Checks at 5-minute intervals
- 100 basic monitors at 1-minute intervals

The duration of the transaction will influence the capacity.

The setup leaves room for:

- Confirming [unconfirmed errors]({{< ref path="/support/kb/alerting/errors/unconfirmed-and-confirmed-errors" lang="en" >}})
- Maintenance of one of the checkpoints, e.g. to upgrade containers or the Docker host

### Redundancy

The capacity as described above does not take into account redundancy of monitors. There are some possible configurations where a private location can actually handle more monitoring tasks than mentioned above. This is the case when you have redundancy at different levels, e.g. when using multiple private locations for your monitoring.

## Hardware requirements {id="hardware-requirements"}

Check the following hardware specifications for adding a checkpoint. For reliability we recommend using two checkpoints and for the best performance we recommend using three or more checkpoints. Each checkpoint should adhere to the specifications as defined below. 

|   | Recommended | Minimum |
| --- | --- | --- |
| **CPU** | 4 cores | 2 cores |
| **RAM** | 8 GB | 4 GB |
| **Storage** | 60 GB on fast storage (SSD) | 60 GB |
| **OS** | Windows Server 2022 LTSC Standard | Windows Server 2019 LTSC Standard* |

*Please be aware that Docker on Windows Server 2019 has known issues with DNS resolving.

## Network requirements

You will need to meet the following network requirements.

**IPv4** — Fixed IPv4 address for each checkpoint server  

**IPv6** — Optional, depending on whether you use IPv6 in the monitored infrastructure. 

**Network** — Although we recommend 1 Gbps, the actual usage of this connection is much lower (usually 1 to 10 Mbps 95%) and very constant. 
A connection to the internet that is well dimensioned to transfer the measurement data to the Uptrends platform. 


## Network Settings

### Firewall

There should not be SSL inspection on the traffic between the checkpoints and the Uptrends cloud servers. 

Make sure that you do not have Group Policy Objects (GPOs) in place that will prevent Docker from creating a local firewall. For the computer running Docker, set the group policy setting *Apply local firewall rules* to 'Yes'.

### IPv6 requirements

If the internal network is IPv6 enabled, please supply a fixed IPv6 address and gateway for each checkpoint server. The IPv6 IP Address enables us to monitor your infrastructure through IPv6 (with the proper firewall configuration). Without the fixed IPv6 address, Uptrends can only monitor through IPv4.

### DNS servers

The checkpoint requires one or more DNS server(s) to be configured on the Docker host. By default, containers will use the DNS configuration from the host to resolve host names for the applications under test and for connectivity to the Uptrends cloud platform. 

### FCrDNS

If you would like to monitor mail servers through an external route, configure reverse DNS using: checkpoint\_name@uptrends.net to resolve to the corresponding external IP address.

