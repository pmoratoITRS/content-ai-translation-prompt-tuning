{
  "hero": {
    "title": "Alert escalatieniveaus"
  },
  "title": "Alert escalatieniveaus",
  "summary": "Met alertdefinities en escalatieniveaus kunt u alerts configureren voor toegewezen ontvangers of integraties, conform het escalatiebeleid van uw organisatie in geval van downtime.",
  "url": "[URL_BASE_TOPICS]alerting/alert-escalatieniveaus",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Wat zijn escalatieniveaus?

Het alertingsysteem van Uptrends is gebouwd met teams in gedachten. Met aanpasbare escalatieniveaus waarmee u ervoor kunt zorgen dat de juiste mensen op het juiste moment worden gewaarschuwd over een mogelijk probleem. 

Een escalatieniveau bevat een reeks parameters voor het genereren van alerts, het aantal herinneringen, de notificatiemethode en wie deze zal ontvangen. Ze kunnen worden geconfigureerd in een alertdefinitie.

U kunt maximaal drie escalatieniveaus configureren en alerts genereren op basis van uw eigen regels:

- Genereer een alert wanneer er gedurende een specifieke tijdsperiode fouten optreden of wanneer er een specifiek aantal fouten is opgetreden
- Definieer hoeveel herinneringen binnen een bepaald interval worden verzonden
- Stel alertmethodes in door [integraties]([LINK_URL_1]) te gebruiken
- Voeg een aangepast bericht toe (alleen voor Slack-, PagerDuty- en e-mailnotificaties)
- Voeg een traceroute-log toe aan e-mails
- Voeg een extra e-mailadres toe om extra mensen te waarschuwen
- Selecteer welke operators of operatorgroepen de alert krijgen
- Beslis (voor elke integratie) of u OK- en herinneringsalerts wilt versturen

## Een alertescalatie instellen

Binnen elke Alertdefinitie heeft u één tot drie escalatieniveaus. Om uw escalaties in te stellen:

1. Ga naar [SHORTCODE_1] Alerting > Alertdefinities [SHORTCODE_2] en selecteer een alertdefinitie om aan te passen. Of zoek naar een specifieke definitie in de [zoekbalk van het Uptrends-menu]([LINK_URL_2]). Als u een nieuwe alertdefinitie moet maken, bekijk dan [Alertdefinities creëren]([LINK_URL_3]).
2. Open het tabblad [SHORTCODE_3] Escalatieniveau 1 [SHORTCODE_4].
3. Selecteer het selectievakje **Actief** als dit nog niet is geselecteerd.
4. Stel de regels voor de **Escalatie** in door de parameters *Genereer een alert als er* in te vullen.
5. Selecteer de frequentie voor de herinneringen. Lees meer in het Knowledge Base-artikel [Alertherinneringen]([LINK_URL_4]).
6. Kies een of meer opties in het gedeelte **Alerts versturen door integraties**, bijvoorbeeld de voorgedefinieerde integratie **Alerts versturen via E-mail**, **SMS** (SMS/Tekst gebruikt berichtcredits) of **Telefoon**. 
7. Als u andere integraties heeft geconfigureerd, kunt u deze hier kiezen. Bekijk het Knowledge Base-artikel [Integraties]([LINK_URL_5]) voor meer informatie.
8. Bij de meeste integraties kunt u beslissen of u OK- en herinneringsalerts wilt ontvangen. Vouw de integratie uit door op het pijltje voor de integratie te klikken en activeer de gewenste opties. 

   ![screenshot alertopties]([LINK_URL_6])

   Houd er rekening mee dat [aanpasbare integraties]([LINK_URL_7]) [berichttypes]([LINK_URL_8]) gebruiken om om te gaan met verschillende alerts (fout, herinnering, OK). De afspraken die u in de berichttypes heeft gemaakt worden weergegeven in de alertdefinitie, maar kunnen daar niet worden gewijzigd. In plaats daarvan moet u wijzigingen aanbrengen in de aangepaste integratie zelf. 
9. Voeg een aangepast bericht toe (optioneel en alleen van toepassing op sommige integraties).
10. Selecteer het selectievakje **Traceroute** om een traceroute-log in de e-mails te ontvangen.
11. Gebruik het gedeelte **Groepen en operators** om de operators voor de escalatie te selecteren. Houd er rekening mee dat alerts alleen worden verstuurd als de toegewezen operator actief is en dienst heeft. *Actief* is een algemene instelling voor een operator en of deze operator dienst heeft wordt afgeleid van de [geen-dienstperiode]([LINK_URL_9]) van de operator.
12. Stel escalatieniveaus 2 en 3 in als het escalatiepad van uw organisatie daarom vraagt. 
13. Klik op de knop [SHORTCODE_5]Opslaan[SHORTCODE_6] als u klaar bent met het configureren van uw niveaus.

## Alerting door integraties

In het Knowledge Base-artikel over [Integraties]([LINK_URL_10]) vindt u meer informatie over de verschillende types integraties, waaronder telefoon (gebruikt berichtcredits) en integraties zoals [PagerDuty]([LINK_URL_11]), [Microsoft Teams]([LINK_URL_12]), [Slack]([LINK_URL_13]) en [StatusHub]([LINK_URL_14]).

## Alertconfiguraties testen

Nadat u uw escalatieniveaus heeft ingesteld en de integraties die u wilt gebruiken heeft toegevoegd, kunt u testen of berichten met succes worden verzonden. Bekijk het Knowledge Base-artikel [Alertberichten testen]([LINK_URL_15]) voor de methoden die beschikbaar zijn voor verschillende integraties.