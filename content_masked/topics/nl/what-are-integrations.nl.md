{
  "hero": {
    "title": "Wat zijn integraties?"
  },
  "title": "Wat zijn integraties?",
  "summary": "Integraties zijn verbindingen met de buitenwereld die zorgen voor het versturen van alertberichten die zijn getriggerd door Uptrends-monitoring.",
  "url": "[URL_BASE_TOPICS]alerting/integraties/wat-zijn-integraties",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Integraties zijn verbindingen met de buitenwereld die zorgen voor het versturen van alertberichten die zijn getriggerd door Uptrends-monitoring. Telkens wanneer een controle een alert triggert, verstuurt Uptrends, op basis van de instellingen die u in alertdefinities hebt geconfigureerd, de juiste berichten met de integraties die u in uw alertdefinities hebt geactiveerd. De eenvoudigste integratie is de E‑mailintegratie; een E‑mailintegratie creëert een e‑mailbericht en verstuurt dit naar de ontvangers die u opgeeft. Een ander eenvoudig voorbeeld is de SMS-integratie; een SMS-integratie stuurt SMS-/tekstberichten naar de mobiele telefoons van uw operators.

## Verbinden met externe systemen

Naast het sturen van alertberichten naar individuele mensen, wilt u waarschijnlijk alertinformatie van Uptrends naar andere systemen sturen voor geautomatiseerde verwerking. Het versturen van de alertinformatie naar geautomatiseerde processen is handig om rechtstreeks verbinding te maken met uw systeem dat incidenten volgt en afhandelt (bijvoorbeeld PagerDuty, Splunk On-Call of ServiceNow) of om eenvoudig alertinformatie te delen in de communicatietool van uw team (bijvoorbeeld in Slack) of met het grote publiek (bijvoorbeeld StatusHub).

Enkele van de beschikbare integraties gebruiken een vast tekstberichtformaat (E-mail, SMS, Telefoon, Slack) terwijl andere zich houden aan het berichtformaat dat door het third-partysysteem wordt verwacht, zodat dat systeem de data die afkomstig is van Uptrends precies kan weergeven en verwerken zoals het wil (PagerDuty, StatusHub, Splunk On-Call, ServiceNow). Wij hebben integratiehandleidingen beschikbaar voor alle ondersteunde third-partysystemen. Raadpleeg onze Knowledge base categorie [Integraties]([LINK_URL_1]) voor de juiste integratiehandleiding.

## Een aangepaste webhook-integratie bouwen

Hoewel Uptrends een groeiende lijst met voorgedefinieerde integraties heeft, is de kans groot dat u verbinding wilt maken met een systeem dat nog niet in de lijst staat. Verbinding maken met systemen die niet door Uptrends worden aangeboden, is dan mogelijk met de functie aangepaste integratie; hiermee kan een integratie worden geconfigureerd met elk systeem dat webhooks ondersteunt, dat wil zeggen als het een API heeft die inkomende berichten kan verwerken.

Als u verbinding maakt met een third-partysysteem, verwacht het third-partysysteem dat de inkomende webhook (d.w.z. de data die van Uptrends naar dat systeem worden verstuurd) een bepaald berichtformaat gebruikt, zodat zij het kunnen verwerken. In de documentatie van het systeem wordt de vereiste inhoud van het bericht uitgelegd, waaronder de betekenis van elk veld en de URL waarin het bericht moet worden verzonden. Met de integratie-editor in Uptrends kunt u alle benodigde data configureren.

U kunt desgewenst ook verbinding maken met een systeem dat geen vereist of gewenst berichtformaat heeft. In dat geval is het handig om de aangepaste integratie genaamd **Uptrends-integratie** te gebruiken. Die heeft een voorgeconfigureerd bericht dat alle alertvariabelen bevat die beschikbaar zijn in Uptrends. U hoeft alleen de URL op te geven van de API waarmee u verbinding wilt maken.

Meer informatie vindt u in dit artikel over [een aangepaste integratie bouwen]([LINK_URL_2]), dat ook nuttig is voor het wijzigen van een van de aanpasbare integraties.
