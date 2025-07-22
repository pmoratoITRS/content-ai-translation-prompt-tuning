{
  "hero": {
    "title": "Alertberichten testen"
  },
  "title": "Alertberichten testen",
  "summary": "Alertberichten zijn een heel handige manier om op de hoogte te blijven van de status en performance van uw websites. Zorg ervoor dat u ze test.",
  "url": "/support/kb/alerting/alertconfiguraties-testen",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/testing-alert-configurations"
}

Alertberichten zijn een heel handige manier om op de hoogte te blijven van de status en performance van uw websites, servers en webservices.

Wanneer er een alert optreedt in de monitoring van Uptrends, kunnen alertberichten worden verzonden naar operators of applicaties van derden. Het bericht kan een telefoonbericht (spraak), e-mail of SMS zijn of een (aangepast) bericht naar een applicatie. Hoe deze berichten moeten worden verzonden, wordt gedefinieerd in integraties. Wanneer berichten moeten worden verzonden, is georganiseerd in alertdefinities, zie het artikel [Alerting]({{< ref path="support/kb/alerting" lang="nl" >}}) voor meer informatie.

Omdat het van cruciaal belang is dat de berichten de operator of applicatie bereiken, wilt u testen of ze werken. Het versturen van een testbericht werkt anders bij verschillende soorten integraties. De stappen voor elke soort integratie worden hieronder uitgelegd.

## Een testbericht versturen via e-mail of SMS

{{< callout >}}
**Opmerking**: U moet een administrator zijn voor toegang tot de accountgegevens van de operators.
{{< /callout >}}

1. Ga naar het menu-item {{< AppElement type="menuitem" >}}Accountinstellingen > Operators, groepen (en deelaccounts){{< /AppElement >}}. 
2. Klik op de knop {{< AppElement type="buttonPrimary" >}} Alle operators bekijken {{< /AppElement >}}.
3. Selecteer in de lijst met operators degene waarvoor u berichten wilt testen.
4. Zorg ervoor dat het primaire e-mailadres en mobiele telefoonnummer zijn ingevuld op het tabblad {{< AppElement type="tab" >}}Algemeen{{< /AppElement >}}.
5. Klik op de knop {{< AppElement type="button" >}}Test-e-mail versturen{{< /AppElement >}} of {{< AppElement type="button" >}}Test-SMS versturen{{< /AppElement >}} om respectievelijk een e-mail of SMS te versturen.

Na deze testprocedure zou u een testbericht moeten ontvangen.

Als u geen administrator bent, kunt evengoed berichten testen voor uw eigen account.

1. Ga onder aan het hoofdmenu naar het gebruikersmenu en selecteer {{< AppElement type="menuitem" >}} Gebruikersinstellingen {{< /AppElement >}}.
2. U ziet uw eigen accountinformatie.
3. Zorg ervoor dat het primaire e-mailadres en mobiele telefoonnummer zijn ingevuld. Gebruik vervolgens de knop {{< AppElement type="button" >}}Test-e-mail versturen{{< /AppElement >}} of {{< AppElement type="button" >}}Test-SMS versturen{{< /AppElement >}} om uw test te starten.

## Een testbericht versturen naar systemen van derden

Verschillende applicaties van derden kunnen alertberichten ontvangen van de Uptrends-app. Er zijn gebruiksklare [integraties](/integraties) voor veel third-partysystemen, die testfunctionaliteit hebben. U moet hun integraties toevoegen en configureren om testberichten te kunnen verzenden.

Als de test slaagt, wordt er een bericht ontvangen in de externe applicatie. Hoe dit in het systeem wordt behandeld en hoe het eruitziet voor de gebruiker, hangt af van welk systeem u gebruikt. Als u bijvoorbeeld een testbericht naar Slack stuurt, zou u een testbericht moeten zien verschijnen in het kanaal dat u heeft gespecificeerd.

### Slack en PagerDuty

Voor Slack en PagerDuty is standaard testfunctionaliteit aanwezig in de integratie:

1.  Ga naar het menu-item {{< AppElement type="menuitem" >}}Alerts > Integraties{{< /AppElement >}}.
2.  Klik in de lijst met integraties op de integratie die u wilt testen.
3.  Zorg ervoor dat alle informatie is ingevuld.
4.  Klik op de knop {{< AppElement type="button" >}}Testalert versturen{{< /AppElement >}}.

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

Om een eenvoudige test uit te voeren voor deze integraties gebruikt u de knop {{< AppElement type="buttonSecondary" >}} Testbericht versturen {{< /AppElement >}} onder aan het integratiescherm.

![screenshot test Microsoft Teams-integratie](/img/content/scr_test-message-to-microsoft-teams.min.png)

Als u de integratie heeft aangepast, wordt er een tabblad {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}} toegevoegd aan uw integratie. Vervolgens kunt u de testberichtfunctionaliteit van de aangepaste integratie gebruiken zoals hieronder wordt beschreven. Hierbij wordt rekening gehouden met de aanpassingen die u heeft toegevoegd.

## Een testbericht versturen voor aanpasbare integraties

Een andere optie is een aanpasbare integratie, waar u kunt configureren dat u een bericht verstuurt naar een applicatie van derden waarvoor Uptrends geen standaardintegratie heeft. U definieert de integratie met behulp van de API van de externe partij. Bij deze integraties kan ook worden getest of ze op de verwachte manier een bericht versturen.

1.  Ga naar het menu-item {{< AppElement type="menuitem" >}}Alerting > Integraties{{< /AppElement >}}.
2.  Klik in de lijst met integraties op de aanpasbare integratie die u wilt testen.
3.  Zorg ervoor dat alle informatie is ingevuld.
4.  Wilt u een snelle en eenvoudige test, gebruik dan de knop {{< AppElement type="buttonSecondary" >}} Testalert versturen {{< /AppElement >}} onder aan het integratiescherm. 
5.  In het geval u berichten wilt testen met uw specifieke instellingen (aanpassingen) gaat u naar het tabblad {{< AppElement type="tab" >}}Aanpassingen{{< /AppElement >}}. Als het goed is heeft u de HTTP-stappen hier al gedefinieerd bij het configureren van de integratie. U kunt stappen definiëren voor de verschillende alerttypes: Fout, OK en Herinnering. Als u heeft besloten om verschillende HTTP-stappen te gebruiken voor verschillende (combinaties van) alerttypes, bestaan er een aantal stapdefinities.  
![screenshot aangepaste integratie stappen voor alerts](/img/content/scr_custom-integration-steps-for-alerts.min.png)
 
6.  Klik bij elke HTTP-stapdefinitie op de knop {{< AppElement type="button" >}}Testalert versturen{{< /AppElement >}}.

Het artikel [Een aangepaste integratie configureren](/support/kb/alerting/integraties/aangepaste-integraties) bevat meer informatie over het testen van berichten voor aanpasbare integraties.

## Problemen oplossen

Als uw berichten niet worden ontvangen zoals verwacht, vindt u hier enkele algemene tips voor het oplossen van problemen: [Alerting - Problemen oplossen](/support/kb/alerting/#problemenoplossen).
