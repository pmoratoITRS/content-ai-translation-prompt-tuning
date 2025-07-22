{
  "hero": {
    "title": "Monitoring von Websites auf anderen Servern"
  },
  "title": "Monitoring von Websites auf anderen Servern (nicht dem Produktionsserver)",
  "summary": "Benötigst Du ein Monitoring von Websites auf anderen Servern als dem Produktionsserver, aber unter dem gleichen Domainnamen? Dies geht ganz einfach mit der Einrichtung anhand der Host-Header.",
  "url": "/support/kb/synthetic-monitoring/verfuegbarkeits-monitoring/http-und-https/monitoring-von-websites-auf-anderen-servern",
  "translationKey": "https://www.uptrends.com/support/kb/http-and-https/monitoring-websites-other-than-the-production-server"
}

Solltest Du das Monitoring einer Website benötigen, die die gleiche Domain wie der Produktionsserver hat, aber ein Backup oder eine Website ist, die nicht in Produktion bzw. öffentlich ist, kannst Du dies mit dem Einrichten anhand der richtigen Host-Header erreichen.

## Welche Typen von Prüfobjekten sind hierfür verfügbar?

Du kannst diese Art des Monitorings bei den Prüfobjekten HTTP, HTTPS und Webservices einrichten. Ein solches Monitoring funktioniert leider nicht mit dem Full Page Check und dem Transaktions-Monitoring.

## Notwendige Angaben

Um Prüfobjekte mit Host-Headern einzurichten, benötigst Du Folgendes:

-   die URL für den Webserver und
-   die IP-Adresse des Servers, auf den Uptrends direkt zugreifen muss

## Einrichten des Prüfobjekts

Um ein Prüfobjekt einzurichten:

1.  Rufe ein neues oder ein bestehendes Prüfobjekt auf

2.  Gib die IP-Adresse in das Feld **URL** auf der Registerkarte {{< AppElement type="tab" >}}Allgemein{{< /AppElement >}} ein.  
      

    ![](/img/content/0bbbd6eb-ed47-4de7-a318-ac200db97c42.png)

3.  Wechsele zur Registerkarte {{< AppElement type="tab" >}}Erweitert{{< /AppElement >}}.

4.  Gib im Feld **Http Request Headers** „Host:“ ein, gefolgt vom Domainnamen (siehe unten)  
      

    ![](/img/content/017121b5-d6c2-43cf-a5cc-4a306557cb8e.png)

5.  Füge ein **Übereinstimmungsmuster** (Registerkarte {{< AppElement type="tab" >}}Fehlerbedingungen{{< /AppElement >}}) mit Inhalt ein, der nur auf der Backup-Website und nicht auf der Live-Website zu finden ist, um sicherzustellen, dass Du auf die richtige Website zugreifst (optional).

6.  Beende die Einrichtung durch Klicken auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.
