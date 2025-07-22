{
  "hero": {
    "title": "Deine Transaktionsdaten deuten"
  },
  "title": "Deine Transaktionsdaten deuten",
  "summary": "Sobald dein Transaktionsprüfobjekt in die Produktion übergeht, erhältst du Kontrolldetailberichte und Dashboards werden mit Daten gefüllt. Mit dieser Übung erfährst du, wie du sie deutest. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/tutorial-record-user-journey-in-shop/transaktions-dashboards-und-berichte-deuten",
  "translationKey": "[URL_1]
}

Die Daten, die während des Monitorings erfasst werden, sind im [Dashboard]([LINK_URL_1]) *Transaktion Übersicht* zu sehen. Wie der Name bereits sagt, ist dies ein Überblick und er enthält Daten über mehrere Transaktionsprüfobjekte. Möchtest du die Details zu einem bestimmten Transaktionsprüfobjekt sehen, öffne die [Kontrolldetails]([LINK_URL_2]) des jeweiligen Prüfobjekts.

## Das Dashboard Transaktion Übersicht

Dein Dashboard *Transaktion Übersicht* enthält Kacheln mit dem aktuellen Status, ein Protokoll kürzlich erfolgter Prüfungen, Infos zu Verfügbarkeit und Performance und eine Grafik zur Verfügbarkeit und Performance deiner Transaktionen.
Es gibt im Grunde zwei [Dashboard-Kacheltypen]([LINK_URL_3]): Diagramm und Liste. Der Typ Liste zeigt die Monitoring-Daten als Tabelle, eine Kachel des Typs Diagramm zeigt eine grafische Darstellung der Daten.

Beachte, dass das Dashboard *Transaktion Übersicht* keine Informationen über deine Transaktionsprüfobjekte im [Entwicklungsmodus]([LINK_URL_4]) enthält.

Um das Dashboard *Transaktion Übersicht* aufzurufen: Wechsle zum Menüelement [SHORTCODE_3] Transaktionen > Transaktion Übersicht [SHORTCODE_4] auf.

![Screenshot Dashboard Transaktion Übersicht dashboard]([LINK_URL_5])

### Account Status

Die Kachel *Account Status* liefert dir den aktuellen Status deiner Transaktionsprüfobjekte im Staging- und Produktionsmodus. Über diese Tabelle kannst du deine Prüfobjekte schnell zwischen Aktiv und deaktiviert schalten und im Produktionsmodus die Alarmierung aktivieren oder deaktivieren.

![Screenshot Kachel Account Status]([LINK_URL_6])

### Letzte Überwachungen

Die Tabelle *Letzte Überwachungen* ist ein chronologisches Protokoll der kürzlich erfolgten Prüfungen. Du kannst die Kachel *Letzte Überwachungen* verwenden, um auf eine bestimmte Prüfung zu klicken (klicke auf das Datum) und den Bericht [*Kontrolldetails*]([LINK_URL_7]) zu sehen.  Das Kamerasymbol in der Spalte **Status** zeigt, dass der *Kontrolldetail*-Bericht einen oder mehrere Screenshots enthält.

![Screenshot Kachel Letzte Überwachungen]([LINK_URL_8])

### Gesamtzeit, Verfügbarkeit und bestätigte Fehler

Diese Liste gibt die durchschnittliche Gesamtzeit, den Verfügbarkeitsprozentsatz und die Anzahl bestätigter Fehler für den Berichtszeitraum. Natürlich kannst du auch andere Messwerte einbinden, indem du auf das Dreipunkte-Menü [SHORTCODE_5] [SHORTCODE_6] klickst, um die Kachel-Einstellungen aufzurufen.

![Screenshot Transaktion Kachel Verfügbarkeit und Fehler]([LINK_URL_9])

[SHORTCODE_1]**Hinweis**: Transaktionen im Staging-Modus werden nicht auf Verfügbarkeit geprüft, ihre Verfügbarkeit beträgt immer 100 %. [SHORTCODE_2]

### Verfügbarkeit und bestätigte Fehler

Die Kachel *Verfügbarkeit und bestätigte Fehler* gibt eine grafische Darstellung der durchschnittlichen Verfügbarkeit und Fehler, die während des Berichtszeitraums für all deine Transaktionsprüfobjekte im Produktionsmodus verzeichnet wurden.

![Screenshot Transaktion Kachel Verfügbarkeit und bestätigte Fehler]([LINK_URL_10])

### Transaktions-Detailbericht [ANCHOR_1]

Die *Transaktions-Übersicht* enthält standardmäßig Daten aller Transaktionsprüfobjekte  oder der Prüfobjekte, die du für dieses Dashboard ausgewählt hast. Möchtest du die Daten für ein einzelnes Prüfobjekt anzeigen, gehe wie folgt vor:

Die Namen der Prüfobjekte sind in einigen Kacheln des Dashboards mit einer gepunkteten Linie unterstrichen. Zeige mit der Maus auf den Namen des Prüfobjekts, das du dir näher ansehen möchtest. Es erscheint ein Pop-up für den Schnellzugriff:

![Screenshot Schnellzugriff Prüfobjekt]([LINK_URL_11])

Klicke in dem Pop-up auf den Link **Dashboard**, um das für dieses Prüfobjekt spezifische Dashboard zu öffnen. Dieses Dashboard enthält Informationen, die du nur auf Basis des einzelnen Prüfobjekts anzeigen kannst.

![Screenshot Prüfobjekt-Dashboard einzelne Transaction]([LINK_URL_12])
### Listen/Diagramme zu Zeiten einzelner Transaktionsschritte

Die Zeit, die jede Aktion benötigt, ist genau so wichtig, wie die Seitenladezeit, wenn ein Nutzer die Website zum ersten Mal aufruft. Lange Wartezeiten zwischen den Nutzerinteraktionen unterwandern das Vertrauen des Nutzers in dein Produkt und deine Marke. Die Listen und Diagramme *Zeit je Transaktionsschritt* sollen dir helfen, potenzielle Probleme und Trends zu identifizieren.

Die Grafik *Zeit je Transaktionsschritt*. Diese Dashboard-Kachel zeigt die Dauer jedes Schritts der Transaktion der für jede Prüfung des Prüfobjekts über eine bestimmte Zeit gemessen wurde.

![Screenshot Kachel Zeit je Transaktionsschritt]([LINK_URL_13])

Eine weitere Art, sich die Performance der Transaktion anzusehen, besteht darin, die durchschnittliche Zeit anzuzeigen, die für jeden Schritt benötigt wird. Abhängig davon, was von einem Schritt erwartet wird, können lange Schrittzeiten daruf hinweisen, dass etwas nicht optimal funktioniert.

![Screenshot durchschnittliche Zeit Transaktionsschritt]([LINK_URL_14])

Die Liste *Zeit je Transaktionsschritt* zeigt die Schrittzeiten für jede Prüfung in Zahlen.

![Screenshot Liste Ziet je Transaktionschritt]([LINK_URL_15])

### Liste und Diagramm zum Fehlertyp

Die Liste und das Diagramm *Fehler Typ* liefern dir einen Überblick über die bestätigten Fehler, die das Prüfobjekt in dem Berichtszeitraum festgestellt hat.

![Screenshot Kachel Fehlertypen]([LINK_URL_16])

## Kontrolldetails [ANCHOR_2]

Zeige die Ergebnisse einer einzelnen Prüfung durch Klicken auf den entsprechenden Eintrag in der Kachel *Letzte Überwachungen* in deinem Dashboard *Transaktion Übersicht* oder über die Kachel *Prüfobjektprotokoll* im [Dashboard des Prüfobjekts]([LINK_URL_17]). Du wirst feststellen, dass alle Informationen bereitstehen: Datum/Uhrzeit, Ergebnis, Checkpoint, Ladezeit, Browsertyp und -version, Betriebssystem und die Ergebnisse pro Schritt.

![screenshot transaction check details]([LINK_URL_18])

In der Regel bezieht sich die **Ladezeit** (siehe Bericht oben) auf die Zeit, die erforderlich war, eine Seite im Browser anzufordern und zu laden. Aber bei Transaktionen ist die Ladezeit die Gesamtzeit, die die Transaktion von der ersten Anfrage bis zur letzten Aktion erforderte (die Summe aller Schrittzeiten).

### Ergebnis pro Schritt

Der Bereich **Ergebnis pro Schritt** sollte dir bekannt vorkommen. Dieser Abschnitt spiegelt dein Skript in einzelnen Schritten mit dem Ergebnis für jede Aktion wider. Du erhältst die Dauer pro Schritt und das Ergebnis jeder Aktion. Wenn eine Aktion fehlschlägt, wird die Prüfung abgebrochen und der Schritt rot im Bericht hervorgehoben. Wenn du über einen Business oder Enterprise Account verfügst, kannst du über den Bericht *Kontrolldetails* die Wasserfalldiagramme und Screenshots aufrufen. Klicke auf das Wasserfallsymbol [SHORTCODE_7] [SHORTCODE_8] (neben dem Schrittnamen), um den zum Schritt gehörenden Wasserfall anzuzeigen.

![]([LINK_URL_19])
