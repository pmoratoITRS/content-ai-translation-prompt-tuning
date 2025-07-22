{
  "hero": {
    "title": "Zertifikate an Private Locations installieren"
  },
  "title": "Zertifikate an Private Locations installieren",
  "summary": "Installiere Zertifikate an Private Locations zur internen Überwachung deiner Netzwerkinfrastruktur.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/private-locations/zertifikate-installieren-an-private-locations",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/install-certificates-private-locations"
}


Bei der Einrichtung deiner [Docker-basierten Private Location]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}) musst du eventuell Zertifikate installieren, um Vertrauen zu erstellen und Verbindungen mit der zu überwachenden Website oder dem Webservice zu authentifizieren.

Die folgenden Zertifikatstypen können installiert werden:

- Client-Zertifikate (PKCS #12)
- Intermediate-Zertifikate einer Zertifizierungsstelle (Certificate Authority, CA) (PKCS #7)
- Root-Zertifikate einer Zertifizierungsstelle (CA) (PKCS #7)

Beachte, dass die [Uptrends Docker-basierte Installations-ZIP-Datei]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints#installation-script" lang="de" >}}) einen **Certificates**-Ordner enthält. Darin sind weitere Ordner für jeden unterstützten Zertifikatstyp zu finden, in denen Zertifikate wie unten beschrieben installiert werden können.

## Zertifikate bei einer Docker-basierten Private Location installieren

Dieser Abschnitt ist ein optionaler Installationsleitfaden für Zertifikate auf Docker-basierten Private Locations. Diese Schritte müssen nur ausgeführt werden, wenn deine zu testenden Anwendungen die Installation eines Zertifikats erfordern.

Stelle vor dem Installieren der Zertifikate sicher, dass die Installationsschritte für [Docker-basierte Private Locations]({{< ref path="/support/kb/synthetic-monitoring/checkpoints/private-locations/install-docker-private-checkpoints" lang="de" >}}) befolgt wurden.

### Zertifikate von Zertifizierungsstellen installieren

**Um CA-Zertifikate zu installieren:**

1. Öffne den Ordner mit der Installation deiner Private Location. Standardmäßig siehst du mehrere Dateien, wie etwa die `docker-compose`-YAML-Datei und Windows PowerShell-Skripte. Diese Dateien sind für den Installationsprozess unerlässlich.

2. Öffne den **Certificates**-Ordner. Dieser Ordner enthält drei weitere Ordner und eine `README`-Markdown-Datei.

3. Lege deine CA-Zertifikate in den entsprechenden **Certificates**-Unterordnern ab:

  - **Intermediate**-Ordner – für alle Intermediate CA-Zertifikat-Dateien (PKCS #7).
  - **Root**-Ordner – für alle Root CA-Zertifikat-Dateien (PKCS #7).
  
4. Führe einen Neustart der Uptrends Checkpoint-Software aus, indem du das `update-images.ps1`-Skript aus dem Root-Verzeichnis der Installation ausführst.

### Client-Zertifikate installieren

Beachte, dass die [Client-Zertifikate bei Multi-Step API (MSA)-Prüfobjekten]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-monitoring-client-certificate-authentication" lang="de" >}}) und Client-Zertifikate bei Private Locations nicht zusammenhängen und verschiedenen Zwecken dienen.

**Um Client-Zertifikate zu installieren:**

1. Öffne den Ordner mit der Installation deiner Private Location. Standardmäßig siehst du mehrere Dateien, wie etwa die `docker-compose`-YAML-Datei und Windows PowerShell-Skripte. Diese Dateien sind für den Installationsprozess unerlässlich.

2. Öffne den **Certificates**-Ordner. Dieser Ordner enthält drei weitere Ordner und eine `README`-Markdown-Datei.

3. Lege dein Client-Zertifikat im **Client**-Ordner ab.

4. Erstelle im **Client**-Ordner eine JSON-Datei mit Namen `clientCertificates.json`. Diese JSON-Datei sollte alle deine Client-Zertifikate auflisten. Andernfalls fahre mit dem nächsten Schritt fort.

- Kopiere und bearbeite zunächst die JSON-Vorlage:

```json
[
    {
        "File": "my-first-client-cert.p12",
        "Password": "letmein",
        "UrlPatterns": ["https://fake.sub.domain.example.com"]
    },
    {
        "File": "AcmeCert.pfx",
        "Password": "anvil123",
        "UrlPatterns": ["https://client.acmecorp.fake:1234", "[*.]acmecorp.real"]
    }
]
```

Beachte, dass das JSON-Snippet aus zwei Client-Zertifikaten besteht. Jedes Client-Zertifikat wird von einem JSON-Objekt mit drei Schlüssel-Wert-Paaren repräsentiert. Das erste Zertifikat, `my-first-client-cert.p12`, kann für eine bestimmte Subdomain verwendet werden. Das zweite Zertifikat, `AcmeCert.pfx`, ist für die Subdomain des Clients `acmecorp.fake` erlaubt, wenn mit HTTPS Port 1234 verbunden oder `acmecorp.real` bzw. eine ihrer Subdomains besucht wird.

Bearbeite die folgenden Werte entsprechend deinen Anforderungen:

  - `File` – der Dateiname und die Dateierweiterung deines Client-Zertifikats.
  - `Password` – das Passwort, das für den Zugriff auf die Daten im Zertifikats-Archiv erforderlich ist, zum Beispiel der private Schlüssel.
  - `UrlPatterns` – die Liste erlaubter URL-Domains oder Subdomains, die das Client-Zertifikat nutzen werden. Diese Liste kann aus mehreren URL-Mustern bestehen, die eine einzelne Domain, Subdomain oder einen Platzhalter für eine Domain und alle ihre Subdomains sein können. Mehr erfährst du unter [URL-Musterformat für Unternehmensrichtlinien](https://chromeenterprise.google/intl/de_de/policies/url-patterns/).

5. Führe einen Neustart der Uptrends Checkpoint-Software aus, indem du das `update-images.ps1`-Skript aus dem Root-Verzeichnis der Installation ausführst.

6. Bestätige, dass sowohl das alte wie auch das neue Zertifikat erkannt werden und korrekt installiert sind. Sollte es Probleme geben, probiere diese einfachen Schritte zur Fehlerbehebung:

- Prüfe, dass der JSON-Dateiname korrekt ist.
- Stelle sicher, dass alle JSON-Schlüssel-Wert-Paare der korrekten JSON-Syntax folgen.
- Prüfe auf Falschkonfigurationen oder Probleme mit Berechtigungen.
