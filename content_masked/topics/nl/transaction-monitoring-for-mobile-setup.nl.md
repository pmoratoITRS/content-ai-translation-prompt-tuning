{
  "hero": {
    "title": "Transactiemonitoring voor mobiel instellen"
  },
  "title": "Transactiemonitoring voor mobiel instellen",
  "summary": "Met Uptrends' Transaction recorder kunt u ook transacties voor uw mobiele site testen. Hier leest u hoe u dit doet.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/transactiemonitoring-voor-mobiel-instellen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Mobiel is overal en het testen van transacties voor desktop alleen garandeert mogelijk niet dat uw transacties correct werken voor uw mobiele gebruikers. Met de transactierecorder van Uptrends kunt u scripts instellen voor het monitoren van de mobiele versie of responsive design-versie van uw website door de viewport van een apparaat te simuleren. U simuleert de viewport van het apparaat door de modus mobiele simulatie in Chrome Developer Tools te gebruiken. Dit doet u als volgt.

## Gebruik de Chrome Device Mode bij het opnemen van een transactie

1.  [Start de Uptrends transaction recorder (Chrome extension)]([LINK_URL_1]) zoals u dat anders ook doet. Er wordt een nieuw browservenster geopend.
2.  Druk op de toets F12 om het Chrome Hulpprogramma’s voor ontwikkelaars te openen.
3.  Zoek het pictogram Apparaatwerkbalk schakelen en klik erop om naar de modus apparaatsimulatie te gaan.  
    ![screenshot transaction recorder apparaatwerkbalk schakelen]([LINK_URL_2])  
4.  Pas zo nodig de apparaatinstellingen aan.
5.  Navigeer naar uw mobiele site.
6.  Klik door uw transactie.
7.  Upload de transactie naar uw account om zelf te scripten en te testen, of upload het script om Support het scripten voor u te laten doen.
8.  Pas de mobiele-monitoringinstellingen in uw nieuwe transactiecontroleregel aan.

Lees meer over [het gebruik van Device Mode]([LINK_URL_3]) in uw Chrome browser.

## Pas de controleregelinstellingen voor mobiele monitoring aan

Nu u uw transactie heeft opgenomen met de Device Mode van Chrome DevTools, moet u de mobiele configuratie in uw controleregelinstellingen voltooien.

1. Ga naar [SHORTCODE_1] Transacties > Transacties beheren [SHORTCODE_2] en open de nieuwe transactiecontroleregel.
2. Schakel naar het tabblad [SHORTCODE_3] Extra [SHORTCODE_4].
3. Pas in het gedeelte *Browser* bij *Device / scherm* uw **Schermgrootte** aan en kies een **User agent** (met de optie om een aangepaste user agent te kiezen), of selecteer **Simuleren van mobiele devices** en kies een van de populaire apparaten.
  ![screenshot tabblad Extra van transactiecontroleregel]([LINK_URL_4])
4. Stel **Bandbreedte begrenzen** in als u de ervaring van de eindgebruiker volledig wilt simuleren. Lees meer over [bandbreedte begrenzen]([LINK_URL_5]) in de Knowledge Base.
5. Klik op de knop [SHORTCODE_5] Opslaan [SHORTCODE_6] om uw wijzigingen op te slaan.
