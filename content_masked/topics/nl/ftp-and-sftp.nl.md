{
  "hero": {
    "title": "FTP en SFTP"
  },
  "title": "FTP en SFTP",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/uptime-monitoring/ftp-en-sftp",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "tableofcontents": true
}

Uw klanten vertrouwen op de beschikbaarheid van uw FTP (File Transfer Protocol) en SFTP (Secure File Transfer Protocol) om bestanden van uw server te downloaden naar hun computer. De controleregeltypes FTP en SFTP controleren de beschikbaarheid van uw servers en rapporteren eventuele downtime. De beschikbare opties hangen af van welk controleregeltype u kiest: FTP of SFTP.

## Welke acties kan ik uitvoeren met een FTP-controleregel?

De FTP-controleregel controleert:

-   **Paginabeschikbaarheid en snelheid**   
    Door de selectievakjes **Laadlimiet**  te selecteren op het tabblad [SHORTCODE_3]Foutcondities[SHORTCODE_4] kunt u verifiëren dat uw FTP-server snel reageert op requests van gebruikers.
-   **Basisserververificatie**  
    Verifieer dat uw authenticatieproces correct werkt door een **Gebruikersnaam** en **Wachtwoord** in te vullen op het tabblad [SHORTCODE_5]Extra[SHORTCODE_6].

## Welke acties kan ik uitvoeren met een SFTP-controleregel?

De SFTP-controleregel gebruikt een versleutelde verbinding bij het uitvoeren van de bestandsoverdracht. De SFTP-controleregel biedt een uitgebreidere reeks testopties dan de FTP-controleregel. De SFTP-controleregel kan verschillende acties uitvoeren. Op het tabblad Extra kunt u kiezen uit:

-   **Verbinden met SFTP server met een gebruikersnaam en wachtwoord**  
    De controleregel verbindt met de SFTP server met de gebruikersnaam en het wachtwoord die u specificeert. De controleregel zal een fout rapporteren wanneer de server niet beschikbaar is of als er een fout optreedt tijdens het inloggen.
-   **Verbinden en controleren dat een bestand bestaat op de SFTP server**  
    In deze modus verbindt de controleregel eerst met de SFTP server, vervolgens controleert de controleregel of een specifiek bestand bestaat op SFTP server.
-   **Verbinden en controleren dat een bestand niet bestaat op de SFTP server**   
    Soms wilt u misschien monitoren of een specifiek bestand niet bestaat op de SFTP server. U kunt deze actie selecteren bij de SFTP-controleregeleigenschappen.
-   **Verbinden en bestand downloaden**   
    In deze modus verbindt de controleregel eerst met de SFTP server, verifieert of een specifiek bestand bestaat op de server en downloadt dan het bestand. De maximale bestandsgrootte voor downloaden is 1 MB.

## Hoe stel ik een (S)FTP-controleregel in?

SFTP (Secure File Transfer Protocol) is het standaardprotocol voor bestandsoverdracht. SFTP wordt gebruikt voor het veilig overbrengen van bestanden tussen twee computers. Met Uptrends kunt u uw SFTP-server monitoren op verbeterde beveiliging en performance.

Volg deze stappen om een (S)FTP-controleregel in te stellen:

1. Klik op de + knop in het menu [SHORTCODE_7] Monitoring > Controleregels beheren [SHORTCODE_8]. 
2. Klik in het pop-upvenster *Kies een controleregel type* eerst op het controleregeltype *FTP* of *SFTP* en klik dan op de knop [SHORTCODE_9] Kiezen [SHORTCODE_10].  
   De nieuwe controleregel is gecreëerd en u bevindt zich in het configuratiescherm van de controleregel. 
3. Geef uw controleregel een **Naam**.  
4. Stel het **Controle-interval** in. Uw [controle-interval]([LINK_URL_1]) is de tijd tussen het einde van de ene controle en het begin van de volgende.
5. Voer de domeinnaam of het IP-adres van uw FTP-server in het veld *Netwerkadres* in.  
6. Als de poort van uw FTP-server anders is dan de standaardpoort, wijzigt u deze in de juiste poort. 
7. Open het tabblad [SHORTCODE_11] Extra [SHORTCODE_12].
8. Kies een optie in het vak **Actie** (ga voor details over de beschikbare acties naar de pagina [overzicht]([LINK_URL_2]).
9. Geef de bestandsnaam of het relevante pad op in het vak **Bestandspad** als u kiest een bestand te downloaden of te verifiëren.
10. Specificeer de **Gebruikersnaam** en het **Wachtwoord** als u authenticatie gebruikt.
11. Als u tevreden bent met de configuratie van uw nieuwe controleregel, klikt u op de knop [SHORTCODE_13] Opslaan [SHORTCODE_14]. 
      
[SHORTCODE_1]**Opmerking**: U kunt ook andere [controleregelinstellingen]([LINK_URL_3]) verkennen in de tabbladen boven aan het configuratiescherm van de controleregel.[SHORTCODE_2]

