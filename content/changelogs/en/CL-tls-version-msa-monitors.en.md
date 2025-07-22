{
  "title": "New TLS versions checkbox option in Multi-step API (MSA) monitors",
  "date": "2024-11-06",
  "url": "/changelog/november-2024-new-tls-versions-checkbox-msa-monitors",
  "translationKey": "https://www.uptrends.com/changelog/november-2024-new-tls-versions-checkbox-msa-monitors"
}

We've added the *TLS version(s)* checkbox option in the MSA visual step editor UI.

By ticking the *Only allow specific TLS versions* checkbox, you can now select specific TLS versions during the TLS handshake for HTTP connection in MSA monitors. You can also uncheck the checkbox if no restrictions are needed.

All [Uptrends checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="en" >}}) support TLS 1.1 and TLS 1.2. Selecting the TLS 1.3 option limits Checkpoint selection to those with TLS 1.3 capability. While TLS 1.1 is still available, it is not recommended.

![TLS versions checkbox in MSA monitors](/img/content/scr-tls-versions-option-checkbox.min.png)