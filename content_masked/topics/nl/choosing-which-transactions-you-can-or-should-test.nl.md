{
  "hero": {
    "title": "Kiezen welke transacties u kunt of moet testen"
  },
  "title": "Kiezen welke transacties u kunt of moet testen",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/transacties/kiezen-welke-transacties-u-kunt-of-moet-testen",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bepalen welke transacties u moet testen met Web Application Monitoring is een belangrijke eerste stap als het gaat om het opzetten van een succesvolle Transactie Monitoring-strategie.

## Welke transacties kan ik monitoren?

Een betere vraag om te stellen is: 'Wat voor soort transacties kan ik NIET monitoren met Web Application Monitoring.' Met Web Application Monitoring kunt u vrijwel elke taak testen die een gebruiker op uw website of service moet uitvoeren. Daarmee heeft u erg veel monitoringmogelijkheden. Enkele veelvoorkomende transacties die u wellicht wilt verifiëren met Web Application Monitoring zijn:

-   In- en uitlogfunctie
-   Zoekfuncties
-   Een reservering plannen of maken
-   Winkelwagentransacties: toevoegen, verwijderen en selecteren van productopties
-   Het invullen en indienen van formulieren, met name formulieren die verbinding maken met andere services, zoals adresverificatie of verzendkostencalculators
-   Financiële transacties

## Hoe u de beste transacties kiest om te monitoren

Uw site zit waarschijnlijk boordevol met mogelijke gebruikersscenario's. Maar u kunt niet elk scenario testen, dus hoe maakt u een keuze? Nou, natuurlijk **wilt u de transacties testen die essentieel zijn voor het succes van uw site en waarop uw gebruikers vertrouwen** (veel hiervan zijn hierboven genoemd). U wilt [uw gebruikersscenario's in kaart brengen]([LINK_URL_1]) en ze onderverdelen in specifieke taken zoals inloggen of een artikel toevoegen aan een winkelwagen. U wilt controleregels creëren die afzonderlijke delen van uw systeem raken. Het instellen van afzonderlijke controleregels om elk aspect van een gebruikersscenario te controleren, zorgt voor betere rapportage en alerting. Als u bijvoorbeeld een winkelwagen wilt testen, navigeert u naar de pagina, voegt een artikel toe aan de winkelwagen, verifieert de winkelwagen en sluit de transactie af. Met deze controleregel test u de paginabeschikbaarheid, de databases die zijn gekoppeld aan product- en gebruikersgegevens en de transactiesnelheid. U wilt transacties testen die:

-   Servers benaderen om de beschikbaarheid van de site, de nauwkeurigheid van de response en de responsetijden te controleren.
-   Databasetoegang en -responses vereisen. Als uw systeem meer dan één database gebruikt, stelt u controleregels in om ze allemaal te benaderen.
-   Gebruikmaken van beschikbaarheid en functionaliteit van externe services. Als uw transactie bijvoorbeeld services van derden gebruikt, zoals locatie- en adresverificatiediensten, wilt u ze misschien allemaal verifiëren.

**Opmerking**: De transacties die u kiest om te monitoren, kunnen onverwachte bijwerkingen hebben. Lees vooral ons artikel [Waarschuwingen, tips en trucs voor Transactie Monitoring]([LINK_URL_2])voordat u een controleregel in production- of stagingmodus plaatst.

## Een opmerking over het kiezen van testlocaties

Zoals u waarschijnlijk wel weet, kan de gebruikerslocatie een enorme impact hebben op de performance en het succes van transacties. Denk goed na over de keuzes van uw controlestationlocaties. We raden af om de hele set beschikbare controlestations voor één controleregel te kiezen. Door brede keuzes te maken zijn performanceproblemen en fouten die een specifiek gebied betreffen, moeilijker te identificeren. Hier leest u waarom.

1.  Als u een groot testgebied heeft gekozen, zal één mislukte controle op één controlestation de alertfase niet halen. Nadat een controlestation een foutconditie heeft gedetecteerd, kiest Uptrends een willekeurig ander controlestation uit de door u aangewezen testlocaties om de fout te verifiëren. Aangezien de verificatiecontrole uit een geheel andere regio kan komen, kan Uptrends de fout niet verifiëren, dus wordt er geen alert verstuurd. Daarom kan een locatiegebaseerde foutconditie aanhouden totdat u een patroon in uw controleregel logs ziet of de verificatiecontrole plaatsvindt in dezelfde regio waar het probleem zich voordoet.

    **Opmerking**: Als u te weinig controlestations kiest, kan dat ook de effectiviteit van uw monitoring verminderen. U moet voor elke controleregel minimaal drie controlestations kiezen, maar we raden aan er meer te kiezen. Bekijk elke transactie zorgvuldig bij het kiezen van uw controlestations.

2.  Performance is in hoge mate een product van de locatie van de gebruiker als gevolg van netwerklatentie en kwaliteit. Sommige locaties kunnen trage responsetijden ondervinden die onopgemerkt blijven omdat ze de minimale responsetijd nauwelijks overschrijden, of de slechte responsetijd wordt niet geverifieerd, zodat er geen alert wordt verstuurd. Door de lage frequentie van de controles hebben de trage responsetijden niet genoeg invloed op performancerapporten om die gemakkelijk op te merken.

**Oplossing**: Dupliceer uw controleregel. Stel de kopieën in om specifieke regio's te controleren. U krijgt rapporten die de ervaring van uw gebruiker binnen de regio beter weergeven. Met het kleinere aantal controlestations kan Uptrends lokale problemen – die bij gebruik van een breder controlestationgebied mogelijk onopgemerkt blijven – vastleggen en u hiervan op de hoogte stellen.
