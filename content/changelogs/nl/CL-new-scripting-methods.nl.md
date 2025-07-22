{
  "title": "Nieuwe scriptingmethodes zijn nu beschikbaar in Multi-step API (MSA)-controleregels",
  "date": "2025-03-12",
  "url": "/changelog/maart-2025-nieuwe-scriptingmethodes",
  "translationKey": "https://www.uptrends.com/changelog/march-2025-new-scripting-methods"
}

De volgende scriptingmethodes kunnen nu worden gebruikt in de tabbladen [Pre-request en Post-response scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#pre-request-and-post-response-scripts" lang="nl" >}}) van Multi-step API (MSA)-controleregels:

- `ut.crypto.cert.parseCrl(bytes)` — parseert een certificaatintrekkingslijst en retourneert de metadata.
- `ut.crypto.md5(value)` — genereert een MD5-hash van de opgegeven waarde.
- `ut.crypto.sha1(value)` — genereert een SHA-1-hash van de opgegeven waarde.
- `ut.crypto.sha256(value)` — genereert een SHA-256-hash van de opgegeven waarde.
- `ut.crypto.sha512(value)` — genereert een SHA-512-hash van de opgegeven waarde.
- `ut.response.bytes` — retourneert een byte-array met de response body. Responses zijn beperkt tot 100 MB.

Houd er rekening mee dat `ut.response.bytes` alleen beschikbaar is in het tabblad {{< AppElement type="tab" >}} Post-response {{< /AppElement >}} van uw MSA-controleregel. Met de scriptingmethodes voor het genereren van MD5- en SHA-hashes kunt u waarden veilig opslaan en verzenden, waardoor gegevensbescherming door hashing wordt gewaarborgd.