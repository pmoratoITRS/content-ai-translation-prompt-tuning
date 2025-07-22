{
  "hero": {
    "title": "Foutcondities - Core Web Vitals"
  },
  "title": "Foutcondities - Core Web Vitals",
  "summary": "Limieten gebruiken op Core Web Vitals om fouten te genereren.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-core-web-vitals",
  "tableofcontents": true,
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Google heeft de Core Web Vitals gedefinieerd als een standaardset kengetallen om de gebruikerservaring van een webpagina te meten.

In Uptrends meten en rapporteren controleregeltypes die een [browsertype met extra kengetallen]([LINK_URL_1]) gebruiken de [Core Web Vitals]([LINK_URL_2]). Aangezien dit soort data beschikbaar is, is het zinvol om deze nader te bekijken en te gebruiken voor het signaleren van fouten wanneer een bepaalde drempel wordt bereikt. Daarom maken de condities voor Core Web Vitals deel uit van de [Foutcondities]([LINK_URL_3]). 

Houd er rekening mee dat verschillende controleregeltypes verschillende foutcondities bieden. Bekijk de tabel in [Welke foutcondities zijn beschikbaar?]([LINK_URL_4]) om na te gaan welke opties beschikbaar zijn voor bepaalde controleregeltypes.

De foutcondities met betrekking tot Core Web Vitals worden hieronder uitgelegd.

## Gebruik de huidige aanbevolen Core Web Vitals [ANCHOR_1]

Google beschrijft de prestatiestatus van uw website aan de hand van drie statussen: goed, verbetering nodig en slecht. 
Met Uptrends kunt u een fout signaleren zodra de status ‘verbetering nodig’ is bereikt. Uptrends gebruikt de benchmarkwaarden die Google definieert, momenteel zijn dit:

**First Contentful Paint:** 1,8 seconden  
**Largest Contentful Paint:** 2,5 seconden  
**Time to Interactive:** 3,8 seconden  
**Cumulative Layout Shift:** 0,1  
**Total Blocking Time:** 0,2 seconden (200 ms)

Als u de foutconditie *Gebruik de aanbevolen Core Web Vitals* gebruikt, wordt er een fout gegenereerd wanneer ten minste één van de benchmarkwaarden wordt overschreden.  

U kunt een combinatie gebruiken van de foutconditie *Gebruik de aanbevolen Core Web Vitals* en de individuele Core Web Vital-foutcondities. In dat geval overschrijven uw eigen instellingen de aanbevolen instellingen.

## Maximale tijd tot First Contentful Paint (FCP)

Gebruik deze foutconditie om een maximum in te stellen voor hoelang het mag duren voordat de browser begint met het weergeven van delen van de pagina die de gebruiker in eerste instantie ziet. Als de gebruiker geen tijdige visuele feedback krijgt over het laden van de pagina, kan dit van invloed zijn op de ervaring van een gebruiker die interacteert met uw website.

## Maximale tijd tot Largest Contentful Paint (LCP)

Met deze foutconditie stelt u een maximum in voor hoelang het mag duren voordat de browser de belangrijkste inhoud van de pagina kan weergeven. Als de gebruiker langer dan verwacht moet wachten tot het grootste deel van de inhoud is geladen, kan dit zijn ervaring beïnvloeden.

## Maximale Time To Interactive (TTI)

U kunt dit gebruiken om een maximum in te stellen voor hoelang het mag duren voordat de pagina reageert op gebruikersinteracties. Als dit te lang duurt, moet de gebruiker wachten tot de pagina is geladen voordat de pagina uiteindelijk reageert op zijn invoer.

## Maximum Cumulative Layout Shift (CLS)

De Cumulative Layout Shift (CLS) meet visuele stabiliteit door te controleren of er een onverwachte verschuiving van pagina-elementen plaatsvindt tijdens het laden van de pagina. Gebruik deze foutconditie om te verzekeren dat de gebruiker geen hinder ondervindt van elementen die op uw pagina verschuiven als gevolg van bijvoorbeeld laat/asynchroon laden van video's.

## Maximale Total Blocking Time (TBT)

Stel deze foutconditie in om een maximum op te geven voor hoelang het laden van de pagina in de browser kan worden geblokkeerd vanwege het wachten tot verbindingen beschikbaar komen, scripts zijn uitgevoerd of het renderen is voltooid. Als de gebruiker moet wachten om met de pagina te interacteren doordat zijn browser te lang wordt geblokkeerd, beïnvloedt dit de ervaring van het gebruik van uw website. 