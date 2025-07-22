{  "title": "Neue Core Web Vitals-Metriken: Interaction to Next Paint (INP)",
  "date": "2024-06-12",
  "url": "/changelog/juni-2024-neu-cwv-inp",
  "translationKey": "https://www.uptrends.com/changelog/june-2024-new-cwv-inp"
}

Bestimmte Prüfobjekttypen wie etwa die [Full Pagechecks]({{< ref path="support/kb/synthetic-monitoring/browser-monitoring" lang="de" >}}) und [Transaktionsprüfobjekte]({{< ref path="/support/kb/synthetic-monitoring/transactions" lang="de" >}}), können [Core Web Vitals]({{< ref path="/support/kb/synthetic-monitoring/monitoring-results/core-web-vitals" lang="de" >}}) als Teil der Seitenlademessungen für die geprüfte URL enthalten. Core Web Vitals sind Googles Standardreihe von Messwerten, um das Nutzererlebnis zu messen.

Wir haben die Reihe der Core Web Vitals in den Prüfobjektergebnissen erweitert, sodass sie nun den Wert „Interaction to Next Paint (INP)“ enthalten. Dieser Wert misst die Reaktionsfähigkeit der Seite auf Nutzerinteraktionen, indem die Zeit zwischen Nutzereingabe und visuellem Feedback auf der Seite erfasst wird.