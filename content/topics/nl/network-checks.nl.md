{
  "hero": {
    "title": "Netwerkcontroles"
  },
  "title": "Netwerkcontroles",
  "summary": "Controleregels voor externe netwerkcontroles zorgen ervoor dat uw netwerk actief en toegankelijk is en stellen u op de hoogte van uitval.  ",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/netwerkcontroles",
  "translationKey": "https://www.uptrends.com/support/kb/network-checks"
}

Uptrends ontwierp zijn HTTP(S)-controleregels om de beschikbaarheid en snelheid van uw website te controleren. maar als u andere niet-webgebaseerde netwerkapparaten van buiten uw firewall moet controleren, heeft u een netwerk check nodig. Uptrends stelt uw team op de hoogte wanneer er een fout met de opgegeven URL of IP-adres optreedt, en afhankelijk van de fout ontvangt u een traceroute om u te assisteren bij het oplossen van het probleem. Met Netwerk checks heeft u twee opties: Ping of Connect.

## Ping

Als u de netwerk check Ping selecteert, gebruiken Uptrends' controlestations ICMP (Internet Control Message Protocol) om een echo request te versturen. Uptrends verzamelt en rapporteert responstijden en verstuurt alerts als er fouten worden gevonden in de reply.

{{< callout >}}
**Opmerking:** ICMP moet ingeschakeld zijn op het apparaat om onnodige alerts te voorkomen; ook bij zwaar netwerkverkeer negeren apparaten soms ICMP requests.
{{< /callout >}}

## Connect

Als u een **netwerk check Connect** selecteert, zal Uptrends proberen te verbinden met het poortnummer dat u toekent. U kunt ieder poortnummer opgeven; om bijvoorbeeld een SSH (Secure Shell)-verbinding te maken met een Linux box specificeert u poort 22.

## Functies

Zowel Ping als Connect biedt talrijke opties voor uw monitoring.

### Interval

Hoewel de standaardinstelling voor de interval vijf minuten is, kunt u de interval aanpassen van één minuut tot eenmaal per uur.

{{< callout >}}
**Opmerking**: Uw controle-interval is de tijd tussen het einde van de ene controle en het begin van de volgende. [Lees meer]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="nl" >}})
{{< /callout >}}

### IP-versie

IPv4 is lang de standaard geweest, maar de nieuwe versie IPv6 is wordt snel populairder. De meeste controlestations van Uptrends ondersteunen IPv6, en we voegen er steeds meer toe.

{{< callout >}}
**Opmerking**: We raden aan de controles zo te configureren dat zowel IPv4 als IPv6 wordt gemonitord. De twee versies gaan verschillend om met routing, waardoor tests kunnen mislukken in de ene versie terwijl die in de andere versie wel slaagt.
{{< /callout >}}

### Performance

Trage connects of pings kunnen duiden op andere netwerk- of hardwareproblemen. Op het tabblad {{< AppElement type="tab" >}}Foutcondities{{< /AppElement >}} kunt u performancelimieten instellen waarbij u op de hoogte wordt gesteld als uw netwerk performanceproblemen ondervindt.

## Traceroute

Uptrends voert in verschillende gevallen traceroute-diagnostiek uit:

1.  Als onderdeel van een controleregelcheck, wanneer de controleregel een connectiviteits-/netwerkprobleem vermoedt. Wanneer een HTTPS-controleregel bijvoorbeeld contact probeert te maken met de webserver, maar er geen TCP-verbinding kan worden gemaakt naar het IP-adres van de server, wordt er een traceroute uitgevoerd om extra diagnostische informatie te verzamelen over de connectiviteit tussen de controlestationlocatie van Uptrends en uw server.
2.  Wanneer u de gratis traceroute-tool gebruikt om een expliciete traceroute uit te voeren op een van de controlestationservers van Uptrends.

Het is belangrijk om te weten welk type traffic wordt verwacht wanneer deze traceroutes worden uitgevoerd. Traceroute-implementaties gedragen zich verschillend op verschillende platforms: sommige implementaties gebruiken UDP-pakketten, sommige gebruiken TCP-pakketten en sommige gebruiken ICMP (ping) echo requests. De traceroutes die Uptrends uitvoert, worden altijd uitgevoerd op Windows-servers, die ICMP-pakketten gebruiken. Daarom zal het gebruik van Uptrends om traceroutes naar uw netwerkomgeving uit te voeren alleen werken als uw netwerk ICMP-pakketten toestaat. Er is geen TCP- of UDP-traffic bij betrokken.

Het configureren van een externe server of netwerkapparaat voor monitoring is vrij eenvoudig en duurt doorgaans slechts een minuut of twee. Het belangrijkste is om te zorgen dat u uw serverdomeinnaam of IP-adres bij de hand heeft!

1. Klik op de + knop in het menu {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}. 
2. Klik in het pop-upvenster *Kies een controleregel type* eerst op het controleregeltype *Ping* of *Connect* en klik dan op de knop {{< AppElement type="button" >}} Kiezen {{< /AppElement >}}.  
   De nieuwe controleregel is gecreëerd en u bevindt zich in het configuratiescherm van de controleregel. 
3. Geef uw controleregel een **Naam**.  
4. Stel het **Controle-interval** in. Uw [controle-interval]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/check-interval-explained" lang="nl" >}}) is de tijd tussen het einde van de ene controle en het begin van de volgende. 
5. Voer in het gedeelte *Details* bij **Netwerkadres** de domeinnaam of het IP-adres in. 
6.  Als u tevreden bent met de configuratie van uw nieuwe controleregel, klikt u op de knop {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}}. U heeft nu uw nieuwe Externe server-controleregel toegevoegd!  
      
    {{< callout >}}**Opmerking**: U kunt ook andere [controleregelinstellingen]({{< ref path="support/kb/synthetic-monitoring/monitor-settings" lang="nl" >}}) verkennen in de tabbladen boven aan het scherm Controleregel toevoegen.{{< /callout >}}

