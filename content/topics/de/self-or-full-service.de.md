{
  "hero": {
    "title": "Optionen für Transaktionsskripte"
  },
  "title": "Optionen für Transaktionsskripte",
  "summary": "Dir stehen mehrere Optionen zur Verfügung, wenn es um das entgültige Skript für deine Transaktionen geht: vom Full Service über den Self Service bis hin zum selbstständigen Skript schreiben.",
  "url": "/support/kb/synthetic-monitoring/transaktionen/self-oder-full-service",
  "translationKey": "https://www.uptrends.com/support/kb/transactions/self-or-full-service"
}

Ein Transaktionsprüfobjekt benötigt ein Skript, mit dem die Schritte, die du überwachen möchtest, abgebildet werden. Je nachdem, wie du mit dem Programmieren vertraut bist, gibt es mehrere Optionen, wie du ein Transaktionsskript handhabst.

- **Benötigst du viel Hilfe**, kann der Uptrends Support das SkriptSchreiben und Testen im Rahmen von [Full-Service Transactions](#full-service) für dich übernehmen.
-   **Wenn du relativ vertraut mit Webtechnologien** wie HTML, CSS, JSON und XPath bist, sind [Self-Service Transactions](#self-service) das Richtige für dich.
-   **Bist du quasi ein Power-User**, kannst du direkt vom visuellen zum Skript-Editor wechseln und aus deinem eigenen Programmiertool kopieren und ein [Skript von Grund auf schreiben](#script-from-scratch). Du kannst deine Transaktionen und Skripte auch über die Uptrends [API]({{< ref path="support/kb/api" lang="de" >}}) verwalten.

Bevor du Skripte für deine Transaktionen erzeugst, solltest du dich für eine Methode entscheiden. Unser [Support]({{< ref path="contact" lang="de" >}}) steht aber immer bereit, dir gegebenenfalls weiterzuhelfen.

## Full-Service Transactions {id="full-service"}

Du zeichnest deine Transaktionen auf, lädst sie hoch, wobei du „Full-Service“ wählst, und Uptrends’ Skript-Entwickler nutzen deine Aufzeichnung, um deine Skripte zu bearbeiten und zu testen. Der gesamte Full-Service-Ablauf dauert etwa eine Woche ab Einreichung deiner Aufzeichnung, bis du ein vollständig eingerichtetes Prüfobjekt in deinem Account erhältst und die [Skriptüberprüfungsrichtlinie]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="de" >}}) gilt.

### Weshalb solltest du Full-Service Transactions nutzen?

Jeder kann die Full-Service-Option nutzen und unser Support freut sich, dir bei deinen Prüfobjekten zu helfen. Du solltest Full-Service Transactions wählen, wenn:

-   du nicht vertraut mit Skripttechnologien wie HTML, CSS, JSON und XPath bist;
-   du einfach keine Zeit oder keine Ressourcen für die Aufgabe bereitstellen kannst;
-   du es einfach nicht selbst machen möchtest.

### Was ist zu tun?

Wenn du Full-Service Transactions wählst, musst du:

1.  den Ablauf deiner Transaktionen üben, um eine saubere Aufzeichnung zu erhalten;
2.  [die Transaktion aufzeichnen]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}});
3.  deine Aufzeichnung für die weitere Skripterstellung hochladen. Nach Beenden der Aufzeichnung, kannst du „Full-Service Transactions“ wählen und die Aufzeichnung beim Support einreichen.

Der Upload-Vorgang erzeugt ein Prüfobjekt mit Anzeigeberechtigung in deinem Account, während das Prüfobjekt sich im Full-Service-Ablauf befindet. Sobald das Skript fertig und getestet ist, benachrichtigen dich die Skript-Entwickler von Uptrends, dass das Prüfobjekt bereitsteht und in deinem Account entsperrt wurde. Bitte lies unsere [Skriptüberprüfungsrichtlinie]({{< ref path="support/kb/synthetic-monitoring/transactions/transaction-script-review-policy" lang="de" >}}), um weitere Informationen über die Dauer der Skripterstellung bei Full-Service Transactions und die Beschränkung hinsichtlich der Zahl eingereichter Aufzeichnungen enthält.

{{< callout >}}
**Hinweis**: Solltest du weitere Infos zum Verständnis des Web Application Monitorings oder einen systematischen Ansatz für deine Transaktionen benötigen, haben wir weitere hilfreiche Artikel bereitgestellt: [Das Web Application Monitoring verstehen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring" lang="de" >}}) und [Deine Transaktionen verstehen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-your-transactions" lang="de" >}}).
{{< /callout >}}

## Self-Service Transactions {id="self-service"}

Bei Self-Service Transactions hast du die komplette Kontrolle über die Erstellung der Transaktionsskripte. Dir stehen die folgenden Optionen zur Verfügung, um deine Skripte zu erstellen:

- Nutze den [Transaktions-Recorder]({{< ref path="support/kb/synthetic-monitoring/transactions/download-and-use-the-transaction-recorder" lang="de" >}}), um den Großteil deiner Arbeit zu erledigen und dann das Skript anhand des [Step-Editors]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}) zu verfeinern.
- Übergehe den Transaktions-Recorder und nutze direkt den [Step-Editor]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}), um deine Skripte von Grund auf im visuellen Schritte-Editor zu erstellen.

Wir empfehlen, mit dem Recorder zu beginnen, da es alles ein bisschen einfacher macht.

### Wer sollte Self-Service Transactions nutzen?

Wir empfehlen jedem, Self-Service Transactions zu nutzen oder auszuprobieren. Es kostet nichts, Skripte im Entwicklungsmodus zu bearbeiten und zu testen. Vielleicht macht es dir sogar Spaß, deine Transaktionsskripte zu bearbeiten und zu testen. Unser [Support]({{< ref path="contact" lang="de" >}}) steht aber immer bereit, dir gegebenenfalls weiterzuhelfen oder die komplette Erstellung zu übernehmen. Du solltest Self-Service Transactions wählen, wenn:

- du vertraut mit grundlegender Webtechnologie bist und in der Regel klarkommst;
- du vertraut mit Client-seitigen Technologien wie HTML, CSS, JSON und XPath bist;

### Was ist zu tun?

1. [Den Transaktionsrekorder herunterladen und nutzen]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-web-application-monitoring#programming-skills" lang="de" >}}) – als einfacher Start.
2.  Öffne dein neues Prüfobjekt in deinem Uptrends Account und [bearbeite und teste]({{< ref path="support/kb/synthetic-monitoring/transactions/understanding-the-step-editor" lang="de" >}}) es.

## Skriptentwicklung von Grund auf {id="scripting-from-scratch"}

Für den Power-User gibt es eine dritte Option. Solltest du dich dafür entscheiden, übergehe den Transaktions-Recorder und den Step-Editor und gib dein Skript direkt in den Transaktionseinstellungen über den Text-Editor ein. Klicke einfach auf {{< AppElement type="button" >}}Wechsle zum Skript{{< /AppElement >}} oben auf der Registerkarte {{< AppElement type="tab" >}}Schritte{{< /AppElement >}}, um den Text-Editor zu öffnen und dein Skript zu bearbeiten oder einzufügen.

Du kannst auch die [API]({{< ref path="support/kb/api" lang="de" >}}) nutzen, um neue Transaktionsprüfobjekte zu erstellen, zu bearbeiten und zu testen.
