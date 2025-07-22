{
  "hero": {
    "title": "Eine Seriennummer in einem SOA Record überprüfen"
  },
  "title": "Eine Seriennummer in einem SOA Record überprüfen",
  "summary": "Überprüfe eine Seriennummer in einem SOA Record mithilfe eines DNS-Prüfobjekts. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/verfuegbarkeits-monitoring/dns/seriennummer-in-soa-record-pruefen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Das DNS-Prüfobjekt kann verwendet werden, um die von einem Nameserver für eine Domain genannte Seriennummer zu verifizieren. Die Seriennummer ist ein spezifisches Merkmal eines Domainnamens, den der Nameserver im SOA (Start of Authority) Record speichert. Der Nameserver zählt die Seriennummer hoch, wenn die DNS-Einstellungen für eine Domain geändert werden. Indem du auf die Seriennummer achtest, weißt du anhand von Warnmeldungen, wenn der DNS-Eintrag sich ändert und sich eventuell jemand daran vergriffen hat. Mit diesem Artikel führen wir dich durch den Prozess, die Seriennummer abzurufen und das DNS-Prüfobjekt einzurichten, um den Wert zu verifizieren.

## Zunächst musst du die aktuelle Seriennummer herausfinden.

Um die aktuelle Seriennummer herausfinden, musst du eine SOA-Anfrage senden.

1.  Öffne ein Terminal-Fenster.
2.  Gib [INLINE_CODE_1] ein und drücke die [Eingabetaste].
3.  Wechsle zur Abfrage des SOA Records, indem du [INLINE_CODE_2] eingibst und die [Eingabetaste] drückst.
4.  Gib den Domainnamen ein und drücke erneut die [Eingabetaste].

Wenn der aktuelle Nameserver auf diese Anfrage antworten kann, wird der Inhalt des SOA Records angezeigt. Einer der zurückgegebenen Werte ist die Seriennummer. Im folgenden Beispiel lautet die Seriennummer 162337499.

![]([LINK_URL_1])

## Ein DNS-Prüfobjekt einrichten, um den SOA Record zu prüfen

Mit der nun bekannten Seriennummer kannst du DNS-Prüfobjekt einrichten, um den SOA Record zu prüfen. Solltest du Hilfe bei der Einrichtung eines DNS-Prüfobjekts benötigen, lies den Artikel [Ein DNS-Prüfobjekt einrichten]([LINK_URL_2]).

1.  Rufe ein bestehendes DNS-Prüfobjekt auf oder erstelle ein neues DNS-Prüfobjekt
2.  Wähle **SOA Record** aus dem Menü **DNS Query**
3.  Gib entweder die IP-Adresse oder den Domainnamen für den zu testenden Nameserver im Feld **DNS Server** ein. Lasse das Feld frei, um den lokalen Nameserver des Checkpoints zu verwenden.
4.  Gib den Domainnamen, für den du den SOA Record verifizieren möchtest, im Feld **Test Wert**ein.
5.  Gib die Seriennummer, die bei dem Test geprüft wird, in das Feld **Erwartetes Ergebnis** ein.

[SHORTCODE_1]
**Hinweis**: Wenn der Nameserver auf diese Anfrage antwortet, werden alle Werte des SOA Records angezeigt, nicht nur die Seriennummer. Es gibt einen Trick, um den gesamten SOA Record anzuzeigen. Bringe das Prüfobjekt zu einer Fehlermeldung, indem du einen falschen Wert als erwartetes Ergebnis eingibst. Gib beispielsweise „Mustertestwert“ in das Feld **Erwartetes Ergebnis** ein. Wenn das Prüfobjekt den Fehler entdeckt, erhältst du den gesamten Inhalt des SOA Records in den Kontrolldetails im Fehlerbericht (siehe Beispiel unten).
[SHORTCODE_2]

![]([LINK_URL_3])
