{
  "hero": {
    "title": "Extra controleregels en credits toevoegen"
  },
  "title": "Extra controleregels en berichtcredits toevoegen",
  "summary": "Als u extra controleregels, API-credits, transactiecredits of berichtcredits nodig heeft, kunt u ons bellen of ze kopen via uw Uptrends-account.",
  "url": "[URL_BASE_TOPICS]account/betaling-en-lidmaatschap/extra-controleregels-en-sms-toevoegen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Credits

Uptrends gebruikt credits om de [prijzen]([LINK_URL_1]) voor verschillende monitoringdiensten te berekenen. Credits zijn nodig om controleregels voor uitvoering te creëren, configureren en plannen.

Elke synthetische controleregel, zoals [Uptime- of Basiscontroleregels]([LINK_URL_2]), [Browsercontroleregels (Full Page Checks of FPC's)]([LINK_URL_3]), [API-controleregels]([LINK_URL_4]) en [Transactiecontroleregels]([LINK_URL_5]) heeft zijn eigen credittype:

- Uptimecontroleregels gebruiken **Uptime-credits**
- Browsercontroleregels gebruiken **Browser-credits**
- API-controleregels gebruiken **API-credits**
- Transactiecontroleregels gebruiken **Transactiecredits**
- **Credits** — geldt alleen voor alle bestaande accounts met één prijsniveau

Uw totale credits zijn afhankelijk van uw [controleregelmodus]([LINK_URL_6]) en [controleregelinstellingen]([LINK_URL_7]). Alle controleregels die zijn ingesteld op de modus **Staging** en **Production** gebruiken credits. Echter, controleregels in de modus **Development** worden als inactief beschouwd en gebruiken geen credits.

Als u niet genoeg controleregelcredits heeft, kunt u gemakkelijk [meer kopen]([LINK_URL_8]) of gewoon uw controleregels creëren en uitvoeren in [Developmentmodus]([LINK_URL_9]).

## Credits berekenen

Om de creditstatus van al uw Synthetische controleregels te bekijken gaat u naar [SHORTCODE_1] Accountinstellingen > Abonnement en facturen [SHORTCODE_2]. Het donutdiagram toont uw credits voor elk controleregeltype:

![Controleregelcredits]([LINK_URL_10])

Zoals weergegeven in de afbeelding, heeft de gebruiker vijf **Browsercredits** of controleregels gekocht. Twee hiervan zijn momenteel in gebruik en er kunnen nog drie FPC-controleregels worden gecreëerd. Verder heeft de gebruiker voor **Uptime-credits** tien credits of Uptime-controleregels gekocht. Vier hiervan zijn momenteel in gebruik en er kunnen nog zes basis controleregels worden gecreëerd.

Voor API- en transactiecontroleregels is het berekenen van credits iets complexer. Credits worden niet berekend voor elke gebruikte controleregel, maar voor elke request of laden van een pagina die de controleregel checkt. 

Als u een API-controleregel heeft gecreëerd (Multi-step API (MSA) of Postman), telt elke HTTP-request als één credit. Als u één MSA-controleregel met drie stappen heeft gecreëerd, kost deze drie credits. Als u twee MSA-controleregels heeft gecreëerd, elk met drie stappen, worden de totale credits berekend als drie stappen voor MSA-A en drie stappen voor MSA-B, in totaal zes API-credits.

Dit geldt ook voor transactiecontroleregels: we rekenen één credit voor elke nieuwe request (laden van pagina), [elke waterval of elke filmstrip]([LINK_URL_11]). Als een transactiecontroleregel vier pagina's doorloopt (laden van nieuwe pagina's) en de waterval en filmstrip in de eerste stap zijn ingeschakeld, wordt dit berekend als het laden van 4 pagina's + 1 waterval + 1 filmstrip, in totaal 6 Transactiecredits. Raadpleeg [Berekenen van credits voor transactiecontroleregels]([LINK_URL_12]) voor meer informatie over transactiecredits.

## Credits toevoegen

Om extra websites, servers, transacties en andere webservices te monitoren zijn er twee manieren om meer credits te kopen:

1. **Neem contact met ons op**  
    Als u momenteel geabonneerd bent en er zeker van wilt zijn dat u het juiste aantal extra controleregels of credits tegen een concurrerend tarief krijgt, neem dan rechtstreeks contact op met uw vertegenwoordiger of [stuur ons een ticket]([LINK_URL_13]).  

2. **Voeg toe via de Uptrends-webapplicatie**
    1. Ga naar [SHORTCODE_3]  Accountinstellingen > Uw abonnement uitbreiden [SHORTCODE_4].
    2. U kunt het aantal Uptime-credits, Browser-credits, API-credits, Transactiecredits en berichtcredits voor uw account verhogen.
    3. Klik op [SHORTCODE_5] Volgende [SHORTCODE_6].
    4. Verstrek uw factuurgegevens en selecteer de gewenste **Betaalmethode**.
    5. Klik op [SHORTCODE_7] Bestelling bevestigen [SHORTCODE_8].
