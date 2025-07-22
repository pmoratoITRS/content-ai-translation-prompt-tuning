{
  "hero": {
    "title": "Anzeige deiner Monitoring-Daten in Grafana"
  },
  "title": "Grafana-Integration",
  "summary": "Ein Leitfaden zur Anzeige deiner Monitoring-Daten in Grafana.",
  "url": "/support/kb/dashboards-und-berichte/grafana",
  "translationKey": "https://www.uptrends.com/support/kb/integrations/grafana"
}

Die Uptrends Grafana-Datenquelle ermöglicht es, Informationen zu Status und Statistiken, die von Uptrends‘ Prüfobjekten und Prüfobjektgruppen berichtet werden, innerhalb der Grafana-Umgebung anzuzeigen. Es nutzt die Uptrends API, um statistische Daten oder Daten zum aktuellen Status deiner Prüfobjekte und Prüfobjektgruppen abzurufen.

Diese Anleitung beschreibt, wie du eine grundlegende Grafana-Instanz einrichtest, die eine Verbindung zu Uptrends aufbauen und Daten abrufen kann, sodass sie in deiner Grafana-Umgebung angezeigt werden. Bitte [nimm Kontakt zu uns auf]({{< ref path="/contact" lang="de" >}}), wenn du ein Problem feststellst, Fragen hast oder uns Feedback geben möchtest.

## Voraussetzungen
- Ein aktiver Uptrends Account
- Uptrends APIv4 Anmeldedaten: Mit diesem Leitfaden erfährst du, wie du sie generierst.
- Eine Grafana-Instanz mit Zugriff auf die Server-Konfiguration.

## Vor der Konfiguration

### Erstelle einen Uptrends APIv4 Account

{{< callout >}} **Hinweis**: Wenn du bereits über APIv4 Anmeldedaten verfügst, kannst du sie verwenden und diesen Schritt überspringen.  {{< /callout >}}

Grafana kommuniziert mit Uptrends über die API (Version 4 – weitere Infos in der [API-Dokumentation]({{< ref path="/support/kb/api" lang="de" >}})), indem die entsprechenden Daten abgefragt und dann in deinen Grafana-Dashboards angezeigt werden. Um diese Abfragen ausführen zu können, muss Grafana Zugang zu deinem registrierten API-Account haben. Erzeuge einen API-Account, indem du den Anweisungen des Artikels [API-Accountmanagement für Operatoren]({{< ref path="/support/kb/account/users/operators/operator-API-management" lang="de" >}}) folgst.

Die in dem Artikel dargestellten Schritte liefern dir einen Benutzernamen und ein Passwort. Schreibe diese auf, da du sie später in Grafanas Datenquelle hinzufügen musst.

Ein API-Account ist mit einem Operator in Uptrends verknüpft. Stelle sicher, dass der Operator zumindest über die [Berechtigung *Monitoring Daten der Gruppe betrachten*]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/monitor-permissions" lang="de" >}}) für jedes Prüfobjekt oder für die Prüfobjektgruppen verfügt, die du in Grafana anzeigen möchtest.

## Installieren des Plug-ins

1. **Lade das Plug-in herunter –** Das Grafana Plug-in von Uptrends gibt es derzeit in der [Version 0.9.274](https://www.uptrends.com/grafana-downloads/Uptrends_Grafana.0.9.274.zip). Die neueste Zip-Datei ist über diesen [Link](https://www.uptrends.com/grafana-downloads/Uptrends_Grafana_latest.zip) verfügbar.
2. **Extrahiere die .zip-Datei und kopiere ihren Inhalt in das Verzeichnis des Grafana-Plug-ins –** der Standard-Ablageort für das Plug-in-Verzeichnis lautet `/var/lib/grafana/plugins`. Weitere Informationen findest du in der Grafana-Dokumentation.
3. **Aktiviere das Plug-in –** das Plug-in ist derzeit unsigniert. Das bedeutet, dass es ausdrücklich in der Grafana-Konfiguration aktiviert werden muss. Führe Folgendes aus, um das Plug-in zu aktivieren:

    - Finde auf dem Server, der als Host deiner Grafana-Instanz dient, die *grafana.ini* (der Standard-Standort lautet `/etc/grafana/grafana.ini`) und öffne die Datei mit deinem bevorzugten Texteditor.
    - Unter `[plugins]` (dies ist eventuell ziemlich weit unten zu finden, die Suchfunktion führt dich schneller an die Stelle) siehst du den Schlüssel `allow_loading_unsigned_plugins`.
    - Füge den Wert `uptrends-uptrends-plugin` zum Befehl `allow_loading_unsigned_plugins` hinzu.

![Unsigniertes Plug-in erlauben](/img/content/scr-grafana-allow-unsigned-plugins.min.png)

4. **Führe einen Neustart von Grafana durch –** das Plug-in sollte nun einsatzbereit in der Grafana-Oberfläche zu sehen sein.

## Erstellen der Datenquelle
1. Rufe in deiner Grafana-Benutzeroberfläche _Konfiguration_ (das Rädchen im linken Menü) -> _Data Sources_ auf.
2. Klicke auf _Add data source_.
3. Wähle _Uptrends_ und klicke auf das angezeigte Plug-in (es sollte `uptrends-plugin` heißen).
4. Gib den APIv4-Benutzernamen und das Passwort ein, die du bei Schritt 1 dieses Leitfadens erzeugt hast, oder nutze bereits bestehende Anmeldedaten.
5. Klicke auf _Save & test_.

![Datenquelle wird erstellt](/img/content/scr-grafana-plugin-config.min.png)

### Ein Dashboard erstellen

Da die Datenquelle nun eingerichtet ist, kann sie Daten von Uptrends abrufen und die Grafana-Dashboards mit diesen Daten befüllen.

1. Wechsle zu *Dashboards > + New Dashboard*, oder bearbeite ein bestehendes Dashboard.
2. Klicke auf *Add a new panel*.

![Editing a panel](/img/content/scr-grafana-edit-panel.min.png)

3. Stelle sicher, dass die richtige Datenquelle (`uptrends-plugin`) als **Data source** des Panels ausgewählt ist.
4. Wähle oben rechts einen Paneltyp und weitere Optionen, wie sie im rechten Menü abgefragt werden.
5. Wähle die Daten aus, die du anzeigen möchtest.

    - Du kannst zwischen Prüfobjekt-Statusdaten (in Bezug auf den aktuellen Fehler/Ok-Status deiner Prüfobjekte) und Prüfobjektstatistiken (in Bezug auf die Performance von Prüfobjekten für einen Zeitraum) wählen.

    - Du kannst bei jeder hinzugefügten Abfrage nach bestimmten Prüfobjekten oder Prüfobjektgruppen filtern. Die Listen der Prüfobjekte und Prüfobjektgruppen sollten automatisch ausgefüllt sein.

  ![Auswahl von Uptrends Daten, die im Panel angezeigt werden](/img/content/scr-grafana-populating-panel.min.png)

6. Klicke oben rechts auf *Apply*.

Diese Anleitung ist nur eine grundlegende Beschreibung, wie du Daten von Uptrends in Grafana anzeigen kannst. Als vollständiges Produkt bietet Grafana viele zusätzliche Optionen.
