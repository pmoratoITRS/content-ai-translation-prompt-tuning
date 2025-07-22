{
  "hero": {
    "title": "IP-Adressen für Whitelists"
  },
  "title": "IP-Adressen für Whitelists",
  "summary": "Uptrends‘ gesamte Services, einschließlich des Anwendungsportals, der Websites, der Uptrends API und aller anderen Services, die mit Uptrends, Uptrends Infra und Uptrends Real User Monitoring in Verbindung stehen, werden von mehreren Standorten mit mehreren IP-Adressen bedient.",
  "url": "/support/kb/account/ip-adressen-fuer-whitelists",
  "translationKey": "https://www.uptrends.com/support/kb/account/ip-addresses-for-whitelisting"
}

{{< callout >}}
**Hinweis:** Suchst du die Liste der **Checkpoint-IP-Adressen**, um sie auf deine Whitelist zu setzen, damit deine Prüfobjekte richtig ausgeführt werden können? Siehe dir die komplette Liste der [Checkpoint-IP-Adressen von Uptrends]({{< ref path="/checkpoints" lang="de" >}}) an.
{{< /callout >}}

Mehrere Services werden von Uptrends Synthetics, Uptrends Infra und Uptrends Real User Monitoring genutzt. Diese Services umfassen das Anwendungsportal, die Websites, die Uptrends API und mehr. Sie werden von mehreren Standorten mit mehreren IP-Adressen bedient. Beispielsweise kann sich die Adresse, zu der die Domain api.uptrends.com aufgelöst wird, alle fünf Minuten ändern. Das gilt für alle Subdomains von uptrends.com.

{{< callout >}}
**Tipp:** Wenn du unsere Anwendungen auf eine Whitelist setzen musst, empfehlen wir dir, die uptrends.com-Domains und Subdomains (nur für HTTPS sowie für IPv4 und IPv6) in die Whitelist aufzunehmen. Damit bist du von jeglichen Änderungen, die bei unseren IP-Adressen vorgenommen werden könnten, unabhängig.
{{< /callout >}}

 Bitte setze diese Reihe von IPv6-Adressen auf deine Whitelist:

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64 

Die folgenden Tabellen zeigen, welche jeweiligen IPv4/IPv6-Adressen für bestimmte Services auf die Whitelist gesetzt werden müssen.

## Uptrends Synthetics
| URL                       | IP-Adresse oder Bereiche                   | Verwendet für                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| `api.uptrends.com`          | {{< tableformatter >}} 
- 178.162.179.211
- 95.211.70.211 {{< /tableformatter >}}  | API Communication (Synthetics) |
| `app.uptrends.com`          | {{< tableformatter >}} 
- 178.162.179.213
- 95.211.70.213 {{< /tableformatter >}}  | Uptrends Anwendung |
| `customername.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.205
- 95.211.70.205 {{< /tableformatter >}} | {{< tableformatter >}} 
SP-initiiertes SSO
Weitere Infos findest du unter [Überblick – Single Sign-On]({{< ref path="support/kb/account/settings/single-sign-on-overview#how-sso-users-log-in" lang="de" >}}), *Anmeldung von SSO-Nutzern*, Option 2. {{< /tableformatter >}} |
| `status.uptrends.com`       | {{< tableformatter >}} 
- 178.162.179.217
- 95.211.70.217  {{< /tableformatter >}} | Public Status Pages |
| `www.uptrends.com`          | {{< tableformatter >}}
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  {{< /tableformatter >}}| Downloads |

## Uptrends Infra
| URL                       | IP-Adresse oder Bereiche                   | Verwendet für                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
|  `api.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.210
- 95.211.70.210 {{< /tableformatter >}} |  API Communication (Infra) | 
|  `app.uptrendsinfra.com` | {{< tableformatter >}} 
- 178.162.179.208
- 95.211.70.208 {{< /tableformatter >}} |  Uptrends Infra Anwendung | 
|  `collector.uptrends.com` | {{< tableformatter >}} 
- 178.162.179.209
- 95.211.70.209 {{< /tableformatter >}} |  {{< tableformatter >}}
Von Agents gesendete Daten
Der Rechner, auf dem der Agent installiert ist, benötigt Zugang hierzu! {{< /tableformatter >}} |
| `www.uptrends.com`| {{< tableformatter >}} 
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5{{< /tableformatter >}} |  Downloads, z. B. die Agent-Updates | 

## Uptrends RUM

| URL                 | Verwendet für                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `code.highcharts.com` | Notwendig zur Anzeige von Karten in der RUM Übersicht. Der Rechner, der das Dashboard anzeigt, muss auf diese Domain zugreifen können.

## Alarme

| IP-Adresse oder Bereich                                                        | Verwendet für          |
|----------------------------------------------------------------------------|-------------------|
| {{< tableformatter >}}
- 168.245.61.22
- 178.162.179.193 
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 {{< /tableformatter >}} | Alarmierung per E-Mail |
| {{< tableformatter >}} 
- 95.211.70.193
- 178.162.179.193{{< /tableformatter >}} | Alarmierung über benutzerdefinierte Integrationen |