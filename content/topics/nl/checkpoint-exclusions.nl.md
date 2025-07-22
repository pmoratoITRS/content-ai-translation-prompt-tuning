{
  "hero": {
    "title": "Controlestations uitsluiten"
  },
  "title": "Controlestations uitsluiten",
  "summary": "Afhankelijk van de regio van waaruit u wilt testen of op van basis eerdere resultaten wilt u mogelijk bepaalde controlestations expliciet uitsluiten.",
  "url": "/support/kb/synthetic-monitoring/controlestations/controlestations-uitsluiten",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/checkpoint-exclusions"
}

We exploiteren een mondiaal netwerk van meer dan {{% Features/Variable variable="CheckpointCount" %}} controlestations om te verzekeren dat uw website over de hele wereld 24/7 beschikbaar is. Hoewel we adviseren zoveel mogelijk controlestations te gebruiken, hoeft u dit niet te doen. We introduceren: **controlestations uitsluiten!**

{{< callout >}}
**Opmerking:** U heeft een Business- of Enterprise-account nodig om controlestations uit te kunnen sluiten. Ervaart u een probleem met een bepaald controlestation, laat ons dat dan weten door een [support-ticket]({{< ref path="contact" lang="nl" >}}) te openen.
{{< /callout >}}

## Uitzonderingen toevoegen aan controlestations

Het is mogelijk een hele regio van controlestations (Canada bijvoorbeeld) geselecteerd te houden (met het voordeel dat u **automatisch nieuwe controlestations krijgt zodra die worden toegevoegd** aan die regio), maar toch controle te hebben over individuele controlestationlocaties die u wilt overslaan.

U kunt uitzonderingen toevoegen door te klikken op de link {{< AppElement type="menuitem" >}}uitzonderingen toevoegen{{< /AppElement >}} in de tekst boven in het tabblad {{< AppElement type="tab" >}}Controlestations{{< /AppElement >}}. Elk controlestation dat u specificeert zal overgeslagen worden bij het uitvoeren van checks voor uw controleregel, ongeacht de selectie die u maakt.

![](/img/sub/support/checkpoint-exclusions.png)

Het kan in verschillende situaties handig zijn controlestations uit te sluiten. Enkele voorbeelden:

- Wanneer het controlestation Kelowna (Canada) onverwachte resultaten oplevert, kunt u Canada als regio selecteren, maar Kelowna uitzonderen.
- Het kan zijn dat uw site wordt gehost vanuit Berlijn en u geen metingen van al te dichtbij wilt. In plaats van Duitsland te deselecteren en alle controlestations afzonderlijk te selecteren, kunt u simpelweg een uitzondering toevoegen.

{{< callout >}}
**Opmerking:** U kunt alleen **specifieke controlestations** uitsluiten. Het is niet mogelijk hele landen van een geselecteerd continent uit te sluiten.
{{< /callout >}}
