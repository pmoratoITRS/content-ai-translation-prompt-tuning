{  "title": "Updates beim Transaktionsrekorder",
  "date": "2024-06-12",
  "url": "/changelog/juni-2024-transaktionsrekorder-updates",
  "translationKey": "https://www.uptrends.com/changelog/june-2024-transaction-recorder-updates"
}

Wir haben unseren [Transaktionsrekorder]({{< ref path="/features/transaction-recorder" lang="de" >}}) einem Update mit einer grafischen Überarbeitung und mehreren neuen Funktionen unterzogen. Die neuen Funktionen sind unter anderem:

- ein neues Kontextmenü bei rechtem Mausklick im Rekorder-Browser, sodass Nutzer Aktionen wie [Hover]({{< ref path="/support/kb/synthetic-monitoring/transactions/page-interactions#hover" lang="de" >}}), [Warte auf Element]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks#wait-for-element" lang="de" >}}), oder [Prüfe Dokumentinhalt]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks#test-document-content" lang="de" >}}) (wenn Text auf der Seite hervorgehoben ist) hinzufügen können, während sie die Transaktion aufzeichnen. Diese Aktionen müssen also nicht mehr im Anschluss hinzugefügt werden!
- die Möglichkeit, [Tastenereignisse]({{< ref path="/support/kb/synthetic-monitoring/transactions/page-interactions#key-event" lang="de" >}}) direkt über die Rekorder-Benutzeroberfläche hinzuzufügen. Der Rekorder kann keine Aktionen wie Drücken der Eingabetaste nach Ausfüllen der Anmeldedaten aufzeichnen. Derartige Aktionen können jedoch anhand der Schaltfläche „**+ Add keyboard action**“ (Tastenaktion hinzufügen) im Rekorder hinzugefügt werden.

![Kontextmenü im Rekorder](/img/content/scr-recorder-context-menu.min.png)