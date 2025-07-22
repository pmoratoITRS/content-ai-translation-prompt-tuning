{
  "hero": {
    "title": "Arbeiten mit Domaingruppen"
  },
  "title": "Arbeiten mit Domaingruppen",
  "summary": "Verstehen Sie, was Domaingruppen sind und wie Sie sie beim Full Page Check Plus einrichten.",
  "url": "/support/kb/synthetic-monitoring/browser-monitoring/arbeiten-mit-domaingruppen",
  "translationKey": "https://www.uptrends.com/support/kb/full-page-check/working-with-domain-groups"
}

Der Full Page Check \+ (FPC\+) ermöglicht Ihnen, schnell die Quelle eines Seitenelements zu identifizieren. Üblicherweise bestehen Seiten aus vielen Elementen, die von unterschiedlichen Anbietern stammen. Beispielsweise erhalten Sie eventuell Inhalte von einem CDN oder Werbeinhalte von Google, während Social-Media-Plug-ins die aktuellsten Posts auf Ihrer Seite zeigen. Mithilfe von Domaingruppen können Sie die problematischen Quellen direkt identifizieren. Indem Sie sich die **Standard Vorlage** ansehen, erfahren Sie schnell mehr über das Verwalten von Domaingruppen.

{{< callout >}}
**Hinweis:** Informationen über die Anzeige der Seitenelemente nach Domaingruppen finden Sie in der Knowledge Base: [Interpretation der Ergebnisse des Wasserfallberichts]({{< ref path="support/kb/synthetic-monitoring/monitoring-results/interpreting-the-results-of-the-waterfall-report" lang="de" >}}).
{{< /callout >}}

## Die Standardvorlage

Uptrends stellt eine Standardvorlage für Domaingruppen bereit. Diese umfasst die am häufigsten genutzten Domains, sodass Sie möglicherweise nichts weiter unternehmen müssen. Aber wir leben natürlich nicht in einer Welt, in der jede Schablone passt, und die Standardvorlage erfüllt eventuell nicht Ihre Anforderung. Mit Uptrends haben Sie mehrere Optionen. Sie können

-   die Standardvorlage direkt ändern (nicht empfohlen)
-   die Standardvorlage kopieren und dann ändern oder
-   eine brandneue Domaingruppe von Grund auf schaffen

Bevor Sie sich durch die Domaingruppeneinstellungen kämpfen, sehen wir uns die Teile an, die eine Domaingruppe definieren.

{{< callout >}}
**Hinweis:** Wenn Sie die Standardvorlage öffnen (im nächsten Schritt), werden Sie die Schaltfläche {{< AppElement type="button" >}}Diese Domaingruppe kopieren{{< /AppElement >}} rechts oben auf der Seite bemerken. Wir empfehlen Ihnen, die Schaltfläche zu benutzen, statt die Standardvorlage direkt zu ändern.
{{< /callout >}}

### Aufrufen der Domaingruppen und der Standardvorlage

Wenn Sie die *Domaingruppen* zum ersten Mal aufrufen, wird nur eine Domaingruppe angezeigt, die **Standard Vorlage**.

Um die Seite der Domaingruppen aufzurufen

1.  Fahren Sie mit der Maus über **Account** im **Haupt**menü
2.  Klicken Sie auf **Domain Gruppen** im Abschnitt **Account Verwaltung** und
3.  klicken Sie auf **Standard Vorlage**, um den Editor zu öffnen.

![](/img/content/2d54879f-3e45-48d2-8144-fab3d5c4215d.png)

## Die definierten Gruppen

Sobald Sie die Standardvorlage aufgerufen haben, sehen Sie im Abschnitt **Gruppen** fünf Domaingruppen definiert. In jedem Abschnitt können Sie weitere Domains anhand der Schaltfläche {{< AppElement type="button" >}}Regel hinzufügen{{< /AppElement >}} aufnehmen. Sie können auch eine Regel ausschließen, indem Sie in der Regeldefinition links im Drop-down-Menü auf "Ausschließen" wechseln. Wenn Sie auf die Schaltfläche rechts von der Regel klicken, können Sie die Regel ganz entfernen.

#### 1st party

Wenn Sie auf den Pfeil neben **Name** klicken und die Gruppeninformation einblenden, sehen Sie, dass die Kontrollkästchen **Wählt automatisch alle Inhalte der Prüfobjekt URL aus** und **Dies ist First Party Content** aktiviert sind. Die Auswahl dieser Kontrollkästchen teilt dem System mit, dass alle Inhalte, die von der für das Prüfobjekt angegebenen URL ausgehen, eingeschlossen werden. First Party Content sind Ihre Inhalte, d. h. Sie selbst steuern diese Inhalte. Möglicherweise verfügen Sie auch über andere Domains, die zu den Inhalten auf dieser Seite beitragen. Stellen Sie sicher, dass Sie diese Domains anhand der Schaltfläche {{< AppElement type="button" >}}Regel hinzufügen{{< /AppElement >}} auflisten.

#### Statistics

Analyse-Content wird im Hintergrund ausgeführt und Analysedienste tragen häufig zu einer schlechten Lade-Performance von Seiten bei. Hier können Sie die URLs für alle von Ihnen genutzten Drittanbieter-Analysetools einfügen. Wenn Sie ein Monitoring mit Google Analytics durchführen möchten, stellen Sie sicher, dass Sie auf der Prüfobjektseite nicht das Kontrollkästchen **Google Analytics blockieren** aktiviert haben.

#### CDN

Manchmal fallen Content Delivery Networks (CDN) aus oder weisen Performance-Probleme auf. Indem Sie die URLs und Regeln für Ihre CDNs eingeben, können Sie deren Performance überwachen.

#### Social

Social-Media-Plug-ins erscheinen harmlos, aber häufig können Social-Media-Inhalte und Aktionsschaltflächen in Sachen Webperformance ein Chaos verursachen. Fügen Sie hier die URLs für Ihre Social-Media-Elemente ein. Uptrends hat bereits fünf der wichtigsten und am häufigsten genutzten Social-Media-URLs für Sie aufgelistet.

#### Ads

Wir haben alle die Klick-Köderseiten gesehen, die so viel Werbung auf einer Seite zeigen, dass Sie aufgeben, das tatsächlich Gesuchte zu sehen. Verhindern Sie, dass Ihre Werbeanbieter Ihre Seite zur Schnecke machen. Überwachen Sie Ihre Werbeanbieter, indem Sie die URLs im Abschnitt **Ads** eingeben.

## Eigene Gruppen hinzufügen

Natürlich können Sie eigene Regeln zu den vordefinierten Gruppen hinzufügen, aber die Standardvorlage lässt Sie drei weitere Gruppen am Ende der Seite einrichten. Denken Sie daran, auf {{< AppElement type="savebutton" >}}Speichern{{< /AppElement >}} zu klicken, bevor Sie die Seite verlassen.
