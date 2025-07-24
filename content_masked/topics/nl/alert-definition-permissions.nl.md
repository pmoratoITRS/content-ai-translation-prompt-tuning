{
  "hero": {
    "title": "Gebruikersrechten voor alertdefinities"
  },
  "title": "Gebruikersrechten voor alertdefinities",
  "summary": "",
  "url": "[URL_BASE_TOPICS]alerting/gebruikersrechten-voor-alertdefinities",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Alertdefinities in Uptrends worden gebruikt om te definiëren wanneer alerts worden gegenereerd bij welk escalatieniveau en welke berichten via integraties naar operators of systemen worden gestuurd. De alertdefinities zijn cruciaal voor uw monitoring en alerting, daarom wilt u bepalen wie ze kan wijzigen. Met gebruikersrechten voor alertdefinities kunt u precies dat doen.

De gebruikersrechten worden op twee plaatsen ingesteld; zo wordt het gebruikersrecht **Alertdefinitie wijzigen** ingesteld in een alertdefinitie en het gebruikersrecht **Alertdefinitie toevoegen** wordt ingesteld voor een operator of operatorgroep. Zo werkt het gebruikersrechtensysteem van Uptrends – sommige gebruikersrechten worden ingesteld voor een item (zoals een controleregel of een alertdefinitie) en sommige voor operators of operatorgroepen. 

In dit artikel worden de gebruikersrechten die in een alertdefinitie worden ingesteld beschreven. Meer informatie over het gebruikersrecht **Alertdefinitie toevoegen** vindt u in het Knowledge Base-artikel [Gebruikersrechten]([LINK_URL_1]) die gerelateerd zijn aan operators.

## Wie kan gebruikersrechten beheren?

De gebruikersrechten voor alertdefinities kunnen door administrators in het algemeen worden ingesteld en gewijzigd.
Daarnaast kan een operator met zowel het gebruikersrecht **Alertdefinitie toevoegen** (ingesteld voor een operator of operatorgroep) als **Alertdefinitie wijzigen** (ingesteld in een alertdefinitie) ook de gebruikersrechten van die specifieke definitie beheren. 

## Types gebruikersrechten

### Alertdefinitie wijzigen

Dit gebruikersrecht geeft de operator of operatorgroep het recht om een alertdefinitie te wijzigen.

Er moet met een aantal zaken rekening worden gehouden:

- De operator kan de alertdefinitie wijzigen en er controleregels en controleregelgroepen aan toevoegen of eruit verwijderen. Dit geldt voor alle controleregels die de operator kan bekijken zoals ingesteld in de [gebruikersrechten voor controleregels]([LINK_URL_2]) voor die operator. Als de operator niet het recht heeft een bepaalde controleregel(groep) te bekijken, kan hij deze niet selecteren in de alertdefinitie.

- De operator kan de alertdefinitie wijzigen en operators of operatorgroepen toevoegen/verwijderen. Dit werkt alleen voor operators of operatorgroepen waarvoor de operator die de wijzigingen aanbrengt weergaverechten heeft. 

- Het is mogelijk dat andere operators controleregels of controleregelgroepen toevoegen die u niet kunt zien, omdat u geen weergaverecht heeft. Hetzelfde geldt voor operators of operatorgroepen. Als er verborgen items aan de alertdefinitie zijn gekoppeld, wordt hierover een notitie weergegeven.

- Het gebruikersrecht Alertdefinitie wijzigen omvat het recht om de definitie te verwijderen. Dit werkt alleen als er geen items (controleregels/controleregelgroepen of operators/operatorgroepen) aan de definitie zijn gekoppeld die voor u niet zichtbaar zijn vanwege het ontbreken van weergaverechten.

## Gebruikersrechten beheren

De gebruikersrechten voor alertdefinities kunnen worden ingesteld vanuit de alertdefinitie of vanuit een operatorgroep. Elke wijziging die op de ene plaats wordt aangebracht, wordt weerspiegeld in de andere.
### Gebruikersrechten instellen via operatorgroepen

1. Ga naar [SHORTCODE_1] Accountinstellingen > Operators, groepen (en deelaccounts) [SHORTCODE_2].
2. Klik op [SHORTCODE_3] Alle operatorgroepen bekijken [SHORTCODE_4] om naar het overzicht van operatorgroepen voor uw account te gaan.
3. Selecteer de groep waarvoor u gebruikersrechten wilt toevoegen en open het tabblad [SHORTCODE_5] Gebruikersrechten  [SHORTCODE_6].
   ![screenshot tabblad gebruikersrechten operatorgroep]([LINK_URL_3])
4. Voeg in het gedeelte **Alertdefinitie gebruikersrechten** een alertdefinitie toe door die te kiezen in de vervolgkeuzelijst. Om een alertdefinitie uit de operatorgroep te verwijderen klikt u op de x rechts naast de naam van de definitie.
5. Klik op de knop [SHORTCODE_7] Opslaan [SHORTCODE_8] om de wijzigingen op te slaan.

### Gebruikersrechten instellen of wijzigen binnen de alertdefinitie

1. Ga naar [SHORTCODE_9] Alerting > Alertdefinities [SHORTCODE_10].
2. Klik in de lijst met alertdefinities op de definitie die u wilt wijzigen.
3. Open het tabblad [SHORTCODE_11] Gebruikersrechten [SHORTCODE_12].
4. Klik op de knop [SHORTCODE_13] Recht toevoegen [SHORTCODE_14].
5. Kies in het pop-upvenster de operatorgroep en het recht en klik dan op de knop [SHORTCODE_15] Toevoegen [SHORTCODE_16].
6. Om een recht te verwijderen selecteert u [SHORTCODE_17] Verwijderen [SHORTCODE_18] in de lijst **Gebruikersrechten**.
7. Klik op [SHORTCODE_19] Opslaan [SHORTCODE_20] om uw zojuist aangebrachte wijzigingen op te slaan.