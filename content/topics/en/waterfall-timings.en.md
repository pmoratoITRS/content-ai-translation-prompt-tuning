{
  "hero": {
    "title": "Waterfall timings"
  },
  "title": "Waterfall timings",
  "url": "/support/kb/synthetic-monitoring/monitoring-results/waterfall-timings",
  "translationKey": "https://www.uptrends.com/support/kb/monitoring-results/waterfall-timings",
  "tableofcontents": true
}

For some kinds of monitors you can get a waterfall chart as a result of the monitor check. The waterfall contains a [waterfall chart]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/waterfall-chart" lang="en" >}}) which is a graphical presentation of how long it took the page elements to load. 


When hovering over the chart you can zoom in on the timings per element. 

![screenshot waterfall timings popup](/img/content/scr_waterfall_chart-popup-detail.min.png)

## Steps of the loading process

The timings are split out by a number of steps that are needed to load the element. A legend with the colors of the steps is located at the top of the waterfall chart: 

![screenshot waterfall timings legend](/img/content/scr_waterfall_chart-timings-legend.min.png)

All timings are shown in milliseconds. The different steps in the loading process are described below.

### Start

The *Start* value is the only value in this collection which is not a duration, but a point in time. More precisely, this is the point in time when the loading of the related page element started within the complete timeline of the page.

### Queue

The *Queue* time is the duration a request was queued for.

There are different reasons for queueing:

- Request with higher priority exist. For example, images often have lower priority than scripts or stylesheets.
- The request is waiting for a TCP socket to be released.
- There are already 6 TCP connections open for the same origin. This reason applies only to HTTP/1.0 and HTTP/1.1. 
- The browser is allocating space in the disk cache.

### Resolve

This is the time that the browser needed to perform the DNS lookup for the page element. The DNS lookup is used to translate a domain name or URL to the corresponding IP address.

### TCP connect

*TCP connect* is the time that it takes to establish the actual TCP connection from the client to the IP address of the web server.

### HTTPS handshake

A handshake consists of a number of sub-steps that are necessary to initiate a secure communication between client and server. This step is also known as a TLS handshake. 

### Send

Once the connection is established and secure communication was negotiated, the client will send a request to the web server. 

### Wait

This is the time it takes between the sending of a request and the response from the web server.

### Receive

This step captures the time needed to receive the response from the web server.

### Timeout

This timing only applies if the request failed. In that case it shows the period during which the client did not receive any response. There will be a start time and timeout period only in this case, no other timings.
