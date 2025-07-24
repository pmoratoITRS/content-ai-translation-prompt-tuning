{
  "hero": {
    "title": "Hoe een HTTP-controleregel werkt"
  },
  "title": "Hoe een HTTP-controleregel werkt",
  "summary": "Leer hoe Uptrends een HTTP(S)-test uitvoert en wat het systeem doet wanneer het een error tegenkomt.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/http-en-https/hoe-een-http-controleregel-werkt",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Hebt u zich ooit afgevraagd wat er gebeurt wanneer Uptrends een HTTP- or HTTPS-controleregel op uw website afvuurt? Afhankelijk van de omstandigheden zijn er veel verschillende scenario's mogelijk; hier worden er enkele besproken.

1.  Uptrends kiest willekeurig één van de door u geconfigureerde wereldwijde controlestations voor de test.
2.  Uptrends probeert de gespecificeerde domeinnaam om te zetten.   
    [SHORTCODE_1]**Opmerking:** U kunt het IP-adres invoeren in plaats van de domeinnaam om het resolve-gedeelte van de test over te slaan, maar dan zult u geen alert ontvangen als uw site resolveproblemen heeft.[SHORTCODE_2] 
3.  Door het het IP-adres te gebruiken probeert Uptrends vervolgens een low-level TCP-verbinding tot stand te brengen via poort 80 bij HTTP, via poort 443 bij HTTPS of de poort die u hebt gespecificeerd.
4.  Na de basis test beschreven in stap 3, openen we een nieuwe TCP-connectie om het HTTP(S)-request te versturen en wachten we op de respons.

## Wat gebeurt er wanneer Uptrends een probleem vindt?

Errors kunnen tijdens elke stap in het testproces optreden, en afhankelijk van de error probeert Uptrends allerlei dingen voordat er een alert wordt verstuurd. Bij de meeste errors zal Uptrends proberen een foutloze verbinding te krijgen via een ander controlestation. Als Uptrends dezelfde fout tegenkomt van een ander controlestation, zal er een alert verstuurd worden. Uptrends maakt hierop wel enkele uitzonderingen op basis van specifieke errors.

### HTTPS-errors

Wanneer het controleregeltype HTTPS wordt gebruikt en de request mislukt (stap 3), kan Uptrends het meerdere keren proberen met verschillende beveiligingsprotocollen voordat de test als mislukte poging wordt gezien.

### HTTP(S) met verstrekte authenticatiegegevens

Bij HTTP- en HTTPS-requests die inloggegevens van gebruikers bevatten, kan Uptrends een mislukte test nogmaals uitvoeren voordat de poging als mislukt wordt gezien.

### Netwerk errors

Als de HTTP- of HTTPS-request mislukt vanwege een netwerkprobleem, probeert Uptrends een traceroute uit te voeren naar het IP-adres. De traceroute stuurt een reeks Ping-pakketten (=ICMP).
