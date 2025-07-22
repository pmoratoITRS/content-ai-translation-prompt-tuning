{
  "hero": {
    "title": "Transaktions-Monitoring für Mobile einrichten"
  },
  "title": "Transaktions-Monitoring für Mobile einrichten",
  "summary": "Mit dem Uptrends Transaktionsrekorder können auch die Transaktionen bei mobilen Websites getestet werden. Erfahre, wie.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/transaktions-monitoring-für-mobile-einrichten",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/transaction-monitoring-for-mobile-setup"
}

Mobile Anwendungen sind aus unserem Alltag nicht wegzudenken. Das Testen für Desktop-Anwendungen allein garantiert eventuell nicht, dass die Transaktionen für deine mobilen Nutzer richtig funktionieren. Bei Uptrends kannst du den Transaktionsrekorder verwenden, um Skripte zum Monitoring der Mobilversion oder des Responsive Designs einer Website einrichten, indem du den Viewport bzw. das Darstellungsfeld eines Geräts simulierst. Den Viewport eines Geräts simulierst du über den Mobile-Simulationsmodus der Entwicklertools von Chrome. Wir sagen dir, wie.

## Den Chrome Device Mode verwenden, wenn du eine Transaktion aufzeichnest

1.  [Starte den Uptrends Transaktionsrekorder (Chrome-Erweiterung)]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder#using-transaction-recorder" lang="de" >}}) wie üblich. Es öffnet sich ein neues Browser-Fenster.
2.  Drücke die F12-Taste, um die Chrome-Entwicklertools aufzurufen.
3.  Mit der Schaltfläche zur Geräteumschaltung kannst du den Simulationsmodus aufrufen.  
![Screenshot Transaktionsrekorder Toolbar für Geräteumstellung](/img/content/scr_transaction-recorder-for-mobile.min.png)
4.  Passe die Geräteeinstellungen nach Bedarf an.
5.  Rufe die mobile Website auf.
6.  Klicke durch die Transaktion.
7.  Lade die Transaktion in deinem Account hoch, um das Skript selbst zu erstellen und zu testen. Oder lade die Aufzeichnung hoch und Uptrends‘ Support kann die Skripterstellung für dich übernehmen.
8.  Passe die mobilen Monitoring Einstellungen in deinem neuen Transaktionsprüfobjekt an.

Erfahre mehr über den [Einsatz des Device Mode](https://developer.chrome.com/docs/devtools/device-mode) im Chrome-Browser.

## Die Monitoring-Einstellungen für das Mobile-Monitoring anpassen

Nach der Aufzeichnung deiner Transaktion mithilfe des Device Mode der Entwicklertools von Chrome musst du die mobilen Einstellungen in deinen Prüfobjekteinstellungen einrichten.

1. Rufe {{< AppElement type="menuitem" >}} Transaktionen > Transaktionen einrichten {{< /AppElement >}} auf und öffne das neue Transaktionsprüfobjekt.
2. Wechsle zur Registerkarte {{< AppElement type="tab" >}} Erweitert {{< /AppElement >}}.
3. Im Abschnitt *Browser* unter *Geräte / Bildschirm* kannst du die **Bildschirmgröße** anpassen und einen **User Agent** (mit der Option, einen benutzerdefinierten User Agent auszuwählen), oder wähle **Mobile Simulation** und wähle eins der beliebten Geräte.
![Screenshot Registerkarte Erweitert des Transaktionsprüfobjekts](/img/content/scr_mobile-simulation-devices.min.png)
4. Lege eine **Bandbreiten-Drosselung** fest, wenn du die Bandbreite der Endnutzer vollständig simulieren möchtest. Lies mehr über die [Bandbreiten-Drosselung]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/bandwidth-throttling" lang="de" >}}) in der Knowledge Base.
5. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um deine Änderungen zu sichern.
