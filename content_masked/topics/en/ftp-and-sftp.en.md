{
  "hero": {
    "title": "FTP and SFTP"
  },
  "title": "FTP and SFTP",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/ftp-and-sftp",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Your clients rely on the availability of your FTP (File Transfer Protocol) and SFTP (Secure File Transfer Protocol) to download files from your server to their computer. The FTP and SFTP monitor types check the availability of your servers and report any down time. Your options vary based on your choice of FTP or SFTP monitor type.

## What actions can an FTP monitor perform?

The basic FTP monitor checks for:

-   **Availability and speed**  
    By selecting the **Load time** check boxes on the [SHORTCODE_3]Error conditions[SHORTCODE_4] tab you can verify that your FTP server is responding quickly to user requests.
-   **Perform basic server authentication**  
    Verify that your basic authentication process works properly by providing a **Username** and **Password** on the [SHORTCODE_5]Advanced[SHORTCODE_6] tab.

## What actions can an SFTP monitor perform?

The SFTP monitor uses an encrypted connection to perform the file transfer. The SFTP monitor gives a broader range of testing options than the FTP monitor type. The SFTP monitor can perform various actions. Using the [SHORTCODE_7]Advanced[SHORTCODE_8] tab choose from:

-   **Connect to an SFTP server with a username and password**  
    The monitor will connect to the SFTP server with the username and password that you specify. The monitor will report an error when the server is not available or if an error occurs during login.
-   **Test if a file on the SFTP server exists**  
    In this mode, the monitor first connects to the SFTP server, and then the monitor verifies if a specific file exists on the server.
-   **Test if a file on the SFTP server does not exist**  
    Sometimes you may want to monitor if a specific file does not exist on the SFTP server. You can select this action in the SFTP monitor properties.
-   **Download a file from the SFTP server**  
    In this mode, the monitor will first connect to the SFTP server, verify if a specific files exists on the server, and then download the file. The maximum download file size is 1MB.

## How do I set up an (S)FTP monitor?

SFTP (Secure File Transfer Protocol) is the standard file transfer protocol. SFTP is used to securely transfer files between two computers. Uptrends allows you to monitor your SFTP server for enhanced security and performance.

To create an (S)FTP monitor, follow these steps:

1. Click the + button in the menu [SHORTCODE_9] Monitoring > Monitor setup [SHORTCODE_10]. 
2. In the pop-up dialog *Select a monitor type*, first click the monitor type *FTP* or *SFTP* and then click the [SHORTCODE_11] Choose [SHORTCODE_12] button.  
   The new monitor is created and you will be in the monitor configuration screen. 
3. Give your monitor a **Name**.  
4. Set the **Check interval**. Your [check interval]([LINK_URL_1]) is the time between the end of one check and the start of the next.
5. Enter the domain name or IP address of your FTP server in the *Network Address* field.  
6. If the port of your FTP server is different than the default shown, change it to the appropriate port. 
7. Open the [SHORTCODE_13] Advanced [SHORTCODE_14] tab.
8. Choose an option in the **Action** box (for details about the available actions visit the [overview]([LINK_URL_2]) page).
9. Provide the file name or relevant path in the **File path** box if you chose to download or verify a file.
10. Specify the **User name** and **Password,** if using authentication.
11. Once you are satisfied with the configuration of your new monitor, click on the [SHORTCODE_15] Save [SHORTCODE_16] button. 
      
[SHORTCODE_1]**Note**: You can also explore other [monitor settings]([LINK_URL_3]) within the tabs at the top of the monitor configuration screen.[SHORTCODE_2]
