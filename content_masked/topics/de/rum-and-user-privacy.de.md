{
  "hero": {
    "title": "RUM und Nutzer-Datenschutz"
  },
  "title": "RUM und Nutzer-Datenschutz",
  "summary": "Das Tracking von realen Nutzer-Performance-Daten kann Bedenken zum Datenschutz in Deinem Unternehmen hervorrufen. Erfahre, wie Uptrends die Privatsphäre des Nutzers schützt und was Du noch wissen musst.",
  "url": "[URL_BASE_TOPICS]rum/rum-und-nutzer-datenschutz",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Der Nutzer-Datenschutz ist wichtig. In diesem Artikel erläutern wir, wie Uptrends die Daten Deiner Besucher nutzt und welche weiteren Schritte Du zum Schutz Deiner Marke und der Privatsphäre des Nutzers unternehmen kannst.

## Privatsphäre, persönliche Daten und das Datenschutzgesetz

Wenn ein Website-Besucher Deine Website aufruft, sendet das RUM-Script in Deinen Seiten eine kleine Anfrage an Uptrends. Es liegt in der Natur des Internets, dass wir auch die IP-Adresse mit der Anfrage erhalten. Wir wissen um den sensiblen Charakter des Erhalts dieser Information, da das System die IP-Adresse verwenden kann, um einzelne Nutzer zu identifizieren und nachzuverfolgen. Wir haben RUM von Grund auf so entwickelt, dass Du die vollständige Kontrolle hältst, wie die IP-Adressen Deiner Besucher verarbeitet werden. Die zwei Hauptaspekte dafür sind:

-   Wir bieten eine IP-Adressen-Anonymisierung auf mehreren Ebenen.
-   Wir speichern IP-Adressen nicht langfristig.

### IP-Adressen-Anonymisierung auf mehreren Ebenen

Um Dir das Herkunftsland (und in manchen Fällen Bundeslandinformationen für Australien, Kanada und den USA) zu nennen, verwendet Uptrends die IP-Adresse. Uptrends identifiziert und erfasst keine persönlichen Daten von den Besuchern Deiner Website und verfolgt sie auch nicht. Wenn die Datenschutzrichtlinie Deiner Website jedoch nicht gestattet, dass Uptrends die volle IP-Adresse Deiner Besucher auf irgendeine Weise nutzt, bieten wir zwei Stufen der Anonymisierung:

-   **Stufe 0:** Die volle IP-Adresse wird verwendet. Dies ist die Standardeinstellung.
-   **Stufe 1:** Wir setzen vor der Prüfung das letzte (zur Identifizierung nützlichste) Oktett der IP-Adresse auf Null.
-   **Stufe 2:** Wir setzen vor der Prüfung die zwei letzten Oktetts der IP-Adresse auf Null.

**Beispiel:** Mit Stufe 1 ändern wir die Original-IP-Adresse [INLINE_CODE_1], die zu [INLINE_CODE_2] wird. Mit der Anonymisierung in Stufe 2 erhalten wir [INLINE_CODE_3].

[SHORTCODE_1]
**Hinweis:** Uptrends speichert keine originalen oder anonymisierten IP-Adressen langfristig (siehe unten).
[SHORTCODE_2]

Indem wir die wichtigsten Teile der IP-Adresse entfernen (hinsichtlich eindeutig identifizierbarer Netzwerk-Adresse), erhalten wir nur einen sehr allgemeinen Eindruck des Standorts jedes Besuchers. Das heißt, je höher der Grad der Anonymisierung, desto weniger genau werden Informationen zu Land und Bundesland sein.

### Festlegen der Anonymisierungsstufe

Solltest Du keine IP-Anonymisierung benötigen, kannst Du das reguläre RUM-Script ohne weitere Konfiguration nutzen. Die Stufen 1 und 2 erfordern kleine Änderungen am Script.

In dem in Deinen Webseiten eingefügten RUM Script wirst Du sehen, dass der AIP-Parameter standardmäßig auf 0 gesetzt ist. **Setze diesen Wert auf 1 für Anonymisierung Stufe 1 und 2 für Anonymisierung Stufe 2.**

**Zum Beispiel:**

[INLINE_CODE_4]

Das Script sendet den Anonymisierungswert mit jeder RUM-Anfrage, die als Teil Deiner Webseiten ausgeführt wird, und die von Dir festgelegte Anonymisierungsstufe tritt sofort in Kraft.

### Wir speichern IP-Adressen nicht langfristig

Wenn Du Dich für die IP-Anonymisierung entscheidest, garantieren wir, dass wir die Original-IP-Adressen nicht untersuchen und diese nicht speichern, weder auf Festplatte, noch auf Wechselmedien oder sonstigen Geräten oder Speichereinrichtungen. Der allererste Schritt in unserer Pipeline besteht darin, die IP-Adressen zu anonymisieren, bevor wir sie auswerten.

Darüber hinaus **verwahren wir nur die IP-Adressinformationen temporär**, bis wir die Originalanfrage durch unsere gesamte Pipeline verarbeitet haben. Danach löschen wir die Informationen. Die Löschung umfasst jede Kombination der IP-Adressinformation, Nutzer-Agent-Daten, URLs, Daten, Zeiten und Zeitzoneninformationen.

## Real User Monitoring und Dein Datenschutzhinweis

Manchmal fragen Kunden des Real User Monitoring, was sie auf ihrer Website dem Datenschutzhinweis hinzufügen müssen. Wir sind natürlich keine Juristen, aber Du solltest eventuell den folgenden Passus in Deine Datenschutzrichtlinie aufnehmen.

*&lt;Dein Markenname hier&gt; nutzt das Uptrends Real User Monitoring, um die Performance zu messen, wie sie vom Website-Besucher erlebt wird. Uptrends verwendet keine Cookies, um Daten zu sammeln oder die Besucher unserer Website zu verfolgen. Stattdessen setzt Uptrends eine kleine Scriptdatei auf unserer Seite ein, die die Performance-Daten für die Besucher unserer Website an die Server von Uptrends sendet. Die von jedem Besucher erfassten Daten umfassen die IP-Adressen, Gerätetypen, Betriebssysteme und verwendeten Browser. Auf Uptrends’ Servern werden die Performance-Daten aller unserer Website-Besucher zusammengefasst und uns mit Informationen bereitgestellt, die uns ermöglichen, das Nutzererlebnis auf der Website auf Grundlage der oben genannten Informationen zu verbessern. Uptrends nutzt die IP-Adressen unserer Website-Besucher, um Informationen über den Staat oder das Land des Besuchers zu erhalten, aber nichts Sonstiges. Darüber hinaus speichert Uptrends IP-Adressen nicht langfristig und Uptrends verfolgt und teilt auch keine Informationen über einzelne Nutzer an Drittparteien mit.*

### Sollten die Anonymisierungsstufen 1 oder 2 genutzt werden, kann Folgendes optional in den Datenschutzhinweis aufgenommen werden 

*Zum Schutz der Privatsphäre der Website-Besucher wird eine Version der Scriptdatei von Uptrends verwendet, bei der die IP-Adresse vor ihrer Verarbeitung anonymisiert wird. Die IP-Adresse wird niemals gespeichert und wird niemals zu etwas anderem genutzt als der Bestimmung des Ursprungslandes.*
