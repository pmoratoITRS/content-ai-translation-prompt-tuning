{
  "hero": {
    "title": "Foutcondities overzicht"
  },
  "title": "Foutcondities overzicht",
  "summary": "Wat zijn foutcondities en hoe gebruik je ze? ",
  "url": "/support/kb/synthetic-monitoring/controleregel-instellingen/foutcondities/foutcondities-overzicht",
  "translationKey": "https://www.uptrends.com/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-overview",
  "tableofcontents": true,
  "sectionlist": false
}

Foutcondities spelen een belangrijke rol bij het genereren van uw monitoringalerts. Het instellen van een foutconditie is de eerste stap van de [alert- en foutstroomcyclus]({{< ref path="support/kb/alerting/alerting-overview" lang="nl" >}}) waarmee u alertberichten kunt ontvangen.

Met een **foutconditie** kunt u een reeks criteria definiëren om uw controleregel te informeren over fouten op uw website, webservice of server. Het dient als basis voor uw controleregel om te bepalen welk websitegedrag in een fout resulteert en welk niet.

Als u bijvoorbeeld wilt dat uw website minder dan drie seconden nodig heeft om te laden, kunt u een foutconditie instellen en drempels voor de laadtijd van de pagina opgeven. Als u wilt controleren of de inhoud, plug-ins of scripts van uw website correct worden geladen, kunt u voor elk type specifieke foutcondities instellen.

Zodra aan een foutconditie is voldaan, wordt er een fout gegenereerd die een alert activeert. Als alerting is geconfigureerd, wordt u onmiddellijk door een alertbericht op de hoogte gesteld.

## Foutcondities voor controleregeltypes {id="error-conditions-by-category"}

Op het tabblad {{< AppElement type="tab" >}} Foutcondities  {{< /AppElement >}} kunt u verschillende foutcondities instellen die beschikbaar zijn voor elk type controleregel. Houd er rekening mee dat de beschikbaarheid van foutcondities kan variëren, afhankelijk van de categorie van de controleregel en welke data deze verzamelt:

![screenshot foutcondities controleregelset-up](/img/content/scr_monitor-setup-errorconditions.min.png)

### Uptime controleregel

De volgende foutcondities zijn beschikbaar voor [Uptimecontroleregel]({{< ref path="/support/kb/synthetic-monitoring/uptime-monitoring/uptime-monitoring-overview" lang="nl" >}})-types:

| Controleregeltype | Foutcondities | 
|--|--|
| HTTPS, Webservice HTTP en HTTPS | {{< tableformatter >}} 
- [Beschikbaarheid van de pagina controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="nl" >}}) 
- [Pagina-inhoud controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="nl" >}})
- [Laadtijd van de pagina controleren]({{< ref path="" lang="nl" >}})
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
{{< /tableformatter >}} |
| DNS, SSL, SFTP, FTP | {{< tableformatter >}}
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
- [Totale tijd van uitvoeren controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}})
{{< /tableformatter >}} |
| SMTP, POP3, IMAP | {{< tableformatter >}}
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
- [Totale tijd van uitvoeren controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}})
{{< /tableformatter >}} |
| Microsoft SQL servers,  MySQL | {{< tableformatter >}}
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
- [Totale tijd van uitvoeren controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}})
{{< /tableformatter >}} |
| Ping, Connect | {{< tableformatter >}}
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
- [Totale tijd van uitvoeren controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}})
{{< /tableformatter >}} |

### Browser- of Full-Page Check (FPC)-controleregel

De volgende foutcondities zijn beschikbaar voor [Browser- of Full-Page Check (FPC)-controleregels]({{< ref path="/support/kb/synthetic-monitoring/browser-monitoring/browser-monitoring-overview" lang="nl" >}}):

| Controleregeltype | Foutcondities |
|--|--|
| Browser of Full-Page Check | {{< tableformatter >}}

- [Beschikbaarheid van de pagina controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="nl" >}}) 
- [Pagina-inhoud controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/content-match" lang="nl" >}})
- [De URL's die door de pagina worden ingeladen controleren]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="nl" >}}) 
- [Laadtijd van de pagina controleren]({{< ref path="" lang="nl" >}})
- [Core Web Vitals controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="nl" >}})
- [W3C Kengetallen controleren]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="nl" >}})
- [Inhoud console controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="nl" >}})
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
{{< /tableformatter >}} |

### Transactiecontroleregel

Foutcondities in [transactiecontroleregels]({{< ref path="/support/kb/synthetic-monitoring/transactions/transactions-overview" lang="nl" >}}) zijn ook beschikbaar voor elke stap. Afhankelijk van de [transactiestapset-up]({{< ref path="/support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="nl" >}}), zijn de volgende foutcondities mogelijk wel of niet beschikbaar:

![screenshot foutcondities controleregelset-up](/img/content/scr-error-condition-transactions.min.png)

| Controleregeltype | Foutcondities |
|--|--|
| Transactie of User journey | {{< tableformatter >}} 
- [Inhoudcontroles]({{< ref path="/support/kb/synthetic-monitoring/transactions/content-checks" lang="nl" >}})
- [Resources controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-resources" lang="nl" >}})
- [De URL's die door de pagina worden ingeladen controleren]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-url-check" lang="nl" >}}) 
- [Core Web Vitals controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-core-web-vitals" lang="nl" >}})
- [W3C Kengetallen controleren]({{< ref path="/support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-w3c" lang="nl" >}})
- [Inhoud console controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-console-content" lang="nl" >}})
- [Beschikbaarheid van de website controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/error-conditions-page-availability" lang="nl" >}}) 
- [Totale tijd van uitvoeren controleren]({{< ref path="support/kb/synthetic-monitoring/monitor-settings/error-conditions/load-time-limit-settings-alerts-and-warnings" lang="nl" >}})
{{< /tableformatter >}} |

Houd er rekening mee dat de [Multi-step API (MSA)-controleregel]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/api-monitoring-overview" lang="nl" >}}) een andere manier gebruikt om fouten te detecteren. Het gebruikt **Assertions** om u controles te laten definiëren om te valideren of de API-respons voldoet aan uw verwachte voorwaarden. Raadpleeg [MSA Assertions]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-assertions" lang="nl" >}}) voor meer informatie.

## Een Foutconditie instellen {id="configure-error-condition"}

U kunt foutcondities toevoegen wanneer u [uw controleregel helemaal vanaf het begin instelt]({{< ref path="support/kb/basics/adding-monitors" lang="nl" >}}) of een bestaande controleregel bewerkt.

Foutcondities instellen:

1. Ga naar {{< AppElement type="menuitem" >}} Monitoring > Controleregels beheren {{< /AppElement >}}.
2. Klik op de controleregel waaraan u een foutconditie wilt toevoegen.
3. Ga naar het tabblad { {{< AppElement type="tab" >}} Foutcondities {{< /AppElement >}}.
4. Klik op de foutconditie om de sectie uit te vouwen en de controleregelinstellingen te configureren.
5. (Optioneel) Om nieuwe controles voor een foutconditie toe te voegen klikt u op de knop {{< AppElement type="buttonSecondary" >}} \+ Nieuwe controle {{< /AppElement >}}.
6. Ga door met het configureren van condities.
7. Klik op {{< AppElement type="savebutton" >}} Opslaan {{< /AppElement >}} om de wijzigingen in de controleregel te bevestigen.

Als u een melding wilt ontvangen wanneer aan een foutconditie is voldaan, [creëert u een alertdefinitie]({{< ref path="/support/kb/alerting/create-alert-definitions" lang="nl" >}}).

![screenshot foutcondities controleregelset-up](/img/content/gif-set-up-error-condition.gif)