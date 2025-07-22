{
  "hero": {
    "title": "Uw aangepaste integratie testen"
  },
  "title": "Uw aangepaste integratie testen",
  "summary": "Aangepaste integraties – een handleiding voor het testen van de configuratie van uw aangepaste integratie",
  "url": "[URL_BASE_TOPICS]alerting/integraties/aangepaste-integraties/uw-aangepaste-integratie-testen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Nadat u een aangepaste integratie heeft gemaakt of gewijzigd, is het handig om deze eerst te testen voordat u deze in production gebruikt. Dit artikel behandelt twee manieren om de nieuw geconfigureerde integratie te testen. Doorgaans betekent een succesvolle test dat u de inkomende alertingdata kunt zien in het externe systeem waarmee u verbinding maakt, nadat deze correct zijn geparseerd of verwerkt.

## Een integratie controleren met testberichten

Het is mogelijk om nieuwe integraties te testen door Uptrends fictieve data te laten genereren en deze naar het externe systeem te sturen. Het tabblad [SHORTCODE_1]Aanpassingen[SHORTCODE_2] in de integratie-editor heeft een knop genaamd **Testalert versturen** waarmee u een testbericht naar het third-partysysteem kunt sturen met de HTTPS-stap(pen) die u heeft gemaakt. Wanneer u deze testfunctie gebruikt, kunt u selecteren welk alerttype (een Foutalert, een Ok-alert of een Herinneringalert) Uptrends moet gebruiken voor dit specifieke testbericht. U kunt zo nodig andere geschikte waarden invullen en de resterende data (die normaal gesproken relevante controleregel- en alertdata zijn) zullen worden gevuld met fictieve waarden.

Zodra Uptrends het bericht genereert en het naar het third-partysysteem of de API verstuurt, worden de volledige berichtinhoud, de response code van de server en de inhoud weergegeven. U kunt de request headers en inhoud en de response headers en inhoud uitvouwen om het uitgaande en inkomende verkeer dat betrokken was bij het versturen van dit testbericht te inspecteren. 

## Een integratie controleren met live-data

Hoewel de hiervoor beschreven testfunctie nuttig is voor het statisch testen van uw bericht en variabelen, en om vast te stellen dat het communicatiekanaal naar het externe systeem correct werkt, is het goed om de mogelijkheid te hebben om te verifiëren dat de integratie ook in een live-situatie correct werkt.  
  
Zorg er eerst voor dat één van uw alertdefinities daadwerkelijk uw integratie gebruikt. Anders triggert Uptrends de integratie nooit om berichten te versturen. Meer informatie over het activeren van integraties in uw alertinginstellingen kunt u vinden in [escalatieniveaus]([LINK_URL_1]).  
  
Vervolgens moet er een foutsituatie optreden, zodat uw monitoring een echte alert genereert. Zodra u een alert in uw Alertstatus of Alertlog-dashboard ziet, klikt u erop om de details van die alert weer te geven. Het tabblad [SHORTCODE_3]Details[SHORTCODE_4] toont alle belangrijkste eigenschappen van de alert; het tabblad [SHORTCODE_5]Berichten[SHORTCODE_6] bevat de informatie die u nodig heeft om het berichtverkeer tussen Uptrends en het externe systeem te inspecteren.  
  
Zoek op het tabblad [SHORTCODE_7]Berichten[SHORTCODE_8] de integratie die u wilt inspecteren; mogelijk worden er andere integraties weergegeven die ook door deze alert zijn getriggerd. Vouw het integratiepaneel en de requests en responses uit. U ziet de volledige inhoud van het uitgaande bericht(en), de responses die door het externe systeem zijn teruggestuurd en eventuele foutberichten die zijn opgetreden als er een probleem was bij het versturen van het alertbericht.
