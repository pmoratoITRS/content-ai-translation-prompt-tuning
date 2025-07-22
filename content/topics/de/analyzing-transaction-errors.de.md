{
  "hero": {
    "title": "Transaktionsfehler analysieren"
  },
  "title": "Transaktionsfehler analysieren",
  "url": "/support/kb/synthetic-monitoring/transaktionen/transaktionsfehler-analysieren",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/analyzing-transaction-errors"
}

Manchmal funktionieren Dinge nicht, wie wir denken oder wie es die Erwartung wäre. Das gilt auch für Ihre überwachten Transaktionen!

Nachfolgend erläutern wir Transaktionsfehler und wie Sie sie analysieren, sodass Sie alle Probleme beheben können.

## Prüfen Sie die HTML-Anzeige

Bei einem entdeckten Transaktionsfehler macht der Service von Uptrends eine Kopie der HTML-Anzeige. Diese Daten können ein leistungsstarkes Tool sein, um zu erfahren, wie eine Seite aussah, als das Problem aufgetreten ist.

**Um die HTML-Anzeige zu prüfen:**

1.  Melden Sie sich bei Ihrem Uptrends Account an und navigieren Sie zum Dashboard Prüfobjektprotokoll im Drop-down-Menü Prüfobjekte.
2.  Klicken Sie auf einen aufgelisteten Transaktionsfehler (gleich ob unbestätigt oder bestätigt).  
    {{< callout >}}**Hinweis:** Wir können keine HTML-Ausgabe für Transaktionen mit einem “Navigations”-Fehler abbilden, da dies bedeutet, dass wir Ihre Website nicht aufrufen konnten.{{< /callout >}} 
3.  Unter Seiteninhalt und neben der Aufforderung HTML-Ergebnis können Sie die HTML-Ausgabe sehen.
4.  Um zu sehen, wie die Seite aussah, wählen Sie den HTML-Codeteil und speichern Sie ihn (in Notepad beispielsweise) als HTML-Datei
5.  Öffnen Sie die Datei in einem Browser, um die Seite anzuzeigen.

## Wird der Fehler nur von einem Checkpoint gemeldet?

Wenn ein Fehler nur von einem einzelnen Checkpoint gemeldet wird, bedeutet dies üblicherweise, dass es ein Verbindungsproblem für Nutzer in der Region ist. Es könnte auch ein spezifisches technisches Problem für den Checkpoint sein.

In diesem Fall empfehlen wir Ihnen, ein [Support-Ticket einzureichen](/contact), sodass wir das Problem untersuchen können.

## Sind Ihre Anmeldedaten noch gültig?

Manchmal ändern sich die Anmeldedaten, die für eine mehrschrittige Transaktion erforderlich sind. In diesem Fall ändern Sie bitte die Anmeldedaten für die Transaktion anhand des Transaktionseditors.
