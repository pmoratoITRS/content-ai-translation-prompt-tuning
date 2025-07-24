{
  "hero": {
    "title": "DNS-Übersicht"
  },
  "title": "DNS-Übersicht",
  "summary": "Finde heraus, warum es Sinn macht, ein DNS-Prüfobjekt zu nutzen und wie du es einrichtest.",
  "url": "[URL_BASE_TOPICS]synthetic-monitoring/verfuegbarkeits-monitoring/dns/dns-ubersicht",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]",
  "sectionlist": false
}

Das Monitoring deines DNS ist eine tolle Möglichkeit, sicherzustellen, dass deine Nutzer deine Website und Services schnell, einfach und sicher aufrufen können.

Wir haben in unserem Artikel [Prüfobjekte hinzufügen]([LINK_URL_1]) beschrieben, wie ein Prüfobjekt erstellt wird. Hier sagen wir dir, wie speziell ein DNS-Prüfobjekt eingerichtet wird.

## Weshalb ein DNS Monitoring einsetzen?

Mit dieser Prüfung sendest du verschiedene Abfragen an einen DNS Nameserver. Der häufigste Aspekt, der geprüft wird, ist, ob der Domainname (www.yourcompany.com) noch auf die IP-Adresse deines Webservers verweist. Der Nameserver deines Internet-Anbieters ist die primäre, direkte Quelle für diese Information. Indem du diese DNS-Abfrage direkt überwachst, werden wir jegliche DNS-Probleme entdecken, noch bevor deine Website für Besucher und Kunden nicht verfügbar ist.

Das DNS Monitoring von Uptrends ermöglicht dir erweiterte DNS-Überprüfungen: Verifiziere Website-Domain-Namen (A- und CNAME-Einträge), Domain-Name-Mapping des Mail-Servers (MX-Einträge), DNS-Zonen-Delegationen (NS-Einträge), autoritative Informationen über DNS-Zonen (SOA-Einträge) und andere DNS-Informationen, die in TXT-Einträgen enthalten sind (einschließlich SPF-Daten für E-Mail-Authentifizierung).

## Ein DNS-Prüfobjekt einrichten

1. Rufe im Menü [SHORTCODE_3] Überwachung > Prüfobjekteinrichtung [SHORTCODE_4] auf und klicke auf die +-Schaltfläche.
2. Stelle den Prüfobjekttyp auf **DNS** ein.
3. Gib den **Namen** und das **Überwachungsintervall** an, das deinen Anforderungen an das DNS Monitoring am besten entspricht.
4. Wähle deine **IP-Version**. Wenn du mit IPv6 testest, hast du die Option, nur die Checkpoints zu wählen, die über ein natives IPV6 verfügen. Wenn du dies nicht aktivierst, werden die Checks von allen ausgewählten Checkpoints ausgeführt, die nativ IPV6 haben, und von IPV4-Checkpoints, die IPV6 emulieren.
5. Gib die **DNS-Serverinformation** ein mit dem *Domainnamen* oder der *IP-Adresse* des DNS-Servers, den du prüfen möchtest, zum Beispiel [INLINE_CODE_1].
6. Es ist wichtig, den **Port** deines DNS-Servers nachzusehen, um zu bestätigen, dass der Standard-Wert 53 lautet.
7. Wähle den **DNS Query**-Typ. Uptrends unterstützt *A Record*, *AAAA Record*, *CNAME Record*, *MX Record*, *NS Record*, *SOA Record*, *TXT Record* oder *Root-Server*.
8. Gib den Domainnamen, auf den du prüfen möchtest, in das Feld **Test Wert** ein, zum Beispiel [INLINE_CODE_2].
9. Gib das **Erwartete Ergebnis** in das dafür vorgesehene Feld ein.
    Zum Beispiel: Für einen Test auf einen Domainnamen deiner Website (eine A-Record-Abfrage) würdest du die IP-Adresse deines Domainnamens eingeben. Der Uptrends Service verifiziert dann, dass die Antwort von der DNS Query mit der IP-Adresse übereinstimmt.

    [SHORTCODE_1]**Tipp**: Wenn dein Domainname über mehrere IP-Adressen verfügt, kannst du einen regulären Ausdruck verwenden, um mehrere Werte abzugleichen.
    Beispiel: 1.2.3.4|5.6.7.8[SHORTCODE_2]
10.  Klicke auf die [SHORTCODE_5] Speichern [SHORTCODE_6]-Schaltfläche, wenn du fertig bist.
