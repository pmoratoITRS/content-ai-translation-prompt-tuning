{
  "hero": {
    "title": "Private locations troubleshooting"
  },
  "title": "Private locations troubleshooting",
  "summary": "Troubleshooting guidelines and examples for troubleshooting your private locations.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

The installation of a private location is fully automated and will leave you with an active container checkpoint that will keep itself up-to-date and is able to run measurements for monitors. This guide provides steps to help you [verify your private location installation]([LINK_URL_1]), [smoke test your setup]([LINK_URL_2]) and [how to troubleshoot]([LINK_URL_3]) any issues during or after the installation of a private location. 

## Verify private location installation

The first step is to verify if your private location is [installed and set up]([LINK_URL_4]) correctly. The automated installation package is pre-configured and consists of three steps.

- Installation of prerequisites (including a reboot if required).
- Pulling the Uptrends container images from Azure.
- Installation of the auto-run & auto-update tasks.


### Installation of prerequisites
Three prerequisites for running the Uptrends container images are installed: the ‘Containers’ Windows feature, the Docker engine and Docker Compose. The installation of the Containers Windows feature may require a reboot for which a prompt will appear. The installation will continue automatically after this reboot (using a Scheduled Task).

If you want to check if these three items are installed correctly there are three commands to execute. 

First, list all Windows features and check if this list includes 'Containers':
1. Open a PowerShell console in admin mode. 
2. Go to the folder where the docker-compose.yml file lives and execute the following command `[INLINE_CODE_1][INLINE_CODE_2][INLINE_CODE_3][INLINE_CODE_4][INLINE_CODE_5][INLINE_CODE_6][INLINE_CODE_7][INLINE_CODE_8][INLINE_CODE_9][INLINE_CODE_10][INLINE_CODE_11][INLINE_CODE_12][INLINE_CODE_13][INLINE_CODE_14][INLINE_CODE_15][INLINE_CODE_16][INLINE_CODE_17][INLINE_CODE_18][INLINE_CODE_19][INLINE_CODE_20][INLINE_CODE_21][INLINE_CODE_22][INLINE_CODE_23][INLINE_CODE_24][INLINE_CODE_25][INLINE_CODE_26]docker-compose up -d[INLINE_CODE_27]docker-compose down[INLINE_CODE_28]docker-compose restart[INLINE_CODE_29][INLINE_CODE_30][INLINE_CODE_31][INLINE_CODE_32][INLINE_CODE_33][INLINE_CODE_34][INLINE_CODE_35][INLINE_CODE_36][INLINE_CODE_37][INLINE_CODE_38][INLINE_CODE_39]Docker-compose logs -t -n 5000[INLINE_CODE_40][INLINE_CODE_41][INLINE_CODE_42][INLINE_CODE_43][INLINE_CODE_44][INLINE_CODE_45][INLINE_CODE_46][INLINE_CODE_47][INLINE_CODE_48][INLINE_CODE_49][INLINE_CODE_50][INLINE_CODE_51][INLINE_CODE_52][INLINE_CODE_53][INLINE_CODE_54][INLINE_CODE_55][INLINE_CODE_56][INLINE_CODE_57][INLINE_CODE_58][INLINE_CODE_59][INLINE_CODE_60][INLINE_CODE_61][INLINE_CODE_62][INLINE_CODE_63]`, if it functions correctly when not using the public DNS' IP address, but encounters issues when it is absent, there may be a problem with DNS resolving. Do note that using 8.8.8.8 as DNS server in production is not desired since that will not be able to resolve internal applications.

Specify specific DNS server(s) in the compose file as shown in the code below. Remember to do this for both containers in the yaml file.

[CODE_BLOCK_4]

Fill in the IP addresses of the DNS servers you wish to use. You can test these against probemaster1.uptrends.com as well as the hostname using nslookup. Remember to do so from within a container.

You may need to allow DNS requests originating from the Docker containers in case your DNS servers make use of an allow-list. If you are running container checkpoints on a cloud platform such as Google Cloud, AWS or Azure, additional configuration may be required to ensure connectivity from within the Docker containers. 

## Still not working? 

If at any time during the troubleshooting process you don't understand something or have a question, please communicate your questions or concerns to Uptrends by [opening a support ticket]([LINK_URL_14]). We will get back to you quickly. 