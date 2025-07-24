{
  "hero": {
    "title": "Verwenden einer IPv6-Adresse statt eines Domainnamens"
  },
  "title": "Verwenden einer IPv6-Adresse statt eines Domainnamens",
  "summary": "Wenn du eine IPv6-Adresse statt eines Domainnamens verwendest, muss diese richtig formatiert werden, damit Uptrends die Monitoring-Checks korrekt und ohne Erzeugung von Fehlern ausführen kann.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/verwenden-einer-ipv6-adresse-statt-eines-domainnamens",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Du kannst eine IPv6-Adresse statt eines Domainnamens im URL-Feld deines Prüfobjekts verwenden, aber beachte: Du musst die Adresse in eckige Klammern setzen und IPv6 als IP-Version deines Prüfobjekts auswählen. Solltest du nicht IPv6 angeben, erzeugt das Prüfobjekt Fehler, wenn Tests von Checkpoints ausgeführt werden, die IPv6 nicht unterstützen.

Zum Beispiel:

[INLINE_CODE_1]

![]([LINK_URL_1])
