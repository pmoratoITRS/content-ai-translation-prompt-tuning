{
  "title": "New scripting methods are now available in Multi-step API (MSA) monitors",
  "date": "2025-03-12",
  "url": "/changelog/march-2025-new-scripting-methods",
  "translationKey": "https://www.uptrends.com/changelog/march-2025-new-scripting-methods"
}

The following scripting methods can now be used in the [Pre-request and Post-response scripting]({{< ref path="/support/kb/synthetic-monitoring/api-monitoring/multi-step-custom-scripting#pre-request-and-post-response-scripts" lang="en" >}}) tabs of Multi-step API (MSA) monitors:

- `ut.crypto.cert.parseCrl(bytes)` — parses a certificate revocation list and returns its metadata.
- `ut.crypto.md5(value)` — generates an MD5 hash of the specified value.
- `ut.crypto.sha1(value)` — generates an SHA-1 hash of the specified value.
- `ut.crypto.sha256(value)` — generates an SHA-256 hash of the specified value.
- `ut.crypto.sha512(value)` — generates an SHA-512 hash of the specified value.
- `ut.response.bytes` — returns a byte array containing the response body. Responses are limited to 100 MB.

Note that `ut.response.bytes` is only available in the {{< AppElement type="tab" >}} Post-response {{< /AppElement >}} tab of your MSA monitor. The scripting methods for generating MD5 and SHA hashes enable you to store and send values securely, ensuring data protection through hashing.