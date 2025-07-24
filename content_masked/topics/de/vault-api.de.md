{
  "hero": {
    "title": "Die Vault API"
  },
  "title": "Die Vault API",
  "url": "[URL_BASE_TOPICS]api/vault-api",
  "translationKey": "[FRONTMATTER_TRANSLATIONKEY]"
}

Die Vault wird verwendet um wiederverwertbare Daten, häufig sensible Daten wie Zertifikate, Public Keys und Benutzername-Password-Kombinationen, zu speichern Alle in der Vault gespeicherten Elemente werden *Vault Item* genannt. Vault Items sind in *Vault Bereiche* organisiert. Die Organisation von Elementen bzw. Items in unterschiedliche Bereiche ist auch hilfreich bei der Zugriffsbeschränkung für bestimmte Operatoren und Gruppen.

Hier beschreiben wir die verfügbaren API-Methoden für die Verwaltung von Vault Items, Vault Bereichen und Autorisierungen für Vault Bereiche. Für eine Beschreibung der Nutzungsszenarien der Vault lies bitte die [Vault-Einführung]([LINK_URL_1]). Um zu erfahren, wie du Zugriff auf die API erhältst, lies die [Einführung in API v4]([LINK_URL_2]).

## Vault Items

Dieses Endpunkteset lässt dich einzelne Vault Items abrufen, erstellen, aktualisieren und löschen. Aufgrund der Sensibilität einiger Vault-Item-Typen werden die sensiblen Daten selbst nie zurückgegeben.

### Beschreibung des Vault Item-Objekts

Die folgenden VaultItem-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name | Beschreibung |
|------|-----------------------------|
| [INLINE_CODE_1] | Die einzigartige Kennung des Vault Items. |
| [INLINE_CODE_2] | Der angezeigte Name des Vault Items. |
| [INLINE_CODE_3] | Die einzigartige Kennung des Vault Bereichs, in dem das Vault Item gespeichert ist. |
| [INLINE_CODE_4] | Gibt an, welche Objekt-Typen oder Prüfobjekte das Vault Item nutzen. |
| [INLINE_CODE_5] | Definiert den Typ des Vault Items. Die derzeit unterstützten Typen sind: [SHORTCODE_1] 

- [INLINE_CODE_6]: für Zertifikats-Archive (d. h. .pfx-Dateien), verwendet für Client-Zertifikate bei Multi-Step API-Prüfobjekten.
- [INLINE_CODE_7]: für öffentliche Schlüssel (Public Keys), genutzt für Single-Sign-on-Konfigurationen.
- [INLINE_CODE_8]: für Benutzername-Password-Kombinationen, die für Authentifizierungseinstellungen bei Prüfobjekten genutzt werden.
- [INLINE_CODE_9]: zur Dateiablage, genutzt bei Self-Service-Transaktionsprüfobjekten. Jedes Dateiformat wird unterstützt, maximale Dateigröße 2 MB.
- [INLINE_CODE_10]: zur Einmal-Passwort-Generation, enthält geheimen Wert und wird für die Zwei-Faktor-Authentifizierung genutzt.
[SHORTCODE_2] |
| [INLINE_CODE_11] | Der Wert, der im Vault Item gespeichert wird. Der Inhalt dieses Felds hängt vom Typ des Vault Items ab: [SHORTCODE_3]
- Für den Typ [INLINE_CODE_12]: Spezifiziere eine Base-64-Verschlüsselung für deine binäre .pfx-Datei, wenn du ein Vault Item dieses Typs erstellst oder aktualisierst. Wenn du das Element wieder abrufst, ist das Wert-Feld immer leer (da es sensible Informationen sind).
- Für Typ [INLINE_CODE_13]: Spezifiziere den Textinhalt deines Public Keys, wenn du ein Vault Item dieses Typs erstellst oder aktualisierst. Wenn du das Element wieder abrufst, enthält das Wert-Feld die Originaldaten des Public Keys.
- Für Typ [INLINE_CODE_14]: Dieses Feld ist unbenutzt. Verwende stattdessen die Benutzername- und Passwort-Felder.
[SHORTCODE_4] |
| [INLINE_CODE_15] | Gibt an, ob der Wert, der im Vault Item gespeichert wird, verschlüsselt ist. Wenn dies bei einem Vault Item auf wahr eingestellt ist, werden die gespeicherten Werte nicht in der Webanwendung oder in der API angezeigt. Dieser Wert sollte nicht bei Erstellen eines neuen Items angegeben werden: Die Elemente [INLINE_CODE_16] und [INLINE_CODE_17] sind immer verschlüsselt (da sie per Definition sensible Daten enthalten), während ein [INLINE_CODE_18] Public Key von seinem Wesen eine öffentliche Information ist und als reiner Text gespeichert werden kann. |
| [INLINE_CODE_19] | Anmerkungen oder Beschreibungen für dieses Vault Item. |
| [INLINE_CODE_20] | Der Benutzername des CredentialSets. |
| [INLINE_CODE_21] | Das Passwort des CredentialSets.

### Vault-Item-Endpunkte

Es gibt die folgenden API-Methoden:

| Abfragetyp | Endpunkt                    | Einsatz                                                               |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET          | [INLINE_CODE_22]                 | Gibt alle in Bereichen gespeicherten Vault Items aus, auf die der Nutzer Zugriff hat. |
| GET          | [INLINE_CODE_23] | Gibt das angegebene Vault Item aus.                                   |
| POST         | [INLINE_CODE_24]                 | Erstellt ein neues Vault Item mit den angegebenen Werten.                 |
| PUT          | [INLINE_CODE_25] | Aktualisiert das angegebene Vault Item.                                   |
| PATCH        | [INLINE_CODE_26] | Aktualisiert bestimmte Teile des angegebenen Vault Items zum Teil. [INLINE_CODE_27] und [INLINE_CODE_28] können nicht geändert werden und bleiben bei dieser Ausführung wie zuvor. |
| DELETE       | [INLINE_CODE_29] | Löscht das angegebene Vault Item.                                   |

#### GET /VaultItem

Die GET-Anfrage [INLINE_CODE_30] hat keine Parameter. Es gibt eine Liste der Vault Items aus, die in Bereichen gespeichert sind, auf die der Nutzer Anzeigezugriff hat.

Beispielinhalt:

[CODE_BLOCK_1]

#### GET /VaultItem/{VaultItemGuid}

Die GET-Anfrage [INLINE_CODE_31] wird das Vault Item ausgeben, das durch die Vault-Item-Guid identifiziert wird.

Beispiel eines Vault Items, das im Inhalt einer 200-Antwort zurückgegeben wird:
[CODE_BLOCK_2]

Bitte beachte, dass Werte, die sensible Informationen enthalten, als leerer String ausgegeben werden.

#### PUT /VaultItem/{VaultItemGuid}

Die PUT-Anfrage an Endpunkt [INLINE_CODE_32] wird das Vault Item, das durch die Vault-Item-Guid identifiziert wird, aktualisieren. Sobald du ein Vault Item aktualisierst, wird jedes Prüfobjekt, das eine Referenz zu diesem Vault Item enthält, auch aktualisiert, sodass deine Änderungen sofort in Kraft treten.

Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

Eine PUT-Anfrage erwartet die folgende Objektstruktur:
[CODE_BLOCK_3]

Bei dem obigen Beispiel würde das Anmerkungsfeld geleert, wenn im Original-Anmerkungsfeld des Vault Items ein Wert vorhanden gewesen wäre.[INLINE_CODE_33] Die einzigen Werte, die nicht angegeben werden müssen, sind die sensiblen Werte. Wenn du zum Beispiel den Wert im Password-Feld oder das gesamte CertificateArchive-Objekt auslässt, bleiben diese unverändert. Darüber hinaus können die Attribute IsSensitive und VaultSectionGuid nicht geändert werden.

#### DELETE /VaultItem/{VaultItemGuid}

Die DELETE-Anfrage an den Endpunkt [INLINE_CODE_34] löscht das angefragte Vault Item.

Wenn das angegebene Vault Item noch genutzt wird (zum Beispiel, wenn ein Prüfobjekt sich auf dieses spezielle Vault Item bezieht), gibt der Service den Statuscode 400 aus, einschließlich entsprechender Nachricht. Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

#### POST /VaultItem

Die POST-Anfrage an den Endpunkt [INLINE_CODE_35] erzeugt ein neues VaultItem-Objekt. Lasse bei der Angabe der VaultItem-Daten die VaultItemGuid aus: Die neue GUID für dieses Element wird als Teil der Antwort zurückgegeben. Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

Beispielinhalt:
[CODE_BLOCK_4]

## Vault Bereiche

Es gibt bei dieser API mehrere Endpunkte, anhand derer du die Vault Bereiche verwalten kannst. Jedes Vault Item gehört exakt zu einem Bereich. Werden nur wenige Vault Items für deinen gesamten Account benötigt, kannst du sie einfach in einem einzigen Vault Bereich speichern. Steigt jedoch die Anzahl der Vault Items in deinem Account, kann es eine gute Idee sein, sie in getrennte Bereiche zu organisieren.

Bei jedem Uptrends Account gibt es zu Beginn standardmäßig einen Vault Bereich. Die Gruppe der Administratoren hat auf diesen Bereich Vollzugriff, das heißt, sie können den Bereich und alle in ihm enthaltenen Vault Items bearbeiten.

Wenn ein neuer Vault Bereich erstellt wird, erhält der Nutzer (Operator), der mit dem API-Account verknüpft ist, von dem der Vault Bereich erstellt wird, automatisch die ChangeVaultSection-Autorisierung für den neuen Bereich. Es werden keine weiteren Autorisierungen erstellt.

### Beschreibung des Vault Bereich-Objekts

Das folgende VaultSection-Objekt wird in den nachfolgend beschriebenen API-Methoden verwendet:

| Name               | Beschreibung                                |
|--------------------|--------------------------------------------|
| [INLINE_CODE_36] | Die einzigartige Kennung des Vault Bereichs. |
| [INLINE_CODE_37]             | Der einzigartige Name des Vault Bereichs.              |

### Vault-Bereich-Endpunkte

| Abfragetyp | Endpunkt                          | Einsatz                                                      |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET          | [INLINE_CODE_38]                    | Gibt alle Bereiche aus, auf die der Nutzerkontext Zugriff hat. |
| GET          | [INLINE_CODE_39] | Gibt den angegebenen Vault Bereich aus.                       |
| POST         | [INLINE_CODE_40]                    | Erstellt einen neuen Vault Bereich mit dem angegebenen Namen.       |
| PUT          | [INLINE_CODE_41] | Aktualisiert den angegebenen Vault Bereich.                       |
| DELETE       | [INLINE_CODE_42] | Löscht den angegebenen Vault Bereich.                       |

#### POST /VaultSection

Die GET-Anfrage [INLINE_CODE_43] hat keine Parameter. Sie gibt eine Liste der Vault Bereiche aus, auf die der Nutzer Anzeigezugriff hat.

Beispielinhalt:
[CODE_BLOCK_5]

#### GET /VaultSection/{VaultSectionGuid}

Die GET-Anfrage [INLINE_CODE_44] wird den Vault Bereich ausgeben, der durch die Vault-Bereich-GUID identifiziert wird.

Beispielinhalt:
[CODE_BLOCK_6]


#### POST /VaultSection

Die POST-Anfrage an den Endpunkt [INLINE_CODE_45] erzeugt ein neues VaultSection-Objekt. Der Operator, mit dessen Nutzerkontext die Abfrage gestellt wird, erhält ViewVaultSection- und ChangeVaultSection-Autorisierungen für den neuen Bereich. Es werden keine weiteren Autorisierungen gewährt. Lasse bei der Angabe der VaultSection-Daten die VaultSectionGuid aus: Die neue GUID für dieses Element wird als Teil der Antwort zurückgegeben.
[CODE_BLOCK_7]

#### PUT /VaultSection/{VaultSectionGuid}

Die PUT-Anfrage an Endpunkt [INLINE_CODE_46] wird den Vault Bereich, der durch die Vault-Item-Guid identifiziert wird, aktualisieren. In der Regel ist der einzige Zweck die Änderung des Vault-Bereich-Namens. Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

[CODE_BLOCK_8]

#### DELETE /VaultSection/{VaultSectionGuid}

Die DELETE-Anfrage an den Endpunkt [INLINE_CODE_47] löscht den angefragten Vault Bereich.

Wenn der angegebene Vault Bereich noch genutzt wird (zum Beispiel, wenn in dem Vault Bereich noch Vault Items gespeichert sind), gibt der Service den Statuscode 400 aus, einschließlich entsprechender Nachricht. Wenn das der Fall ist, musst du die Vault Items erst löschen, bevor du den Vault Bereich löschen kannst. Beachte, dass du keine Vault Items löschen kannst, die noch in Verwendung sind (z. B. wenn das Vault Item noch von einem Prüfobjekt genutzt wird). Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

## Autorisierungen für Vault Bereiche

Neben der Trennung von Vault Items erlauben Vault Bereiche auch, dass sich steuern lässt, wer Zugriff auf welche Elemente hat. Wenn eine spezielle Operator-Gruppe exklusiven Zugriff auf bestimmte Vault Items haben soll, verschiebe diese Vault Items in einen separaten Bereich. Nur Personen, die Zugriff zu dem Vault Bereich haben, können die Vault Items sehen, die darin enthalten sind.

Sobald du den neuen Vault Bereich erstellt hast (entweder anhand der API oder der Online-App), ist der Bereich zunächst nur für dich sichtbar. Wenn du Vault Items hinzufügst, können andere Operatoren diese Vault Items nicht bearbeiten oder nutzen.

Damit andere diesen neuen Vault Bereich nutzen, Elemente hinzufügen und/oder diese Vault Items in Prüfobjekteinstellungen auswählen können, musst du ihnen Zugriff gewähren. Dies erreichst du anhand der folgenden API-Methoden.

Es gibt zwei Typen der Autorisierung: [INLINE_CODE_48] und [INLINE_CODE_49]. Diese Autorisierungstypen können Operatoren und Operator-Gruppen gewährt werden.

### Beschreibung des Autorisierungsobjekts

Die folgenden Autorisierungsobjekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name                | Beschreibung                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INLINE_CODE_50]   | Die einzigartige Kennung der Autorisierung.                                                                                                                        |
| [INLINE_CODE_51]         | Die einzigartige ID des Kontexts, für den die Autorisierung erstellt wurde. Im Falle der Vault Bereich-Autorisierung ist dies die Vault-Bereich-Guid. |
| [INLINE_CODE_52] | [INLINE_CODE_53] oder [INLINE_CODE_54].                                                                                                                |
| [INLINE_CODE_55]      | Wenn die Autorisierung für einen einzelnen Operator gilt, ist dies die Operator-Guid. Sie lautet [INLINE_CODE_56] bei Operator-Gruppen-Autorisierungen.             |
| [INLINE_CODE_57]   | Wenn die Autorisierung für eine Operator-Gruppe gilt, ist dies die Operator-Gruppen-ID. Sie lautet [INLINE_CODE_58] bei Autorisierungen für einzelne Operatoren.        |

### Autorisierungsendpunkte für Vault Bereiche

| Abfragetyp | Endpunkt                                                            | Einsatz                                                                                   |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET          | [INLINE_CODE_59]                     | Gibt eine Liste aller Autorisierungen für den angegebenen Vault Bereich aus.                   |
| POST         | [INLINE_CODE_60]                     | Erstellt eine neue Autorisierung für den angegebenen Vault Bereich mit den angegebenen Werten. |
| DELETE       | [INLINE_CODE_61] | Löscht die angegebene Autorisierung.                                                    |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

Die GET-Anfrage an [INLINE_CODE_62] gibt eine Liste aller Autorisierungen für den Vault Bereich, der in VaultSectionGuid angegeben ist.

Beispielinhalt:
[CODE_BLOCK_9]


Die Autorisierung gilt entweder für einen Operator oder eine Operator-Gruppe. Bei einer operatorspezifischen Autorisierung ist die OperatorGuid ausgefüllt und die OperatorGroupId leer. Bei einer Autorisierung für eine Operator-Gruppe wird die OperatorGroupId einen Wert enthalten und die OperatorGuid leer sein.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

Die POST-Anfrage an [INLINE_CODE_63] wird eine neue Autorisierung für den angegebenen Vault Bereich erstellen.

Beispielinhalt:

[CODE_BLOCK_10]

Wenn du eine Autorisierung des Typs ChangeVaultSection erstellst, wird automatisch eine zusätzliche ViewVaultSection-Autorisierung für den gleichen Operator oder die gleiche Operator-Gruppe hinzugefügt. Wenn ein Operator oder eine Operator-Gruppe für einen Vault Bereich über die Autorisierung Ändern + Anzeigen verfügt, wird dies als *Komplette Kontrolle* in der Uptrends App angezeigt.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

Die DELETE Anfrage an [INLINE_CODE_64] löscht die bestehende Autorisierung.
ende Autorisierung.
