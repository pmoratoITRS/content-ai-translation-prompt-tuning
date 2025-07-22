{
  "title": "MonitorCheck API",
  "url": "/support/kb/api/monitorcheck-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/monitorcheck-api"
}

Monitor check data kunnen worden opgehaald met behulp van de **MonitorCheck** API-eindpunten die deel uitmaken van [API v4](/support/kb/api/v4). Monitor checks zijn de individuele metingen die we voor elke controleregel verzamelen, dus de MonitorCheck API geeft toegang tot die ruwe data. Nadat de data zijn opgehaald, kunt u die opslaan in een database voor offline analyse, audit of back-updoeleinden. De volgende drie eindpunten zijn beschikbaar:

| MonitorCheck endpoint      | **Gebruik**                                                       |
|----------------------------|-------------------------------------------------------------------|
| /MonitorCheck              | Retourneert alle Monitor check data in de account.                |
| /MonitorCheck/Monitor      | Retourneert Monitor check data voor een specifieke controleregel. |
| /MonitorCheck/MonitorGroup | Retourneert Monitor check data voor een Monitor-groep.            |

Een gangbaar scenario is om uw data te downloaden (voor alle controleregels, voor een groep of een specifieke controleregel) voor een bepaalde periode (bijvoorbeeld voor de vorige maand). Afhankelijk van het aantal controleregels dat u hebt en de monitoringinterval waarmee ze worden uitgevoerd, kan dit een aanzienlijke hoeveelheid data zijn. Een goede manier om API calls snel en responsief te houden, is door data in blokken te downloaden en verwerken, bijvoorbeeld 100 items per keer. De MonitorCheck API-methoden zijn geoptimaliseerd voor het downloaden van data in blokken.

Alle MonitorCheck-eindpunten maken gebruik van de volgende parameters:

|                |                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Periode om op te filteren (standaard: Last24Hours). <br>Laat dit leeg als u een aangepaste periode wilt specificeren met *start* en *end*.        |
| **start**      | Het begin van een aangepaste periode. <br>Laat dit leeg als u de parameter *period* gebruikt.                                                     |
| **end**        | Het einde van een aangepaste periode. <br>Laat dit leeg als u de parameter *period* gebruikt.                                                     |
| **errorLevel** | Het minimale foutniveau van te retourneren checks <br>(standaard: NoError, wat betekent dat er geen filter is toegepast).                          |
| **cursor**     | Parameter voor het doorlopen van de data, zie hieronder.                                                                                      |
| **take**       | Het aantal te retourneren rijen (standaard: 100; dit is tevens het maximum).                                                                  |
| **sorting**    | Specificeert of de data moeten worden gesorteerd op datum in Ascending (oplopende) <br>of Descending (aflopende) volgorde (standaard: Descending). |

## Doorloop uw data door een cursor te gebruiken

Een cursor is een stringwaarde die functioneert als een aanwijzer in de tijdlijn van uw data. Wanneer u begint met het aanvragen van een grote hoeveelheid data (bijvoorbeeld alle controleregeldata voor de afgelopen maand), retourneert de API het eerste blok van 100 items. Samen met die data krijgt u een cursorwaarde die u kunt gebruiken om gemakkelijk bij het tweede blok data te komen enzovoort. U kunt dit proces herhalen totdat u alle data hebt gedownload voor de periode die u hebt aangevraagd. Een lege cursor geeft aan dat u het einde van de reeks hebt bereikt en dat er geen data meer te verwachten zijn.

## Vooruit of achteruit in de tijd

U kunt kiezen of u met recente data begint en achteruit in de tijd werkt (sorting=Descending) of aan het begin van een tijdsperiode begint en vooruit naar de huidige tijd werkt (sorting=Ascending).  
  
Dit laatste is vooral handig en efficiënt als u een geautomatiseerd proces gebruikt dat regelmatig updates voor huidige data ontvangt. U kunt bijvoorbeeld elke 5 minuten toegang krijgen tot de API met Last24Hours, Ascending, en de cursorwaarde van de vorige respons te specificeren: de API zal alleen data retourneren die na uw laatste API request zijn gegenereerd. Het resultaat kan een lege lijst bevatten als er nog geen nieuwe data beschikbaar zijn, maar als de API respons een niet-lege cursorwaarde bevat, kunnen nieuwe data in een latere request worden opgehaald.t.

## MonitorCheck details ophalen

Wanneer u een lijst met MonitorChecks ophaalt, bevat elke MonitorCheck vermelding de basisgegevens voor die controle, zoals hieronder wordt beschreven. Echter, afhankelijk van het controleregeltype zijn er mogelijk meer gedetailleerde data beschikbaar. Die details kunnen worden opgehaald met afzonderlijke API calls. De koppeling tussen de basis MonitorCheck en alle gerelateerde details worden beschreven als relaties. Wanneer er aan een MonitorCheck inderdaad een of meer details gekoppeld zijn, worden deze weergegeven in het 'Relationships' member (zie hieronder): het zal een koppeling bevatten naar elk geschikt detaileindpunt dat toegang geeft tot die data. De volgende detaileindpunten zijn momenteel beschikbaar:

| Detail endpoint                            | Usage                                                                                           |
|--------------------------------------------|-------------------------------------------------------------------------------------------------|
| /MonitorCheck/{monitorCheckId}/Http        | Retourneert details voor een HTTP-controle, inclusief HTML-inhoud en headerinformatie.          |
| /MonitorCheck/{monitorCheckId}/Waterfall   | Retourneert de volledige waterfall van een Full Page Check-controleregel of een Transactiestap. |
| /MonitorCheck/{monitorCheckId}/Transaction | Retourneert resultaten van elke transactiestap, inclusief de staptijden.                        |

## Algemene datastructuur

Een MonitorCheck respons gebruikt het volgende formaat om de feitelijke data te scheiden van de geleverde metadata:

### Root

Root bevat de volgende members:

|            |                                                                            |
|------------|----------------------------------------------------------------------------|
| **Data**   | Een array of een enkel object met (een subset van) de gevraagde data.      |
| **Links**  | Koppelingen die verwijzen naar zichzelf en naar de volgende dataset.       |
| **Cursor** | Bevat cursorwaarden die moeten worden gebruikt om de dataset te doorlopen. |

### Data

De data member kan een reeks objecten of een enkel object bevatten. Hoe dan ook, het enkele MonitorCheck object of de MonitorCheck objecten in de reeks zal de volgende members hebben:

<table>
<thead>
  <tr>
    <th class="cell-small"></th>
    <th class="cell-large"></th>
    <th class="cell-large"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="bold">Id</td>
    <td>De unieke monitor check identifier. Deze Id komt overeen met de monitor check Id die u in de adresbalk ziet wanneer u de details van een controle bekijkt in Uptrends.</td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Type</td>
    <td>Het objecttype (een vaste waarde “MonitorCheck” voor deze API-methoden).</td>
    <td></td>
  </tr>
  <tr>
    <td class="bold">Attributes</td>
    <td>De kenmerken van het object dat de feitelijke data bevat. Deze kenmerken omvatten:</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">MonitorGuid</td>
    <td>De GUID van de controleregel die overeenkomt met deze monitor check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">Timestamp</td>
    <td>De datum en tijd waarop de controle van de controleregel is voltooid op basis van de lokale tijd van de aangemelde operator.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorCode</td>
    <td>De numerieke foutcode van Uptrends in geval van een foutresultaat, of 0 in geval van een OK-resultaat.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalTime</td>
    <td>Het aantal milliseconden dat nodig is om de monitor check te voltooien.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolveTime</td>
    <td>Het aantal milliseconden dat nodig is om de DNS query voor deze controle/check uit te voeren, indien van toepassing.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ConnectionTime</td>
    <td>Het aantal milliseconden dat nodig is om een verbinding tot stand te brengen.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">DownloadTime</td>
    <td>Het aantal milliseconden dat nodig is om de responsdata te downloaden.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">TotalBytes</td>
    <td>Het aantal gedownloade bytes voor deze check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ResolvedIpAddress</td>
    <td>Het IP-adres dat voor de gespecificeerde domeinnaam is gevonden als onderdeel van deze monitor check.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorLevel</td>
    <td>Een waarde die de status OK/Error voor deze check weergeeft: NoError als het resultaat OK was, Unconfirmed als er een fout werd gevonden, Confirmed als een fout werd gevonden bij een tweede controle, direct na een Unconfirmed fout.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorDescription</td>
    <td>Een tekstwaarde die de gevonden fout beschrijft of OK als er geen fout is gevonden.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ErrorMessage</td>
    <td>Eventuele aanvullende foutinformatie, indien beschikbaar.</td>
  </tr>
  <tr>
    <td></td>
    <td class="bold">ServerId</td>
    <td>De Id van de Uptrends-controlestationserver die deze check heeft uitgevoerd.</td>
  </tr>
   <tr>
    <td></td>
    <td class="bold">HttpStatusCode</td>
    <td>De geretourneerde HTTP-statuscode (indien van toepassing).</td>
  </tr>
  <tr>
    <td class="bold">Relationships</td>
    <td>De reeks relationships bevat een lijst met data/objecten die gerelateerd zijn aan de huidige data. Deze lijst kan koppelingen bevatten om de gerelateerde data op te halen. Relation data hebben dezelfde structuur, in die zin dat die vermeldingen ook de members Id, Type en Links bevatten.</td>
    <td></td>
  </tr>
</tbody>
</table>