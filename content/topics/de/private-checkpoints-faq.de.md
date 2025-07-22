{
  "hero": {
    "title": "Private Checkpoints – FAQ"
  },
  "title": "Private Checkpoints – FAQ",
  "summary": "Häufig gestellte Fragen über Uptrends' private Checkpoints",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-standorte/private-checkpoints-faq",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/private-checkpoints-faq"
}

## Kann ich mehrere private Checkpoints haben?

Ja, das geht. Wenn dein Unternehmen beispielsweise über mehrere Hosting-Standorte verfügt, kannst du an jedem relevanten Standort einen [privaten Checkpoint]({{< ref path="support/kb/synthetic-monitoring/checkpoints/#user-managed" lang="de" >}}) einrichten.

## Kann ich meinen privaten Checkpoint bei mehreren Uptrends Accounts verwenden?

Ja, das geht. Sag uns, für welche Accounts du deinen privaten Checkpoint nutzen möchtest, und der Checkpoint wird für diese Accounts aktiviert. Nur du wirst Zugriff auf deinen privaten Checkpoint haben.

## Warum gibt es standardmäßig zwei private Checkpoints? {id="two-default-private-checkpoints"}

Wenn du einen neuen [privaten Standort]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations" lang="de" >}}) einrichtest, werden standardmäßig zwei private Checkpoints zu diesem Standort hinzugefügt.

Der Grund ist, dass du in der empfohlenen Einrichtung zwei Checkpoints benötigst, um eine regelrechte Verfügbarkeit für deinen privaten Standort zu haben. Wenn du redundante Checkpoints hast, kann ein Checkpoint gewartet werden, während der andere weiterhin für das Monitoring deines Standorts verfügbar ist. Und sollte einer der Checkpoints aus irgendeinem Grund ausfallen, kann der andere ebenfalls immer noch deine Websites, Services oder Server überwachen.

## Kann ich Transaktionsprüfobjekte für meine internen Unternehmensanwendungen nutzen?

Ja, das ist möglich. Die Funktion von Uptrends ist verfügbar, sodass du ohne Frage ein Transaktions-Monitoring bei deinen intern gehosteten Anwendungen einsetzen kannst.

## Muss ich Transaktionsskripte selbst erstellen?

Nein. Zeichne deine [Transaktionen]({{< ref path="features/transaction-recorder" lang="de" >}}) mit dem Chrome-Plug-in des Transaktionsrekorders wie gewohnt auf. Du kannst dann wählen, ob du selbst oder unsere Transaktionsentwickler deine Aufzeichnung in eine stabile, ausführbare Transaktion umwandeln.

## Welche Prüfobjekt-Browsertypen werden unterstützt?

Der Full Pagecheck und Transaktionsprüfobjekte mit den [Browsertypen mit extra Metriken]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/extra-metrics-and-features" lang="de" >}}) werden an privaten Standorten unterstützt. Beachte, dass ältere Prüfobjekte ohne Browser mit extra Metriken nicht unterstützt werden.

## Wie verhindere ich, dass Screenshots und Filmstrips in die Cloud hochgeladen werden?

Nutze [Datenschutz]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-data-protection" lang="de" >}}), um die Erzeugung von Screenshots, Filmstrips und Fehler-Screenshots für ein HTTP(S)-Prüfobjekt an deinen Checkpoints für private Standorte zu verhindern.

## Wie kann ich Fehler beheben?

Nutze den [Leitfaden zur Fehlerbehebung]({{< ref path="support/kb/synthetic-monitoring/checkpoints/private-locations/private-locations-troubleshooting" lang="de" >}}) der Uptrends Knowledge Base.

## Ich möchte mehr erfahren. Wen kann ich ansprechen?

Dein Uptrends Monitoring Consultant steht immer bereit. Wenn du die Telefonnummer oder E-Mail-Adresse deines Consultants kennst, wende dich direkt an ihn oder sie. Wenn du nicht weißt, wer dein Monitoring Consultant ist, oder nicht über die Kontaktinfos verfügst, rufe bitte unsere [Kontaktseite]({{< ref path="contact" lang="de" >}}) im Web auf und reiche ein Support-Ticket ein. Du kannst dich auch telefonisch an unsere internationalen Standorte wenden.

## Hast du noch Fragen oder Bedenken?

Sollte dir zu irgendeinem Zeitpunkt bei der Einrichtung etwas nicht klar sein, oder wenn du sonstige Fragen hast, wende dich bitte an Uptrends, indem du ein [Support-Ticket]({{< ref path="contact" lang="de" >}}). einreichst. Wir werden uns so schnell wie möglich zurückmelden.