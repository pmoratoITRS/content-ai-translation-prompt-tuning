{
  "hero": {
    "title": "Verwenden einer IPv6-Adresse statt eines Domainnamens"
  },
  "title": "Verwenden einer IPv6-Adresse statt eines Domainnamens",
  "summary": "Wenn du eine IPv6-Adresse statt eines Domainnamens verwendest, muss diese richtig formatiert werden, damit Uptrends die Monitoring-Checks korrekt und ohne Erzeugung von Fehlern ausführen kann.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/verwenden-einer-ipv6-adresse-statt-eines-domainnamens",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/using-an-ipv6-address-instead-of-a-domain-name"
}

Du kannst eine IPv6-Adresse statt eines Domainnamens im URL-Feld deines Prüfobjekts verwenden, aber beachte: Du musst die Adresse in eckige Klammern setzen und IPv6 als IP-Version deines Prüfobjekts auswählen. Solltest du nicht IPv6 angeben, erzeugt das Prüfobjekt Fehler, wenn Tests von Checkpoints ausgeführt werden, die IPv6 nicht unterstützen.

Zum Beispiel:

`http://[2a01:5cc0:1:2::4]`

![](/img/content/e40e8c6e-6235-4d19-8a5e-9012b1c3259e.png)
