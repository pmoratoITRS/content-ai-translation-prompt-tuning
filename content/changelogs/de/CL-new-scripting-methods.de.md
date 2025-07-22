{
  "title": "Neue Skriptmethoden sind bei Multi-Step API (MSA)-Prüfobjekten verfügbar",
  "date": "2025-03-12",
  "url": "/changelog/maerz-2025-neue-skriptmethoden",
  "translationKey": "https://www.uptrends.com/changelog/march-2025-new-scripting-methods"
}

Die folgenden Skriptmethoden können nun auf den Tabs für [Vor-Anfrage- und Nach-Antwort-Skripte]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#pre-request-and-post-response-scripts" lang="de" >}}) bei Multi-Step API (MSA)-Prüfobjekten verwendet werden:

- `ut.crypto.cert.parseCrl(bytes)` – parst eine Revozierungsliste von Zertifikaten und gibt ihre Metadaten zurück.
- `ut.crypto.md5(value)` – generiert einen MD5-Hash des angegebenen Werts.
- `ut.crypto.sha1(value)` – generiert einen SHA-1-Hash des angegebenen Werts.
- `ut.crypto.sha256(value)` – generiert einen SHA-256-Hash des angegebenen Werts.
- `ut.crypto.sha512(value)` – generiert einen SHA-512-Hash des angegebenen Werts.
- `ut.response.bytes` – gibt eine Byte-Zeichenfolge mit der Antwort aus. Antworten sind auf 100 MB begrenzt.

Beachte, dass `ut.response.bytes` nur auf dem Tab {{< AppElement type="tab" >}} Nach-Antwort {{< /AppElement >}} des MSA-Prüfobjekts verfügbar ist. Die Skriptmethoden zur Generierung von MD5- und SHA-Hashes ermöglichen dir, Werte sicher zu speichern und zu senden. Der Datenschutz wird durch das Hashen gewährleistet.