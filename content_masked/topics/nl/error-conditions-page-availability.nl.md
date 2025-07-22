{
  "hero": {
    "title": "Foutcondities - Beschikbaarheid"
  },
  "title": "Foutcondities - Beschikbaarheid ",
  "summary": "Een overzicht van de beschikbare foutcondities voor de categorie *Beschikbaarheid*. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-paginabeschikbaarheid",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De foutcondities in de controleregelset-up worden gebruikt om situaties te definiëren waarvoor u een fout wilt signaleren. Lees het Knowledge Base-artikel [Foutcondities]([LINK_URL_1]) voor meer algemene informatie en hoe u [Een foutconditie configureert]([LINK_URL_2]). 

De foutconditie **Beschikbaarheid** controleert de beschikbaarheid van de pagina (HTTP/S- of webservice-controleregel), de website (transacties) of resource (andere controleregels). Deze kan verschillende opties hebben, afhankelijk van het controleregeltype. Bekijk de tabel bij [Welke foutcondities zijn beschikbaar?]([LINK_URL_3]) om meer te weten komen.

De beschikbaarheidscontrole voor een HTTP(S)- of Webservice HTTP(S)-controleregel ziet er bijvoorbeeld zo uit:

![screenshot foutconditie paginabeschikbaarheid]([LINK_URL_4])

## Algemene beschikbaarheidscontrole

Standaard controleren alle controleregeltypes de beschikbaarheid van de gemonitorde website, pagina of resource. 

Waar van toepassing, bijv. voor een HTTP(S)- of Webservice HTTP(S)-controleregel, resulteert elke response status code die groter is dan 400 in een fout. Voor andere controleregeltypes, bijv. DNS, (S)FTP, mailservers of databaseservers, is er geen HTTP response status code maar een controle of de server of service bereikbaar is.

## HTTP status code controleren

Voor controleregeltypes die reageren met een HTTP status code is de optie om te controleren op een specifieke status code beschikbaar.

Soms verwacht u een foutcode of een andere code dan een geslaagde. Als u bijvoorbeeld op een oude webpagina een redirect naar een nieuwe pagina heeft, wilt u misschien weten of de redirect mislukt. Als u wilt controleren op een bepaalde response, selecteert u de optie **Controleren of de response HTTP status code correspondeert met ...** en selecteert u een status code uit de lijst.

Ga voor een volledige lijst met statuscodes naar de Internet Assigned Numbers Authority's (IANA) [HTTP Status Code Registry]([LINK_URL_5]).