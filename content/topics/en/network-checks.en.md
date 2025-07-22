{
  "hero": {
    "title": "Network Checks"
  },
  "title": "Network Checks",
  "summary": "External Network Check monitors make sure your network is active and accessible and notifies you of outages. ",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/network-checks",
  "translationKey": "https://www.uptrends.com/support/kb/network-checks"
}

Uptrends designed its HTTP(S) monitors to check the availability and speed of your website, but when you need to check other non-web, networked devices from outside your firewall, you need a Network Check. Uptrends will notify your team when it encounters an error with your provided URL or IP address, and depending on the error, you will receive a traceroute to assist you in fixing the problem. With Network Checks, you have two options: ping or connect.

## Ping

When you select the **Ping network check**, Uptrends' checkpoints use ICMP (Internet Control Message Protocol) to send an echo request. Uptrends gathers and reports response times and issues alerts for any errors found in the reply. 

{{< callout >}}
**Note:** You must have ICMP enabled on the device to avoid needless alerts; also in the event of heavy network traffic, sometimes devices ignore ICMP requests.
{{< /callout >}}

## Connect

When you select a **Connect Network Check**, Uptrends will attempt to connect to the port number you designate. You can provide any port number; for example, to make a SSH (Secure Shell) connection to a Linux box you would indicate port 22.

## Features and settings

Both the Ping and Connect provide you with many options for your monitoring. A few highlights are listed below. Please see the knowledge base article [Monitor settings]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="en" >}}) for further information.

### Interval

Although the default setting for interval is five minutes, you can adjust the interval from one minute up to once an hour. The [check interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="en" >}}) is the time between the end of one check and the start of the next. 

### IP version

IPv4 has long been the standard, but the new version IPv6 is quickly gaining acceptance. Most of the Uptrends checkpoints support IPv6.

Uptrends recommendeds that you set up checks to monitor both IPv4 and IPv6. The two versions handle routing differently, so tests could fail on one version while the other succeeds.

### Performance

Slow connects or pings may indicate other network or hardware issues. Using the {{< AppElement type="tab" >}}Error conditions{{< /AppElement >}} tab, you can set performance limits to notify you when your network experiences performance problems.

### Traceroute

Uptrends performs traceroute diagnostics in several cases:

1.  As part of a monitor check, when the monitor suspects a connectivity/networking issue. For example, when an HTTPS monitor tries to contact the web server, but no TCP connection can be created to the server's IP address, a traceroute will be performed as a way to collect some extra diagnostics about the connectivity between Uptrends' checkpoint location and your server.
2.  When you use the free traceroute tool to perform an explicit traceroute on one of Uptrends' checkpoint servers.

It's important to understand what type of traffic to expect when these traceroutes are performed. Traceroute implementations behave differently on different platforms: some implementation use UDP packets, some use TCP packets, and some use ICMP (ping) echo requests. The traceroutes that Uptrends executes are always performed on Windows servers, which use ICMP packets. Therefore, using Uptrends to perform traceroutes to your networking environment will only work if your network allows ICMP packets. No TCP or UDP traffic is involved.

## Setting up a Ping or Connect monitor

Configuring an external server or network device for monitoring is pretty simple, typically taking just a minute or two to complete. The important thing is to make sure that you have your server domain name or IP address ready to go!

1. Click the + button in the menu {{< AppElement type="menuitem" >}} Monitoring > Monitor setup {{< /AppElement >}}. 
2. In the pop-up dialog *Select a monitor type*, first click the monitor type *Ping* or *Connect* and then click the {{< AppElement type="button" >}} Choose {{< /AppElement >}} button.  
   The new monitor is created and you will be in the monitor configuration screen. 
3. Give your monitor a **Name**.  
4. Set the **Check interval**. Your [check interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="en" >}}) is the time between the end of one check and the start of the next. 
5. Enter the server address you want to monitor in the **Network address** within the *Details* section, including the appropriate domain name or IP address. 
6.  Once you are satisfied with the configuration of your new monitor, click on the {{< AppElement type="savebutton" >}} Save {{< /AppElement >}} button. You’ve now added your new External Server monitor!  
      
{{< callout >}}**Note**: You can also explore other [monitor settings]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="en" >}}) within the tabs at the top of the Add Monitor screen.{{< /callout >}}