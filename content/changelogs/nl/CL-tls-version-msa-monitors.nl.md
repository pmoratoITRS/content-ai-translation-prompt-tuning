{
  "title": "Nieuwe optie TLS-versies in Multi-step API (MSA)-controleregels",
  "date": "2024-11-06",
  "url": "/changelog/november-2024-nieuw-selectievakje-tls-versies-msa-controleregels",
  "translationKey": "https://www.uptrends.com/changelog/november-2024-new-tls-versions-checkbox-msa-monitors"
}

We hebben het selectievakje *TLS-versie(s)* toegevoegd in de gebruikersinterface van de MSA visuele stap-editor.

Door het selectievakje *Alleen specifieke TLS-versies toestaan* aan te vinken, kunt u nu specifieke TLS-versies selecteren tijdens de TLS-handshake voor HTTP-verbinding in MSA-controleregels. U kunt het vinkje ook uitzetten als er geen beperkingen nodig zijn.

Alle [Uptrends-controlestations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="nl" >}}) ondersteunen TLS 1.1 en TLS 1.2. Als de optie TLS 1.3 wordt geselecteerd, wordt de controlestationselectie beperkt tot die met TLS 1.3-functionaliteit. Hoewel TLS 1.1 nog steeds beschikbaar is, wordt het niet aanbevolen.

![Selectievakje TLS-versies in MSA-controleregels](/img/content/scr-tls-versions-option-checkbox.min.png)