{
  "hero": {
    "title": "Prüfobjektvorlagen"
  },
  "title": "Prüfobjektvorlagen",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/pruefobjekt-management/pruefobjektvorlagen",
  "summary": "Mit einer Prüfobjektvorlage kannst du bestimmte Einstellungen gleichzeitig auf mehrere Prüfobjekte anwenden.",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Es war nie so einfach wie mit Uptrends, die Verfügbarkeit oder den Performance-Status von Websites, Servern oder Webservices zu überwachen. Aber was, wenn du eine Reihe von Services überwachen und diese schnell einrichten möchtest? Auftritt: **Prüfobjektvorlagen**.

Eine Prüfobjektvorlage ist ein Hilfsmittel, das zum Einrichten einer Gruppe von neuen Prüfobjekten mit ähnlichen Einstellungen wie *Fehlerbedingungen*, *Checkpoints* und *Wartungszeiträumen* verwendet wird. Betrachte sie als eine Möglichkeit, blitzschnell Prüfobjektkonfigurationen zu duplizieren.

## Warum sind Prüfobjektvorlagen nützlich?

Wenn du eine Reihe von Prüfobjekten einrichtest, die dieselben Fehlerbedingungen, Checkpoints für das Monitoring oder Wartungszeiträume haben, kann eine manuelle Konfiguration recht zeitintensiv und aufwendig sein. Indem du eine Prüfobjektvorlage nutzt, kannst du Zeit und Aufwand beim Festlegen von Einstellungen sparen und schnell zu deiner eigentlichen Aufgabe zurückkehren.

[SHORTCODE_1] **Hinweis**: Du musst Administrator sein oder über die [Berechtigung Prüfobjekt Vorlagen verwalten]([LINK_URL_1]) verfügen, um Vorlagen zu erstellen, zu bearbeiten oder anzuwenden. [SHORTCODE_2]

## Wie erstelle ich eine Prüfobjektvorlage?

1.  Scrolle zu [SHORTCODE_5]Accounteinstellungen > Prüfobjektvorlagen[SHORTCODE_6].
2.  Klicke auf die Schaltfläche [SHORTCODE_7]Prüfobjektvorlage hinzufügen[SHORTCODE_8] oben rechts.
3. Du kannst nun die Einstellungen deiner Vorlage anpassen:
- Gib deiner Prüfobjektvorlage einen Namen.
- In den Prüfobjekteinstellungen gibt es die Möglichkeit, [Ladezeit-Limits]([LINK_URL_2]) einzugeben, damit ein Fehler generiert wird, wenn die Server-Antwort langsamer als die angegebene Dauer ist.
Ebenso kannst du einen [User Agent]([LINK_URL_3]) auswählen, um den Browsertyp und das Betriebssystem des Nutzers anzugeben. Dies wird bei HTTPS-Anfragen an den Server gesendet. Standardmäßig ist der User Agent auf *Unverändert lassen* eingestellt.
- Unter [Checkpoints]([LINK_URL_4]) kannst du die Kontrollkästchen nutzen, um die Standorte festzulegen, von denen aus überwacht werden soll.
- Du kannst darüber hinaus [Wartungszeiträume]([LINK_URL_5]) hinzufügen und Intervalle angeben.

[SHORTCODE_3] **Hinweis**: Beim Einsatz einer Prüfobjektvorlage wenden wir nur die Einstellungen an, die du bei Erstellung der Vorlage geändert hast. Möchtest du also beispielsweise eine Vorlage nutzen, um Wartungszeiträume anzuwenden, achte darauf, nur diese Einstellungen anzupassen, wenn du die Vorlage erstellst. Das Gleiche gilt für die Anwendung einer bestimmten Checkpoint-Auswahl oder von Fehlerbedingungen. [SHORTCODE_4]

4.  Klicke auf die grüne [SHORTCODE_9]Speichern[SHORTCODE_10]-Schaltfläche, wenn du fertig bist.

Du kannst jetzt die gespeicherten Prüfobjektvorlagen auf jedes erstellte Prüfobjekt anwenden. Dabei hast du zwei Optionen. Bei der ersten Option kannst du ein einzelnes Prüfobjekt aktualisieren oder Sammel-Updates auf mehrere Prüfobjekte über das Menü [SHORTCODE_11]Prüfobjektvorlagen[SHORTCODE_12] anwenden. Die zweite Option ermöglicht dir, eine Vorlage direkt auf das aktuelle Prüfobjekt über den [SHORTCODE_13]Prüfobjekteditor [SHORTCODE_14]-Bildschirm anzuwenden. Nachfolgend findest du eine detaillierte Anweisung zur Anwendung von Prüfobjektvorlagen.

## Anwenden einer Prüfobjektvorlage
Um eine Vorlage auf ein einzelnes Prüfobjekt anzuwenden oder um ein Sammel-Update bei mehreren Prüfobjekten gleichzeitig durchzuführen

1. Scrolle zu [SHORTCODE_15]Accounteinstellungen > Prüfobjektvorlagen[SHORTCODE_16].
2. Klicke bei der gewünschten Prüfobjektvorlage auf **Anwenden**.
3. Wähle das oder die Prüfobjekte oder Prüfobjektgruppen, auf die die Vorlage angewendet werden soll.
4. Klicke auf [SHORTCODE_17] Anwenden [SHORTCODE_18].

Damit werden die festgelegten Einstellungen auf die ausgewählten Prüfobjekte bzw. Prüfobjektgruppen angewendet.

## Anwenden einer Prüfobjektvorlage über den Prüfobjekteditor-Bildschirm
Um eine Prüfobjektvorlage direkt aus dem aktuellen Prüfobjekt anzuwenden

1. Gehe zu [SHORTCODE_19]Überwachung > Prüfobjekteinrichtung[SHORTCODE_20].
2. Klicke auf das Prüfobjekt, bei dem du die Vorlage anwenden möchtest.
3. Klicke unten auf der Editorseite auf [SHORTCODE_21] Vorlage anwenden [SHORTCODE_22].
4. Wähle im Dialogfenster „Vorlage anwenden“ die gewünschte Prüfobjektvorlage aus dem Drop-down-Menü. Daraufhin werden die verfügbaren Abschnitte der gewählten Vorlage angezeigt. Über die Kontrollkästchen kannst du einzelne Bereiche anwenden oder übergehen. Deaktivierte Kontrollkästchen zeigen an, dass die Vorlage in dem Bereich über keine Einstellungen verfügt.

![Ein Screenshot mit einem Pop-up, das zeigt, wie Prüfobjektvorlagen im Editorfenster des Prüfobjekts angewendet werden]([LINK_URL_6])

5. Klicke auf die [SHORTCODE_23]Anwenden[SHORTCODE_24]-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu bestätigen.
