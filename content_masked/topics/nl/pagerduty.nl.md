{
  "hero": {
    "title": "Ontvang website monitoring alerts in PagerDuty"
  },
  "title": "PagerDuty",
  "summary": "Ontvang website monitoring alerts van Uptrends in PagerDuty. Meld u aan bij Uptrends voor een gratis proefperiode van 30 dagen!",
  "url": "[URL_BASE_TOPICS]alerting/integraties/pagerduty",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

PagerDuty biedt alerting, on-call scheduling, escalatiebeleid en incident tracking om uw team te waarschuwen en systeeminformatie te verzamelen. Door Uptrends' integratie met **PagerDuty** kunt u alertberichten vanuit uw **Uptrends-account** naar een **PagerDuty-account** sturen. U configureert de integratie in drie stappen:

1.  Configureer de integratie in PagerDuty
2.  Configureer de integratie in Uptrends
3.  Voeg in Uptrends de integratie toe aan een alertdefinitie

Bent u benieuwd naar wat u te zien krijgt als deze integratie is geconfigureerd? Hieronder ziet u een voorbeeld van de integratie in PagerDuty. Lees de **gedetailleerde aanwijzingen** hierna over de configuratie!

![]([LINK_URL_1])

## 1. De integratie configureren in PagerDuty

Deze voorbereiding is alleen van toepassing als u alerts wilt ontvangen in uw PagerDuty-account. De integratie tussen Uptrends en PagerDuty bestaat uit alerts die door Uptrends worden verzonden naar een door de gebruiker gedefinieerde service in PagerDuty. Om Uptrends in staat te stellen alerts naar die PagerDuty-service te sturen, dient u binnen uw PagerDuty-account een service te creëren. Dit proces wordt hieronder beschreven.

1.  Selecteer **Services** in de bovenste menubalk van het hoofdscherm van uw PagerDuty-account.
2.  De pagina *Services* verschijnt. Klik op de knop **\+ New Service**.
3.  De pagina *Create a Service* verschijnt. Op deze pagina kunt u de servicegegevens invullen. 
4.  Voer een naam in voor de service en voeg desgewenst een omschrijving toe. Selecteer een bestaande Escalation Policy of genereer zo nodig een nieuwe. Selecteer indien nodig een geschikte **Alert Grouping**-instelling.
5. Het is **niet** nodig om op dit punt een integratie toe te voegen, omdat er automatisch een wordt gemaakt. Klik op *Create service without an integration*.
6.  Nu gaat u naar de servicepagina van uw nieuwe service. Het tabblad *Integrations* bevat de **Integration Key** van uw service.

Hiermee is de configuratie van de integratie in PagerDuty voltooid.

## 2. De integratie configureren in Uptrends

De functie Integraties in Uptrends is toegankelijk via het hoofdmenu.

1.  Klik in het zijbalkmenu op **Alerting**. Begin met het toevoegen van een nieuwe integratie door te klikken op het plusteken **+** naast *Integraties*. ![Een nieuwe integratie toevoegen]([LINK_URL_2])
2.  Selecteer *PagerDuty* om een PagerDuty-integratie te creëren. ![PagerDuty selecteren]([LINK_URL_3])
3.  Klik op de knop **Alert with PagerDuty**, om te starten met het proces om Uptrends en PagerDuty te koppelen. Log in met uw PagerDuty-inloggegevens. ![PagerDuty-inlogportal]([LINK_URL_4])
4. Selecteer in het volgende scherm de PagerDuty-service(s) die u wilt gebruiken met uw Uptrends-alerting. 
![De PagerDuty service(s) selecteren]([LINK_URL_5])
5.  Nadat u op *Connect* heeft geklikt, keert u vanzelf terug naar Uptrends.
6.  Om de definitie te voltooien voert u een naam in voor deze integratie en klikt u op de knop [SHORTCODE_3]Opslaan[SHORTCODE_4] in de linker benedenhoek. Nu keert u terug naar het venster Integraties dat uw nieuwe integratiedefinitie bevat.
7.  Klik op deze integratie als u deze wilt bewerken of testberichten wilt versturen.
![PD post setup]([LINK_URL_6])

[SHORTCODE_1]
**Tip:** Als u een integratiedefinitie deactiveert, zal deze integratie niet gebruikt worden voor alerts. Dit kan handig zijn als u bijvoorbeeld het ontvangen van alerts in uw PagerDuty service tijdelijk wilt uitschakelen.
[SHORTCODE_2]

## 3. De integratie toevoegen aan een alertdefinitie in Uptrends

Een integratiedefinitie op zichzelf doet niets. U moet deze **koppelen aan een of meer escalatieniveaus om alerts te ontvangen** via de integratie.

1.  Om een integratiedefinitie aan een escalatieniveau te koppelen navigeert u in Uptrends naar de betreffende alertdefinitie en escalatieniveau.

 ![Navigeer naar alertdefinities]([LINK_URL_7])

2.  Elk tabblad [SHORTCODE_5]Escalatieniveau[SHORTCODE_6] bevat een element genaamd **Alerts versturen door integraties**. Lees het Knowledge Base-artikel [Alert escalatieniveaus]([LINK_URL_8]) om te leren hoe escalaties werken.
3. Selecteer de integratiedefinitie die u aan dit escalatieniveau wilt koppelen. In dit geval de **PagerDuty**-integratie.
4.  Vergeet niet op de knop [SHORTCODE_7]Opslaan[SHORTCODE_8] te klikken om uw wijzigingen op te slaan.

**Dat is alles!** U heeft de PagerDuty-integratie met succes geconfigureerd.

Zoals gewoonlijk kunt u als u vragen heeft [contact opnemen met ons support team]([LINK_URL_9]).
