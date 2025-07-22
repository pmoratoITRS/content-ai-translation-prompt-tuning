{
  "hero": {
    "title": "Anzeige deiner Monitoring-Daten in Grafana"
  },
  "title": "Grafana-Integration",
  "summary": "Ein Leitfaden zur Anzeige deiner Monitoring-Daten in Grafana.",
  "url": "[URL_BASE_TOPICS]dashboards-und-berichte/grafana",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die Uptrends Grafana-Datenquelle ermöglicht es, Informationen zu Status und Statistiken, die von Uptrends‘ Prüfobjekten und Prüfobjektgruppen berichtet werden, innerhalb der Grafana-Umgebung anzuzeigen. Es nutzt die Uptrends API, um statistische Daten oder Daten zum aktuellen Status deiner Prüfobjekte und Prüfobjektgruppen abzurufen.

Diese Anleitung beschreibt, wie du eine grundlegende Grafana-Instanz einrichtest, die eine Verbindung zu Uptrends aufbauen und Daten abrufen kann, sodass sie in deiner Grafana-Umgebung angezeigt werden. Bitte [nimm Kontakt zu uns auf]([LINK_URL_1]), wenn du ein Problem feststellst, Fragen hast oder uns Feedback geben möchtest.

## Voraussetzungen
- Ein aktiver Uptrends Account
- Uptrends APIv4 Anmeldedaten: Mit diesem Leitfaden erfährst du, wie du sie generierst.
- Eine Grafana-Instanz mit Zugriff auf die Server-Konfiguration.

## Vor der Konfiguration

### Erstelle einen Uptrends APIv4 Account

[SHORTCODE_1] **Hinweis**: Wenn du bereits über APIv4 Anmeldedaten verfügst, kannst du sie verwenden und diesen Schritt überspringen.  [SHORTCODE_2]

Grafana kommuniziert mit Uptrends über die API (Version 4 – weitere Infos in der [API-Dokumentation]([LINK_URL_2])), indem die entsprechenden Daten abgefragt und dann in deinen Grafana-Dashboards angezeigt werden. Um diese Abfragen ausführen zu können, muss Grafana Zugang zu deinem registrierten API-Account haben. Erzeuge einen API-Account, indem du den Anweisungen des Artikels [API-Accountmanagement für Operatoren]([LINK_URL_3]) folgst.

Die in dem Artikel dargestellten Schritte liefern dir einen Benutzernamen und ein Passwort. Schreibe diese auf, da du sie später in Grafanas Datenquelle hinzufügen musst.

Ein API-Account ist mit einem Operator in Uptrends verknüpft. Stelle sicher, dass der Operator zumindest über die [Berechtigung *Monitoring Daten der Gruppe betrachten*]([LINK_URL_4]) für jedes Prüfobjekt oder für die Prüfobjektgruppen verfügt, die du in Grafana anzeigen möchtest.

## Installieren des Plug-ins

1. **Lade das Plug-in herunter –** Das Grafana Plug-in von Uptrends gibt es derzeit in der [Version 0.9.274]([LINK_URL_5]). Die neueste Zip-Datei ist über diesen [Link]([LINK_URL_6]) verfügbar.
2. **Extrahiere die .zip-Datei und kopiere ihren Inhalt in das Verzeichnis des Grafana-Plug-ins –** der Standard-Ablageort für das Plug-in-Verzeichnis lautet [INLINE_CODE_1]. Weitere Informationen findest du in der Grafana-Dokumentation.
3. **Aktiviere das Plug-in –** das Plug-in ist derzeit unsigniert. Das bedeutet, dass es ausdrücklich in der Grafana-Konfiguration aktiviert werden muss. Führe Folgendes aus, um das Plug-in zu aktivieren:

    - Finde auf dem Server, der als Host deiner Grafana-Instanz dient, die *grafana.ini* (der Standard-Standort lautet [INLINE_CODE_2]) und öffne die Datei mit deinem bevorzugten Texteditor.
    - Unter [INLINE_CODE_3] (dies ist eventuell ziemlich weit unten zu finden, die Suchfunktion führt dich schneller an die Stelle) siehst du den Schlüssel [INLINE_CODE_4].
    - Füge den Wert [INLINE_CODE_5] zum Befehl [INLINE_CODE_6] hinzu.

![Unsigniertes Plug-in erlauben]([LINK_URL_7])

4. **Führe einen Neustart von Grafana durch –** das Plug-in sollte nun einsatzbereit in der Grafana-Oberfläche zu sehen sein.

## Erstellen der Datenquelle
1. Rufe in deiner Grafana-Benutzeroberfläche _Konfiguration_ (das Rädchen im linken Menü) -> _Data Sources_ auf.
2. Klicke auf _Add data source_.
3. Wähle _Uptrends_ und klicke auf das angezeigte Plug-in (es sollte [INLINE_CODE_7] heißen).
4. Gib den APIv4-Benutzernamen und das Passwort ein, die du bei Schritt 1 dieses Leitfadens erzeugt hast, oder nutze bereits bestehende Anmeldedaten.
5. Klicke auf _Save & test_.

![Datenquelle wird erstellt]([LINK_URL_8])

### Ein Dashboard erstellen

Da die Datenquelle nun eingerichtet ist, kann sie Daten von Uptrends abrufen und die Grafana-Dashboards mit diesen Daten befüllen.

1. Wechsle zu *Dashboards > + New Dashboard*, oder bearbeite ein bestehendes Dashboard.
2. Klicke auf *Add a new panel*.

![Editing a panel]([LINK_URL_9])

3. Stelle sicher, dass die richtige Datenquelle ([INLINE_CODE_8]) als **Data source** des Panels ausgewählt ist.
4. Wähle oben rechts einen Paneltyp und weitere Optionen, wie sie im rechten Menü abgefragt werden.
5. Wähle die Daten aus, die du anzeigen möchtest.

    - Du kannst zwischen Prüfobjekt-Statusdaten (in Bezug auf den aktuellen Fehler/Ok-Status deiner Prüfobjekte) und Prüfobjektstatistiken (in Bezug auf die Performance von Prüfobjekten für einen Zeitraum) wählen.

    - Du kannst bei jeder hinzugefügten Abfrage nach bestimmten Prüfobjekten oder Prüfobjektgruppen filtern. Die Listen der Prüfobjekte und Prüfobjektgruppen sollten automatisch ausgefüllt sein.

  ![Auswahl von Uptrends Daten, die im Panel angezeigt werden]([LINK_URL_10])

6. Klicke oben rechts auf *Apply*.

Diese Anleitung ist nur eine grundlegende Beschreibung, wie du Daten von Uptrends in Grafana anzeigen kannst. Als vollständiges Produkt bietet Grafana viele zusätzliche Optionen.
