{
  "hero": {
    "title": "Ondersteunende protocollen"
  },
  "title": "Ondersteunde protocollen",
 "summary":"Een lijst met protocollen die door Uptrends worden ondersteund.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/ondersteunende-protocollen",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/supported-protocols"
}

## Ondersteunde protocollen

Vraagt u zich af of Uptrends de protocollen ondersteunt die u nodig heeft om uw websites, servers, webapplicaties en andere webservices te monitoren? **Antwoord**: Dat doen we zeker!

**Uptrends ondersteunt**: *HTTP*, *HTTPS*, *SMTP*, *POP3*, *IMAP*, *Ping*, *DNS*, *FTP*, *Connect*, *SQL*, *MySQL* en meer.

## HTTP

#### Wat is het HTTP-protocol?

Het **HTTP-protocol** wordt gebruikt om onbeveiligde webpagina's te bekijken en ermee te werken. Het is het standaard controleregeltype in Uptrends en moet gekozen worden als u een webpagina moet controleren.

#### Hoe werkt het HTTP-protocol?

Eerst moet u een [nieuwe controleregel toevoegen]({{< ref path="support/kb/basics" lang="nl" >}}) (compleet met URL die gemonitord moet worden).

Als de controleregel vervolgens wordt uitgevoerd, maakt de Uptrends-service verbinding met het webadres. Het controleert op veelvoorkomende netwerk- en HTTP-fouten en probeert de inhoud van de webpagina te downloaden.

{{< callout >}}
**Opmerking**: Dit type controleregel downloadt alleen de HTML-inhoud van een pagina. De download bevat geen afbeeldingen, scripts of interactieve elementen die mogelijk deel uitmaken van de pagina. Als u de volledige inhoud van een webpagina wilt controleren, raden we u aan het controleregeltype Full page check te overwegen.
{{< /callout >}}

#### Kan ik nog meer monitoren met het HTTP-protocol?

Ja! Naast de eenvoudige controles die hiervoor zijn genoemd, kunt u ook controleren op:

**Laadtijden**:

Als u tijdlimieten instelt, controleren we of de totale tijd die nodig is om de webpagina te laden binnen die limieten blijft. Met andere woorden: we kunnen controleren of uw webpagina zo snel laadt als u verwacht.

**Grootte**:

We kunnen testen of de gedownloade inhoud groter is dan het minimum aantal bytes of tekens dat u opgeeft. Dit is nuttig als u zeker wilt weten dat een bepaald bestand op uw webserver (een gegenereerde afbeelding bijvoorbeeld) niet defect of leeg is.

**Inhoud**:

Uptrends kan verifiëren dat een bepaald woord of zinsdeel daadwerkelijk aanwezig is in de inhoud van de pagina. Dit is een krachtige manier om te controleren of uw webpagina de juiste inhoud weergeeft.

Kies een woord of zinsdeel dat een essentieel onderdeel is van uw pagina, iets wat niet wordt weergegeven als er een fout is. Vul uw woord of zinsdeel gewoon in in het veld Pagina inhoud match.

In sommige gevallen wilt u misschien controleren op de afwezigheid van een woord. Dit doet u door te beginnen met een uitroepteken. Als u bijvoorbeeld wilt dat wij verifiëren dat het woord ‘error’ NIET voorkomt in de inhoud, vult u !error in.

## HTTPS

#### Wat is het HTTPS-protocol en hoe werkt het?

Het **HTTPS-protocol** is en werkt precies hetzelfde als HTTP (zie hierboven), behalve dat het kan worden gebruikt voor het controleren van een webpagina die is beveiligd met een SSL Certificaat.

## SMTP, POP3 en IMAP

#### Wat zijn de SMTP-, POP3- en IMAP-protocollen?

De **SMTP-, POP3- en IMAP-protocollen** worden gebruikt om verbinding te maken met mailservers om uitgaande e-mail te testen.

#### Hoe werken de SSMTP-, POP3- en IMAP-protocollen?

Eerst moet u een nieuwe controleregel toevoegen, het SMTP-, POP3- of IMAP-protocol selecteren en de juiste IP- en poortinformatie invullen.

Terwijl de controleregel wordt uitgevoerd, probeert de Uptrends monitoring service het IP-adres te bereiken. Als Uptrends het adres kan bereiken wordt uptime geregistreerd.

{{< callout >}}
**Opmerking**: Als u ervoor kiest de optionele gebruikersnaam en wachtwoord (inloggegevens voor uw e-mailserver) toe te voegen, zal de Uptrends-service ook proberen in te loggen als onderdeel van de controletest.
{{< /callout >}}

## Ping

#### Wat is het Ping-protocol?

**Ping** (of ICMP) is een heel eenvoudige manier om te zien of een server nog steeds actief en bereikbaar is.

#### Hoe werkt het Ping-protocol?

Het Ping-protocol werkt door zogenaamde ICMP Echo requests te versturen om te zien hoe lang het duurt voordat die request de server bereikt. U kunt deze optie kiezen als u op die server geen andere services (web, database of mail) heeft draaien die toegankelijk zijn via internet.

{{< callout >}}
**Opmerking**: Uw netwerk- of serverinstellingen moeten uitdrukkelijk ICMP-requests toestaan.
{{< /callout >}}

## DNS

#### Wat is het DNS-protocol?

Met het **DNS-protocol** kunt u de uptimestatus monitoren van de infrastructuur die uw gebruikers voorziet van een eenvoudige manier om naar uw websiteadres te navigeren. (Bijvoorbeeld: www.uptrends.nl in plaats van een IP-adres)

Uptrends kan locale, primaire en specifieke DNS monitoren.

#### How werkt het DNS-protocol?

Log eerst in, voeg een nieuwe controleregel (DNS) toe en configureer deze met het DNS-serveradres (domeinnaam of IP-adres), poortnummer, type DNS query, testwaarde en verwacht resultaat.

Het meest voor de hand liggende om te controleren is of uw domeinnaam (www\.uwbedrijf.nl) nog verwijst naar het IP-adres van uw webserver. Is dit niet het geval, dan kunnen uw gebruikers uw website waarschijnlijk niet vinden. Door deze DNS query direct te monitoren, detecteert Uptrends eventuele DNS-problemen, zelfs voordat uw website niet meer beschikbaar is voor gebruikers.

Met Uptrends' DNS-controleregel kunt u uitgebreide DNS-gezondheidscontroles uitvoeren: verifieer de domeinnamen van uw website (A- en CNAME-records), de mailserver domeinnaam-mappings (MX-records), gedelegeerden van de DNS-zone (NS-records), gezaghebbende informatie over DNS-zones (SOA-records) en andere DNS-informatie, omvat in TXT-records (waaronder SPF-informatie voor e-mailauthenticatie).

## FTP

#### Wat is het FTP-protocol?

Met het **FTP-protocol** kunt u de beschikbaarheid van uw FTP-server monitoren via de poort van uw keuze.

#### Hoe werkt het FTP-protocol?

Om het FTP-protocol te laten werken, moet u eerst inloggen en een FTP-controleregel met de juiste gegevens toevoegen.

De Uptrends-service zal vervolgens de status ervan monitoren door regelmatig verbinding te maken met de FTP-server via de juiste poort om te verzekeren dat deze operationeel is.

{{< callout >}}
**Opmerking**: Het is mogelijk om inloggegevens aan de controleregel toe te voegen, zodat u weet dat de FTP-inlogfuncties goed werken. U kunt momenteel echter geen bestanden van die server ophalen met de Uptrends-service.
{{< /callout >}}

## Connect

Als geen ander protocol geschikt is voor uw situatie, kunt u het **Connect-protocol** gebruiken om een heel eenvoudige test te doen. Als u een domeinnaam of IP-adres van uw server of firewall opgeeft, en een poort, proberen we een eenvoudige verbinding te openen met die combinatie van adres en poort.

## SQL

#### Wat is het SQL-protocol?

Met het **SQL-protocol** kunt u de uptime van uw Microsoft SQL server database monitoren.

{{< callout >}}
**Opmerking:** SQL-servers kunnen alleen worden gemonitord als ze direct (en regelmatig) toegankelijk zijn via internet.
{{< /callout >}}

#### Hoe werkt het SQL-protocol?

Om een SQL-controleregel uit te voeren, moet u eerst inloggen en een SQL-controleregel aan uw account toevoegen. U moet minimaal het IP-adres van de server en een poort opgeven (standaard 1433).

De Uptrends-service probeert dan verbinding te maken met de betreffende server en rapporteert positief als alles in orde is, en zal een onbevestigde (en mogelijk later bevestigde) fout triggeren als deze niet bereikbaar is.

{{< callout >}}
**Opmerking**: U kunt een gebruikersnaam en wachtwoord opgeven om uw login te testen, evenals een databasenaam zodat we kunnen controleren of de database toegankelijk is.
{{< /callout >}}

## MySQL

#### Wat is het MySQL-protocol?

Het **MySQL-protocol** stelt de Uptrends-applicatie in staat om de beschikbaarheid van MySQL-databases te monitoren.

#### Hoe werkt het MySQL-protocol?

Het MySQL-protocol werkt vrijwel hetzelfde als het SQL-protocol, maar dan met MySQL-databases! (De standaardpoort om verbinding te maken met MySQL-databases is 3306.)
