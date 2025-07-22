{
  "hero": {
    "title": "Monitor API"
  },
  "title": "Monitor API",
  "url": "[URL_BASE_TOPICS]api/monitor-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die Endpunkte, die Teil der Monitor API (Prüfobjekt-API) sind, ermöglichen das Verwalten deiner Prüfobjekteinstellungen in Uptrends. Monitors bzw. Prüfobjekte werden von dir in Uptrends definiert, um festzulegen, was überwacht werden soll. Üblicherweise testet ein Prüfobjekt eine einzelne Webseite, eine Folge von API-Aufrufen oder den Klickpfad eines Nutzers einer Website.

Die Prüfobjekt-API verfügt über mehrere Endpunkte, mithilfe derer du Prüfobjektdefinitionen erstellen, ändern, kopieren oder löschen kannst. Nachfolgend beschreiben wir diese Endpunkte.

## Erste Schritte

-   Um die API aufzurufen, benötigst du einen API-Account.
-   Du kannst die Monitor API-Endpunkte in unserer [Swagger-Umgebung]([LINK_URL_1]) kennenlernen bzw. ausprobieren.
-   Jede API-Methode wird unten beschrieben.
-   Bei den meisten dieser Methoden arbeitest du mit einem Prüfobjekt-Objekt, das die Einstellungen für ein Prüfobjekt enthält. Weitere Infos zu den entsprechenden Einstellungen und Feldern findest du im Artikel zu [Felder der Monitor API]([LINK_URL_2]).

## GET /Monitor

Gibt eine Liste der im Account enthaltenen Prüfobjekte zurück.

[INLINE_CODE_1]

Antwort:

    [
    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts homepage",
    "IsActive": true,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // More fields here
    },
    // More monitors here
    ]

## GET /Monitor/{monitorGuid}

Gibt ein einzelnes Prüfobjekt zurück, wird durch angegebene monitorGuid identifiziert.

[INLINE_CODE_2]

Antwort:

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts homepage",
    "IsActive": true,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // More fields here
    }

## PATCH /Monitor/{monitorGuid}

Aktualisiert die Definition des angegebenen Prüfobjekts. Der Anfragetext für diese Anfrage sollte eine Teilliste der Felder enthalten, die aktualisiert werden sollen. Üblicherweise wird diese Anfrage verwendet, um nur einige wenige Felder zu aktualisieren. Führe nur Felder in der Anfrage auf, die aktualisiert werden sollen. Das Feld [INLINE_CODE_3] ist optional. Wenn du es angibst, muss es der MonitorGuid der URL entsprechen.

Die folgende PATCH-Anfrage wird verwendet, um ein Prüfobjekt zu deaktivieren, indem ein neuer Wert für das Feld [INLINE_CODE_4] angegeben wird.

[INLINE_CODE_5]

Anfragetext:

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "IsActive": false
    }

## PUT /Monitor/{monitorGuid}

Aktualisiert die Definition des angegebenen Prüfobjekts. Der Anfragetext für diese Anfrage sollte die vollständige Liste der Prüfobjekt-Felder enthalten. In der Regel führst du erst eine GET-Anfrage aus, um die bestehende Definition des zu aktualisierenden Prüfobjekts abzurufen. Dann nimmst du die notwendigen Änderungen an diesem Inhalt vor und sendest ihn mithilfe der PUT-Anfrage zurück.

Die folgende PUT-Anfrage wird verwendet, um die Felder Name und IsActive des Prüfobjekts zu ändern, aber die anderen Felder müssen ebenfalls aufgeführt werden, da wir eine PUT-Anfrage verwenden, nicht eine PATCH-Anfrage für eine Teiländerung.

[INLINE_CODE_6]

Anfragetext:

    {
    "MonitorGuid": "1d2f5fac-730c-45b0-a077-4ab82aaee14e",
    "Name": "Galactic Resorts product page",
    "IsActive": false,
    "GenerateAlert": true,
    "MonitorType": "Https",
    "CheckInterval": 5
    // Remaining fields here    
    }

## POST /Monitor

Erstellt ein neues Prüfobjekt. Der Anfragetext für diese Anfrage sollte die vollständige Liste der Prüfobjekt-Felder enthalten, die für den zu erstellenden Prüfobjekttyp erforderlich sind.

Wenn du zum ersten Mal eine API-Anfrage wie diese erstellst, kann es nützlich sein, zunächst ein Prüfobjekt in der Uptrends-Anwendung einzurichten. Rufe dann die Definition für das Prüfobjekt mithilfe einer GET-Anfrage ab, um dir die Struktur der Prüfobjektdefinition als Beispiel anzusehen.

Die folgende POST-Anfrage wird verwendet, um ein grundlegendes HTTPS-Prüfobjekt einzurichten, das von Checkpoints in Europa ausgeführt wird:

[INLINE_CODE_7]

Anfragetext:

    {
    "Name": "My new monitor",
    "IsActive": true,
    "GenerateAlert": true,
    "IsLocked": false,
    "CheckInterval": 5,
    "MonitorMode": "Production",
    "CustomFields": [],
    "SelectedCheckpoints": {
        "Regions": [
        1004
        ]
    },
    "UsePrimaryCheckpointsOnly": true,
    "MonitorType": "Https",
    "Notes": "Monitors uptime for the homepage",
    "AlertOnLoadTimeLimit1": true,
    "LoadTimeLimit1": 2500,
    "AlertOnLoadTimeLimit2": true,
    "LoadTimeLimit2": 5000,
    "RequestHeaders": [],
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36",
    "Username": "",
    "AuthenticationType": "None",
    "CheckCertificateErrors": true,
    "IpVersion": "IpV4",
    "AlertOnMinimumBytes": false,
    "MinimumBytes": 0,
    "HttpMethod": "Get",
    "CheckHttpStatusCode": false,
    "ExpectedHttpStatusCode": 401,
    "TlsVersion": "Tls12_Tls11_Tls10",
    "RequestBody": "",
    "Url": "[URL_1]
    }

## DELETE /Monitor/{monitorGuid}

Löscht das angegebene Prüfobjekt.

[INLINE_CODE_8]

## POST /Monitor/{monitorGuid}/Clone

Erstellt einen Klon (eine Kopie) des angegebenen Prüfobjekts. Das kopierte Prüfobjekt wird zunächst nicht aktiv sein, sodass du vor dem Aktivieren Änderungen vornehmen kannst.

### Optionale Parameter

-   **includeMaintenancePeriods**: true oder false (Standard: true). Gibt an, ob auch die bestehenden Wartungszeiträume aus dem Original-Prüfobjekt in der Kopie übernommen werden sollen.
-   **includeMonitorGroups**: true oder false (Standard: true). Gibt an, ob auch die Mitglieder der Prüfobjektgruppen in der Kopie übernommen werden sollen. Wenn „true“ angegeben wird, ist die Kopie Teil derselben Prüfobjektgruppen wie das Original-Prüfobjekt. Wenn „false“ angegeben wird, ist die Kopie nur Teil der Gruppe *Alle Prüfobjekte*.

Die folgende POST-Anfrage erstellt eine Kopie eines bestehenden Prüfobjekts und gibt an, dass die Wartungszeiträume nicht vom Original übernommen werden, aber dass das neue Prüfobjekt Teil derselben Prüfobjektgruppen sein soll.

[INLINE_CODE_9]

## Weitere APIs in Bezug auf Prüfobjekte

-   Wenn du Monitoring-Daten (d.h. Monitoring-Check-Daten, die von einem Prüfobjekt geliefert werden) benötigst, sieh dir die [MonitorCheck API]([LINK_URL_3]) an.
-   Prüfobjekte können in Gruppen organisiert werden. Sieh dir dazu die [MonitorGroup API]([LINK_URL_4]) an.
-   Prüfobjekte verfügen über automatisierte Aktiv/Inaktiv-Pläne, den *Wartungszeiträumen*. Sieh dir dazu die [Wartungszeiträume in der API]([LINK_URL_5]) an.
