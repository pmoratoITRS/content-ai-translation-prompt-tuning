{
  "hero": {
    "title": "Databasecontroleregels"
  },
  "title": "Databasecontroleregels",
  "summary": "Bewaak uw MySQL en SQL Server-database-servers.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/databasecontroleregels",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Tenzij u een statische brochurewebsite hebt, is uw website of webservice afhankelijk van een database om content op te halen, gebruikers te beheren of orders te verwerken. Weten wat de responstijden van uw database zijn kan een catastrofe helpen voorkomen. Met Uptrends' controleregels voor database servers kunt u altijd op de hoogte zijn van problemen met uw database.

Uptrends gebruikt zijn {{% Features/Variable variable="CheckpointCount" %}} controlestations om uw database server extern te monitoren.

[SHORTCODE_1]
**Opmerking:** Indien uw database niet toegankelijk is via internet kunt u dit type controleregel niet gebruiken. Echter, u kunt servers achter uw firewall monitoren met [Uptrends Infra]([LINK_URL_1]).
[SHORTCODE_2]

## Hoe werkt het?

Met Uptrends' database monitoring kunt u Microsoft SQL Server of MySQL monitoren. De controlestations van Uptrends zullena proberen een verbinding te maken met het IP-adres en de database die u specificeert op het tabblad [SHORTCODE_5]Extra[SHORTCODE_6] , en als u inloggegevens invult zal het controlestation proberen in te loggen. Behalve bij het overschrijden van de responstijden die u specificeert in het tabblad [SHORTCODE_7]Foutcondities[SHORTCODE_8] , zal Uptrends een alert triggeren bij mislukte of verbroken verbindingen.

[SHORTCODE_3]
**Opmerking**: Wilt u meer weten over beveiliging en het delen van uw inloggegevens voor uw database? Lees dan meer over hoe Uptrends uw inloggegevens beveiligt: [Encryptie en de beveiliging van uw website]([LINK_URL_2]).
[SHORTCODE_4]

Een database-controleregeltype stuurt u alerts op basis van responstijd en verbindingsproblemen. U zult zien dat het instellen van een databaseservercontroleregel lijkt op het instellen van een controleregeltype HTTPS met slechts enkele speciale velden. Meer informatie over het instellen van controleregels en foutcondities vindt u in de [knowledge base]([LINK_URL_3]). Voor een databasecontroleregel moet u het volgende weten:

-   Naam van de database,
-   URL of IP van de database, en optioneel
-   Inloggegevens van de database.

## De controleregel instellen

Een databasecontroleregel instellen:

1.  Klik op [SHORTCODE_9]\+ Controleregel toevoegen[SHORTCODE_10] bij de **Monitoring**-opties op het [SHORTCODE_11]Hoofd[SHORTCODE_12]-menu.
2.  Selecteer **Microsoft SQL Server** of **MySQL** onder **Database Servers** in het vak **Type**.
3.  Typ de domeinnaam of het IP-adres van de database server in het vak **Netwerkadres**.
4.  Vul de andere velden in op het tabblad [SHORTCODE_13]Algemeen[SHORTCODE_14].
5.  Stel uw verwachte responstijden in op het tabblad [SHORTCODE_15]Foutcondities[SHORTCODE_16].
6.  Klik op het tabblad [SHORTCODE_17]Extra[SHORTCODE_18].
7.  Vul indien nodig een **Gebruikersnaam** en **Wachtwoord** in.
8.  Vul de **Databasenaam** in.
9.  Kies uw controlestations op het tabblad [SHORTCODE_19]Controlestations[SHORTCODE_20].
10.  Klik op [SHORTCODE_21]Opslaan[SHORTCODE_22].