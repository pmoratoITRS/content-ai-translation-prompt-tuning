{
  "title": "Neu: Browser-Cache bei Transaktionsprüfobjekten löschen",
  "date": "2025-01-29",
  "url": "/changelog/januar-2025-browser-cache-loeschen-in-transaktionspruefobjekten",
  "translationKey": "https://www.uptrends.com/changelog/january-2025-clear-browser-cache-transaction-monitors"
}

Uptrends‛ [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="de" >}}) öffnen immer einen echten Browser, um Nutzeraktivitäten zu simulieren und die Performance deiner Website zu testen. Der Browser beginnt, ohne Daten im Cache gespeichert zu haben, speichert jedoch später Website-Ressourcen temporär, um Ladevorgänge zu beschleunigen.

Wenn du das Verhalten deiner E-Commerce-Websites hinsichtlich des Ablegens von Artikeln im Warenkorb bei bestehenden Nutzern (mit im Cache gespeicherten Daten) und bei neuen Besuchern (ohne im Cache gespeicherte Daten) vergleichen möchtest, kann das Leeren des Cache hilfreich sein.

Mit der neuen Schritt-Aktion **Browser-Cache leeren** bei Transaktionsprüfobjekten kannst du nun den Browser-Cache löschen, damit Seitenelemente direkt vom Server und nicht aus dem Cache geladen werden.  Diese Funktion hilft dir, die Website-Performance bei erstmaligen Besuchern zu prüfen, und stellt sicher, dass die Benutzeroberfläche (mit Bildern, Text und weiteren Front-End-Elementen) korrekt geladen wird. Diese Schritt-Aktion erfordert keine Transaktions-Credits. Nutze sie, um deinen Monitoring-Anforderungen besser gerecht zu werden. Weitere Informationen findest du im Artikel über den [Schritte-Editor für Transaktionen]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}).

![GIF Browser-Cache leeren](/img/content/gif-transaction-clear-browser-cache.gif)