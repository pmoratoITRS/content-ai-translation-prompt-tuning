{
  "hero": {
    "title": "Multi-step Monitoring – Client-Zertifikate"
  },
  "title": "Multi-step Monitoring – Client-Zertifikatauthentifizierung",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-zertifikatauthentifizierung",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/multi-step-monitoring-client-certificate-authentication"
}

Viele APIs erfordern, dass der Aufrufende Authentifizierungsinformationen angibt, um die Identität – und möglicherweise die Zugriffsberechtigungen – des Aufrufenden zu verifizieren. Authentifizierungsinformationen können über den HTTP-Header (Basic/NTLM/Digest-Authentifizierung), durch Austausch von Zugriffs-Tokens (OAuth) übermittelt werden, indem vom Client die Mitgabe eines Client-Zertifikats in der Anfrage erwartet oder eine Kombination davon weitergegeben wird.

In diesem Artikel werden Optionen für **Client-Zertifikate** behandelt. Um die üblichen Authentifizierungsmethoden einzurichten, lies bitte [den Artikel zu Authentifizierungsarten]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/multi-step-authentication" lang="de" >}}).

## Typen von Client-Zertifikaten

Der Abschnitt Client-Zertifikat auf der Registerkarte Schritte unter „Request“ bei einem Multi-step API Monitoring-Prüfobjekt stellt die folgenden Optionen bereit. Wenn du mehrere Schritte in ddeiner Schritt-Definition verwendest, stelle bitte sicher, dass bei jedem Schritt die gewünschten Einstellungen vorliegen.

-   **Uptrends Client Zertifikat**: Diese Option ist nützlich, wenn du von API-Nutzern verlangst, ihr eigenes Client-Zertifikat zu erzeugen und mitzuliefern, um ihre Identität zu beweisen. Wenn du diese Option wählst, wird ein Uptrends gehörendes Zertifikat mitgesendet, wenn die HTTP-Abfrage übermittelt wird. Deine API kann die eingehende Anfrage anhand des entsprechenden öffentlichen Schlüssels (Public Key) verifizieren. Passen die Schlüssel zusammen, kannst du sicher sein, dass die Abfrage von jemandem stammt, der das Originalzertifikat (d. h. Uptrends) besitzt, – niemandem sonst. Das Client-Zertifikat von Uptrends ist nicht für [private (Container-)Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="de" >}}) verfügbar.
Weitere Informationen findest du im Artikel über [Uptrends‘ Informationen zum Public Key (öffentlichen Schlüssel)]({{< ref path="support/kb/synthetic-monitoring/api-monitoring/uptrends-client-certificate-public-key-information" lang="de" >}}).
-   **Individuelles Client Zertifikat**: Wähle diese Option, wenn du das mit der Abfrage mitzugebende Client-Zertifikat besitzt oder kontrollierst. Sobald du die Zertifikatsdatei nach Uptrends hochgeladen hast, kannst du sie in das Prüfobjekt des Multi-step API Monitorings aufnehmen. Da dir das Zertifikat gehört, wird die API in der Lage sein, eingehende Anfragen, die es nutzen, zu verifizieren. Lies den nächsten Abschnitt, um dies einzurichten.
-   **Kein**: Wähle *Kein*, wenn du kein Client-Zertifikat für die HTTP-Anfrage nutzt.

## Einrichten eines benutzerdefinierten oder individuellen Client-Zertifikats

Um ein Client-Zertifikat in das Prüfobjekt des Multi-step API Monitorings aufzunehmen, musst du es zunächst nach Uptrends hochladen. Zertifikate (und andere sensible Informationen) werden in deine Vault hochgeladen und gespeichert. Sobald du der Vault eine Zertifikatsdatei hinzugefügt hast, kannst du sie in der Monitoring-Einrichtung nutzen.

### Hochladen eines Client-Zertifikats

Wenn du dich für die Option des individuellen Client-Zertifikats zum ersten Mal entscheidest, wirst du sehen, dass noch keine Zertifikate verfügbar sind. Um ein Zertifikat hinzuzufügen, klicke auf *Item hinzufügen*, um zur Vault zu wechseln. Wähle alternativ im Menü {{< AppElement type="menuitem" >}}Accounteinstellungen > Vault{{< /AppElement >}}, öffne einen Vault-Bereich und klicke {{< AppElement type="button" >}}Vault Item hinzufügen{{< /AppElement >}}.

Auf der Seite *Neues Vault Item* gibst du einen einzigartigen Namen für das Zertifikat ein, damit du es später wiederfindest. Stelle sicher, dass der Typ des neuen Vault Items auf **Zertifikats-Archiv** eingestellt ist. Gib unter *Beschreibung* alle Informationen ein, die du für wichtig erachtest.

Wähle schließlich eine Zertifikatsdatei aus, die du hochladen möchtest. Die Datei muss dem Format PKCS #12 entsprechen oder ein Zertifikats-Archiv sein, das sowohl den privaten wie den öffentlichen Schlüssel enthält. Dateien im Format PKCS #12 haben die Erweiterung .pfx oder .p12.

Ein Zertifikats-Archiv ist in der Regel verschlüsselt. Daher benötigen wir das zugehörige Passwort, um das Archiv zu verwenden. Bitte gib das Passwort im Feld *Archiv-Password* an und klicke auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}}.

### Einsatz von Client-Zertifikaten in einem Multi-step-Prüfobjekt

Sobald du in der Vault ein geeignetes Client-Zertifikat gespeichert hast, kannst du es in einem Multi-step API Monitoring nutzen. Klicke im Abschnitt **Client-Zertifikat** eines Schritts auf **Aktualisieren**, um die Liste der verfügbaren Zertifikate zu aktualisieren. Wähle dann für jeden Schritt, der ein Zertifikat erfordert, das zugehörige Zertifikat.
