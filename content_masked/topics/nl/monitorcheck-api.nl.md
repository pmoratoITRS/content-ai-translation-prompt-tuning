{
  "title": "MonitorCheck API",
  "url": "[URL_BASE_TOPICS]api/monitorcheck-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Monitor check data kunnen worden opgehaald met behulp van de **MonitorCheck** API-eindpunten die deel uitmaken van [API v4]([LINK_URL_1]). Monitor checks zijn de individuele metingen die we voor elke controleregel verzamelen, dus de MonitorCheck API geeft toegang tot die ruwe data. Nadat de data zijn opgehaald, kunt u die opslaan in een database voor offline analyse, audit of back-updoeleinden. De volgende drie eindpunten zijn beschikbaar:

| MonitorCheck endpoint      | **Gebruik**                                                       |
|----------------------------|-------------------------------------------------------------------|
| /MonitorCheck              | Retourneert alle Monitor check data in de account.                |
| /MonitorCheck/Monitor      | Retourneert Monitor check data voor een specifieke controleregel. |
| /MonitorCheck/MonitorGroup | Retourneert Monitor check data voor een Monitor-groep.            |

Een gangbaar scenario is om uw data te downloaden (voor alle controleregels, voor een groep of een specifieke controleregel) voor een bepaalde periode (bijvoorbeeld voor de vorige maand). Afhankelijk van het aantal controleregels dat u hebt en de monitoringinterval waarmee ze worden uitgevoerd, kan dit een aanzienlijke hoeveelheid data zijn. Een goede manier om API calls snel en responsief te houden, is door data in blokken te downloaden en verwerken, bijvoorbeeld 100 items per keer. De MonitorCheck API-methoden zijn geoptimaliseerd voor het downloaden van data in blokken.

Alle MonitorCheck-eindpunten maken gebruik van de volgende parameters:

|                |                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **period**     | Periode om op te filteren (standaard: Last24Hours). [HTML_TAG_1]Laat dit leeg als u een aangepaste periode wilt specificeren met *start* en *end*.        |
| **start**      | Het begin van een aangepaste periode. [HTML_TAG_2]Laat dit leeg als u de parameter *period* gebruikt.                                                     |
| **end**        | Het einde van een aangepaste periode. [HTML_TAG_3]Laat dit leeg als u de parameter *period* gebruikt.                                                     |
| **errorLevel** | Het minimale foutniveau van te retourneren checks [HTML_TAG_4](standaard: NoError, wat betekent dat er geen filter is toegepast).                          |
| **cursor**     | Parameter voor het doorlopen van de data, zie hieronder.                                                                                      |
| **take**       | Het aantal te retourneren rijen (standaard: 100; dit is tevens het maximum).                                                                  |
| **sorting**    | Specificeert of de data moeten worden gesorteerd op datum in Ascending (oplopende) [HTML_TAG_5]of Descending (aflopende) volgorde (standaard: Descending). |

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

[HTML_TAG_6]
[HTML_TAG_7]
  [HTML_TAG_8]
    [HTML_TAG_9][HTML_TAG_10]
    [HTML_TAG_11][HTML_TAG_12]
    [HTML_TAG_13][HTML_TAG_14]
  [HTML_TAG_15]
[HTML_TAG_16]
[HTML_TAG_17]
  [HTML_TAG_18]
    [HTML_TAG_19]Id[HTML_TAG_20]
    [HTML_TAG_21]De unieke monitor check identifier. Deze Id komt overeen met de monitor check Id die u in de adresbalk ziet wanneer u de details van een controle bekijkt in Uptrends.[HTML_TAG_22]
    [HTML_TAG_23][HTML_TAG_24]
  [HTML_TAG_25]
  [HTML_TAG_26]
    [HTML_TAG_27]Type[HTML_TAG_28]
    [HTML_TAG_29]Het objecttype (een vaste waarde “MonitorCheck” voor deze API-methoden).[HTML_TAG_30]
    [HTML_TAG_31][HTML_TAG_32]
  [HTML_TAG_33]
  [HTML_TAG_34]
    [HTML_TAG_35]Attributes[HTML_TAG_36]
    [HTML_TAG_37]De kenmerken van het object dat de feitelijke data bevat. Deze kenmerken omvatten:[HTML_TAG_38]
    [HTML_TAG_39][HTML_TAG_40]
  [HTML_TAG_41]
  [HTML_TAG_42]
    [HTML_TAG_43][HTML_TAG_44]
    [HTML_TAG_45]MonitorGuid[HTML_TAG_46]
    [HTML_TAG_47]De GUID van de controleregel die overeenkomt met deze monitor check.[HTML_TAG_48]
  [HTML_TAG_49]
  [HTML_TAG_50]
    [HTML_TAG_51][HTML_TAG_52]
    [HTML_TAG_53]Timestamp[HTML_TAG_54]
    [HTML_TAG_55]De datum en tijd waarop de controle van de controleregel is voltooid op basis van de lokale tijd van de aangemelde operator.[HTML_TAG_56]
  [HTML_TAG_57]
  [HTML_TAG_58]
    [HTML_TAG_59][HTML_TAG_60]
    [HTML_TAG_61]ErrorCode[HTML_TAG_62]
    [HTML_TAG_63]De numerieke foutcode van Uptrends in geval van een foutresultaat, of 0 in geval van een OK-resultaat.[HTML_TAG_64]
  [HTML_TAG_65]
  [HTML_TAG_66]
    [HTML_TAG_67][HTML_TAG_68]
    [HTML_TAG_69]TotalTime[HTML_TAG_70]
    [HTML_TAG_71]Het aantal milliseconden dat nodig is om de monitor check te voltooien.[HTML_TAG_72]
  [HTML_TAG_73]
  [HTML_TAG_74]
    [HTML_TAG_75][HTML_TAG_76]
    [HTML_TAG_77]ResolveTime[HTML_TAG_78]
    [HTML_TAG_79]Het aantal milliseconden dat nodig is om de DNS query voor deze controle/check uit te voeren, indien van toepassing.[HTML_TAG_80]
  [HTML_TAG_81]
  [HTML_TAG_82]
    [HTML_TAG_83][HTML_TAG_84]
    [HTML_TAG_85]ConnectionTime[HTML_TAG_86]
    [HTML_TAG_87]Het aantal milliseconden dat nodig is om een verbinding tot stand te brengen.[HTML_TAG_88]
  [HTML_TAG_89]
  [HTML_TAG_90]
    [HTML_TAG_91][HTML_TAG_92]
    [HTML_TAG_93]DownloadTime[HTML_TAG_94]
    [HTML_TAG_95]Het aantal milliseconden dat nodig is om de responsdata te downloaden.[HTML_TAG_96]
  [HTML_TAG_97]
  [HTML_TAG_98]
    [HTML_TAG_99][HTML_TAG_100]
    [HTML_TAG_101]TotalBytes[HTML_TAG_102]
    [HTML_TAG_103]Het aantal gedownloade bytes voor deze check.[HTML_TAG_104]
  [HTML_TAG_105]
  [HTML_TAG_106]
    [HTML_TAG_107][HTML_TAG_108]
    [HTML_TAG_109]ResolvedIpAddress[HTML_TAG_110]
    [HTML_TAG_111]Het IP-adres dat voor de gespecificeerde domeinnaam is gevonden als onderdeel van deze monitor check.[HTML_TAG_112]
  [HTML_TAG_113]
  [HTML_TAG_114]
    [HTML_TAG_115][HTML_TAG_116]
    [HTML_TAG_117]ErrorLevel[HTML_TAG_118]
    [HTML_TAG_119]Een waarde die de status OK/Error voor deze check weergeeft: NoError als het resultaat OK was, Unconfirmed als er een fout werd gevonden, Confirmed als een fout werd gevonden bij een tweede controle, direct na een Unconfirmed fout.[HTML_TAG_120]
  [HTML_TAG_121]
  [HTML_TAG_122]
    [HTML_TAG_123][HTML_TAG_124]
    [HTML_TAG_125]ErrorDescription[HTML_TAG_126]
    [HTML_TAG_127]Een tekstwaarde die de gevonden fout beschrijft of OK als er geen fout is gevonden.[HTML_TAG_128]
  [HTML_TAG_129]
  [HTML_TAG_130]
    [HTML_TAG_131][HTML_TAG_132]
    [HTML_TAG_133]ErrorMessage[HTML_TAG_134]
    [HTML_TAG_135]Eventuele aanvullende foutinformatie, indien beschikbaar.[HTML_TAG_136]
  [HTML_TAG_137]
  [HTML_TAG_138]
    [HTML_TAG_139][HTML_TAG_140]
    [HTML_TAG_141]ServerId[HTML_TAG_142]
    [HTML_TAG_143]De Id van de Uptrends-controlestationserver die deze check heeft uitgevoerd.[HTML_TAG_144]
  [HTML_TAG_145]
   [HTML_TAG_146]
    [HTML_TAG_147][HTML_TAG_148]
    [HTML_TAG_149]HttpStatusCode[HTML_TAG_150]
    [HTML_TAG_151]De geretourneerde HTTP-statuscode (indien van toepassing).[HTML_TAG_152]
  [HTML_TAG_153]
  [HTML_TAG_154]
    [HTML_TAG_155]Relationships[HTML_TAG_156]
    [HTML_TAG_157]De reeks relationships bevat een lijst met data/objecten die gerelateerd zijn aan de huidige data. Deze lijst kan koppelingen bevatten om de gerelateerde data op te halen. Relation data hebben dezelfde structuur, in die zin dat die vermeldingen ook de members Id, Type en Links bevatten.[HTML_TAG_158]
    [HTML_TAG_159][HTML_TAG_160]
  [HTML_TAG_161]
[HTML_TAG_162]
[HTML_TAG_163]