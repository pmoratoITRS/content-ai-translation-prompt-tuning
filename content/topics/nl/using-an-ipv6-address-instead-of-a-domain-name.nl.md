{
  "hero": {
    "title": "Een IPv6-adres gebruiken in plaats van een domeinnaam"
  },
  "title": "Een IPv6-adres gebruiken in plaats van een domeinnaam",
  "summary": "Als u een IPv6-adres moet gebruiken in plaats van een domeinnaam, moet u het juiste formaat gebruiken om Uptrends de controles correct te laten uitvoeren zonder fouten te genereren.",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/een-ipv6-adres-gebruiken-in-plaats-van-een-domeinnaam",
  "translationKey": "https://www.uptrends.com/support/kb/monitor-settings/using-an-ipv6-address-instead-of-a-domain-name"
}

U kunt een IPv6-adres gebruiken in plaats van de domeinnaam in het URL-veld van uw controleregel als u daarvoor kiest, maar onthoud dat u het adres tussen rechte haakjes moet zetten en IPv6 moet selecteren bij de IP-versie van uw controleregel. Als u IPv6 niet aangeeft, genereert uw controleregel fouten wanneer deze wordt getest vanaf controlestations die IPv6 niet ondersteunen.

Bijvoorbeeld:

 

`http://[2a01:5cc0:1:2::4]`

![](/img/content/e40e8c6e-6235-4d19-8a5e-9012b1c3259e.png)
