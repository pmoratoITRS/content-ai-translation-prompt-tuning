{
  "title": "Van klassieke naar nieuwe gebruikersinterface",
  "summary": "Hoe verhoudt de nieuwe gebruikersinterface zich tot de klassieke?",
  "url": "/support/kb/basisprincipes/gebruikersinterface/van-klassiek-nieuwe-ui",
  "translationKey": "https://www.uptrends.com/support/kb/user-interface/from-classic-to-new-ui",
  "draft": false
}

{{< callout >}} **Opmerking**: Het nieuwe menu is de standaard vanaf 10 mei 2023 en alle accounts zijn ingesteld om het nieuwe menu te gebruiken. U kunt niet terugschakelen naar het klassieke menu. {{< /callout >}}

De gebruikersinterface (UI) van de Uptrends-app bestaat al een aantal jaren en het was tijd voor verandering. 

Een van de doelen van de nieuwe gebruikersinterface is de integratie van Uptrends' producten Synthetics, RUM en Infra binnen dezelfde Uptrends-app. Dit wordt duidelijk in het nieuwe zijmenu en het nieuwe dashboard "360-graden-overzicht", dat informatie van de verschillende producten toont. Bovendien kreeg de gebruikersinterface een frissere uitstraling en zijn hubs toegevoegd die gerelateerde informatie op één plek presenteren. 

Dit artikel helpt u om uw weg te vinden in de nieuwe gebruikersinterface van de Uptrends-app. Veel dingen zijn veranderd, maar hebben mogelijk geen invloed op de manier waarop u werkt. Zo zijn bijvoorbeeld de dashboards gerestyled voor een frisse uitstraling. Dit ziet er anders uit, maar toch vindt u de dingen die u nodig heeft op de bekende plekken.

Het menu is een ander verhaal. Dat is helemaal herzien, de posities van menu's en zelfs sommige namen zijn veranderd. Uptrends raadt aan de vergelijkingstabel [Klassiek versus nieuw menu](#classic-vs-new-menu) en het gedeelte [Menu](#menu) te bekijken voor meer informatie over de wijzigingen.

## Klassiek versus nieuw menu {id="classic-vs-new-menu"}

Onderstaande tabel laat het verschil zien tussen het klassieke menu en het nieuwe menu. 

{{< callout >}}**Tip:** Als u niet weet waar u iets in het nieuwe menu kunt vinden, maar u de menunaam kent in het klassieke menu, kunt u altijd de zoekfunctie in het zijmenu gebruiken om te zoeken naar de nieuwe menulocatie.{{< /callout >}}

| Klassiek menu                                     | Nieuw zijmenu                                                               |
|--------------------------------------------------|--------------------------------------------------------------------------------|
| Controleregels > Controleregel log                           | Monitoring > Controleregel log                                      |
| Controleregels > Controleregelstatus                        | Monitoring > Statusdetails                                                    |
| Controleregels > Controleregels                              | Monitoring > Controleregels beheren                                                     |
| Controleregels > Controleregelgroepen                        | Accountinstellingen > Controleregelgroepen                                        |
| Controleregels > RUM-websites                          | RUM > Echte gebruikers > RUM websites                                                |
| Controleregels > Controleregelsjablonen                     | Accountinstellingen > Controleregelsjablonen                                     |
| Controleregels > Onderhoudsperiodes                   | Accountinstellingen > Onderhoudsperiodes                                   |
| Dashboards, diverse dashboards                   | Dashboards > Alles bekijken                                                    |
| Dashboards > Dashboard toevoegen                       | Dashboards > Nieuw dashboard toevoegen  OF Dashboards > Alles bekijken >  Nieuw dashboard toevoegen|
| Dashboards > Dashboards beheren                   | Dashboards > Alles bekijken                                                         |
| Dashboards > Geplande rapporten beheren            | Accountinstellingen > Geplande rapporten                                     |
| Dashboards > Publieke statuspagina’s beheren          | Accountinstellingen  > Publieke statuspagina's                                   |
| Alerts > Alertstatus                            | Alerting > Huidige alertstatus                                                |
| Alerts > Alertlog                               | Alerting > Alerthistorie                                                       |
| Alerts > Alertdefinities                       | Alerting > Alertdefinities                                                   |
| Alerts > Integraties                            | Alerting > Integraties                                                        |
| SLA > SLA-overzicht                               | Dashboards > Synthetics > SLA overzicht                        |
| SLA > SLA-definities                            | Accountinstellingen > SLA-definities                                       |
| Account > alle menu's                              | Accountinstellingen                                                         |
| Apps & Extra's > Tools                            | Tools & apps > Diagnose-tools           |
| Apps & Extra's > Transaction recorder             | Tools & apps > Transaction recorder OF Synthetics > Transacties > Transaction recorder downloaden                      |
| Apps & Extra's > Mobiele apps                      | Tools & apps > Mobiele apps                                           |
| Support > alle menu's                              | Support                                                                        |
| Onbevestigde/bevestigde foutenteller (rechtsboven)  | Labels (geel of rood met teller), rechts van Synthetics, RUM, en Infra in het menu           |
| Gebruikersaccount (naam), rechtsboven bij klassiek menu | Gebruikersaccount (naam), onder aan het zijmenu                                     |

## Wijzigingen in de gebruikersinterface

De volgende verbeteringen maken deel uit van de nieuwe gebruikersinterface:

- Zijmenu, bekijk het gedeelte [Menu](#menu) voor de details.
- Hubs, een nieuwe manier om u in een notendop informatie te geven over de feitelijke monitoringssituatie, wat achtergrondinformatie en koppelingen naar verdere informatie.
- Dashboardoverzicht ({{< AppElement type="menuitem" >}} Dashboards > Alles bekijken {{< /AppElement >}}), inclusief miniatuurweergaven, waarmee u door alle Synthetics-, Infra-, RUM- en 360-dashboards kunt bladeren en zoeken. 
- Optie om dashboards als favoriet te markeren door te klikken op de knop {{< AppElement type="menuitem" >}}Favoriet{{< /AppElement >}} (ster) in de rechterbovenhoek van het dashboard terwijl het dashboard zichtbaar is.
- Een Favorieten-sectie in het Dashboard-menu om snel toegang te krijgen tot dashboards die als favoriet zijn gemarkeerd. 
- Zoekoptie om door alle menu-items en veel Uptrends-items te zoeken.
- Speciale secties in het Synthetics-menu voor transactie-, browser-, API- en uptime-controleregels.
- Tandwielpictogrammen {{< AppElement type="iconProperties" >}}{{< /AppElement >}} van de dashboardtegels zijn gewijzigd in menupictogrammen met drie stippen {{< AppElement type="iconTileSettings" >}}{{< /AppElement >}}
- Feedbackoptie (in het menu Support) om snel feedback te sturen.

Bezoek de pagina [Gebruikersinterface]({{< ref path="support/kb/basics/user-interface" lang="nl" >}}) voor een gedetailleerde beschrijving van de onderdelen van de gebruikersinterface.

## Wijzigingen in het menu {id="menu"}

De volgende wijzigingen zijn doorgevoerd in het nieuwe menu:

- Terwijl het klassieke menu bovenaan staat, bevindt het nieuwe zich aan de zijkant. 
- De drie belangrijkste producten [Uptrends Synthetics]({{< ref path="products/synthetics/website-monitoring" lang="nl" >}}), [Uptrends Real User Monitoring]({{< ref path="products/real-user-monitoring" lang="nl" >}}) en [Uptrends Infra]({{< ref path="products/infra/server-monitoring" lang="nl" >}}) zijn toegankelijk in één menu.
- Binnen Synthetics zijn er speciale secties voor de belangrijkste controleregeltypes: Transacties, Browsergebaseerde controleregels (Full Page Checks), API-controleregels en Uptime-controleregels (HTTP(S), SSL, DNS, SMTP, Ping, etc.)
- U kunt het menu in- en uitvouwen, waardoor er meer (of minder) ruimte voor dashboards is. Optioneel kunt u het menu vastzetten.
- De favoriete dashboards verschijnen als snelkoppelingen in het menu {{< AppElement type="menuitem" >}}Dashboards{{< /AppElement >}}.   
- Een [zoekfunctie]({{< ref path="support/kb/basics/user-interface/search" lang="nl" >}}) voor menu-items en veel Uptrends-app-items is beschikbaar boven aan het zijmenu. 
- De groepering van menu-items en hun menunamen zijn gewijzigd. Bekijk de vergelijkingstabel [Klassiek versus nieuw menu](#classic-vs-new-menu). 

