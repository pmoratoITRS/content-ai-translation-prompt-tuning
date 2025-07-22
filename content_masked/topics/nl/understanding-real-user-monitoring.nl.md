{
  "hero": {
    "title": "Real User Monitoring begrijpen"
  },
  "title": "Real User Monitoring begrijpen",
  "summary": "In dit artikel leggen we basisbegrippen van RUM uit en hoe RUM werkt. ",
  "url": "[URL_BASE_TOPICS]rum/real-user-monitoring-begrijpen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

In dit artikel worden de basisbegrippen en de theorie van de set-up uitgelegd.

## Wat is Real User Monitoring?

Als het gaat om het meten van de performance die door de feitelijke gebruikers van uw site worden ervaren, is Real User Monitoring (RUM) onverslaanbaar. RUM legt de performance van uw RUM enabled pagina's vast, aggregeert de data en geeft deze weer in interactieve dashboards waar u de performance kunt vergelijken op basis van bekeken pagina, apparaat, browser en versie, besturingssysteem en versie en gebruikerslocatie.

RUM is een passieve benadering van monitoring omdat het afhankelijk is van uw gebruikers die uw site bezoeken voor het genereren van data. Als uw site down gaat, kunnen uw gebruikers de site niet bezoeken en zijn er dus geen gegevens voor de rapportage. Daarvoor gebruikt u uw synthetic of actieve monitoring. Uw [synthetic controleregels]([LINK_URL_1]) zoals controleregels voor Uptime, Performance, API en Transactie, controleren uw site op regelmatige basis en als zij een probleem ervaren laten we u dat onmiddellijk weten aan de hand van uw [alertinginstellingen]([LINK_URL_2]).

## Hoe werkt Real User Monitoring?

U plaatst een heel klein, [non-invasief script]([LINK_URL_3]) in de [INLINE_CODE_1] tags op de pagina’s die u met RUM wilt volgen. Wanneer uw gebruikers een RUM enabled pagina bezoeken, legt het script de performance van de pagina vast. Nadat het laden van de pagina is voltooid, combineert het script de performance data met informatie over de omgeving en locatie van de gebruiker en stuurt deze naar de cloud. Uptrends haalt de data [bijna in realtime]([LINK_URL_4]) op en geeft deze weer in uw RUM dashboards. Het resultaat is een uitgebreid beeld van de feitelijke performance van uw site zoals die door uw gebruikers is ervaren. Als u zich bezorgd maakt over gebruikersprivacy, lees dan het artikel over [RUM en gebruikersprivacy]([LINK_URL_5]).

## Hoe ziet een RUM Script eruit?

Uptrends' engineers hebben het RUM script zo ontworpen dat het zo non-invasief is als mogelijk is. Het kleine script laadt snel en heeft vrijwel geen invloed op de paginaperformance. Het doet zijn werk op de achtergrond terwijl het laden van de pagina voortgaat, en nadat het laden is voltooid, eindigt het script door de gebruikers- en performancedata naar de cloud te sturen. Uw script zal lijken op het script hieronder.

[CODE_BLOCK_1]
