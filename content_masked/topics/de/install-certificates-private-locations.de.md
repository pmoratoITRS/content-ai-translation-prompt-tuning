{
  "hero": {
    "title": "Zertifikate an Private Locations installieren"
  },
  "title": "Zertifikate an Private Locations installieren",
  "summary": "Installiere Zertifikate an Private Locations zur internen Überwachung deiner Netzwerkinfrastruktur.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/checkpoints/private-locations/zertifikate-installieren-an-private-locations",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Bei der Einrichtung deiner [Docker-basierten Private Location]([LINK_URL_1]) musst du eventuell Zertifikate installieren, um Vertrauen zu erstellen und Verbindungen mit der zu überwachenden Website oder dem Webservice zu authentifizieren.

Die folgenden Zertifikatstypen können installiert werden:

- Client-Zertifikate (PKCS #12)
- Intermediate-Zertifikate einer Zertifizierungsstelle (Certificate Authority, CA) (PKCS #7)
- Root-Zertifikate einer Zertifizierungsstelle (CA) (PKCS #7)

Beachte, dass die [Uptrends Docker-basierte Installations-ZIP-Datei]([LINK_URL_2]) einen **Certificates**-Ordner enthält. Darin sind weitere Ordner für jeden unterstützten Zertifikatstyp zu finden, in denen Zertifikate wie unten beschrieben installiert werden können.

## Zertifikate bei einer Docker-basierten Private Location installieren

Dieser Abschnitt ist ein optionaler Installationsleitfaden für Zertifikate auf Docker-basierten Private Locations. Diese Schritte müssen nur ausgeführt werden, wenn deine zu testenden Anwendungen die Installation eines Zertifikats erfordern.

Stelle vor dem Installieren der Zertifikate sicher, dass die Installationsschritte für [Docker-basierte Private Locations]([LINK_URL_3]) befolgt wurden.

### Zertifikate von Zertifizierungsstellen installieren

**Um CA-Zertifikate zu installieren:**

1. Öffne den Ordner mit der Installation deiner Private Location. Standardmäßig siehst du mehrere Dateien, wie etwa die [INLINE_CODE_1]-YAML-Datei und Windows PowerShell-Skripte. Diese Dateien sind für den Installationsprozess unerlässlich.

2. Öffne den **Certificates**-Ordner. Dieser Ordner enthält drei weitere Ordner und eine [INLINE_CODE_2]-Markdown-Datei.

3. Lege deine CA-Zertifikate in den entsprechenden **Certificates**-Unterordnern ab:

  - **Intermediate**-Ordner – für alle Intermediate CA-Zertifikat-Dateien (PKCS #7).
  - **Root**-Ordner – für alle Root CA-Zertifikat-Dateien (PKCS #7).
  
4. Führe einen Neustart der Uptrends Checkpoint-Software aus, indem du das [INLINE_CODE_3]-Skript aus dem Root-Verzeichnis der Installation ausführst.

### Client-Zertifikate installieren

Beachte, dass die [Client-Zertifikate bei Multi-Step API (MSA)-Prüfobjekten]([LINK_URL_4]) und Client-Zertifikate bei Private Locations nicht zusammenhängen und verschiedenen Zwecken dienen.

**Um Client-Zertifikate zu installieren:**

1. Öffne den Ordner mit der Installation deiner Private Location. Standardmäßig siehst du mehrere Dateien, wie etwa die [INLINE_CODE_4]-YAML-Datei und Windows PowerShell-Skripte. Diese Dateien sind für den Installationsprozess unerlässlich.

2. Öffne den **Certificates**-Ordner. Dieser Ordner enthält drei weitere Ordner und eine [INLINE_CODE_5]-Markdown-Datei.

3. Lege dein Client-Zertifikat im **Client**-Ordner ab.

4. Erstelle im **Client**-Ordner eine JSON-Datei mit Namen [INLINE_CODE_6]. Diese JSON-Datei sollte alle deine Client-Zertifikate auflisten. Andernfalls fahre mit dem nächsten Schritt fort.

- Kopiere und bearbeite zunächst die JSON-Vorlage:

[CODE_BLOCK_1]

Beachte, dass das JSON-Snippet aus zwei Client-Zertifikaten besteht. Jedes Client-Zertifikat wird von einem JSON-Objekt mit drei Schlüssel-Wert-Paaren repräsentiert. Das erste Zertifikat, [INLINE_CODE_7], kann für eine bestimmte Subdomain verwendet werden. Das zweite Zertifikat, [INLINE_CODE_8], ist für die Subdomain des Clients [INLINE_CODE_9] erlaubt, wenn mit HTTPS Port 1234 verbunden oder [INLINE_CODE_10] bzw. eine ihrer Subdomains besucht wird.

Bearbeite die folgenden Werte entsprechend deinen Anforderungen:

  - [INLINE_CODE_11] – der Dateiname und die Dateierweiterung deines Client-Zertifikats.
  - [INLINE_CODE_12] – das Passwort, das für den Zugriff auf die Daten im Zertifikats-Archiv erforderlich ist, zum Beispiel der private Schlüssel.
  - [INLINE_CODE_13] – die Liste erlaubter URL-Domains oder Subdomains, die das Client-Zertifikat nutzen werden. Diese Liste kann aus mehreren URL-Mustern bestehen, die eine einzelne Domain, Subdomain oder einen Platzhalter für eine Domain und alle ihre Subdomains sein können. Mehr erfährst du unter [URL-Musterformat für Unternehmensrichtlinien]([LINK_URL_5]).

5. Führe einen Neustart der Uptrends Checkpoint-Software aus, indem du das [INLINE_CODE_14]-Skript aus dem Root-Verzeichnis der Installation ausführst.

6. Bestätige, dass sowohl das alte wie auch das neue Zertifikat erkannt werden und korrekt installiert sind. Sollte es Probleme geben, probiere diese einfachen Schritte zur Fehlerbehebung:

- Prüfe, dass der JSON-Dateiname korrekt ist.
- Stelle sicher, dass alle JSON-Schlüssel-Wert-Paare der korrekten JSON-Syntax folgen.
- Prüfe auf Falschkonfigurationen oder Probleme mit Berechtigungen.
