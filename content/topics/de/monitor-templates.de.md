{
  "hero": {
    "title": "Prüfobjektvorlagen"
  },
  "title": "Prüfobjektvorlagen",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-management/pruefobjektvorlagen",
  "summary":"Mit einer Prüfobjektvorlage kannst du bestimmte Einstellungen gleichzeitig auf mehrere Prüfobjekte anwenden.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-management/monitor-templates"
}

Es war nie so einfach wie mit Uptrends, die Verfügbarkeit oder den Performance-Status von Websites, Servern oder Webservices zu überwachen. Aber was, wenn du eine Reihe von Services überwachen und diese schnell einrichten möchtest? Auftritt: **Prüfobjektvorlagen**.

Eine Prüfobjektvorlage ist ein Hilfsmittel, das zum Einrichten einer Gruppe von neuen Prüfobjekten mit ähnlichen Einstellungen wie *Fehlerbedingungen*, *Checkpoints* und *Wartungszeiträumen* verwendet wird. Betrachte sie als eine Möglichkeit, blitzschnell Prüfobjektkonfigurationen zu duplizieren.

## Warum sind Prüfobjektvorlagen nützlich?

Wenn du eine Reihe von Prüfobjekten einrichtest, die dieselben Fehlerbedingungen, Checkpoints für das Monitoring oder Wartungszeiträume haben, kann eine manuelle Konfiguration recht zeitintensiv und aufwendig sein. Indem du eine Prüfobjektvorlage nutzt, kannst du Zeit und Aufwand beim Festlegen von Einstellungen sparen und schnell zu deiner eigentlichen Aufgabe zurückkehren.

{{< callout >}} **Hinweis**: Du musst Administrator sein oder über die [Berechtigung Prüfobjekt Vorlagen verwalten]({{< ref path="/support/kb/account/users/operators/permissions#manage-monitor-templates" lang="de" >}}) verfügen, um Vorlagen zu erstellen, zu bearbeiten oder anzuwenden. {{< /callout >}}

## Wie erstelle ich eine Prüfobjektvorlage?

1.  Scrolle zu {{< AppElement type="menuitem" >}}Accounteinstellungen > Prüfobjektvorlagen{{< /AppElement >}}.
2.  Klicke auf die Schaltfläche {{< AppElement type="button" >}}Prüfobjektvorlage hinzufügen{{< /AppElement >}} oben rechts.
3. Du kannst nun die Einstellungen deiner Vorlage anpassen:
- Gib deiner Prüfobjektvorlage einen Namen.
- In den Prüfobjekteinstellungen gibt es die Möglichkeit, [Ladezeit-Limits]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="de" >}}) einzugeben, damit ein Fehler generiert wird, wenn die Server-Antwort langsamer als die angegebene Dauer ist.
Ebenso kannst du einen [User Agent]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/user-agents-and-real-browser-checks" lang="de" >}}) auswählen, um den Browsertyp und das Betriebssystem des Nutzers anzugeben. Dies wird bei HTTPS-Anfragen an den Server gesendet. Standardmäßig ist der User Agent auf *Unverändert lassen* eingestellt.
- Unter [Checkpoints]({{< ref path="/support/kb/synthetic-monitoring/checkpoints" lang="de" >}}) kannst du die Kontrollkästchen nutzen, um die Standorte festzulegen, von denen aus überwacht werden soll.
- Du kannst darüber hinaus [Wartungszeiträume]({{< ref path="/support/kb/synthetic-monitoring/monitor-management/maintenance-periods" lang="de" >}}) hinzufügen und Intervalle angeben.

{{< callout >}} **Hinweis**: Beim Einsatz einer Prüfobjektvorlage wenden wir nur die Einstellungen an, die du bei Erstellung der Vorlage geändert hast. Möchtest du also beispielsweise eine Vorlage nutzen, um Wartungszeiträume anzuwenden, achte darauf, nur diese Einstellungen anzupassen, wenn du die Vorlage erstellst. Das Gleiche gilt für die Anwendung einer bestimmten Checkpoint-Auswahl oder von Fehlerbedingungen. {{< /callout >}}

4.  Klicke auf die grüne {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, wenn du fertig bist.

Du kannst jetzt die gespeicherten Prüfobjektvorlagen auf jedes erstellte Prüfobjekt anwenden. Dabei hast du zwei Optionen. Bei der ersten Option kannst du ein einzelnes Prüfobjekt aktualisieren oder Sammel-Updates auf mehrere Prüfobjekte über das Menü {{< AppElement type="menuitem" >}}Prüfobjektvorlagen{{< /AppElement >}} anwenden. Die zweite Option ermöglicht dir, eine Vorlage direkt auf das aktuelle Prüfobjekt über den {{< AppElement type="menuitem" >}}Prüfobjekteditor {{< /AppElement >}}-Bildschirm anzuwenden. Nachfolgend findest du eine detaillierte Anweisung zur Anwendung von Prüfobjektvorlagen.

## Anwenden einer Prüfobjektvorlage
Um eine Vorlage auf ein einzelnes Prüfobjekt anzuwenden oder um ein Sammel-Update bei mehreren Prüfobjekten gleichzeitig durchzuführen

1. Scrolle zu {{< AppElement type="menuitem" >}}Accounteinstellungen > Prüfobjektvorlagen{{< /AppElement >}}.
2. Klicke bei der gewünschten Prüfobjektvorlage auf **Anwenden**.
3. Wähle das oder die Prüfobjekte oder Prüfobjektgruppen, auf die die Vorlage angewendet werden soll.
4. Klicke auf {{< AppElement type="button" >}} Anwenden {{< /AppElement >}}.

Damit werden die festgelegten Einstellungen auf die ausgewählten Prüfobjekte bzw. Prüfobjektgruppen angewendet.

## Anwenden einer Prüfobjektvorlage über den Prüfobjekteditor-Bildschirm
Um eine Prüfobjektvorlage direkt aus dem aktuellen Prüfobjekt anzuwenden

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Klicke auf das Prüfobjekt, bei dem du die Vorlage anwenden möchtest.
3. Klicke unten auf der Editorseite auf {{< AppElement type="button" >}} Vorlage anwenden {{< /AppElement >}}.
4. Wähle im Dialogfenster „Vorlage anwenden“ die gewünschte Prüfobjektvorlage aus dem Drop-down-Menü. Daraufhin werden die verfügbaren Abschnitte der gewählten Vorlage angezeigt. Über die Kontrollkästchen kannst du einzelne Bereiche anwenden oder übergehen. Deaktivierte Kontrollkästchen zeigen an, dass die Vorlage in dem Bereich über keine Einstellungen verfügt.

![Ein Screenshot mit einem Pop-up, das zeigt, wie Prüfobjektvorlagen im Editorfenster des Prüfobjekts angewendet werden](/img/content/scr-apply-monitor-template-monitor-editor-page.min.png)

5. Klicke auf die {{< AppElement type="button" >}}Anwenden{{< /AppElement >}}-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu bestätigen.
