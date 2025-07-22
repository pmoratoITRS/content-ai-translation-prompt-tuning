{
  "hero": {
    "title": "Een controleregel voor SOAP-webservice instellen"
  },
  "title": "SOAP instellen",
  "url": "support/kb/synthetic-monitoring/api-monitoring/soap-webservice-controleregel-instellen",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/setting-up-a-soap-web-service-probe"
}

Als u een **SOAP-controleregel** aan uw Uptrends-account wilt toevoegen, vindt u de instructies in dit artikel.

## Een controleregel voor SOAP-webservice instellen

Om een SOAP-service te testen, wordt doorgaans een methode van die webservice aangeroepen, door er invoerdata naar te posten in de vorm van een SOAP-envelop en dan te verifiëren dat de response correct is.

1.  Ga naar het configuratiescherm Controleregel toevoegen. (Weet u niet meer hoe u dit doet, ga dan naar het artikel [Een controleregel toevoegen]({{< ref path="support/kb/basics/adding-monitors" lang="nl" >}})) Stel uw controleregeltype in op Webservice HTTP of Webservice HTTPS.  
      
    {{< callout >}}**Opmerking**: Door het controleregeltype Webservice te gebruiken, weten we zeker dat we Content-Type: text/xml gebruiken wanneer we requests naar uw server versturen. Omdat SOAP-enveloppen in XML-formaat zijn, zou dit bij de meeste webservices moeten werken.{{< /callout >}} 
2.  Vul de betreffende informatie in bij naam, controle-interval, URL en poort.  
3.  Ga naar het tabblad {{< AppElement type="tab" >}}Extra{{< /AppElement >}} en stel de HTTP method in op Post.  
4.  Specificeer uw SOAP request (de volledige SOAP-envelop) in het Post-dataveld.  
      
    Meestal ziet het er zo uit:  
    *…Message information goes here…*  
5.  Uw webserver verwacht waarschijnlijk een SOAP Action HTTP header, die de server vertelt welke methode uw webservice moet uitvoeren.  
      
    In het veld HTTP headers specificeert u de header in het volgende formaat:  
      
    `SOAPAction: http://mywebservice.example.com/MyServiceMethod`
      
    {{< callout >}}**Opmerking**: Als uw webserver een ander type inhoud verwacht, kunt u een ander Content-Type specificeren in het veld HTTP headers. Bijvoorbeeld: Content-Type: application/xml{{< /callout >}} 
6.  Het is waarschijnlijk nuttig om te verifiëren dat uw webservice terugkomt met de juiste inhoud.  
      
    U kunt naar een specifiek stukje inhoud zoeken door dit te specificeren in het veld *Pagina inhoud match* op het tabblad {{< AppElement type="tab" >}}Foutcondities{{< /AppElement >}}.  
      
    De Uptrends-service zoekt dan bij elke controle die het uitvoert naar die inhoud in de HTPP response.

## Werkt uw SOAP-controleregel niet?

Lukt het u niet uw SOAP-controleregel werkend te krijgen, neem dan contact op met support door [een support ticket te sturen](/contact).

Stuur zo mogelijk een schermopname van een HTTP request die wel werkt. Meestal heeft u er een in uw eigen webservice-testtool die u kunt gebruiken om ons een Fiddler-schermopname te sturen, of een cURL command die alle benodigde gegevens bevat (URL/POST data/HTTP headers).
