{
  "title": "Public-Key-Informationen zu Uptrends’ Client-Zertifikat",
  "summary": "Der Einsatz von Uptrends’ öffentlichem Schlüssel bei deinen Multi-Step API-Prüfobjekt-Requests, um sicherzustellen, dass API-Prüfobjekt-Abfragen von Uptrends stammen.",
  "url": "/support/kb/synthetic-monitoring/api-monitoring/uptrends-client-zertifikat-informationen-oeffentlicher-schluessel",
  "translationKey": "https://www.uptrends.com/support/kb/api-monitoring/uptrends-client-certificate-public-key-information"
}

Das Uptrends Client-Zertifikat kann in Prüfobjekten des Multi-Step API Monitorings genutzt werden, um die Authentizität der HTTP-Abfrage zu gewährleisten, die von deinen Prüfobjekten erstellt wurde: Dein API-Server kann die Identität des Checkpoint-Servers von Uptrends verifizieren – dem Ort, von dem die HTTP-Anfragen gesendet werden.

Die Checkpoint-Server nutzen den privaten Schlüssel des Zertifikats, um die Anfrage zu signieren. Niemand sonst hat Zugang zu dem privaten Schlüssel, also kann niemand die Anfrage auf gleiche Weise signieren und vorgeben, Uptrends zu sein. Das bedeutet, dass du als empfangende Partei sicherstellen kannst, dass die Abfragen tatsächlich von Uptrends‘ Servern stammen. Dies geschieht, indem du die Identität der eingehenden Abfrage anhand des entsprechenden öffentlichen Schlüssels (Public Key) von Uptrends verifizierst. Public-Key-Informationen zu Uptrends Client-Zertifikat stehen unten.

{{< callout >}}
**Bitte beachte:** Das Client-Zertifikat von Uptrends ist nicht für [private (Container-)Checkpoints]({{< ref path="support/kb/synthetic-monitoring/checkpoints/" lang="de" >}}) verfügbar.
{{< /callout >}}



## Wie kann ich sicher sein, dass dieser Public Key echt ist?

Bei der Feststellung der Identität und Authentizität ist es wichtig, sicherzustellen, dass du mit den richtigen Informationen arbeitest.

### Vertrauenswürdige Verbindung und Übertragung

-   Wir haben sichergestellt, dass du die Inhalte dieser Seite immer über eine HTTPS-Verbindung siehst. Diese sichere Verbindung bedeutet, dass niemand den Inhalt während der Übertragung vom Webserver zu deinem Browser widerrechtlich ändern kann (kein Content-Hijacking).
-   Selbst wenn jemand es schafft, dir in böser Absicht einen HTTP-Link (d. h. eine nicht sichere Verbindung) auf eine Website von Uptrends zu senden, der schließlich abgefangen werden könnte und bei dem die Inhalte gefälscht sind (ein sogenannter Downgrade-Angriff), wird dies dein Browser nicht akzeptieren. Browser werden sich weigern, Uptrends über eine nicht sichere Verbindung aufzurufen, aus folgenden Gründen:
    -   Die Website von Uptrends und das Kunden-App-Portal befolgen eine HTTP Strict Transport Security (HSTS)-Richtlinie. Das bedeutet, dass Browser die Anweisung erhalten, niemals einem nicht sicheren HTTP-Link zur Domain uptrends.com zu folgen, sondern stattdessen immer HTTPS zu nutzen.
    -   Die Domain uptrends.com war unter den ersten 1.000 Domains, die in der HSTS-Preload-Liste aufgenommen wurde. Diese Preload-Liste ist in Mainstream-Browsern wie Chrome, Edge, Opera und Safari hartcodiert. Das bedeutet, diese Browser werden immer und ohne Ausnahme HTTPS für uptrends.com und seine Sub-Domains verwenden.

### Vertrauenswürdige Identität

Wenn du das TLS-Zertifikat für diese Website prüfst, wirst du feststellen, dass die Website Uptrends B.V. gehört. Das Zertifikat ist von Sectigo Limited signiert, eine der weltweit anerkannten Zertifizierungsstellen. Dein Browser würde nicht einmal der Verbindung vertrauen, wenn sie nicht von einer Zertifizierungsstelle signiert ist. Dies ist die beste Möglichkeit zu beweisen, dass die von dir besuchte Domain tatsächlich Uptrends gehört und du tatsächlich darauf vertrauen kannst, dass die Inhalte von Uptrends stammen.

## Public-Key-Informationen

Die folgenden Informationen beschreiben die Eigenschaften des Public Keys, der zum Client-Zertifikat von Uptrends‘ Checkpoint-Server passt, wenn sie dazu angewiesen sind, sie zu nutzen. Dieses Client-Zertifikat, genauso wie die Zertifikate, die zu unserer Website gehören, wurden von einer Zertifizierungsstelle signiert.

<table>
  <thead>
    <tr>
      <th class="cell-small"></th>
      <th class="cell-extralarge"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="bold">Aussteller</td>
      <td>CN = Sectigo RSA Client Authentication and Secure Email CA <br>O = Sectigo Limited<br>L = Salford<br>S = Greater Manchester<br>C = GB</td>
    </tr>
    <tr>
      <td class="bold">Subjekt</td>
      <td>E = certificates@uptrends.com</td>
    </tr>
    <tr>
      <td class="bold">Allgemeiner Name</td>
      <td>Uptrends</td>
    </tr>
    <tr>
      <td class="bold">Seriennummer</td>
      <td>1a223e5481b066dfda30e5f35cdb3a81</td>
    </tr>
    <tr>
      <td class="bold">Ablaufdatum</td>
      <td>Sunday, 27 July 2025 01:59:59</td>
    </tr>
    <tr>
      <td class="bold">Öffentlicher Schlüssel (Base64)</td>
      <td>—–BEGIN CERTIFICATE—– <br>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<br>—–END CERTIFICATE—–<br></td>
    </tr>
  </tbody>
</table>
