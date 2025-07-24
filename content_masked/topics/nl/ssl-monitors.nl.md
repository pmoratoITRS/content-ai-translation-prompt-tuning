{
  "hero": {
    "title": "SSL Certificaat-controleregels"
  },
  "title": "SSL Certificaat-controleregels",
  "summary": "De geavanceerde SSL-monitoring van Uptrends houdt uw SSL-certificaten bij en controleert op vervaldatums en wijzigingen in uw certificaat die kunnen duiden op een inbreuk op de beveiliging. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/controleregels-ssl-certificaat",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Uw SSL (Secure Socket Layers) certificaat is belangrijker dan de meeste mensen denken. Onderzoek heeft aangetoond dat de meeste gebruikers het advies van de browser opvolgen en uw site verlaten voor een concurrent als zij een waarschuwing krijgen over een ongeldig of vervallen SSL certificaat. SSL-fouten overkomen iedereen; zelfs Google is het slachtoffer geworden van een verlopen certificaat. Bij personeelsverloop en veranderingen in verantwoordelijkheden kunnen SSL certificaten buiten beeld raken. Met Uptrends kunt u al uw SSL-informatie op één plaats bewaren en alerts ontvangen over vervaldata en veranderingen in uw certificaat.

## Wat wordt er gemonitord?

Naast het instellen van de vervaldatum van uw SSL certificaat kunt u ook de volgende certificaatwaarden volgen:

-   Algemene naam
-   Organisatie
-   Organisatorische eenheid
-   Serienummer
-   Vingerafdruk
-   Verleend door algemene naam
-   Verleend door organisatie
-   Verleend door organisatorische eenheid

Als een van deze waarden op uw sitecertificaat verandert (een mogelijke aanwijzing van een hack), stuurt Uptrends een alert.

#### Alert- en foutberichten

Dit zijn de berichten die u ziet zodra uw SSL-certificaat bijna verloopt:

- **SSL certificaat verloopt binnenkort** – Dit is een algemene foutmelding op basis van het aantal dagen dat u heeft ingesteld in het veld [SHORTCODE_1] Expiratie waarschuwingsdagen [SHORTCODE_2] op het tabblad [SHORTCODE_3] Algemeen [SHORTCODE_4] van uw SSL-controleregel. Wanneer de datum van uw certificaat overeenkomt met de waarde die in dit veld is ingesteld, ziet u dit bericht in het dashboard *Foutenoverzicht* of op plaatsen waar fouten zijn gegroepeerd.

Op uw SSL-controleregel > dashboards *Controleregel log* en *Alerthistorie* vindt u meer specifieke alertberichten met het aantal resterende dagen voordat uw certificaat verloopt: 

- **SSL-certificaat verloopt over 1 dag**
- **SSL-certificaat verloopt over minder dan 1 dag**
- **SSL-certificaat verloopt over *n* dagen** – De *n* geeft het werkelijke aantal dagen in numeriek formaat weer waarop het SSL-certificaat verloopt. Als er bijvoorbeeld nog maar *45* dagen over zijn, wordt het alertbericht weergegeven als *SSL-certificaat verloopt over 45 dagen*.

Deze berichten worden ook weergegeven in het scherm *Details van de controle* wanneer u een actie [SHORTCODE_5] Test starten [SHORTCODE_6] uitvoert op SSL-controleregels.

## Stel een SSL certificaat-controleregel in

Het instellen van een SSL Certificaat-controleregel is vergelijkbaar met het configureren van een webpaginacontroleregel. Als u hulp nodig heeft bij de basisstappen van controleregelconfiguratie, raadpleeg dan het knowledgebase-artikel [Een controleregel toevoegen]([LINK_URL_1]).

Een SSL Certificaat-controleregel instellen:

1. Ga naar [SHORTCODE_7] Monitoring > Controleregels beheren [SHORTCODE_8] en klik op de [SHORTCODE_9][SHORTCODE_10].
2. In het pop-upvenster *Kies een controleregeltype* kiest u *SSL Certificaat* en klikt dan op de knop [SHORTCODE_11] Kiezen [SHORTCODE_12].  
3. Stel uw [algemene controleregelinstellingen]([LINK_URL_2]) in.
4. Voer in het veld *URL* de URL of het browseradres in dat u wilt monitoren.
5. Vul het gedeelte SSL Certificaat correct in, informatie zou direct beschikbaar moeten zijn bij de uitgever van uw SSL Certificaat.

![Detailsgedeelte SSL Certificaat]([LINK_URL_3])

6. Klik op de knop [SHORTCODE_13] Opslaan [SHORTCODE_14] om de wijzigingen toe te passen.

Uptrends monitort nu de SSL-certificaatgegevens van uw website en waarschuwt u wanneer aan de gespecificeerde voorwaarden in de tabbladen [SHORTCODE_15]Foutcondities[SHORTCODE_16] en [SHORTCODE_17]Extra[SHORTCODE_18] wordt voldaan. Raadpleeg het knowledgebase-artikel [controleregelinstellingen]([LINK_URL_4]) voor meer informatie.