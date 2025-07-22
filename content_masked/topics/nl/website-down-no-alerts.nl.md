{
  "hero": {
    "title": "Mijn website is uit de lucht maar ik ontvang geen alerts"
  },
  "title": "Mijn website is uit de lucht maar ik ontvang geen alerts",
  "summary": "Uw website is uit de lucht, maar u heeft geen alert ontvangen? U moet het volgende doen.",
  "url": "[URL_BASE_TOPICS]alerting/website-down-geen-alerts",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Dus uw website, server of webservice is uit de lucht, maar u heeft geen alert of bericht ontvangen. Wat is er aan de hand? Dit kan verschillende oorzaken hebben…

Bedenk dat er een heel proces achter alerting zit. Het begint met een controleregelcheck die een fout kan signaleren. Als de fout wordt bevestigd, kan deze een alert genereren en deze alert kan het versturen van een bericht (gedefinieerd in een integratie) in gang zetten. Wilt u hier meer over weten, lees dan verder in het KB-artikel [Overzicht alerting]([LINK_URL_1]). Het probleem kan dus in de alert- of in de berichtfase zitten.

Heeft u geen alert of bericht ontvangen, terwijl dat wel had gemoeten… bekijk dan onze boilerplate met tips voor probleemoplossing hieronder.

## Controleer uw controleregels

- **Is uw controleregel actief?**  
  Als een controleregel is gedeactiveerd, ontvangt u geen alerts aangezien deze dan niet actief wordt gemonitord.
- **Is uw alerting actief?**  
  De activeringsstatus van zowel controleregels als alerts is te vinden in het dashboard Controleregelstatus: 

  ![screenshot dashboard controleregelstatus]([LINK_URL_2])

- **Heeft u nog berichtcredits?**  
  Het versturen van telefoon- of SMS-berichten kost berichtcredits. Als al uw berichtcredits verbruikt zijn, ontvangt u dit soort berichten niet totdat u nieuwe berichtcredits koopt. Meer informatie vindt u in het artikel [SMS-verbruiksdetails]([LINK_URL_3]).
- **Is de fout opgetreden tijdens de onderhoudsperiode van de controleregel?**  
  Alerts worden niet verstuurd tijdens geconfigureerde [onderhoudsperiodes]([LINK_URL_4]) van een controleregel. U vindt de instelling op het tabblad [SHORTCODE_9]Onderhoudsperiode[SHORTCODE_10] van de controleregel.
- **Heeft u een inhoudcontrole opgenomen in uw foutcondities?**  
  Als u een controle doet op *Pagina-inhoudmatch*, moet een (deel van) de gecontroleerde inhoud exact overeenkomen met het woord of de zin die u controleert. 

## Controleer uw Alerthistorie

De Uptrends-app houdt een actieve log bij van alle alertingactiviteiten. De Alerthistorie is een van de belangrijkste tools om te controleren of er alerts zijn verstuurd. Is dit niet het geval, dan is dit de plek om aan probleemoplossing te werken.

Om te controleren of er alerts zijn gegenereerd en berichten zijn verstuurd doet u het volgende:  
Ga in de Uptrends-applicatie naar het menu-item [SHORTCODE_11] Alerting > Alerthistorie[SHORTCODE_12].   
U ziet nu een actieve log van alle alerts die zijn verstuurd, inclusief datum/tijd, escalatieniveau en instellingen voor herinneringen.

Klik op een vermelding in de Alerthistorie voor gedetailleerde informatie over die specifieke alert. Er verschijnt een venster Details van de alert met de tabbladen [SHORTCODE_13]Details[SHORTCODE_14] en [SHORTCODE_15]Berichten[SHORTCODE_16].

![screenshot dashboard Alerthistorie met checkdetail]([LINK_URL_5])

Er kunnen zich verschillende situaties voordoen:

- **Is er geen vermelding in de Alerthistorie?**  
  Controleer dan de instellingen in uw controleregel en controleer daarna de alertdefinities.
- **Is er wel een vermelding, maar werd er geen bericht verstuurd?**  
  In het tabblad Berichten wordt duidelijk weergegeven welke berichten zijn verzonden en naar wie.
- **Is er geen bericht verstuurd voor uw aangepaste integratie?**  
 Controleer het tabblad Berichten om de fout te vinden die werd ontvangen van de derde partij. In het voorbeeld hierboven, als Slack het bericht niet correct heeft ontvangen, wordt de vermelding Slack - “Slack to Master operator” rood gemarkeerd en de response van de Slack API (inclusief foutcodes en info) wordt weergegeven als u de vermelding openvouwt.

## Controleer de operatorinstellingen

[SHORTCODE_1]
**Opmerking**: U moet een administrator zijn om toegang te krijgen tot de accountgegevens van de operators. Zonder administratorbevoegdheden kunt u alleen uw eigen account controleren.
[SHORTCODE_2]

Om de instellingen van een operator te bekijken gaat u naar het menu-item [SHORTCODE_17]Accountinstellingen > Operators[SHORTCODE_18] en selecteert u in de lijst met operators degene die geen berichten ontvangt.

Controleer het volgende::

- Zijn het telefoonnummer en het e-mailadres van de betreffende operator correct?  
  [SHORTCODE_3]**Opmerking**: Controleer of de juiste landcode en netnummer zijn ingevuld bij het telefoonnummer![SHORTCODE_4] 
- Wordt de betreffende operator vermeld als ‘Heeft dienst’?  
  ![]([LINK_URL_6])
- Verstuur een test-SMS vanuit de operatorinstellingen ( [SHORTCODE_19]Accountinstellingen > Operators[SHORTCODE_20]) om te controleren of het werkt. Ontvangt u de test-SMS niet binnen 10 minuten, wijzig dan de SMS-gateway.  
  Dit kunt u doen als een algemene instelling (geldig voor alle operators) in de SMS-integratie op het tabblad [SHORTCODE_21]Algemeen[SHORTCODE_22] door een andere *SMS-aanbieder* te kiezen.  
  Of u wijzigt de instellingen voor een individuele operator in de *Telefooninstellingen* op het tabblad [SHORTCODE_23]Algemeen[SHORTCODE_24] van de operator. Soms is het nodig om de gateway voor operators op een andere locatie afzonderlijk te wijzigen.  
  Wijzig de gateway en herhaal uw test..  
  [SHORTCODE_5]**Opmerking**: SMS- en spraakalerts die naar telefoonnummers van operators in China en India worden gestuurd, kunnen geblokkeerd worden door nationale spamfilters en bel-me-niet-registers. [Lees meer]([LINK_URL_7]) [SHORTCODE_6] 
- Verstuur vanuit de operatorinstellingen een test-e-mail om te controleren of het werkt.  [SHORTCODE_7]**Opmerking**: Controleer de blacklist-/spammap op uw e-mailserver als u geen e-mailberichten ontvangt, want soms komen berichten daar terecht. Bekijk onze aanbeveling voor [whitelisting]([LINK_URL_8]) aan het eind van dit artikel.[SHORTCODE_8] 

Meer informatie over het versturen van testberichten vindt u in het KB-artikel [Alertberichten testen]([LINK_URL_9]).

## Controleer uw alertdefinities en escalatieniveaus

Om alerts te genereren moet er een alertdefinitie bestaan en moet de controleregel eraan zijn toegewezen. Om berichten te versturen moet er minstens één escalatieniveau zijn gedefinieerd en actief zijn. 

- **Is de alertdefinitie geactiveerd?**  
  De instelling is te vinden op het tabblad [SHORTCODE_25]Algemeen[SHORTCODE_26] van een alertdefinitie.
- **Is de betreffende gemonitorde service toegewezen aan een alertdefinitie?**  
  U moet al uw alertdefinities controleren om te zien welke controleregels eraan zijn gekoppeld. Als u veel alertdefinities heeft en de informatie die u zoekt niet kunt vinden, vul dan een [support ticket]([LINK_URL_10]) in om hulp te krijgen.
- **Zijn de escalatieniveaus actief?**  
  Controleer de instelling op het bijbehorende tabblad [SHORTCODE_27] Escalatieniveau [SHORTCODE_28].
- **Hoe is het genereren van de alert geconfigureerd?**  
  Het is belangrijk dat u weet dat deze instellingen invloed kunnen hebben op hoe en wanneer we alerts versturen op basis van bevestigde/onbevestigde fouten.  
  **Bijvoorbeeld:**  
  De instelling *Genereer een alert als er 1 of meer fouten opgetreden zijn* betekent dat we alleen een alert versturen wanneer er één fout is bevestigd. Deze bevestigde fout herkent u aan een rode balk in uw controleregel log.  
  De instelling *Genereer een alert als er 2 of meer fouten opgetreden zijn* betekent dat we alleen alerts versturen nadat er 2 fouten achter elkaar zijn opgetreden (zonder OK-controles ertussen).

## Controleer uw IP-whitelist en e-mailinstellingen [ANCHOR_1]

- Het is mogelijk dat uw e-mailservers de alertmails blokkeren of deze als spam beoordelen. U kunt dit voorkomen door de e-mail-IP’s van Uptrends toe te voegen aan uw whitelist. Ga naar de [IP-whitelist]([LINK_URL_11]) voor de feitelijke IP-adressen voor e-mail.
- Uptrends gebruikt **DKIM-ondertekening** voor e-mailauthenticatie, om spoofing en phishing te helpen voorkomen door een handtekening toe te voegen aan onze uitgaande berichten, zoals alert-e-mails. Als het DKIM-mechanisme om welke reden dan ook faalt, kunnen dergelijke e-mails uiteindelijk als spam worden gemarkeerd.
