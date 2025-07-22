{
  "hero": {
    "title": "Subaccount – Einrichtung"
  },
  "title": "Subaccount – Einrichtung",
  "summary": "In diesem Artikel erläutern wir die Einrichtung eines neuen Subaccounts.",
  "url": "[URL_BASE_TOPICS]account/nutzer/subaccounts/sub-account-einrichtung",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

## Einen Subaccount erstellen

Um einen Subaccount zu erstellen:

1.  Rufe den Operator-Hub über [SHORTCODE_5] Accounteinstellungen > Operator, Gruppen und Subaccounts [SHORTCODE_6] auf.
2.  Klicke auf [SHORTCODE_7] Subaccount hinzufügen [SHORTCODE_8] im Bereich Subaccounts.

Nun kannst du auf den Registerkarten der Seite *Neuer Subaccount* einige Angaben zum Subaccount machen.

## Allgemein
### Subaccount Info

1.  Gib einen **Subaccount Namen** an. Nach dem Speichern wird dies der Name sein, der verwendet wird, um eine Prüfobjektgruppe und Operator-Gruppe zu erstellen.
2.  Füge einen **Kunden Bezug** (optional) ein.

### Berechtigung

In diesem Abschnitt bestimmst du, ob die Operatoren des Subaccounts Prüfobjekte ändern oder hinzufügen können.

1.  Aktiviere das Kontrollkästchen **Änderungen von Prüfobjekten zulassen**, um Operatoren zu gestatten, Einstellungen anzupassen. Das Aktivieren dieser Funktion erlaubt Subaccount-Besitzer auch, zusätzliche Operatoren hinzuzufügen. Sie können jedoch keine Operatoren löschen.
2.  Aktiviere das Kontrollkästchen **Hinzufügen von Prüfobjekten zulassen**, um Operatoren eines Subaccounts zu gestatten, eigene Prüfobjekte einzurichten. Wenn sie Prüfobjekte einrichten dürfen, kannst du angeben, wie viele sie hinzufügen dürfen. Dafür steht das Feld **Maximale Anzahl von Prüfobjekten** zur Verfügung.

[SHORTCODE_1]
**Hinweis**: Wenn in einem Subaccount Prüfobjekte hinzugefügt werden, unterliegt das neue Prüfobjekt der Verfügbarkeit auf Basis nicht genutzter Prüfobjekte des primären Accounts. Wenn in einem primären Account keine Prüfobjekte mehr verfügbar sind, kann in einem Subaccount kein neues Prüfobjekt hinzugefügt werden, selbst wenn die maximale Anzahl hier noch nicht erreicht ist.
[SHORTCODE_2]

### Neues Prüfobjekt – Info

Die Erstellung eines Subaccounts erfordert, dass du Informationen für ein HTTP/HTTPS-Prüfobjekt angibst. Wähle den **Prüfobjekt Typ** und gib eine **Prüfobjekt URL** für das neue Prüfobjekt ein. Uptrends wird dieses Prüfobjekt zu einer Prüfobjektgruppe mit dem gleichen Namen wie den des Subaccounts hinzufügen.

## SLA

Wenn mit dem neuen Subaccount-Besitzer eine SLA besteht, lege die Anforderungen für die SLA auf der Registerkarte [SHORTCODE_9]SLA[SHORTCODE_10] fest. Solltest du Infos zur Einrichtung eines SLA-Monitorings benötigen, leitet dich unser [SLA-Bereich]([LINK_URL_1]) durch den Vorgang.

## Weitere Prüfobjekte

Auf der Registerkarte [SHORTCODE_11]Weitere Prüfobjekte[SHORTCODE_12] kannst du bereits bestehende Prüfobjekte hinzufügen. Du kannst auch später noch neue Prüfobjekte hinzufügen.

## Operatoren

Auf dieser Registerkarte kannst du bestehende Operatoren für den Subaccount aus der Liste auswählen. Subaccount-Operatoren können nur zur Gruppe *Jeder* und zu ihrer Subaccount-Gruppe gehören.

## Speichern

Klicke auf [SHORTCODE_13]Speichern[SHORTCODE_14], um den neuen Subaccount und das neue Prüfobjekt zu erstellen.

[SHORTCODE_3]
**Hinweis**: Sollen die Subaccount-Operatoren Warnmeldungen erhalten, musst du eine neue [Meldedefinition]([LINK_URL_2]) erstellen. Wenn Alarme per SMS oder Telefon/Sprachnachricht gemeldet werden sollen, gib die Mobiltelefonnummern bei den [Operator-Einstellungen]([LINK_URL_3]) an.
[SHORTCODE_4]
