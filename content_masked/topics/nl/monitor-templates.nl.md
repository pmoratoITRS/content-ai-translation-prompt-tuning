{
  "hero": {
    "title": "Controleregelsjablonen"
  },
  "title": "Controleregelsjablonen",
  "summary": "Met een controleregelsjabloon kunt u bepaalde instellingen op meerdere controleregels tegelijk toepassen.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregelbeheer/controleregelsjablonen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Met Uptrends is het nog nooit zo eenvoudig geweest om de uptime of performancestatus van een website, server of webservice te monitoren. Maar wat doet u als u een reeks services wilt monitoren en deze snel wilt opzetten? Dan gebruikt u **Controleregelsjablonen**.

Een controleregelsjabloon is een tool die kan worden gebruikt voor het toevoegen van bepaalde instellingen, zoals *foutcondities*, *controlestations* en *onderhoudsperiodes* aan groepen controleregels. U kunt ze beschouwen als een manier om controleregelconfiguraties te dupliceren, maar dan supersnel.

## Waarom zijn controleregelsjablonen handig?

Als u een reeks controleregels maakt die dezelfde regels volgen voor foutcondities, controlestations of onderhoudsperiodes, kan het handmatig configureren veel moeite en tijd kosten. Door een controleregelsjabloon te gebruiken, kunt u met minimale moeite en tijd specifieke instellingen toevoegen aan controleregels, en verdergaan met waar u het beste in bent.

[SHORTCODE_1] **Opmerking**: U moet een beheerder zijn of het [gebruikersrecht Beheer controleregelsjablonen]([LINK_URL_1]) hebben om sjablonen te kunnen maken, bewerken en toepassen. [SHORTCODE_2]

## Hoe creëer ik een controleregelsjabloon?

1.  Ga naar [SHORTCODE_5]Accountinstellingen > Controleregelsjablonen[SHORTCODE_6]. 
2.  Klik in de rechter bovenhoek van het scherm op de knop [SHORTCODE_7]Sjabloon toevoegen[SHORTCODE_8].   
3. Nu kunt u uw sjablooninstellingen aanpassen:
- Voer een naam in voor uw controleregelsjabloon.
- Op het tabblad Instellingen voor controleregels heeft u een optie om [laadtijdlimieten]([LINK_URL_2]) in te voeren om een fout te genereren als de respons van de server langzamer is dan deze duur.
Verder kunt u een [user agent]([LINK_URL_3]) selecteren om het browsertype en het besturingssysteem van de gebruiker te identificeren dat naar de server wordt gestuurd tijdens HTTPS requests. De user agent is standaard ingesteld op *Ongewijzigd laten*.
- Gebruik de selectievakjes op het tabblad [controlestations]([LINK_URL_4]) om de locaties te bepalen van waaruit u wilt monitoren. 
- U kunt ook [Onderhoudsperiodes]([LINK_URL_5]) toevoegen en de herhaling ervan instellen.

[SHORTCODE_3] **Opmerking**: Als u een controleregelsjabloon toepast, passen we alleen de instellingen toe waarin u wijzigingen heeft aangebracht toen de sjabloon werd gemaakt. Als u bijvoorbeeld een sjabloon wilt gebruiken om alleen een onderhoudsperiode toe te passen, zorg er dan voor dat u alleen die instelling aanpast bij het creëren van de controleregelsjabloon. Hetzelfde geldt voor het toepassen van een bepaalde controlestationselectie of foutconditie. [SHORTCODE_4]

4.  Als u klaar bent, klikt u op de groene knop [SHORTCODE_9]Opslaan[SHORTCODE_10].

U kunt nu uw opgeslagen controleregelsjablonen toepassen op elke bestaande controleregel, hierbij heeft u twee opties. De eerste optie is om één controleregel bij te werken of bulkupdates uit te voeren voor meerdere controleregels via het menu [SHORTCODE_11]Controleregelsjablonen[SHORTCODE_12]. Met de tweede optie kunt u een sjabloon van uw huidige controleregel rechtstreeks toepassen via het scherm [SHORTCODE_13]controleregel-editor[SHORTCODE_14]. Zie de onderstaande stapsgewijze instructies voor meer informatie over het toepassen van controleregelsjablonen.

## Een controleregelsjabloon toepassen
Om een sjabloon op één controleregel toe te passen of om bulkupdates op meerdere controleregels tegelijk uit te voeren:

1. Ga naar [SHORTCODE_15]Accountinstellingen > Controleregelsjablonen[SHORTCODE_16]. 
2. Zoek de juiste controleregelsjabloon in de lijst en klik op **Toepassen**. 
3. Selecteer de individuele controleregel(s) of controleregelgroep(en) waarop u de sjabloon wilt toepassen.
4. Klik op de knop [SHORTCODE_17] Toepassen [SHORTCODE_18].

Hiermee worden de opgegeven instellingen toegepast op de geselecteerde controleregel(s)/controleregelgroep(en).

## Een controleregelsjabloon toepassen met het scherm controleregel-editor
Om een sjabloon rechtstreeks vanaf uw huidige controleregel toe te passen:

1. Ga naar [SHORTCODE_19]Monitoring > Controleregels beheren[SHORTCODE_20].
2. Klik op de controleregelnaam waarop u de sjabloon wilt toepassen.
3. Klik onder aan de pagina controleregel-editor op de knop [SHORTCODE_21] Sjabloon toepassen [SHORTCODE_22].
4. In het venster Sjabloon toepassen selecteert u in het menu welke controleregelsjabloon u wilt toepassen. Alle beschikbare secties van uw gekozen sjabloon worden weergegeven. U kunt de selectievakjes gebruiken om afzonderlijke secties toe te passen of over te slaan. Uitgeschakelde selectievakjes geven aan dat de sjabloon geen instellingen voor die sectie bevat.

![Een screenshot met een pop-up over hoe je controleregelsjablonen toepast in het venster controleregel-editor]([LINK_URL_6])

5. Klik op de knop [SHORTCODE_23] Toepassen [SHORTCODE_24] om de wijzigingen in uw huidige controleregel te bevestigen.
