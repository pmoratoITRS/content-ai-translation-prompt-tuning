{
  "hero": {
    "title": "Telefoon (stem) alerts instellen"
  },
  "title": "Telefoon (stem) alerts instellen",
  "summary": "Alles wat u moet weten over Uptrends' telefoonalerts: set-up, voorbeeldberichten, testen en selectie van uitgaande nummers. ",
  "url": "/support/kb/alerting/telefoon-alerts",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/phone-alerts"
}

Soms kan een e-mail, SMS of geïntegreerd bericht via Slack of PagerDuty de klus niet klaren. Soms moet de telefoon overgaan om uw aandacht te trekken als u slaapt of een belangrijke wedstrijd kijkt. Met telefoonalerts heeft u die mogelijkheid. Op basis van uw alertdefinities, escalatieniveau’s en dienstroosters van operators kunt u de telefoon laten overgaan en uw dienstdoende operator ontvangt vervolgens een automatisch spraakbericht over de alertsituatie. In dit Knowledge Base-artikel leert u meer over:

-   [Instellen van uw telefoonalerts](#set-up-phone-alert-integration)
-   [Instellen van uw operators voor telefoonalerts](#setting-up-operators)
-   [Instellen van uw alertdefinities met telefoonalerts](#setting-up-escalations-for-phone-alerts)
-   [Gebruik van berichtcredits](#cost-for-using-phone-alerts)
-   [Wat u kunt verwachten als u de telefoon beantwoordt](#what-to-expect-when-the-phone-rings)

## Uptrends instellen voor telefoonalertintegratie {id="set-up-phone-alert-integration"}

Om telefoonalerts aan uw arsenaal aan berichtentools toe te voegen, moet u een account van Premium-niveau of hoger hebben hebben.

{{< callout >}}
**Opmerking:** U kunt uw Starter-account eenvoudig upgraden door uw accountmanager te bellen of een serviceticket maken dan neemt iemand snel contact met u op. Ga naar de pagina [Contact]({{< ref path="contact" lang="nl" >}}) voor meer details.
{{< /callout >}}

Standaard staat telefoonalerting niet meteen aan; voor telefoonintegratie moet u deze inschakelen op de pagina **Integraties** van het menu {{< AppElement type="menuitem" >}}Alerting{{< /AppElement >}}. Vervolgens kunt u telefoonalerts toevoegen aan uw alertescalaties. Om telefoonalerts in te schakelen doet u het volgende:

1.  Selecteer **Telefoon** in het vak **Integratietype**.
2.  Gebruik de standaardnaam of verander de naam in het vak **Integratienaam**.
3.  Kies in het menu een **Uitgaand telefoonnummer**. Kies een nummer op basis van uw locatie; indien een land niet in de lijst staat, kies dan het dichtsbijzijnde land. U (en uw team) kunnen het nummer toevoegen aan uw contactpersonen voor een snelle identificatie. Als u **Systeemstandaard** geselecteerd laat, kiest Uptrends het beste nummer op basis van de landcode van de ontvangers (operators).  
    {{< callout >}}**Opmerking:** Bekijk de [lijst van ondersteunde landen]({{< ref path="support/kb/alerting/phone-alerts-troubleshooting" lang="nl" >}}) en landcodes voor het ontvangende telefoonnummer van de operator. Als u het land en de code van de operator niet in de lijst ziet, zullen ze GEEN telefoonalerts ontvangen.{{< /callout >}} 
4.  Selecteer de **Taal** voor de telefoonalert alleen als u de taalinstellingen op operatorniveau wilt overschrijven.
5.  Controleer of de controleregelnaam tekst-naar-spraakvriendelijk is; zo niet, schakel dan het selectievakje **Gebruik alternatieve controleregelnamen** in. Meer informatie over [spraakvriendelijke controleregelnamen inschakelen en instellen]({{< ref path="support/kb/alerting/speech-friendly-monitor-names-for-phone-alerts" lang="nl" >}}).
6.  Schakel het selectievakje **Actief** in als dit nog niet is ingeschakeld.
7.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

![screenshot telefoonintegratie](/img/content/scr_integrations-phone.min.png)

## Operators instellen {id="setting-up-operators"}

Op het tabblad {{< AppElement type="tab" >}}Algemeen{{< /AppElement >}} van de pagina Operatorinstellingen heeft u de optie om een **Mobiel nummer** in te vullen en het **Uitgaande telefoonnummer** te overschrijven dat u heeft gedefinieerd bij het inschakelen van telefoonintegraties. Als u SMS-berichten al in uw alertdefinities gebruikt, hoeft u mogelijk geen van uw operatorprofielen aan te passen.

### Een mobiel nummer toevoegen

Het systeem gebruikt het mobiele nummer van de operator om SMS-alerts te versturen, en Uptrends gebruikt hetzelfde nummer voor telefoonalerts. Om een telefoonnummer toe te voegen doet u het volgende:

1.  Typ een plusteken (\+) gevolgd door de landcode, gevolgd door het telefoonnummer.
2.  Gebruik geen andere niet-numerieke tekens; een correct Nederlands telefoonnummer bijvoorbeeld moet er ongeveer zo uitzien: \+31612345678.
3.  Klik op {{< AppElement type="savebutton" >}}Opslaan.{{< /AppElement >}} 

{{< callout >}}
**Opmerking:** Ja, u kunt een vast nummer gebruiken in het vak **Mobiel nummer** (heeft iemand nog een vaste lijn?), maar als u ook SMS-alerts gebruikt, ontvangt die operator de SMS-alerts niet. Als u een vaste lijn moet gebruiken voor het mobiele telefoonnummer van een operator, zorg er dan voor dat u die operator nooit opneemt in escalaties die u heeft gedefinieerd voor SMS-alerts.
{{< /callout >}}

### Overschrijven van het standaard uitgaande telefoonnummer

Als u een **Uitgaand telefoonnummer** heeft gedefinieerd op de pagina Telefoonintegratie, moet u die keuze mogelijk voor individuele operators overschrijven. Door **Instellingen van de telefoonintegratie overschrijven** te selecteren, zal Uptrends het alternatieve nummer gebruiken dat u selecteert in het nummerselectievak.

![screenshot telefooninstellingen operator](/img/content/scr_integrations-override-phone-settings.min.png)
## Escalaties voor telefoonalerts instellen {id="setting-up-escalations-for-phone-alerts"}

Nu u uw telefoonalerts heeft ingeschakeld en de mobiele nummers van uw operators allemaal in het systeem staan, is het tijd om uw escalatieniveau’s voor telefoonalerting
in te stellen.

1.  Selecteer **Alertdefinities** bij de optie **Alerting** in het hoofdmenu.
2.  Klik om een bestaande definitie te kiezen of creëer een nieuwe definitie door te klikken op de knop {{< AppElement type="button" >}}Alertdefinitie toevoegen{{< /AppElement >}} op het actiemenu.
3.  Selecteer een van de tabbladen {{< AppElement type="tab" >}}Escalatieniveau{{< /AppElement >}}.
4.  Schakel in het gedeelte **Alerts versturen door integraties** het selectievakje **Telefoon** in. Als u Telefoon niet als optie ziet, moet u de telefoonintegratie nog inschakelen of u moet het selectievakje **Actief** op de pagina Telefoonintegratie selecteren (zie [instellen](#set-up-uptrends-for-phone-alert-integration) hierboven).
5.  Klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.

![screenshot alertdefinitie telefoonintegratie](/img/content/scr_phone-integration-alert-definition.min.png)

Dat is het! Als een fout een alert voor deze definitie en dit escalatieniveau triggert, zal Uptrends het nummer zoeken van de operator die op dat moment dienst heeft en die op het telefoonnummer bellen met een geautomatiseerd bericht.

## Kosten voor het gebruik van telefoonalerts {id="cost-for-using-phone-alerts"}

Als u al gebruikmaakt van SMS-berichten, bent u waarschijnlijk wel bekend met berichtcredits. Elk accountniveau bevat aanvankelijk een aantal credits, maar als deze verbruikt zijn moet u extra credits kopen anders stoppen we met het verzenden van telefoon- en SMS-alerts. Telefoonalerts gebruiken dezelfde credits. Bezoek voor meer informatie de pagina [SMS/telefoon berichtcredits]({{< ref path="support/kb/alerting/sms-credit-usage" lang="nl" >}}).

{{< callout >}}
**Opmerking:** Het testen van uw telefoonalerts en tekstberichten is GRATIS. Uptrends gebruikt uw berichtcredits niet voor uw testdoeleinden.
{{< /callout >}}

## Wat u kunt verwachten wanneer de telefoon rinkelt {id="what-to-expect-when-the-phone-rings"}

Wat vertelt de telefoonalert u? Als het systeem over de foutinformatie beschikt, hoort u mogelijk ongeveer het volgende:

> "Hallo, dit is Uptrends.  
> We hebben een fout gedetecteerd voor de controleregel Home Page. De fout was HTTP pattern matched en begon een minuut geleden.  
> De HTTP error code was 500.  
> De tijdslimiet van 12 was overschreden.  
> Goedendag."

Dit hebben we natuurlijk verzonnen; uw bericht geeft u informatie op basis van uw specifieke alertsituatie en controleregel. Als de informatie niet beschikbaar is, hoort u iets als dit:

> "Hallo, dit is Uptrends.  
> Er is een fout opgetreden voor één van uw controleregels. Op dit moment is er niet meer informatie beschikbaar. Verifieer de status van uw controleregels in Uptrends.  
> Goedendag."

## Problemen met telefoonalerts oplossen

Heeft u problemen met het ontvangen van telefoonalerts? We hebben een [Handleiding voor het oplossen van problemen met Telefoonalerts]({{< ref path="support/kb/alerting/phone-alerts-troubleshooting" lang="nl" >}}).

## Heeft u vragen?

Als u meer hulp nodig heeft bij het instellen van operators, het definiëren van alerts en escalaties, bezoek dan de Uptrends [knowledge base]({{< ref path="support/kb" lang="nl" >}}). Als u de informatie die u nodig heeft nog steeds niet kunt vinden, staan wij klaar om u te helpen. Ga naar de pagina [Contact]({{< ref path="contact" lang="nl" >}}) voor telefoonnummers van support of om een support-ticket te openen.
