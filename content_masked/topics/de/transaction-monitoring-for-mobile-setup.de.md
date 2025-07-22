{
  "hero": {
    "title": "Transaktions-Monitoring für Mobile einrichten"
  },
  "title": "Transaktions-Monitoring für Mobile einrichten",
  "summary": "Mit dem Uptrends Transaktionsrekorder können auch die Transaktionen bei mobilen Websites getestet werden. Erfahre, wie.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transaktionen/transaktions-monitoring-für-mobile-einrichten",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mobile Anwendungen sind aus unserem Alltag nicht wegzudenken. Das Testen für Desktop-Anwendungen allein garantiert eventuell nicht, dass die Transaktionen für deine mobilen Nutzer richtig funktionieren. Bei Uptrends kannst du den Transaktionsrekorder verwenden, um Skripte zum Monitoring der Mobilversion oder des Responsive Designs einer Website einrichten, indem du den Viewport bzw. das Darstellungsfeld eines Geräts simulierst. Den Viewport eines Geräts simulierst du über den Mobile-Simulationsmodus der Entwicklertools von Chrome. Wir sagen dir, wie.

## Den Chrome Device Mode verwenden, wenn du eine Transaktion aufzeichnest

1.  [Starte den Uptrends Transaktionsrekorder (Chrome-Erweiterung)]([LINK_URL_1]) wie üblich. Es öffnet sich ein neues Browser-Fenster.
2.  Drücke die F12-Taste, um die Chrome-Entwicklertools aufzurufen.
3.  Mit der Schaltfläche zur Geräteumschaltung kannst du den Simulationsmodus aufrufen.  
![Screenshot Transaktionsrekorder Toolbar für Geräteumstellung]([LINK_URL_2])
4.  Passe die Geräteeinstellungen nach Bedarf an.
5.  Rufe die mobile Website auf.
6.  Klicke durch die Transaktion.
7.  Lade die Transaktion in deinem Account hoch, um das Skript selbst zu erstellen und zu testen. Oder lade die Aufzeichnung hoch und Uptrends‘ Support kann die Skripterstellung für dich übernehmen.
8.  Passe die mobilen Monitoring Einstellungen in deinem neuen Transaktionsprüfobjekt an.

Erfahre mehr über den [Einsatz des Device Mode]([LINK_URL_3]) im Chrome-Browser.

## Die Monitoring-Einstellungen für das Mobile-Monitoring anpassen

Nach der Aufzeichnung deiner Transaktion mithilfe des Device Mode der Entwicklertools von Chrome musst du die mobilen Einstellungen in deinen Prüfobjekteinstellungen einrichten.

1. Rufe [SHORTCODE_1] Transaktionen > Transaktionen einrichten [SHORTCODE_2] auf und öffne das neue Transaktionsprüfobjekt.
2. Wechsle zur Registerkarte [SHORTCODE_3] Erweitert [SHORTCODE_4].
3. Im Abschnitt *Browser* unter *Geräte / Bildschirm* kannst du die **Bildschirmgröße** anpassen und einen **User Agent** (mit der Option, einen benutzerdefinierten User Agent auszuwählen), oder wähle **Mobile Simulation** und wähle eins der beliebten Geräte.
![Screenshot Registerkarte Erweitert des Transaktionsprüfobjekts]([LINK_URL_4])
4. Lege eine **Bandbreiten-Drosselung** fest, wenn du die Bandbreite der Endnutzer vollständig simulieren möchtest. Lies mehr über die [Bandbreiten-Drosselung]([LINK_URL_5]) in der Knowledge Base.
5. Klicke auf die [SHORTCODE_5]Speichern[SHORTCODE_6]-Schaltfläche, um deine Änderungen zu sichern.
