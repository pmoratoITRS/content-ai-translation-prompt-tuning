{
  "hero": {
    "title": "Alertberichten testen"
  },
  "title": "Alertberichten testen",
  "summary": "Alertberichten zijn een heel handige manier om op de hoogte te blijven van de status en performance van uw websites. Zorg ervoor dat u ze test.",
  "url": "[URL_BASE_TOPICS]alerting/alertconfiguraties-testen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Alertberichten zijn een heel handige manier om op de hoogte te blijven van de status en performance van uw websites, servers en webservices.

Wanneer er een alert optreedt in de monitoring van Uptrends, kunnen alertberichten worden verzonden naar operators of applicaties van derden. Het bericht kan een telefoonbericht (spraak), e-mail of SMS zijn of een (aangepast) bericht naar een applicatie. Hoe deze berichten moeten worden verzonden, wordt gedefinieerd in integraties. Wanneer berichten moeten worden verzonden, is georganiseerd in alertdefinities, zie het artikel [Alerting]([LINK_URL_1]) voor meer informatie.

Omdat het van cruciaal belang is dat de berichten de operator of applicatie bereiken, wilt u testen of ze werken. Het versturen van een testbericht werkt anders bij verschillende soorten integraties. De stappen voor elke soort integratie worden hieronder uitgelegd.

## Een testbericht versturen via e-mail of SMS

[SHORTCODE_1]
**Opmerking**: U moet een administrator zijn voor toegang tot de accountgegevens van de operators.
[SHORTCODE_2]

1. Ga naar het menu-item [SHORTCODE_3]Accountinstellingen > Operators, groepen (en deelaccounts)[SHORTCODE_4]. 
2. Klik op de knop [SHORTCODE_5] Alle operators bekijken [SHORTCODE_6].
3. Selecteer in de lijst met operators degene waarvoor u berichten wilt testen.
4. Zorg ervoor dat het primaire e-mailadres en mobiele telefoonnummer zijn ingevuld op het tabblad [SHORTCODE_7]Algemeen[SHORTCODE_8].
5. Klik op de knop [SHORTCODE_9]Test-e-mail versturen[SHORTCODE_10] of [SHORTCODE_11]Test-SMS versturen[SHORTCODE_12] om respectievelijk een e-mail of SMS te versturen.

Na deze testprocedure zou u een testbericht moeten ontvangen.

Als u geen administrator bent, kunt evengoed berichten testen voor uw eigen account.

1. Ga onder aan het hoofdmenu naar het gebruikersmenu en selecteer [SHORTCODE_13] Gebruikersinstellingen [SHORTCODE_14].
2. U ziet uw eigen accountinformatie.
3. Zorg ervoor dat het primaire e-mailadres en mobiele telefoonnummer zijn ingevuld. Gebruik vervolgens de knop [SHORTCODE_15]Test-e-mail versturen[SHORTCODE_16] of [SHORTCODE_17]Test-SMS versturen[SHORTCODE_18] om uw test te starten.

## Een testbericht versturen naar systemen van derden

Verschillende applicaties van derden kunnen alertberichten ontvangen van de Uptrends-app. Er zijn gebruiksklare [integraties]([LINK_URL_2]) voor veel third-partysystemen, die testfunctionaliteit hebben. U moet hun integraties toevoegen en configureren om testberichten te kunnen verzenden.

Als de test slaagt, wordt er een bericht ontvangen in de externe applicatie. Hoe dit in het systeem wordt behandeld en hoe het eruitziet voor de gebruiker, hangt af van welk systeem u gebruikt. Als u bijvoorbeeld een testbericht naar Slack stuurt, zou u een testbericht moeten zien verschijnen in het kanaal dat u heeft gespecificeerd.

### Slack en PagerDuty

Voor Slack en PagerDuty is standaard testfunctionaliteit aanwezig in de integratie:

1.  Ga naar het menu-item [SHORTCODE_19]Alerts > Integraties[SHORTCODE_20].
2.  Klik in de lijst met integraties op de integratie die u wilt testen.
3.  Zorg ervoor dat alle informatie is ingevuld.
4.  Klik op de knop [SHORTCODE_21]Testalert versturen[SHORTCODE_22].

### AlertOps, Microsoft Teams, Opsgenie, ServiceNow, Statuspage, Splunk On-Call, Zapier

Om een eenvoudige test uit te voeren voor deze integraties gebruikt u de knop [SHORTCODE_23] Testbericht versturen [SHORTCODE_24] onder aan het integratiescherm.

![screenshot test Microsoft Teams-integratie]([LINK_URL_3])

Als u de integratie heeft aangepast, wordt er een tabblad [SHORTCODE_25]Aanpassingen[SHORTCODE_26] toegevoegd aan uw integratie. Vervolgens kunt u de testberichtfunctionaliteit van de aangepaste integratie gebruiken zoals hieronder wordt beschreven. Hierbij wordt rekening gehouden met de aanpassingen die u heeft toegevoegd.

## Een testbericht versturen voor aanpasbare integraties

Een andere optie is een aanpasbare integratie, waar u kunt configureren dat u een bericht verstuurt naar een applicatie van derden waarvoor Uptrends geen standaardintegratie heeft. U definieert de integratie met behulp van de API van de externe partij. Bij deze integraties kan ook worden getest of ze op de verwachte manier een bericht versturen.

1.  Ga naar het menu-item [SHORTCODE_27]Alerting > Integraties[SHORTCODE_28].
2.  Klik in de lijst met integraties op de aanpasbare integratie die u wilt testen.
3.  Zorg ervoor dat alle informatie is ingevuld.
4.  Wilt u een snelle en eenvoudige test, gebruik dan de knop [SHORTCODE_29] Testalert versturen [SHORTCODE_30] onder aan het integratiescherm. 
5.  In het geval u berichten wilt testen met uw specifieke instellingen (aanpassingen) gaat u naar het tabblad [SHORTCODE_31]Aanpassingen[SHORTCODE_32]. Als het goed is heeft u de HTTP-stappen hier al gedefinieerd bij het configureren van de integratie. U kunt stappen definiëren voor de verschillende alerttypes: Fout, OK en Herinnering. Als u heeft besloten om verschillende HTTP-stappen te gebruiken voor verschillende (combinaties van) alerttypes, bestaan er een aantal stapdefinities.  
![screenshot aangepaste integratie stappen voor alerts]([LINK_URL_4])
 
6.  Klik bij elke HTTP-stapdefinitie op de knop [SHORTCODE_33]Testalert versturen[SHORTCODE_34].

Het artikel [Een aangepaste integratie configureren]([LINK_URL_5]) bevat meer informatie over het testen van berichten voor aanpasbare integraties.

## Problemen oplossen

Als uw berichten niet worden ontvangen zoals verwacht, vindt u hier enkele algemene tips voor het oplossen van problemen: [Alerting - Problemen oplossen]([LINK_URL_6]).
