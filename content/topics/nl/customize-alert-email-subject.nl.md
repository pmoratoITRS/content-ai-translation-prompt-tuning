{
  "hero": {
    "title": "Onderwerp en opmaak van e-mail-alertbericht aanpassen"
  },
  "title": "Onderwerp en opmaak van e-mail-alertbericht aanpassen",
  "summary": "In dit artikel vindt u instructies voor het aanpassen van het onderwerp van e-mailalerts en het inschakelen van HTML-opmaak.",
  "url": "/support/kb/alerting/aanpassen-mailonderwerp-alerts",
  "translationKey": "https://www.uptrends.com/support/kb/alerting/customize-alert-email-subject",
  "tableofcontents": true,
  "sectionlist": true
}

Om de status van uw controleregels eenvoudig via e-mail te volgen en te categoriseren, kunt u met Uptrends de onderwerpen van alert-e-mails aanpassen in de integratie **Alerting via e-mail**. U kunt zowel voor afzonderlijke controleregels als groepen controleregels alerts ontvangen, afhankelijk van de fouten die binnen een bepaald tijdsbestek zijn gegenereerd. Elk onderwerp dat u instelt, wordt toegepast op alle uitgaande alert-e-mails.

Het onderwerp van de e-mail aanpassen:

1. Ga naar {{< AppElement type="menuitem" >}} Alerting > Integraties {{< /AppElement >}} > **Alerting via e-mail** integratie. 
2. Vink het selectievakje **Integratie aanpassen** aan om het tabblad {{< AppElement type="tab" >}} Aanpassingen {{< /AppElement >}} weer te geven.
3. Ga naar het tabblad {{< AppElement type="tab" >}} Aanpassingen {{< /AppElement >}}.
4. Om e-mails in HTML-formaat te ontvangen, raadpleegt u de instructies voor [HTML-opmaak]({{< ref path="/support/kb/alerting/customize-alert-email-subject#html-formatting" lang="nl" >}}). Ga anders door naar de volgende stap.
5. Kies het selectievakje [Alerttype]({{< ref path="/support/kb/alerting/integrations/custom-integrations/message-types" lang="nl" >}}) (Fout, Herinnering, OK) om het onderwerp voor elke afzonderlijke of meerdere controleregels aan te passen. 
6. Voer een nieuw onderwerp in. U kunt een breed scala aan variabelen gebruiken, zoals de [Automatische variabelen]({{< ref path="/support/kb/synthetic-monitoring/transactions/automatic-variables" lang="nl" >}}) en [Alertsysteemvariabelen]({{< ref path="/support/kb/alerting/integrations/custom-integrations/alerting-system-variables" lang="nl" >}}) in het onderwerpveld van de e-mail. Gebruik bijvoorbeeld de variabelen `{{@monitor.name}}` en `{{@alert.timestamp}}` om te verwijzen naar de naam van de controleregel en de datum- en tijdwaarde van de alert.

7. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen te bevestigen.


![Aanpassen van alert-e-mailonderwerp](/img/content/scr-customizing-email-subjects_020624.min.png)

## HTML-opmaak

U kunt de uitgaande alertmails instellen in HTML-formaat om e-mails te ontvangen met uitgebreide opmaak (banners, kleuren, afbeeldingen en hyperlinks) in plaats van platte tekst. Houd er rekening mee dat u door de standaard plattetekstmails in te stellen op HTML-opmaak, problemen kunt ondervinden met de geautomatiseerde systemen die de opmaak verwerken. Standaard is de HTML-opmaak alleen ingeschakeld voor nieuwe accounts. Raadpleeg de onderstaande instructies als u deze instelling wilt in- of uitschakelen.

HTML-opmaak inschakelen:

1. Ga naar het tabblad {{< AppElement type="tab" >}} Aanpassingen {{< /AppElement >}} en vink het selectievakje **Gebruik HTML-mail** aan.
2. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen te bevestigen.

HTML-opmaak uitschakelen:

1. Ga naar het tabblad {{< AppElement type="tab" >}} Aanpassingen {{< /AppElement >}} en schakel het selectievakje **Gebruik HTML-mail** uit.
2. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen te bevestigen.
