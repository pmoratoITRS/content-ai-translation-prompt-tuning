{
  "hero": {
    "title": "DNS-overzicht"
  },
  "title": "DNS-overzicht",
  "summary": "Ontdek waarom u een DNS-controleregel gebruikt en hoe u die instelt.",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/dns/dns-overzicht",
  "translationKey": "https://www.uptrends.com/support/kb/dns/dns-overview",
  "sectionlist": false
}

Het monitoren van uw DNS is een uitstekende manier om te verzekeren dat uw gebruikers uw website en services gemakkelijk, snel en veilig kunnen bereiken.

Hoewel we in ons artikel [Een controleregel toevoegen]({{< ref path="support/kb/basics/adding-monitors" lang="nl" >}}) hebben uitgelegd hoe u een controleregel toevoegt, vindt u hier meer specifieke informatie over het configureren van een DNS-controleregel.

## Waarvoor gebruikt u een DNS-controleregel?

Met deze controle kunt u verschillende queries uitvoeren op een DNS-naamserver. Het meest voor de hand liggende om te controleren is of uw domeinnaam (www\.uwonderneming.nl) nog steeds verwijst naar het IP-adres van uw webserver. De naamserver van uw provider is de primaire bron van deze informatie. Door deze DNS-query rechtstreeks te monitoren, detecteren wij DNS-problemen, zelfs voordat uw website niet meer beschikbaar is voor uw bezoekers en klanten.

Met Uptrends' DNS-controleregel kunt u uitgebreide DNS-gezondheidschecks uitvoeren: verifieer uw websitedomeinnamen (A en CNAME records), mailserver domeinnaam mappings (MX records), DNS zones (NS records), machtigingsgegevens over DNS-zones (SOA records) en andere DNS-informatie uit TXT records (met inbegrip van SPF-informatie voor e-mail-authenticatie).

## Een DNS-controleregel instellen

1. Navigeer naar het menu {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}} en klik rechts op de + knop.
2. Stel uw controleregeltype in op **DNS**.
3. Voer de **Naam** in en het **controle-interval** dat het meest geschikt is voor uw DNS-monitoring behoeften.
4. Selecteer uw **IP-versie**. Als u test met IPv6, heeft u de mogelijkheid om alleen die controlestations te gebruiken die native IPV6 hebben; indien niet aangevinkt, zullen controles worden gedaan vanaf alle geselecteerde controlestations met native IPV6 en met IPV6-emulatie op IPV4-controlestations.
5. Vul de gegevens van de DNS-server in door de *domeinnaam* of het *IP-adres* te specificeren van de **DNS-server** die u wilt testen, bijvoorbeeld `n1s.uwprovider.nl`.
6. Het is belangrijk om de **Poort** voor uw DNS-server te controleren, om te bevestigen of de standaardwaarde van 53 van toepassing is.
7. Selecteer uw type **DNS query**. Uptrends ondersteunt *A Record*, *AAAA Record*, *CNAME Record*, *MX Record*, *NS Record*, *SOA Record*, *TXT Record* of *Root Server*.
8. Specificeer in het veld **Testwaarde** de domeinnaam die u wilt testen, bijvoorbeeld `www.uwdomein.nl`.
9. Vul het **Verwachte resultaat** in in het veld met die naam.
    Bijvoorbeeld: Voor het testen van de domeinnaam van uw website (een A Record query) vult u het IP-adres van uw domeinnaam in. De Uptrends-service zal dan verifiëren dat de response van de DNS-query overeenkomt met het IP-adres.

    {{< callout >}}**Tip**: Als uw domeinnaam meerdere IP-adressen heeft, kunt u een reguliere expressie gebruiken om meerdere waarden te matchen
    Voorbeeld: 1.2.3.4|5.6.7.8{{< /callout >}}
10.  Klik op de knop {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}} wanneer u klaar bent.

