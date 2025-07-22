{
  "hero": {
    "title": "IP-Adressen für Whitelists"
  },
  "title": "IP-Adressen für Whitelists",
  "summary": "Uptrends‘ gesamte Services, einschließlich des Anwendungsportals, der Websites, der Uptrends API und aller anderen Services, die mit Uptrends, Uptrends Infra und Uptrends Real User Monitoring in Verbindung stehen, werden von mehreren Standorten mit mehreren IP-Adressen bedient.",
  "url": "[URL_BASE_TOPICS]account/ip-adressen-fuer-whitelists",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

[SHORTCODE_27]
**Hinweis:** Suchst du die Liste der **Checkpoint-IP-Adressen**, um sie auf deine Whitelist zu setzen, damit deine Prüfobjekte richtig ausgeführt werden können? Siehe dir die komplette Liste der [Checkpoint-IP-Adressen von Uptrends]([LINK_URL_1]) an.
[SHORTCODE_28]

Mehrere Services werden von Uptrends Synthetics, Uptrends Infra und Uptrends Real User Monitoring genutzt. Diese Services umfassen das Anwendungsportal, die Websites, die Uptrends API und mehr. Sie werden von mehreren Standorten mit mehreren IP-Adressen bedient. Beispielsweise kann sich die Adresse, zu der die Domain api.uptrends.com aufgelöst wird, alle fünf Minuten ändern. Das gilt für alle Subdomains von uptrends.com.

[SHORTCODE_29]
**Tipp:** Wenn du unsere Anwendungen auf eine Whitelist setzen musst, empfehlen wir dir, die uptrends.com-Domains und Subdomains (nur für HTTPS sowie für IPv4 und IPv6) in die Whitelist aufzunehmen. Damit bist du von jeglichen Änderungen, die bei unseren IP-Adressen vorgenommen werden könnten, unabhängig.
[SHORTCODE_30]

 Bitte setze diese Reihe von IPv6-Adressen auf deine Whitelist:

- 2001:1af8:4300:b152::0/64
- 2001:1af8:8100:b001::0/64 

Die folgenden Tabellen zeigen, welche jeweiligen IPv4/IPv6-Adressen für bestimmte Services auf die Whitelist gesetzt werden müssen.

## Uptrends Synthetics
| URL                       | IP-Adresse oder Bereiche                   | Verwendet für                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
| [INLINE_CODE_1]          | [SHORTCODE_1] 
- 178.162.179.211
- 95.211.70.211 [SHORTCODE_2]  | API Communication (Synthetics) |
| [INLINE_CODE_2]          | [SHORTCODE_3] 
- 178.162.179.213
- 95.211.70.213 [SHORTCODE_4]  | Uptrends Anwendung |
| [INLINE_CODE_3] | [SHORTCODE_5] 
- 178.162.179.205
- 95.211.70.205 [SHORTCODE_6] | [SHORTCODE_7] 
SP-initiiertes SSO
Weitere Infos findest du unter [Überblick – Single Sign-On]([LINK_URL_2]), *Anmeldung von SSO-Nutzern*, Option 2. [SHORTCODE_8] |
| [INLINE_CODE_4]       | [SHORTCODE_9] 
- 178.162.179.217
- 95.211.70.217  [SHORTCODE_10] | Public Status Pages |
| [INLINE_CODE_5]          | [SHORTCODE_11]
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5  [SHORTCODE_12]| Downloads |

## Uptrends Infra
| URL                       | IP-Adresse oder Bereiche                   | Verwendet für                                                    |
|---------------------------|---------------------------------------|-------------------------------------------------------------|
|  [INLINE_CODE_6] | [SHORTCODE_13] 
- 178.162.179.210
- 95.211.70.210 [SHORTCODE_14] |  API Communication (Infra) | 
|  [INLINE_CODE_7] | [SHORTCODE_15] 
- 178.162.179.208
- 95.211.70.208 [SHORTCODE_16] |  Uptrends Infra Anwendung | 
|  [INLINE_CODE_8] | [SHORTCODE_17] 
- 178.162.179.209
- 95.211.70.209 [SHORTCODE_18] |  [SHORTCODE_19]
Von Agents gesendete Daten
Der Rechner, auf dem der Agent installiert ist, benötigt Zugang hierzu! [SHORTCODE_20] |
| [INLINE_CODE_9]| [SHORTCODE_21] 
- 95.211.70.203
- 195.201.9.51
- 104.194.9.119
- 2001:1af8:4300:b152:1::203
- 2a01:4f8:13b:f1c::
- 2605:9880:300:600:44:3770:c7c4:5[SHORTCODE_22] |  Downloads, z. B. die Agent-Updates | 

## Uptrends RUM

| URL                 | Verwendet für                                                                                                                      |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_10] | Notwendig zur Anzeige von Karten in der RUM Übersicht. Der Rechner, der das Dashboard anzeigt, muss auf diese Domain zugreifen können.

## Alarme

| IP-Adresse oder Bereich                                                        | Verwendet für          |
|----------------------------------------------------------------------------|-------------------|
| [SHORTCODE_23]
- 168.245.61.22
- 178.162.179.193 
- 178.162.179.195
- 95.211.70.193
- 95.211.70.195 [SHORTCODE_24] | Alarmierung per E-Mail |
| [SHORTCODE_25] 
- 95.211.70.193
- 178.162.179.193[SHORTCODE_26] | Alarmierung über benutzerdefinierte Integrationen |