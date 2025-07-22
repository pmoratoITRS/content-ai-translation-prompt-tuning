{
  "hero": {
    "title": "Deine Transaktionsdaten deuten"
  },
  "title": "Deine Transaktionsdaten deuten",
  "summary": "Sobald dein Transaktionsprüfobjekt in die Produktion übergeht, erhältst du Kontrolldetailberichte und Dashboards werden mit Daten gefüllt. Mit dieser Übung erfährst du, wie du sie deutest. ",
  "url": "/support/kb/synthetic-monitoring/transaktionen/tutorial-record-user-journey-in-shop/transaktions-dashboards-und-berichte-deuten",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/tutorial-record-user-journey-in-shop/making-sense-of-your-transaction-dashboards-and-reports"
}

Die Daten, die während des Monitorings erfasst werden, sind im [Dashboard]({{< ref path="support/kb/dashboards-and-reporting/dashboards" lang="de" >}}) *Transaktion Übersicht* zu sehen. Wie der Name bereits sagt, ist dies ein Überblick und er enthält Daten über mehrere Transaktionsprüfobjekte. Möchtest du die Details zu einem bestimmten Transaktionsprüfobjekt sehen, öffne die [Kontrolldetails]({{< ref path="#tutorial-check-details" lang="de" >}}) des jeweiligen Prüfobjekts.

## Das Dashboard Transaktion Übersicht

Dein Dashboard *Transaktion Übersicht* enthält Kacheln mit dem aktuellen Status, ein Protokoll kürzlich erfolgter Prüfungen, Infos zu Verfügbarkeit und Performance und eine Grafik zur Verfügbarkeit und Performance deiner Transaktionen.
Es gibt im Grunde zwei [Dashboard-Kacheltypen]({{< ref path="support/kb/dashboards-and-reporting/dashboards/custom-report-tiles" lang="de" >}}): Diagramm und Liste. Der Typ Liste zeigt die Monitoring-Daten als Tabelle, eine Kachel des Typs Diagramm zeigt eine grafische Darstellung der Daten.

Beachte, dass das Dashboard *Transaktion Übersicht* keine Informationen über deine Transaktionsprüfobjekte im [Entwicklungsmodus]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/monitor-mode" lang="de" >}}) enthält.

Um das Dashboard *Transaktion Übersicht* aufzurufen: Wechsle zum Menüelement {{< AppElement type="menuitem" >}} Transaktionen > Transaktion Übersicht {{< /AppElement >}} auf.

![Screenshot Dashboard Transaktion Übersicht dashboard](/img/content/scr_transaction-tutorial-transaction-overview.min.png)

### Account Status

Die Kachel *Account Status* liefert dir den aktuellen Status deiner Transaktionsprüfobjekte im Staging- und Produktionsmodus. Über diese Tabelle kannst du deine Prüfobjekte schnell zwischen Aktiv und deaktiviert schalten und im Produktionsmodus die Alarmierung aktivieren oder deaktivieren.

![Screenshot Kachel Account Status](/img/content/scr_transaction-tutorial-account-status.min.png)

### Letzte Überwachungen

Die Tabelle *Letzte Überwachungen* ist ein chronologisches Protokoll der kürzlich erfolgten Prüfungen. Du kannst die Kachel *Letzte Überwachungen* verwenden, um auf eine bestimmte Prüfung zu klicken (klicke auf das Datum) und den Bericht [*Kontrolldetails*]({{< ref path="#tutorial-check-details" lang="de" >}}) zu sehen.  Das Kamerasymbol in der Spalte **Status** zeigt, dass der *Kontrolldetail*-Bericht einen oder mehrere Screenshots enthält.

![Screenshot Kachel Letzte Überwachungen](/img/content/scr_transaction-tutorial-last-checks.min.png)

### Gesamtzeit, Verfügbarkeit und bestätigte Fehler

Diese Liste gibt die durchschnittliche Gesamtzeit, den Verfügbarkeitsprozentsatz und die Anzahl bestätigter Fehler für den Berichtszeitraum. Natürlich kannst du auch andere Messwerte einbinden, indem du auf das Dreipunkte-Menü {{< AppElement type="iconTileSettings" >}} {{< /AppElement >}} klickst, um die Kachel-Einstellungen aufzurufen.

![Screenshot Transaktion Kachel Verfügbarkeit und Fehler](/img/content/scr_transaction-dashboard-tile-total-uptime-errors.min.png)

{{< callout >}}**Hinweis**: Transaktionen im Staging-Modus werden nicht auf Verfügbarkeit geprüft, ihre Verfügbarkeit beträgt immer 100 %. {{< /callout >}}

### Verfügbarkeit und bestätigte Fehler

Die Kachel *Verfügbarkeit und bestätigte Fehler* gibt eine grafische Darstellung der durchschnittlichen Verfügbarkeit und Fehler, die während des Berichtszeitraums für all deine Transaktionsprüfobjekte im Produktionsmodus verzeichnet wurden.

![Screenshot Transaktion Kachel Verfügbarkeit und bestätigte Fehler](/img/content/scr_transaction-tutorial-uptime-confirmed-errors.min.png)

### Transaktions-Detailbericht {id="monitor-own-dashboard"}

Die *Transaktions-Übersicht* enthält standardmäßig Daten aller Transaktionsprüfobjekte  oder der Prüfobjekte, die du für dieses Dashboard ausgewählt hast. Möchtest du die Daten für ein einzelnes Prüfobjekt anzeigen, gehe wie folgt vor:

Die Namen der Prüfobjekte sind in einigen Kacheln des Dashboards mit einer gepunkteten Linie unterstrichen. Zeige mit der Maus auf den Namen des Prüfobjekts, das du dir näher ansehen möchtest. Es erscheint ein Pop-up für den Schnellzugriff:

![Screenshot Schnellzugriff Prüfobjekt](/img/content/scr_transaction-tutorial-monitor-quick-access.min.png)

Klicke in dem Pop-up auf den Link **Dashboard**, um das für dieses Prüfobjekt spezifische Dashboard zu öffnen. Dieses Dashboard enthält Informationen, die du nur auf Basis des einzelnen Prüfobjekts anzeigen kannst.

![Screenshot Prüfobjekt-Dashboard einzelne Transaction](/img/content/scr_transaction-tutorial-drilldown.min.png)
### Listen/Diagramme zu Zeiten einzelner Transaktionsschritte

Die Zeit, die jede Aktion benötigt, ist genau so wichtig, wie die Seitenladezeit, wenn ein Nutzer die Website zum ersten Mal aufruft. Lange Wartezeiten zwischen den Nutzerinteraktionen unterwandern das Vertrauen des Nutzers in dein Produkt und deine Marke. Die Listen und Diagramme *Zeit je Transaktionsschritt* sollen dir helfen, potenzielle Probleme und Trends zu identifizieren.

Die Grafik *Zeit je Transaktionsschritt*. Diese Dashboard-Kachel zeigt die Dauer jedes Schritts der Transaktion der für jede Prüfung des Prüfobjekts über eine bestimmte Zeit gemessen wurde.

![Screenshot Kachel Zeit je Transaktionsschritt](/img/content/scr_transaction-tutorial-step-timing.min.png)

Eine weitere Art, sich die Performance der Transaktion anzusehen, besteht darin, die durchschnittliche Zeit anzuzeigen, die für jeden Schritt benötigt wird. Abhängig davon, was von einem Schritt erwartet wird, können lange Schrittzeiten daruf hinweisen, dass etwas nicht optimal funktioniert.

![Screenshot durchschnittliche Zeit Transaktionsschritt](/img/content/scr_transaction-tutorial-average-steptime.min.png)

Die Liste *Zeit je Transaktionsschritt* zeigt die Schrittzeiten für jede Prüfung in Zahlen.

![Screenshot Liste Ziet je Transaktionschritt](/img/content/scr_transaction-tutorial-step-timing-drilldown.min.png)

### Liste und Diagramm zum Fehlertyp

Die Liste und das Diagramm *Fehler Typ* liefern dir einen Überblick über die bestätigten Fehler, die das Prüfobjekt in dem Berichtszeitraum festgestellt hat.

![Screenshot Kachel Fehlertypen](/img/content/scr_transaction-tutorial-error-types.min.png)

## Kontrolldetails {id="tutorial-check-details"}

Zeige die Ergebnisse einer einzelnen Prüfung durch Klicken auf den entsprechenden Eintrag in der Kachel *Letzte Überwachungen* in deinem Dashboard *Transaktion Übersicht* oder über die Kachel *Prüfobjektprotokoll* im [Dashboard des Prüfobjekts]({{< ref path="#monitor-own-dashboard" lang="de" >}}). Du wirst feststellen, dass alle Informationen bereitstehen: Datum/Uhrzeit, Ergebnis, Checkpoint, Ladezeit, Browsertyp und -version, Betriebssystem und die Ergebnisse pro Schritt.

![screenshot transaction check details](/img/content/scr_transaction-check-details.min.png)

In der Regel bezieht sich die **Ladezeit** (siehe Bericht oben) auf die Zeit, die erforderlich war, eine Seite im Browser anzufordern und zu laden. Aber bei Transaktionen ist die Ladezeit die Gesamtzeit, die die Transaktion von der ersten Anfrage bis zur letzten Aktion erforderte (die Summe aller Schrittzeiten).

### Ergebnis pro Schritt

Der Bereich **Ergebnis pro Schritt** sollte dir bekannt vorkommen. Dieser Abschnitt spiegelt dein Skript in einzelnen Schritten mit dem Ergebnis für jede Aktion wider. Du erhältst die Dauer pro Schritt und das Ergebnis jeder Aktion. Wenn eine Aktion fehlschlägt, wird die Prüfung abgebrochen und der Schritt rot im Bericht hervorgehoben. Wenn du über einen Business oder Enterprise Account verfügst, kannst du über den Bericht *Kontrolldetails* die Wasserfalldiagramme und Screenshots aufrufen. Klicke auf das Wasserfallsymbol {{< AppElement type="iconWaterfall" >}} {{< /AppElement >}} (neben dem Schrittnamen), um den zum Schritt gehörenden Wasserfall anzuzeigen.

![](/img/content/77be77be-5520-4eab-9bf5-1d423f1acd6b.png)
