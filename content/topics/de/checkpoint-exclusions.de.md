{
  "hero": {
    "title": "Checkpoint-Ausschlüsse"
  },
  "title": "Checkpoint-Ausschlüsse",
  "summary": "Abhängig von der Region, aus der du testen möchtest, oder basierend auf vorherigen Ergebnissen möchtest du eventuell einige Checkpoints ausschließen.",
  "url": "/support/kb/synthetic-monitoring/checkpoints/checkpoint-ausschluesse",
  "translationKey": "https://www.uptrends.com/support/kb/checkpoints/checkpoint-exclusions"
}

Wir betreiben ein globales Netzwerk mit mehr als {{% Features/Variable variable="CheckpointCount" %}} Checkpoints, um sicherzustellen, dass deine Website weltweit rund um die Uhr verfügbar ist. Obwohl wir empfehlen, so viele Checkpoints wie möglich zu nutzen, bleibt dir die Wahl. Wir stellen vor: **Checkpoint-Ausschlüsse!**

{{< callout >}}
**Hinweis:** Du benötigst entweder einen Business oder Enterprise Account, um Checkpoints auszuschließen. Sollte es ein Problem mit einem bestimmten Checkpoint geben, reiche bitte ein [Support-Ticket]({{< ref path="contact" lang="de" >}}) ein.
{{< /callout >}}

## Checkpoint-Ausschlüsse hinzufügen

Es ist möglich, eine gesamte Region von Checkpoints (z. B. Kanada) ausgewählt (mit dem Vorteil, **automatisch neue Checkpoints zu erhalten, sowie sie zu der Region hinzugefügt werden**) zu lassen, aber mehr Kontrolle über einzelne Checkpoint-Standorte zu haben, die du auslassen möchtest.

Du kannst Ausschlüsse hinzufügen, indem du auf den Link {{< AppElement type="menuitem" >}}Ausschlüsse hinzufügen{{< /AppElement >}} im Text oben auf der Registerkarte {{< AppElement type="tab" >}}Checkpoints{{< /AppElement >}} klickst. Alle Checkpoints, die du angibst, werden übergangen, wenn die Überprüfungen für dein Prüfobjekt vorgenommen werden, ungeachtet der Auswahl, die du triffst.

![](/img/sub/support/checkpoint-exclusions.png)

Checkpoint-Ausschlüsse können bei unterschiedlichen Gelegenheiten praktisch sein. Einige Beispiele:

- Wenn der Checkpoint Kelowna (Kanada) unerwartete Ergebnisse liefert, kannst du Kanada als eine Region auswählen, aber Kelowna ausschließen.
- Deine Seite wird zum Beispiel in Berlin gehostet und du möchtest keine Messungen, die direkt aus der Nähe kommen. Statt eine Region, beispielsweise Deutschland ganz zu deaktivieren und individuelle Checkpoints einzeln zu aktivieren, kannst du einfach Ausschlüsse bestimmen.

{{< callout >}}
**Hinweis:** Du kannst nur **spezifische Checkpoints** ausschließen. Es ist nicht möglich, ganze Länder von einem ausgewählten Kontinent auszuschließen.
{{< /callout >}}
