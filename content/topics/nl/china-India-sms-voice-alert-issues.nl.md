{
  "hero": {
    "title": "Problemen met SMS- en stemalerts in China en India"
  },
  "title": "Problemen met SMS- en stemalerts in China en India",
  "summary": "Spamfilters en bel-me-nietregisters kunnen alertberichten naar sommige regio’s blokkeren, dus overweeg deze andere opties voor uw operators in China of India.  ",
  "url": "/support/kb/alerting/problemen-met-sms-en-stemalerts-in-china-en-india",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/china-india-sms-voice-alert-issues"
}

Ontvangen uw operators in China of India geen alerts of slechts enkele van hun alerts? Overheidsvoorschriften in China en India’s National Customer Preference Register (ook bekend als Do Not Disturb Registry) blokkeren effectief sommige telefoontjes en tekstberichten.

## Spamfilters in China

China onderzoekt telefoongesprekken en teksten die afkomstig zijn van buiten het land en blokkeert telefoongesprekken en SMS-berichten die als spam worden beschouwd, zoals samengevat door [Twilio.](https://support.twilio.com/hc/en-us/articles/360016488474-Calling-Limitations-to-China)

"Ons netwerk en onze operationele partners moeten aan strenge normen voldoen voor het afleveren van gesprekken in China. Volgens deze normen zijn gespreksverkeer korter dan twee minuten en grote aantallen oproepen met dezelfde beller-ID ongewenst, en niet-conforme entiteiten riskeren volledige en permanente afsluiting zonder waarschuwing. Om compliant te blijven met onze partners kan Twilio in de toekomst geen ondersteuning meer bieden voor low-ACD naar China. Dit is een universeel gedrag voor al het internationale verkeer dat tot stand wordt gebracht met China en is niet uniek voor het Twilio-platform. Aanvullende details worden beschreven in onze FAQ Calling limitations to China."

Verschillende factoren om te voldoen aan China’s strenge eisen aan telefoon en SMS voorkomen dat onze alertberichten doorkomen:

- Gemiddelde gespreksduur van twee minuten of langer: stemberichten afkomstig van Uptrends-telefoon-/voice alerts voldoen nooit aan deze vereiste.
- Frequente oproepen die afkomstig zijn van hetzelfde nummer.
- Drie SMS-berichten met dezelfde inhoud die worden verzonden veroorzaken een blokkade. Afhankelijk van uw escalatie-instellingen kunnen herinneringsberichten de limiet van drie berichten overschrijden.
- Vijf verschillende berichten afkomstig van hetzelfde nummer naar een nummer in China activeren een handmatige beoordeling en een 24-uursblokkering van alle berichten.

Zoals u kunt zien werken **SMS berichten naar nummers die in China eindigen niet betrouwbaar en mogelijk helemaal niet, en stem-/telefoonmeldingen werken helemaal niet.** We raden u ten sterkste aan een aantal van onze andere waarschuwingsmethoden (die hieronder worden beschreven) in overweging te nemen.

## India’s spraak/SMS-blokkering

Als uw operator in India geen spraak- of SMS-alertberichten van Uptrends ontvangt, heeft hij zijn nummer waarschijnlijk vermeld in het [National Customer Preference Register](https://www.trai.gov.in/faqcategory/unsolicited-commercial-communicationsucc) (NCPR). In het NCPR kunnen consumenten spraak- en SMS-berichten blokkeren op basis van de marktsector of alle marktsectoren blokkeren. Als de operator het nummer heeft geregistreerd, moet de operator drie maanden wachten nadat hij zijn nummer heeft geregistreerd om het nummer uit de blokkeerlijst te verwijderen.

## Alternatieven voor SMS- en spraakalerts in China en India

Uptrends heeft meerdere opties naast SMS- en stemalerts voor het waarschuwen van uw operators in China en India.

- **E-mail** —  e-mail is een effectieve alertingtool voor dienstdoende operators.
- [**Integraties**]({{< ref path="/integrations" lang="nl" >}}) — als u Slack, PagerDuty, StatusHub, Splunk On-Call (voorheen VictorOps) of ServiceNow gebruikt, kunt u deze snel integreren in uw Uptrends-account om berichten te verzenden naar uw operators in China en India.
- [**Webhooks**]({{< ref path="/support/kb/alerting/integrations/custom-integrations" lang="nl" >}}) — 
als uw third-party service of app API-berichtrequests kan ontvangen en verwerken, kunt u via die services alerts ontvangen van Uptrends.
- **Pushberichten met de Uptrends App** — De [Uptrends App]({{< ref path="/mobile-apps" lang="nl" >}}) voor iPhone en Android kan pushberichten naar uw operators sturen.
