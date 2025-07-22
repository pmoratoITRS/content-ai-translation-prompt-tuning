{
  "hero": {
    "title": "Andere websites dan de productieserver monitoren"
  },
  "title": "Andere websites dan de productieserver monitoren",
  "summary": "Moet u een website monitoren die niet de productieserver is, maar wel dezelfde domeinnaam heeft? Dit kunt u doen met de juiste configuratie waarbij u host headers gebruikt.",
  "url": "/support/kb/synthetic-monitoring/uptime-monitoring/http-en-https/andere-websites-dan-de-productieserver-monitoren",
  "translationKey": "https://www.uptrends.com/support/kb/http-and-https/monitoring-websites-other-than-the-production-server"
}

Als u een controleregel nodig hebt voor het monitoren van een website die een domein deelt maar niet uw productieserver is, zoals een back-up- of niet-productiesite, kunt u dat doen met de juiste controleregelconfiguratie waarbij u host headers gebruikt..

## Welke controleregeltypes kunt u hiervoor gebruiken?

U kunt dit type monitoring configureren met HTTP-, HTTPS- en webservicecontroleregels. Helaas werkt dit niet met de Full page check en Transactie monitoring.

## Wat u nodig hebt

Om controleregels te configureren met host headers hebt u nodig:

-   De URL van de webserver waarnaar hij luistert, en
-   Het IP-adres van de server waartoe Uptrends rechtstreeks toegang moet hebben.

## De controleregel configureren

Om een controleregel te configureren doet u het volgende:

1.  Open een bestaande of nieuwe controleregel.

2.  Voer het IP-adres in in het veld **URL** op het tabblad {{< AppElement type="tab" >}}Algemeen{{< /AppElement >}}.

    ![](/img/content/377b33f5-3e3f-488f-ab03-e683d9542dc2.png)

3.  Ga naar het tabblad {{< AppElement type="tab" >}}Extra{{< /AppElement >}}.

4.  Voer "Host:" in, gevolgd door de domeinnaam (zie hieronder)  
    ![](/img/content/a18cdb82-fbb6-45c4-a2f2-f4031a33d34e.png)

5.  Voeg een **Pagina inhoud match** toe (tabblad {{< AppElement type="tab" >}}Foutcondities{{< /AppElement >}}) die inhoud bevat die uniek is voor de back-upsite en niet op de live site voorkomt om ervoor te zorgen dat u de juiste site bezoekt (optioneel).

6.  Voltooi uw configuratie en klik op {{< AppElement type="savebutton" >}}Opslaan{{< /AppElement >}}.
