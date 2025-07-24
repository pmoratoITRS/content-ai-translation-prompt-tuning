{
  "hero": {
    "title": "Encryptie en de beveiliging van uw website"
  },
  "title": "Encryptie en de beveiliging van uw website",
  "summary": "Uptrends gebruikt geavanceerde coderingsstandaarden om de gebruikersnamen en wachtwoorden van uw sites te beschermen. ",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/encryptie-en-de-beveiliging-van-uw-website",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

De beveiliging van uw website is belangrijk, en Uptrends vat beveiliging niet licht op. We gaan zorgvuldig om met de door u verstrekte gebruikersnamen en wachtwoorden. We versleutelen gevoelige gegevens meteen, voordat we uw gegevens in onze database opslaan. Binnen onze organisatie houden we strakke controle op de toegang tot de versleutelde versie van deze gegevens.

## Hoe we uw data beschermen

Ons systeem gebruikt het [Rijndael]([LINK_URL_1])-algoritme (ook bekend als **Advanced Encryption Standard**) voor het versleutelen van gevoelige gegevens. Hierbij gebruiken we [PBKDF2]([LINK_URL_2]) (volgens RFC 2898) voor het genereren van de encryptiesleutel die we nodig hebben om de versleuteling uit te voeren. We gebruiken 256-bit, cryptografisch veilige, random waarden voor het genereren van de salt- en IV-waarden die nodig zijn voor het genereren van de encryptiesleutel en het uitvoeren van de encryptie. Tot slot vindt alle communicatie tussen Uptrends’ subsystemen plaats via versleutelde en geverifieerde verbindingen.

## Wat u kunt doen

Naast encryptie en toegangsbeleid van onze kant, raden we onze klanten aan toe te zien op de beveiliging aan hun kant.

### Beperk toegangsrechten

Beperk toegangsrechten van de inloggegevens die u ons verstrekt. Idealiter hebben de inlogaccounts die gespecificeerd zijn in transacties en andere controleregeltypes minimale toegangsrechten. Geef deze accounts precies genoeg privileges om de vereiste controles uit te voeren.

### Gebruik afzonderlijke inlogaccounts

We adviseren u ook om binnen uw systeem afzonderlijke inlogaccounts te maken waarmee alleen monitoringtaken kunnen worden uitgevoerd. Deze accounts kunt u opnemen in de whitelist met betrekking tot de locaties van ([IP-adressen]([LINK_URL_3]), d.w.z. de adressen van Uptrends' controlestationservers) waarvoor u die toegangsrechten heeft toegekend.

### Houd inloggedrag in de gaten

Als uw systeem logging gebruikt om het gedrag van elke ingelogde account te volgen, is het raadzaam om dat gedrag te monitoren. Houd dit gedrag in de gaten zodat u zeker weet dat de testaccounts niets doen wat u niet wilt.

### Update wachtwoorden op tijd

Tot slot raden we aan de wachtwoorden tijdig bij te werken in uw controleregelinstellingen en transactiemonitoringscripts (zie [Transactiewaarden wijzigen]([LINK_URL_4])) als u de beveiliging zo heeft ingesteld dat wachtwoorden verlopen. Als u uw wachtwoorden up-to-date houdt, voorkomt u dat uw controleregels onnodige errors rapporteren.

## Partners in beveiliging

Met onze voortdurende toewijding aan beveiliging en uw actieve deelname bij het toepassen van deze beveiligingsmaatregelen, werken we op de best mogelijke manier samen om kwetsbaarheid tot een minimum te beperken.
