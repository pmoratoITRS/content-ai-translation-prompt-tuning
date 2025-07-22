{
  "hero": {
    "title": "Alertherinneringen in escalaties"
  },
  "title": "Alertherinneringen in escalaties",
  "summary": "Alertdefinities hebben een herinneringsoptie voor alle escalatieniveaus.",
  "url": "/support/kb/alerting/alertherinneringen-in-escalaties",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/alert-reminders-in-escalations"
}

## Wat zijn herinneringen?

Een herinnering is een methode om operators herhaaldelijk te informeren over een onopgeloste fout. Wanneer een alert wordt gegenereerd (altijd gebaseerd op een bevestigde fout), kunt u operators of systemen op de hoogte stellen door een bericht te versturen (door een integratie te gebruiken). De operators moeten dan actie ondernemen om het gesignaleerde probleem op te lossen. Voor het geval de operators het bericht niet hebben gezien of geen actie hebben ondernomen, kunt u herinneringen versturen om de aandacht van de operators te trekken of om de urgentie van het probleem te benadrukken.  
Als de SLA's (service level agreements) met uw klanten een oplossing binnen een gespecificeerd tijdsbestek beloven, wilt u er zeker van zijn dat de operators het bericht ontvangen en handelen in overeenstemming met de verwachtingen die uiteengezet zijn in de SLA.

De herinneringen in de Uptrends-app zijn onderdeel van Escalatieniveaus in Alertdefinities. Afhankelijk van de escalatieniveaus in uw SLA's, wilt u wellicht het herinneringsmechanisme hier implementeren.

Nadat een alert is gecreëerd en voortduurt, worden de herinneringen volgens uw specificaties verstuurd zolang er geen OK-alert is gegenereerd. Zodra de gesignaleerde fout is opgelost (een OK-controle en een OK-alert heeft), wordt het versturen van herinneringen gestopt.

## Hoe u herinneringen implementeert

De instelling *Herinneringen* is onderdeel van de [Escalatieniveaus]({{< ref path="/support/kb/alerting/alert-escalation-levels" lang="nl" >}}) binnen een Alertdefinitie.

![](/img/content/c8407764-8f48-49fa-8608-79e3ee2b1c4f.png)

U stelt het maximale aantal en het interval van herinneringen in door de zin te voltooien met waarden voor 'n' en 'x':  
*Stuur maximaal 'n' herinneringsalerts, elke 'x' minuten.*

Houd rekening met het volgende bij het instellen van de waarden:

-   Als u geen herinneringen wilt sturen, stelt u 'n' in op 0.
-   Synchroniseer het herinneringsinterval 'x' met de Escalatie-interval (indien gebruikt). Als u bijvoorbeeld de Escalatie heeft ingesteld op “Genereer een alert als er langer dan 5 minuten een fout optreedt”, heeft het geen zin om een herinnering in te stellen voor elke 3 minuten.
-   Denk aan het controle-interval (in de controleregelinstellingen). Als u heeft ingesteld dat de herinneringen vaker worden verstuurd dan de controleregel checks uitvoert, werkt dit mogelijk niet efficiënt. Er kan een situatie ontstaan waarin u een herinnering stuurt terwijl de volgende controleregelcheck een OK-resultaat retourneert en de herinnering dus niet meer nodig is.

{{< callout >}}
**Opmerking:** Om controle te houden over uw herinneringen moet u vermijden dat herinneringen van verschillende escalatieniveaus elkaar overlappen. Als u escalatieniveau 1 instelt op 3 herinneringen elke 5 minuten, en escalatieniveau 2 bijvoorbeeld na 10 minuten begint te werken, dan overlappen de twee elkaar.
{{< /callout >}}

## Welke integraties zijn geschikt voor herinneringen?

Integraties zijn de definities van hoe een bericht wordt verstuurd nadat een alert is gecreëerd. Niet alle integraties zijn even geschikt voor gebruik met herinneringen.

De implementatie van herinneringen is nuttig bij integraties zoals e-mail, sms en Slack. Met andere woorden, herinneringen zijn logisch bij integraties waarbij een echte persoon het bericht ontvangt en erop reageert.

Bij andere integraties zoals PagerDuty, StatusHub, Splunk On-Call, ServiceNow en waarschijnlijk enkele aanpasbare integraties, is het wellicht niet logisch om herinneringen te implementeren. Vaak stellen dergelijke integraties een status binnen een systeem in, gebaseerd op een foutalert of OK-alert. Een herinnering verandert de status zelf niet en heeft daarom in de meeste gevallen geen zin. De foutstatus blijft in het systeem aanwezig totdat het systeem een OK-alertbericht ontvangt. Een herinnering verandert dat proces niet en wordt daarom niet aanbevolen.
