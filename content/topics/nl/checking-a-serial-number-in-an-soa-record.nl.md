{
  "hero": {
    "title": "Een serienummer in een SOA record controleren"
  },
  "title": "Een serienummer in een SOA record controleren",
  "summary": "Een serienummer in een SOA record verifiëren met behulp van een DNS-controleregel. ",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/dns/een-serienummer-in-een-soa-record-controleren",
  "translationKey": "https://www.uptrends.com/support/kb/dns/checking-a-serial-number-in-an-soa-record"
}

U kunt een DNS-monitor gebruiken om het serienummer te controleren dat is gerapporteerd door een naamserver voor een domein. Het serienummer is een specifieke eigenschap van een domeinnaam, dat de naamserver opslaat in de SOA record (Start of Authority). De naamserver verhoogt het serienummer telkens wanneer de DNS-instellingen van een domein worden gewijzigd. Door het serienummer in de gaten te houden zult u zodra uw DNS entry wijzigt hiervan op de hoogte zijn en alerts ontvangen vanwege mogelijke manipulatie. In dit artikel wordt stapsgewijs uitgelegd hoe u het serienummer achterhaalt en hoe u een DNS-controleregel instelt om de waarde te testen.

## Eerst moet u het huidige serienummer achterhalen

Om het huidige serienummer te achterhalen moet u een SOA query uitvoeren.

1.  Open een opdrachtprompt.
2.  Typ `nslookup` en druk op \[Enter\].
3.  Schakel naar querying SOA records door `set type=soa` te typen en druk op \[Enter\].
4.  Typ de naam van de desbetreffende domeinnaam en druk op \[Enter\].

Als de huidige naamserver op deze query kan reageren, geeft het u de inhoud van de SOA records. Een van de waarden die u ontvangt is het serienummer. In het onderstaande voorbeeld is het serienummer 162337499.

![](/img/content/4a94bdaf-0a6c-41ac-8d4b-5b2d941b37e1.png)

## Een DNS-controleregel instellen om de SOA record te controleren

Nu u het serienummer weet, moet u een DNS-controleregel instellen om de SOA record te controleren. Als u hulp nodig heeft bij het instellen van een DNS-controleregel, ga dan naar [Een DNS-controleregel instellen]({{< ref path="support/kb/synthetic-monitoring/uptime-monitoring/dns" lang="nl" >}}).

1.  Open een bestaande DNS-controleregel of maak een nieuwe DNS-controleregel
2.  Selecteer **SOA Record** in het menu **DNS Query**
3.  Voer in het vak **DNS Server** het IP-adres of de domeinnaam in van de server die u wilt testen. Laat dit vak leeg om de lokale naamserver op het controlestation te gebruiken.
4.  Voer in het vak **Testwaarde** de domeinnaam in waarvoor u de SOA record wilt verifiëren.
5.  Voer in het vak **Verwacht resultaat** het serienummer in dat u wilt testen.

{{< callout >}}
**Opmerking**: Als de naamserver een resultaat retourneert, bevat het resultaat alle waarden van de SOA record, niet alleen de serienummerwaarde. Er is een truc om de volledige inhoud van de SOA record op te halen ter referentie: forceer dat de controleregel faalt door een ongeldig verwacht resultaat te gebruiken. Voer bijvoorbeeld "dummy testvalue" in in het vak **Verwacht resultaat**. Wanneer de controleregel faalt, ontvangt u de volledige inhoud van de SOA record in het foutrapport Details van de controle (zie voorbeeld hieronder).
{{< /callout >}}

![](/img/content/99d458d1-7366-4722-9ca6-27201259d8f1.png)
