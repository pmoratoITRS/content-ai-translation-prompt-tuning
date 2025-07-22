{
  "hero": {
    "title": "Preise für das Parallel-Monitoring"
  },
  "title": "Preise für das Parallel-Monitoring",
  "summary": "In diesem Artikel erfährst du, nach welchen Formeln die Credits des Parallel-Monitorings berechnet werden. Dazu gibt es Beispiele.",
  "url": "/support/kb/synthetic-monitoring/parallel-monitoring/preisberechnung-beispiele",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/pricing-calculation-examples"
}

## Preise für Full Page Checks (FPC) und Transaktionsprüfobjekte

Der Preis wird anhand des Credit-Systems berechnet, bei dem unterschiedliche Prüfobjekttypen unterschiedliche Grundpreise haben – als Credit ausgedrückt. Im Allgemeinen ist die Berechnung wie folgt:

Preis = Grundpreis des Prüfobjekts x Anzahl der Checkpoints, die die Prüfung ausführen

### Vergleichsbeispiel

Die folgende Tabelle zeigt anhand eines Beispiels wie das Preissystem funktioniert – als Vergleich zwischen parallelem und klassischem Monitoring.

<table><colgroup><col style="width: 50%"/><col style="width: 50%"/></colgroup><thead><tr class="header"><th>Parallel-Monitoring</th><th>Standard-Monitoring</th></tr></thead><tbody><tr class="odd"><td>Transaktion (Grundpreis 4 Credits), benutzerdefiniert auf 3 Checkpoints ausgeführt<br />
4 Credits x 3 = <strong>12 Credits</strong></td><td>Transaktion (Grundpreis 4 Credits)<br />
4 Credits x 1 = <strong>4 Credits</strong></td></tr></tbody></table>

## Preise für einfache Prüfobjekte und Multi-step API (MSA)-Prüfobjekte 

Für diese Prüfobjekte wird ein Preisstufenmodell mit einem Skalierungsfaktor angesetzt. Die Preisberechnung unterscheidet sich daher zu der von Full Page Checks und Transaktionsprüfobjekten. Einfache Prüfobjekte umfassen Ping, Http(s), SSL-Zertifikate usw. Bedenke auch, dass der Preis bei einem MSA-Prüfobjekt von der Anzahl der Schritte abhängt. Unten findest du die Preisformel.

**Einfache Prüfobjekte**

Preis = Grundpreis des Prüfobjekts x Skalierungsfaktor aus der Preisstufentabelle unten

**MSA-Prüfobjekt**

Preis = Anzahl der Schritte des MSA-Prüfobjekts x Skalierungsfaktor aus der Preisstufentabelle unten

### Preisstufentabelle {id="tiered-pricing-table"}

<table>
  <colgroup><col style="width: 50%"/><col style="width: 50%"/></colgroup>
  <thead><tr class="header"><th>Anzahl Checkpoints</th><th>Skalierungsfaktor</th></tr></thead>
  <tbody>
    <tr><td>1 bis 2</td><td>N/A (siehe Hinweis am Ende d. Tabelle)</td></tr>
    <tr><td>3 bis 4</td><td>2</td></tr>
    <tr><td>5 bis 7</td><td>3</td></tr>
    <tr><td>8 bis 10</td><td>4</td></tr>
    <tr><td>11 bis 14</td><td>5</td></tr>
    <tr><td>15 bis 18</td><td>6</td></tr>
    <tr><td>19 bis 22</td><td>7</td></tr>
    <tr><td>23 bis 26</td><td>8</td></tr>
    <tr><td>27 bis 30</td><td>9</td></tr>
    <tr><td>31 bis 35</td><td>10</td></tr>
    <tr><td>36 bis 40</td><td>11</td></tr>
    <tr><td>41 bis 45</td><td>12</td></tr>
    <tr><td>46 bis 50</td><td>13</td></tr>
  </tbody>
</table>

{{< callout >}} **Hinweis**: Du musst mindestens drei (hoch verfügbare) oder fünf (unter allen) Checkpoints wählen, um das Parallel-Monitoring zu nutzen. Für das Standard-Monitoring musst du ebenfalls mindestens drei Checkpoints auswählen, aber es wird jeweils nur einer zum jeweiligen Testzeitpunkt eingesetzt (und in der Preisberechnung berücksichtigt). {{< /callout >}}
### Vergleichsbeispiele

Die folgenden Tabellen zeigen anhand von Beispielen, wie das Preissystem funktioniert – als Vergleich zwischen parallelem und Standard-Monitoring und für unterschiedliche Level beim Preisstufenmodell.

**Einfache Prüfobjekte**

<table><colgroup><col style="width: 50%"/><col style="width: 50%"/></colgroup>
  <thead><tr class="header"><th>Parallel-Monitoring (Preisstufen)</th><th>Standard-Monitoring</th></tr></thead>
  <tbody>
    <tr><td>HTTPS-Prüfobjekt (Grundpreis 1 Credit), benutzerdefiniert auf 4 Checkpoints ausgeführt<br />
1 Credit x 2 (Skalierungsfaktor) = <strong>2 Credits</strong></td><td>HTTPS-Prüfobjekt (Grundpreis 1 Credit)<br />
1 Credit x 1 = <strong>1 Credit</strong></td></tr>
    <tr><td>HTTPS-Prüfobjekt (Grundpreis 1 Credit), benutzerdefiniert auf 10 Checkpoints ausgeführt<br />
1 Credit x 4 (Skalierungsfaktor) = <strong>4 Credits</strong></td><td>HTTPS-Prüfobjekt (Grundpreis 1 Credit)<br />
1 Credit x 1 = <strong>1 Credit</strong></td></tr>
  </tbody>
</table>

**Multi-step API-Prüfobjekt**

<table><colgroup><col style="width: 50%"/><col style="width: 50%"/></colgroup>
  <thead><tr class="header"><th>Parallel-Monitoring (Preisstufen)</th><th>Standard-Monitoring</th></tr></thead>
  <tbody>
<tr><td>MSA-Prüfobjekt mit 10 Schritten, benutzerdefiniert auf 4 Checkpoints ausgeführt<br />
10 Credits (Anzahl d. Schritte) x 2 (Skalierungsfaktor) = <strong>20 Credits</strong></td>
<td>MSA-Prüfobjekt mit 10 Schritten (Grundpreis 10 Credits)<br />
10 Credits (Anzahl d. Schritte) x 1 = <strong>10 Credits</strong></td></tr>
   <tr><td>MSA-Prüfobjekt mit 10 Schritten, benutzerdefiniert auf 10 Checkpoints ausgeführt<br />
10 Credits (Anzahl d. Schritte) x 4 (Skalierungsfaktor) = <strong>40 Credits</strong></td>
<td>MSA-Prüfobjekt mit 10 Schritten (Grundpreis 10 Credits)<br />
10 Credits (Anzahl d. Schritte) x 1 = <strong>10 Credits</strong></td></tr> 
  </tbody>
</table>

{{< callout >}} **Hinweis**: Im Allgemeinen ist also zu bedenken, dass ein Prüfobjekttyp mit einem höheren Grundpreis (Credits pro Prüfobjekt) zu einem hohen Credit-Verbrauch führt, wenn viele Checkpoints einbezogen werden. {{< /callout >}}
