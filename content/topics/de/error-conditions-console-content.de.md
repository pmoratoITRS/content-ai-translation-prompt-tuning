{
  "hero": {
    "title": "Fehlerbedingungen – Konsoleninhalt"
  },
  "title": "Fehlerbedingungen – Konsoleninhalt",
  "summary": "Basiere Prüfobjektchecks und Fehlergenerierung auf dem Inhalt des Konsolenprotokolls deines Browsers.",
  "url": "/support/kb/synthetic-monitoring/pruefobjekt-einstellungen/fehlerbedingungen/fehlerbedingungen-konsoleninhalt",
  "tableofcontents": true,
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/error-conditions-console-content"
}

Jedes Prüfobjekt führt einige Standardüberprüfungen je nach Prüfobjekttyp aus. Zusätzlich kannst du in den Fehlerbedingungen eines Prüfobjekts benutzerdefinierte Prüfungen festlegen, die für bestimmte Situationen Warnmeldungen generieren. Der Knowledge-Base-Artikel [Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions" lang="en" >}}) erläutert, welche dies sind und wie sie konfiguriert werden können.

Dieser Artikel erläutert, wie die Fehlerbedingungen der Kategorie *Konsoleninhalte* funktionieren. Bei einem Prüfobjekt findest du sie auf der Registerkarte {{< AppElement type="tab" >}} Fehlerbedingungen {{< /AppElement >}} im Abschnitt *Prüfe Console Inhalte*. Beachte, dass nicht alle Prüfobjekttypen dieselben Fehlerbedingungen beinhalten. Sieh dir die Tabelle der [verfügbaren Fehlerbedingungen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions#error-conditions-by-category" lang="en" >}}) an, um herauszufinden, welche Optionen für bestimmte Prüfobjekttypen möglich sind.

## Das Konsolenprotokoll des Browsers 

Wenn eine Webseite in einem Browser geladen wird, erfasst das Konsolenprotokoll des Browsers alle Protokollnachrichten. In Chrome beispielsweise findest du diese Nachrichten über die Taste „F12“, mit der du die DevTools öffnest. Wechsle dann auf die Registerkarte *Console*. Die Protokollnachrichten können des Typs Info, Warnung oder Fehler (Elementladefehler, JavaScript-Fehler usw.) sein. Protokollnachrichten können vom Webentwickler umgesetzt werden.

Du kannst Fehlerbedingungen definieren, die auf der Existenz und optional auf dem Inhalt der Protokollnachrichten basieren. Mit diesen Fehlerbedingungen kannst du prüfen, ob ein Protokoll einen Eintrag des Typs Info, Warnung oder Fehler sowie ob es einen bestimmten Text enthält. Ein Fehler wird erzeugt, wenn die definierte Bedingung erfüllt wurde.

Beachte, dass diese Fehlerbedingung sich von der Fehlerbedingung [Prüfe Seiteninhalt]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="en" >}}), bei der du den Inhalt der Seite selbst überwachst, unterscheidet.

## Konsolenprotokollnachricht existiert {id="contains-content"}

Prüfe, ob es eine Konsolenprotokollnachricht gibt und prüfe optional, ob sie einen bestimmten Inhalt enthält.

Um diese Fehlerbedingung zu definieren:

1. Gehe zu {{< AppElement type="menuitem" >}}Überwachung > Prüfobjekteinrichtung{{< /AppElement >}}.
2. Klicke auf den Prüfobjektnamen, um ihn zu bearbeiten.
3. Öffne die Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}}.
4. Klicke im Abschnitt *Prüfe Console Inhalte* auf {{< AppElement type="buttonSecondary" >}} \+ Neue Prüfung {{< /AppElement >}}, um eine neue Prüfung hinzuzufügen.

    ![Screenshot Konsoleninhalt prüfen](/img/content/scr_errorconditions-console-content.min.png)

5. Wähle die Option **Error, wenn die Console einen bestimmten Inhalt enthält**.
6. Wähle den Message Level (Info, Fehler, Warnung).
7. Das Feld **Nachrichten Text** funktioniert folgendermaßen: Wenn du es frei lässt, prüft das Prüfobjekt nur, ob ein Protokolleintrag des ausgewählten Message Levels besteht, ungeachtet seines Inhalts. Wenn du auf einen bestimmten Inhalt im Protokolleintrag prüfen möchtest, gib den Text in das Feld **Nachrichten Text** ein. Das kann ein Wort, eine Phrase oder ein regulärer Ausdruck sein.
8. Füge nach Bedarf weitere Prüfungen hinzu.
9. Klicke auf die {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}-Schaltfläche, um alle Änderungen bei dem Prüfobjekt zu sichern.

## Konsolenprotokollsnachricht existiert nicht

Statt die Existenz von Protokollnachrichten zu prüfen, solltest du eventuell auch prüfen, dass es keine Protokollnachrichten und optional mit bestimmtem Inhalt gibt.

Führe die gleichen Schritte wie unter [Konsolenprotokollnachricht existiert]({{< ref path="#contains-content" lang="en" >}}) aus, aber wähle die Option **Error, wenn die Console einen bestimmten Inhalt nicht enthält**.

Wähle dann, auf welchen Message Level (Info, Fehler, Warnung) im Protokoll du prüfen möchtest. Wenn du das Feld **Nachrichten Text** frei lässt, erzeugt diese Bedingung einen Fehler, wenn keine Protokollnachrichten des Levels existieren. Wenn du etwas in das Feld **Nachrichten Text** eingibst, erzeugt diese Bedingung einen Fehler, wenn keine Protokollnachrichten des Levels mit dem angegebenen Text existieren.

## Ergebnis einer Inhaltsprüfung der Konsolenmeldung

Das Prüfobjekt führt die Prüfung aus, wobei deine Einstellungen für diese Fehlerbedingung berücksichtigt werden. Wenn du die [Kontrolldetails]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/check-details" lang="en" >}}) öffnest, kannst du dir die Ergebnisse ansehen. Hat die Prüfung statt einer „OK“-Meldung einen Fehler ergeben, kannst du anhand der Informationen in den Kontrolldetails sehen, welche Fehlerbedingung den Fehler ausgelöst hat. Es kann dir einen Hinweis bieten, wo du mit der Fehlerbehebung ansetzen kannst.

