{
  "hero": {
    "title": "Prüfobjekt-Anmerkungen"
  },
  "title": "Prüfobjekt-Anmerkungen",
  "summary": "Hinzufügen und Bearbeiten von Anmerkungen bei deinen Prüfobjekten, um die Kommunikation zu vereinfachen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-einstellungen/pruefobjekt-anmerkungen",
  "translationKey": "[URL_1]
}

 Die Anmerkungen bzw. Notizen bei Uptrends‘ Prüfobjekten können genutzt werden, um die interne Kommunikation zwischen Operatoren zu vereinfachen. Es ist eine gute Möglichkeit, Themen zu (den Einstellungen von) Prüfobjekten anzuzeigen. Das Dashboard **Prüfobjektstatus** zeigt, welche Prüfobjekte über eine Anmerkung bzw. Notiz verfügen, und ihr Inhalt kann sichtbar gemacht werden, ohne dass das Prüfobjekt aufgerufen werden muss. So können Operatoren schnell Informationen zum internen Status erhalten, die von einem anderen Operator eingegeben wurden, darunter:

- Prüfobjektstatus
- Häufige Fehler und Anweisungen, wie sie behoben werden, wenn sie auftreten
- Kurzinfo, wer an etwas arbeitet, sodass andere Teammitglieder sich auf andere Probleme konzentrieren können

Nehmen wir ein _SSL-Zertifikats-Prüfobjekt_ als Beispiel. Das Prüfobjekt warnt im Vorhinein, dass das Zertifikat ablaufen wird. Als Nächstes ergreift ein Operator die Maßnahme, das Zertifikat zu erneuern, und vermerkt in den Anmerkungen, dass das Thema in Arbeit ist. Wurde das Zertifikat dann erneuert, kann der Text in den **Anmerkungen** gelöscht werden.
 
## Wie füge ich eine Prüfobjekt-Anmerkung hinzu? 
Jeder Bearbeitungsbildschirm eines Prüfobjekts verfügt über ein freies Textfeld mit dem Titel **Anmerkungen**.
Rufe die Prüfobjekteinstellungen auf:
1. Gehe zu [SHORTCODE_1] Überwachung > Prüfobjekteinrichtung [SHORTCODE_2].
2. Klicke auf [SHORTCODE_3] Prüfobjekteinrichtung [SHORTCODE_4].
3. Klicke auf den Namen des Prüfobjekts, für das du die Einstellungen aufrufen möchtest. Klicke den zugehörigen Link in der Spalte **Prüfobjekt Name**. Du kannst die Übersicht auch filtern, indem du (einen Teil des) Prüfobjektnamens, -typs, der -gruppe oder der URL in das Suchfeld eingibst und die Eingabetaste drückst.
4. Die Prüfobjektkonfiguration öffnet sich auf der Registerkarte [SHORTCODE_5] Allgemein [SHORTCODE_6].
![Eingabe einer Anmerkung im Freitextfeld]([LINK_URL_1])
5. Gib unter **Metadaten** im Feld **Anmerkungen** deine Notizen ein.
6. Wenn du alle gewünschten Anmerkungen eingefügt hast, klicke auf [SHORTCODE_7] Speichern [SHORTCODE_8].

## Wo werden die Notizen angezeigt? 
Die Notizen werden im Dashboard **Prüfobjektstatus** angezeigt. (Rufe im Menü [SHORTCODE_9] Überwachung > Prüfobjektstatus [SHORTCODE_10] auf.) Die zweite Dashboard-Spalte zeigt dir, welche Prüfobjekte über eine Notiz bzw. Anmerkung verfügen. Wenn für das Prüfobjekt eine Anmerkung eingegeben wurde, wird dies durch ein aktives Symbol angezeigt. Gibt es keine Anmerkungen, ist das Symbol ausgegraut. Zeigt ein Operator mit der Maus auf das Symbol, kann er die Notiz lesen.

![Notiz im Status-Dashboard des Prüfobjekts]([LINK_URL_2])

Notizen sind auch in der Kurzinfo des Prüfobjekts sichtbar:

![Anmerkung in der Kurzinfo des Status-Dashboards]([LINK_URL_3])
## Wer hat Zugriff auf Prüfobjekt-Notizen? 
Gehe zu [SHORTCODE_11] Accounteinstellungen > Account Einstellungen [SHORTCODE_12]. Auf der Registerkarte [SHORTCODE_13] Einstellungen [SHORTCODE_14] unter Zugriff auf Prüfobjekt-Notizen kannst du festlegen, welche Operatoren das Recht haben, Notizen anzuzeigen.
![Zugriff auf Prüfobjekt-Notizen]([LINK_URL_4])
Hinweis: Die Berechtigungseinstellung ist nur bei Enterprise Accounts verfügbar.