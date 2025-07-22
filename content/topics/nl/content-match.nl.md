{
  "hero": {
    "title": "Foutcondities – Pagina-inhoud"
  },
  "title": "Foutcondities – Pagina-inhoud",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/foutcondities/inhoudmatch",
  "summary": "Inhoudmatches zijn een manier om te controleren of de pagina die u monitort de juiste inhoud weergeeft.",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/content-match"
}

Er zijn situaties waarin slechts de helft van de inhoud van uw website correct wordt geladen. Ontbrekende secties, tekst en alinea’s maken het voor gebruikers moeilijk om door uw website te navigeren. Als u een e-commercesite heeft, heeft deze slechte gebruikerservaring invloed op de prestaties van uw site en verliest u omzet zonder dat u het doorheeft.

## Foutconditie Pagina-inhoud

De foutconditie Pagina-inhoud garandeert dat de inhoud van uw website correct en volledig wordt geladen. Hiermee kunt u alle teksten, zinnen en reguliere expressies en matches opgeven als deze inhoud op uw website wordt weergegeven.

![Foutconditie pagina-inhoud](/img/content/scr-error-condition-page-content.min.png)

## Inhoudmatch

Een inhoudmatch is een lijst met woorden die u specificeert en die de controleregel als referentiepunt gebruikt om te controleren of deze overeenkomen met de geladen inhoud van de website:

- Als een controleregel die de pagina controleert de inhoud *vindt*, wordt er *geen fout* gerapporteerd.
- Als een controleregel die de pagina controleert de inhoud *niet kan vinden*, wordt er *een fout* gerapporteerd.

## Inhoudmatch voor elk controleregeltype

Er zijn verschillende typen inhoudmatches beschikbaar voor verschillende controleregeltypes. inhoudmatch varieert afhankelijk van de categorie van de controleregel en welke data deze verzamelt:

### Uptime-controleregels

Uptime-controleregels verifiëren pagina-inhoud door een GET-request te doen naar de URL van uw website. Zodra de request succesvol is, valideert de controleregel de GET-responsinhoud van uw website.

Als u een website-URL monitort: https://galacticresorts.com/, zijn voorbeelden van inhoudchecks:

| Inhoudmatch-types | Voorbeelden |
|--|--|
| Document Object Model (DOM) of HTML-elementen | {{< tableformatter >}}
- `<title>Home Page - GalacticResorts.com</title>`
- `<a class="btn btn-primary btn-lg" href="/Products/Index/97f8fcc9-11b5-4d86-b208-ccb6d2be35e3">Book now!</a>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />` 
{{< /tableformatter >}} |
| {{< tableformatter >}} Tekstinhoud met gebruik van [reguliere expressie]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="nl" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Home Page - GalacticResorts.com
- Holiday destinations
- Norcadia Prime | Alpha Cygnus IX
{{< /tableformatter >}} |
| {{< tableformatter >}} [Geavanceerde]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="nl" >}}) inhoudmatch {{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "GalacticResottt", "IsPositive": false }]`{{< /tableformatter >}} |

### Browsercontroleregels

Browsercontroleregels verifiëren pagina-inhoud door de bron van de pagina van de website te controleren. De paginabron is de ruwe structuur van de website in HTML-formaat, inclusief de metadata, scripts en stijlinformatie van de pagina.

Als u een website-URL monitort: https://galacticresorts.com/, zijn voorbeelden van inhoudchecks:

| Inhoudmatch-types | Voorbeelden |
|--|--|
| Document Object Model (DOM) of HTML-elementen | {{< tableformatter >}}
- `<h2>Norcadia Prime</h2>`
- `<li><a href="/APIHelp" target="_blank">API</a></li>`
- `<img src="/Content/planet2-thumb.jpg" style="float: left;" />` 
{{< /tableformatter >}} |
| {{< tableformatter >}} Tekstinhoud met gebruik van [reguliere expressie]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#regular-content-match" lang="nl" >}}) {{< /tableformatter >}} | {{< tableformatter >}}
- Browse our stellar destinations...
- Holiday destinations
- !GalactccResorts
{{< /tableformatter >}} |
| {{< tableformatter >}} [Geavanceerde]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match#advanced-content-match" lang="nl" >}}) inhoudmatch {{< /tableformatter >}} | {{< tableformatter >}}
- `[{ "Pattern": "Alpha Cygnus IX", "IsPositive": true }, { "Pattern": "Holiday destinations", "IsPositive": true }]`{{< /tableformatter >}} |

{{< callout >}} **Opmerking:** Om de paginabron van uw website te openen gaat u naar uw website en drukt u op de toets **Ctrl + U**. U kunt ook met de rechtermuisknop ergens op de pagina klikken en op **Paginabron weergeven** klikken. Houd er rekening mee dat niet alle elementen in de paginabron geldige inhoudchecks zijn.{{< /callout >}}

### Multi-step API (MSA)-controleregels

MSA-controleregels controleren een inhoudmatch via **Assertions**. Met assertions kunt u controles definiëren om te valideren of de API-respons voldoet aan uw verwachte condities. Bijvoorbeeld als de respons statuscode 200 is of als de respons body als JSON specifieke teksten bevat. Voor meer informatie, zie [MSA Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="nl" >}}).

### Transactie-controleregels

Transactie-controleregels valideren pagina-inhoud door pagina-elementen te controleren die in de browser worden weergegeven. Ze controleren op specifieke tekst, knoppen, afbeeldingen en andere UI-elementen die zichtbaar zijn op uw website. Transactie-controleregels gebruiken **Inhoudcontroles**, acties die voor elke stap zijn geconfigureerd en die verifiëren of elk laden van de pagina verloopt zoals verwacht. Het kan bijvoorbeeld controleren of de tekst 'Succesvol toegevoegd aan winkelwagen' op de pagina verschijnt. Raadpleeg [Inhoudcontroles]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}}) voor meer informatie.

## Types inhoudmatch

Hieronder staan types inhoudmatch die beschikbaar zijn voor sommige controleregeltypes:

### Gewone inhoudmatch {id = "regular-content-match"}

Een inhoudmatch kan worden ingesteld met behulp van reguliere expressies. Een reguliere expressie (regex of regexp) is een speciale tekenreeks die een zoekpatroon beschrijft. U kunt een inhoudmatch opgeven met:

- Eén woord: `Uptrends`
- Meerdere woorden of zinnen in een bepaalde volgorde: `product.*order` (bijvoorbeeld, product EN order moeten voorkomen)
- Symbolen om andere elementen te matchen:
  - `!error` — gebruikt een uitroepteken om de betekenis van een woord om te keren of te ontkennen. Deze inhoudmatch betekent dat het woord *error* niet mag worden weergegeven.
  - `In de aanbieding|Bestsellers` — gebruikt een verticale balk om een ander woord te matchen. Deze inhoudmatch betekent dat de tekst `In de aanbieding` OF `Bestsellers` zichtbaar moet zijn op uw website.

Raadpleeg voor meer informatie [Regular Expression Language - Quick Reference](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference).


### Geavanceerde inhoudmatch

U kunt meerdere inhoudmatches tegelijk gebruiken door waarden op te slaan in JSON-formaat. Als u twee patronen wilt combineren, die elke vorm van pagina-elementen en reguliere expressies kunnen zijn, gebruikt u:

```json
    [
      {
        "Pattern": "PhraseA",
        "IsPositive": true
      },
      { 
        "Pattern": "PhraseB", 
        "IsPositive": false 
      }
    ]
```

Geef een geldige inhoudmatch in het veld `Pattern`. Stel `IsPositive` in op `true` als het patroon moet matchen met de inhoud van uw website of op `false` als het niet matcht met enige inhoud van uw website.  

{{< callout >}} **Opmerking:** De Geavanceerde inhoudmatch werkt voor de controleregels HTTPS, Webservices HTTP en HTTPS, en Full Page Check. {{< /callout >}}

Als u het tijdstempel van uw website wilt controleren op een inhoudmatch, gebruikt u:

```json
    [
    {
      "Pattern": "some content before the timestamp value (?<hour>\\d\\d):(?<minute>\\d\\d)",
      "IsPositive": true,
      "DateTime": { 
        "OffsetUTC": 60, 
        "MaxDifference": 5 
      } 
    } 
    ]
```

De JSON-sleutel, `Pattern`, kan waarden in regex-vorm bevatten, zoals \<year\>, \<month\>, \<day\>, \<hour\>, \<minute\>, and \<second\>. Al deze waarden kunnen worden geëxtraheerd uit de inhoud van de website en worden samengevoegd met de huidige servertijd en vervolgens geëvalueerd in termen van UTC.

De `OffsetUTC` is het aantal minuten dat moet worden afgetrokken om het te vergelijken met de servertijd in UTC. Als de webpagina een tijdstempel in UTC\+1 bevat, moet de offset 60 zijn. Als de webpagina een tijdstempel in EST (UTC-5) bevat, moet de offset -300 zijn.

De `MaxDifference` verwijst naar het maximale tijdsverschil in minuten dat is toegestaan tussen de paginatijd van de website en uw lokale tijd. Als uw lokale tijd bijvoorbeeld 10:06 is en de paginatijd van uw website 10:00, treedt er een fout op als `MaxDifference` is ingesteld op 5 minuten of minder.

## Waar configureer je een inhoudmatch

Om een inhoudmatch te configureren moet u een foutconditie toevoegen van het type **Pagina-inhoud controleren**:

1. Ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Klik op de controleregel waaraan u een inhoudmatch wilt toevoegen.  
3. Navigeer naar het tabblad {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}}.  
4. Voer in **Pagina-inhoud controleren** uw inhoudmatch-informatie in.
5. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijziging in de controleregel te bevestigen.

Als u klaar bent, kunt u [een alertdefinitie creëren]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="nl" >}}) om een bericht te ontvangen wanneer aan de foutconditie **Pagina-inhoud controleren** is voldaan.
