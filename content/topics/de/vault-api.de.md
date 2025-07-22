{
  "hero": {
    "title": "Die Vault API"
  },
  "title": "Die Vault API",
  "url": "/support/kb/api/vault-api",
  "translationKey": "https://www.uptrends.com/support/kb/api/vault-api"
}

Die Vault wird verwendet um wiederverwertbare Daten, häufig sensible Daten wie Zertifikate, Public Keys und Benutzername-Password-Kombinationen, zu speichern Alle in der Vault gespeicherten Elemente werden *Vault Item* genannt. Vault Items sind in *Vault Bereiche* organisiert. Die Organisation von Elementen bzw. Items in unterschiedliche Bereiche ist auch hilfreich bei der Zugriffsbeschränkung für bestimmte Operatoren und Gruppen.

Hier beschreiben wir die verfügbaren API-Methoden für die Verwaltung von Vault Items, Vault Bereichen und Autorisierungen für Vault Bereiche. Für eine Beschreibung der Nutzungsszenarien der Vault lies bitte die [Vault-Einführung]({{< ref path="/support/kb/account/vault" lang="de" >}}). Um zu erfahren, wie du Zugriff auf die API erhältst, lies die [Einführung in API v4]({{< ref path="/support/kb/api/v4" lang="de" >}}).

## Vault Items

Dieses Endpunkteset lässt dich einzelne Vault Items abrufen, erstellen, aktualisieren und löschen. Aufgrund der Sensibilität einiger Vault-Item-Typen werden die sensiblen Daten selbst nie zurückgegeben.

### Beschreibung des Vault Item-Objekts

Die folgenden VaultItem-Objekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name | Beschreibung |
|------|-----------------------------|
| `VaultItemGuid` | Die einzigartige Kennung des Vault Items. |
| `Name` | Der angezeigte Name des Vault Items. |
| `VaultSectionGuid	` | Die einzigartige Kennung des Vault Bereichs, in dem das Vault Item gespeichert ist. |
| `VaultItemUsedBy` | Gibt an, welche Objekt-Typen oder Prüfobjekte das Vault Item nutzen. |
| `VaultItemType` | Definiert den Typ des Vault Items. Die derzeit unterstützten Typen sind: {{< tableformatter >}} 

- `CertificateArchive`: für Zertifikats-Archive (d. h. .pfx-Dateien), verwendet für Client-Zertifikate bei Multi-Step API-Prüfobjekten.
- `Certificate`: für öffentliche Schlüssel (Public Keys), genutzt für Single-Sign-on-Konfigurationen.
- `CredentialSet`: für Benutzername-Password-Kombinationen, die für Authentifizierungseinstellungen bei Prüfobjekten genutzt werden.
- `File`: zur Dateiablage, genutzt bei Self-Service-Transaktionsprüfobjekten. Jedes Dateiformat wird unterstützt, maximale Dateigröße 2 MB.
- `OneTimePassword`: zur Einmal-Passwort-Generation, enthält geheimen Wert und wird für die Zwei-Faktor-Authentifizierung genutzt.
{{< /tableformatter >}} |
| `Value` | Der Wert, der im Vault Item gespeichert wird. Der Inhalt dieses Felds hängt vom Typ des Vault Items ab: {{< tableformatter >}}
- Für den Typ `CertificateArchive`: Spezifiziere eine Base-64-Verschlüsselung für deine binäre .pfx-Datei, wenn du ein Vault Item dieses Typs erstellst oder aktualisierst. Wenn du das Element wieder abrufst, ist das Wert-Feld immer leer (da es sensible Informationen sind).
- Für Typ `Certificate`: Spezifiziere den Textinhalt deines Public Keys, wenn du ein Vault Item dieses Typs erstellst oder aktualisierst. Wenn du das Element wieder abrufst, enthält das Wert-Feld die Originaldaten des Public Keys.
- Für Typ `CredentialSet`: Dieses Feld ist unbenutzt. Verwende stattdessen die Benutzername- und Passwort-Felder.
{{< /tableformatter >}} |
| `IsSensitive` | Gibt an, ob der Wert, der im Vault Item gespeichert wird, verschlüsselt ist. Wenn dies bei einem Vault Item auf wahr eingestellt ist, werden die gespeicherten Werte nicht in der Webanwendung oder in der API angezeigt. Dieser Wert sollte nicht bei Erstellen eines neuen Items angegeben werden: Die Elemente `CertificateArchive` und `CredentialSet` sind immer verschlüsselt (da sie per Definition sensible Daten enthalten), während ein `Certificate` Public Key von seinem Wesen eine öffentliche Information ist und als reiner Text gespeichert werden kann. |
| `Notes` | Anmerkungen oder Beschreibungen für dieses Vault Item. |
| `UserName` | Der Benutzername des CredentialSets. |
| `Password` | Das Passwort des CredentialSets.

### Vault-Item-Endpunkte

Es gibt die folgenden API-Methoden:

| Abfragetyp | Endpunkt                    | Einsatz                                                               |
|--------------|-----------------------------|---------------------------------------------------------------------|
| GET          | `VaultItem`                 | Gibt alle in Bereichen gespeicherten Vault Items aus, auf die der Nutzer Zugriff hat. |
| GET          | `VaultItem/{VaultItemGuid}` | Gibt das angegebene Vault Item aus.                                   |
| POST         | `VaultItem`                 | Erstellt ein neues Vault Item mit den angegebenen Werten.                 |
| PUT          | `VaultItem/{VaultItemGuid}` | Aktualisiert das angegebene Vault Item.                                   |
| PATCH        | `VaultItem/{VaultItemGuid}` | Aktualisiert bestimmte Teile des angegebenen Vault Items zum Teil. `VaultItemType` und `VaultItemUsedBy` können nicht geändert werden und bleiben bei dieser Ausführung wie zuvor. |
| DELETE       | `VaultItem/{VaultItemGuid}` | Löscht das angegebene Vault Item.                                   |

#### GET /VaultItem

Die GET-Anfrage `VaultItem` hat keine Parameter. Es gibt eine Liste der Vault Items aus, die in Bereichen gespeichert sind, auf die der Nutzer Anzeigezugriff hat.

Beispielinhalt:

```json
[
  {
    "VaultItemGuid": " FE1656C1-A606-43BB-BD61-1EEE9715EE9E ",
    "Name": "Web shop test login",
    "Value": "",
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "test@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
    "VaultItemUsedBy": "1 monitor"
  },
  {
    "VaultItemGuid": "A9CB1BE3-1715-4C31-9040-51CBBFAE23CB",
    "Name": "Marketing web site login",
    "Value": "",
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F ",
    "VaultItemType": "CredentialSet",
    "IsSensitive": true,
    "Notes": "This is not a real account",
    "UserName": "testmarketing@acme.com",
    "Password": "",
    "CertificateArchive": {
      "Issuer": "",
      "NotBefore": "",
      "NotAfter": "",
      "Password": "",
      "ArchiveData": ""
    },
  "VaultItemUsedBy": "-"
  }
]
```

#### GET /VaultItem/{VaultItemGuid}

Die GET-Anfrage `VaultItem/{VaultItemGuid}` wird das Vault Item ausgeben, das durch die Vault-Item-Guid identifiziert wird.

Beispiel eines Vault Items, das im Inhalt einer 200-Antwort zurückgegeben wird:
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "IsSensitive": true,
  "Notes": "Certificate archive test",
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Issuer": "Acme Corp, Inc.",
    "NotBefore": "2018-06-12T14:10:50.489Z",
    "NotAfter": "2020-06-12T14:10:50.489Z",
    "Password": "",
    "ArchiveData": ""
  },
  "VaultItemUsedBy": "1 monitor"
}
```

Bitte beachte, dass Werte, die sensible Informationen enthalten, als leerer String ausgegeben werden.

#### PUT /VaultItem/{VaultItemGuid}

Die PUT-Anfrage an Endpunkt `VaultItem/{VaultItemGuid}` wird das Vault Item, das durch die Vault-Item-Guid identifiziert wird, aktualisieren. Sobald du ein Vault Item aktualisierst, wird jedes Prüfobjekt, das eine Referenz zu diesem Vault Item enthält, auch aktualisiert, sodass deine Änderungen sofort in Kraft treten.

Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

Eine PUT-Anfrage erwartet die folgende Objektstruktur:
```json
{
  "VaultItemGuid": "FE1656C1-A606-43BB-BD61-1EEE9715EE9E",
  "Name": "Test certificate archive",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CredentialSet",
  "IsSensitive": true,
  "UserName": "",
  "Password": "",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

Bei dem obigen Beispiel würde das Anmerkungsfeld geleert, wenn im Original-Anmerkungsfeld des Vault Items ein Wert vorhanden gewesen wäre.`If you omit a parameter, it will not remain unchanged, but be considered empty.` Die einzigen Werte, die nicht angegeben werden müssen, sind die sensiblen Werte. Wenn du zum Beispiel den Wert im Password-Feld oder das gesamte CertificateArchive-Objekt auslässt, bleiben diese unverändert. Darüber hinaus können die Attribute IsSensitive und VaultSectionGuid nicht geändert werden.

#### DELETE /VaultItem/{VaultItemGuid}

Die DELETE-Anfrage an den Endpunkt `VaultItem/{VaultItemGuid}` löscht das angefragte Vault Item.

Wenn das angegebene Vault Item noch genutzt wird (zum Beispiel, wenn ein Prüfobjekt sich auf dieses spezielle Vault Item bezieht), gibt der Service den Statuscode 400 aus, einschließlich entsprechender Nachricht. Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

#### POST /VaultItem

Die POST-Anfrage an den Endpunkt `VaultItem` erzeugt ein neues VaultItem-Objekt. Lasse bei der Angabe der VaultItem-Daten die VaultItemGuid aus: Die neue GUID für dieses Element wird als Teil der Antwort zurückgegeben. Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

Beispielinhalt:
```json
{
  "Name": "Test certificate archive",
  "Value": "",
  "VaultSectionGuid": "141D9649-0CE7-4748-AA0D-D3021D0D5A47",
  "VaultItemType": "CertificateArchive",
  "Notes": "Certificate archive test",
  "CertificateArchive": {
    "Password": "TheOtherPassword",
    "ArchiveData": "[your base64-encoded private certificate]"
  }
}
```

## Vault Bereiche

Es gibt bei dieser API mehrere Endpunkte, anhand derer du die Vault Bereiche verwalten kannst. Jedes Vault Item gehört exakt zu einem Bereich. Werden nur wenige Vault Items für deinen gesamten Account benötigt, kannst du sie einfach in einem einzigen Vault Bereich speichern. Steigt jedoch die Anzahl der Vault Items in deinem Account, kann es eine gute Idee sein, sie in getrennte Bereiche zu organisieren.

Bei jedem Uptrends Account gibt es zu Beginn standardmäßig einen Vault Bereich. Die Gruppe der Administratoren hat auf diesen Bereich Vollzugriff, das heißt, sie können den Bereich und alle in ihm enthaltenen Vault Items bearbeiten.

Wenn ein neuer Vault Bereich erstellt wird, erhält der Nutzer (Operator), der mit dem API-Account verknüpft ist, von dem der Vault Bereich erstellt wird, automatisch die ChangeVaultSection-Autorisierung für den neuen Bereich. Es werden keine weiteren Autorisierungen erstellt.

### Beschreibung des Vault Bereich-Objekts

Das folgende VaultSection-Objekt wird in den nachfolgend beschriebenen API-Methoden verwendet:

| Name               | Beschreibung                                |
|--------------------|--------------------------------------------|
| `VaultSectionGuid` | Die einzigartige Kennung des Vault Bereichs. |
| `Name`             | Der einzigartige Name des Vault Bereichs.              |

### Vault-Bereich-Endpunkte

| Abfragetyp | Endpunkt                          | Einsatz                                                      |
|--------------|-----------------------------------|------------------------------------------------------------|
| GET          | `VaultSection`                    | Gibt alle Bereiche aus, auf die der Nutzerkontext Zugriff hat. |
| GET          | `VaultSection/{VaultSectionGuid}` | Gibt den angegebenen Vault Bereich aus.                       |
| POST         | `VaultSection`                    | Erstellt einen neuen Vault Bereich mit dem angegebenen Namen.       |
| PUT          | `VaultSection/{VaultSectionGuid}` | Aktualisiert den angegebenen Vault Bereich.                       |
| DELETE       | `VaultSection/{VaultSectionGuid}` | Löscht den angegebenen Vault Bereich.                       |

#### POST /VaultSection

Die GET-Anfrage `VaultSection` hat keine Parameter. Sie gibt eine Liste der Vault Bereiche aus, auf die der Nutzer Anzeigezugriff hat.

Beispielinhalt:
```json
[
  {
    "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "Name": "Vault items"
  },
  {
    "VaultSectionGuid": "3A3C0CE8-9931-4312-8A15-00017CBB615F",
    "Name": "Marketing web site vault items"
  }
]
```

#### GET /VaultSection/{VaultSectionGuid}

Die GET-Anfrage `VaultSection/{VaultSectionGuid}` wird den Vault Bereich ausgeben, der durch die Vault-Bereich-GUID identifiziert wird.

Beispielinhalt:
```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Vault items"
}
```


#### POST /VaultSection

Die POST-Anfrage an den Endpunkt `VaultSection` erzeugt ein neues VaultSection-Objekt. Der Operator, mit dessen Nutzerkontext die Abfrage gestellt wird, erhält ViewVaultSection- und ChangeVaultSection-Autorisierungen für den neuen Bereich. Es werden keine weiteren Autorisierungen gewährt. Lasse bei der Angabe der VaultSection-Daten die VaultSectionGuid aus: Die neue GUID für dieses Element wird als Teil der Antwort zurückgegeben.
```json
{
  "Name": "Development vault items"
}
```

#### PUT /VaultSection/{VaultSectionGuid}

Die PUT-Anfrage an Endpunkt `VaultSection/{VaultSectionGuid}` wird den Vault Bereich, der durch die Vault-Item-Guid identifiziert wird, aktualisieren. In der Regel ist der einzige Zweck die Änderung des Vault-Bereich-Namens. Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

```json
{
  "VaultSectionGuid": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "Name": "Web shop vault items"
}
```

#### DELETE /VaultSection/{VaultSectionGuid}

Die DELETE-Anfrage an den Endpunkt `VaultSection/{VaultSectionGuid}` löscht den angefragten Vault Bereich.

Wenn der angegebene Vault Bereich noch genutzt wird (zum Beispiel, wenn in dem Vault Bereich noch Vault Items gespeichert sind), gibt der Service den Statuscode 400 aus, einschließlich entsprechender Nachricht. Wenn das der Fall ist, musst du die Vault Items erst löschen, bevor du den Vault Bereich löschen kannst. Beachte, dass du keine Vault Items löschen kannst, die noch in Verwendung sind (z. B. wenn das Vault Item noch von einem Prüfobjekt genutzt wird). Diese Anfrage erfordert eine ChangeVaultSection-Autorisierung.

## Autorisierungen für Vault Bereiche

Neben der Trennung von Vault Items erlauben Vault Bereiche auch, dass sich steuern lässt, wer Zugriff auf welche Elemente hat. Wenn eine spezielle Operator-Gruppe exklusiven Zugriff auf bestimmte Vault Items haben soll, verschiebe diese Vault Items in einen separaten Bereich. Nur Personen, die Zugriff zu dem Vault Bereich haben, können die Vault Items sehen, die darin enthalten sind.

Sobald du den neuen Vault Bereich erstellt hast (entweder anhand der API oder der Online-App), ist der Bereich zunächst nur für dich sichtbar. Wenn du Vault Items hinzufügst, können andere Operatoren diese Vault Items nicht bearbeiten oder nutzen.

Damit andere diesen neuen Vault Bereich nutzen, Elemente hinzufügen und/oder diese Vault Items in Prüfobjekteinstellungen auswählen können, musst du ihnen Zugriff gewähren. Dies erreichst du anhand der folgenden API-Methoden.

Es gibt zwei Typen der Autorisierung: `ViewVaultSection` und `ChangeVaultSection`. Diese Autorisierungstypen können Operatoren und Operator-Gruppen gewährt werden.

### Beschreibung des Autorisierungsobjekts

Die folgenden Autorisierungsobjekte werden in den nachfolgend beschriebenen API-Methoden verwendet:

| Name                | Beschreibung                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AuthorizationId`   | Die einzigartige Kennung der Autorisierung.                                                                                                                        |
| `ContextId`         | Die einzigartige ID des Kontexts, für den die Autorisierung erstellt wurde. Im Falle der Vault Bereich-Autorisierung ist dies die Vault-Bereich-Guid. |
| `AuthorizationType` | `ViewVaultSection` oder `ChangeVaultSection`.                                                                                                                |
| `OperatorGuid`      | Wenn die Autorisierung für einen einzelnen Operator gilt, ist dies die Operator-Guid. Sie lautet `null` bei Operator-Gruppen-Autorisierungen.             |
| `OperatorGroupId`   | Wenn die Autorisierung für eine Operator-Gruppe gilt, ist dies die Operator-Gruppen-ID. Sie lautet `null` bei Autorisierungen für einzelne Operatoren.        |

### Autorisierungsendpunkte für Vault Bereiche

| Abfragetyp | Endpunkt                                                            | Einsatz                                                                                   |
|--------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| GET          | `VaultSection/{VaultSectionGuid}/Authorization`                     | Gibt eine Liste aller Autorisierungen für den angegebenen Vault Bereich aus.                   |
| POST         | `VaultSection/{VaultSectionGuid}/Authorization`                     | Erstellt eine neue Autorisierung für den angegebenen Vault Bereich mit den angegebenen Werten. |
| DELETE       | `VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}` | Löscht die angegebene Autorisierung.                                                    |

#### GET /VaultSection/{VaultSectionGuid}/Authorization

Die GET-Anfrage an `VaultSection/{VaultSectionGuid}/Authorization` gibt eine Liste aller Autorisierungen für den Vault Bereich, der in VaultSectionGuid angegeben ist.

Beispielinhalt:
```json
[
  {
    "AuthorizationId": "7210DD2D-3AAE-4F89-A2A8-000060F118F1 ",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ChangeVaultSection",
    "OperatorGuid": "5F71AFD7-8BEE-4C8D-9827-A107308473BE",
    "OperatorGroupId": ""
  },
  {
    "AuthorizationId": "0BACEE61-0582-40FD-B1A2-00034401421A",
    "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
    "AuthorizationType": "ViewVaultSection",
    "OperatorGuid": "",
    "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
  }
]
```


Die Autorisierung gilt entweder für einen Operator oder eine Operator-Gruppe. Bei einer operatorspezifischen Autorisierung ist die OperatorGuid ausgefüllt und die OperatorGroupId leer. Bei einer Autorisierung für eine Operator-Gruppe wird die OperatorGroupId einen Wert enthalten und die OperatorGuid leer sein.

#### POST /VaultSection/{VaultSectionGuid}/Authorization

Die POST-Anfrage an `VaultSection/{VaultSectionGuid}/Authorization` wird eine neue Autorisierung für den angegebenen Vault Bereich erstellen.

Beispielinhalt:

```json
{
  "ContextId": "8D4BAED2-56C2-4220-B36D-00013511D234",
  "AuthorizationType": "ViewVaultSection",
  "OperatorGuid": "",
  "OperatorGroupId": "629F7189-6706-4DC2-989E-99DF511B09CB"
}
```

Wenn du eine Autorisierung des Typs ChangeVaultSection erstellst, wird automatisch eine zusätzliche ViewVaultSection-Autorisierung für den gleichen Operator oder die gleiche Operator-Gruppe hinzugefügt. Wenn ein Operator oder eine Operator-Gruppe für einen Vault Bereich über die Autorisierung Ändern + Anzeigen verfügt, wird dies als *Komplette Kontrolle* in der Uptrends App angezeigt.

#### DELETE /VaultSection/{VaultSectionGuid}/Authorization/{AuthorizationGuid}

Die DELETE Anfrage an `VaultSection/{VaultSectionGuid}/ Authorization/AuthorizationGuid` löscht die bestehende Autorisierung.
ende Autorisierung.
