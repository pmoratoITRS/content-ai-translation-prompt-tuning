{
  "hero": {
    "title": "Prijzen voor Gelijktijdige monitoring"
  },
  "title": "Prijzen voor Gelijktijdige monitoring",
  "summary": "In dit artikel vindt u de formules die worden gebruikt om te berekenen hoeveel credits de gelijktijdige monitoring kost en enkele voorbeelden.",
  "url": "/support/kb/synthetic-monitoring/gelijktijdige-monitoring/prijzen-berekening-voorbeelden",
  "translationKey": "https://www.uptrends.com/support/kb/concurrent-monitoring/pricing-calculation-examples"
}


## Prijzen voor controleregeltypes Full page check en transactie

De prijs wordt berekend volgens het creditssysteem, waarbij verschillende soorten controleregels verschillende basisprijzen hebben, uitgedrukt in credits. Dus in het algemeen is de berekening:

Prijs = de basiscontroleregelprijs x het aantal controlestations dat in de controle is opgenomen

### Voorbeelden

In onderstaande tabel kunt u twee voorbeelden van de prijzen van Gelijktijdige monitoring versus Standaard monitoring vergelijken.

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Gelijktijdige monitoring</th><th>Standaard monitoring</th></tr></thead><tbody><tr class="odd"><td>Transactie (kosten van 4 credits), door de gebruiker gedefinieerd om op 3 controlestations uit te voeren<br />
4 credits x 3 = <strong>12 credits</strong></td><td>Transactie (kosten van 4 credits)<br />
4 credits x 1 = <strong>4 credits</strong></td></tr></tbody></table>

## Prijzen voor basiscontroleregels en Multi-step API (MSA)-controleregels 

Voor deze controleregels geldt een gedifferentieerde prijsstelling met een schaalfactor, daarom wordt de prijs anders berekend dan voor de controleregeltypes Full page checks en transactie. De basiscontroleregels omvatten Ping, Http(s), SSL-certificaat enzovoort. Houd er ook rekening mee dat voor een MSA-controleregel de prijs afhankelijk is van het aantal stappen. Zie onderstaande prijsformules.

**Basiscontroleregel**

Prijs = de basiscontroleregelprijs x de schaalfactor uit onderstaande gedifferentieerde prijstabel

**MSA-controleregel**

Prijs = het aantal stappen in de MSA-controleregel x de schaalfactor uit onderstaande gedifferentieerde prijstabel

### Gedifferentieerde prijstabel {id="tiered-pricing-table"}

<table>
  <colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
  <thead><tr class="header"><th>Aantal controlestations</th><th>Schaalfactor</th></tr></thead>
  <tbody>
    <tr><td>1 tot en met 2</td><td>N.v.t. (zie opmerking onder de tabel)</td></tr>
    <tr><td>3 tot en met 4</td><td>2</td></tr>
    <tr><td>5 tot en met 7</td><td>3</td></tr>
    <tr><td>8 tot en met 10</td><td>4</td></tr>
    <tr><td>11 tot en met 14</td><td>5</td></tr>
    <tr><td>15 tot en met 18</td><td>6</td></tr>
    <tr><td>19 tot en met 22</td><td>7</td></tr>
    <tr><td>23 tot en met 26</td><td>8</td></tr>
    <tr><td>27 tot en met 30</td><td>9</td></tr>
    <tr><td>31 tot en met 35</td><td>10</td></tr>
    <tr><td>36 tot en met 40</td><td>11</td></tr>
    <tr><td>41 tot en met 45</td><td>12</td></tr>
    <tr><td>46 tot en met 50</td><td>13</td></tr>
  </tbody>
</table>

{{< callout >}} **Opmerking**: U moet minimaal drie (hoge beschikbaarheid) of vijf (uit alle) controlestations kiezen om gelijktijdige monitoring te gebruiken. Voor standaard monitoring moet u ook minimaal drie controlestations kiezen, maar er wordt er maar één tegelijk gebruikt (en opgenomen in de prijsberekening). {{< /callout >}}
### Voorbeelden

In de volgende tabellen ziet u voorbeelden van hoe de prijsstelling werkt, vergeleken tussen gelijktijdige en standaard monitoring en ook voor verschillende niveaus in gedifferentieerde prijsstelling.

**Basiscontroleregel**

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
  <thead><tr class="header"><th>Gelijktijdige monitoring (gedifferentieerde prijsstelling)</th><th>Standaard monitoring</th></tr></thead>
  <tbody>
    <tr><td>HTTPS-controleregel (basisprijs van 1), door de gebruiker gedefinieerd om op 4 controlestations uit te voeren<br />
1 credit x 2 (schaalfactor) = <strong>2 credits</strong></td><td>HTTPS-controleregel (basisprijs van 1)<br />
1 credit x 1 = <strong>1 credit</strong></td></tr>
    <tr><td>HTTPS-controleregel (basisprijs van 1), door de gebruiker gedefinieerd om op 10 controlestations uit te voeren<br />
1 credit x 4 (schaalfactor) = <strong>4 credits</strong></td><td>HTTPS-controleregel (basisprijs van 1)<br />
1 credit x 1 = <strong>1 credit</strong></td></tr>
  </tbody>
</table>

**Multi-step API-controleregel**

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup>
  <thead><tr class="header"><th>Gelijktijdige monitoring (gedifferentieerde prijsstelling)</th><th>Standaard monitoring</th></tr></thead>
  <tbody>
<tr><td>MSA-controleregel met 10 stappen, door de gebruiker gedefinieerd om op 4 controlestations uit te voeren<br />
10 credits (aantal stappen) x 2 (schaalfactor) = <strong>20 credits</strong></td>
<td>MSA-controleregel met 10 stappen (basisprijs van 10)<br />
10 credits (aantal stappen) x 1 = <strong>10 credits</strong></td></tr>
   <tr><td>MSA-controleregel met 10 stappen, door de gebruiker gedefinieerd om op 10 controlestations uit te voeren<br />
10 credits (aantal stappen) x 4 (schaalfactor) = <strong>40 credits</strong></td>
<td>MSA-controleregel met 10 stappen (basisprijs van 10)<br />
10 credits (aantal stappen) x 1 = <strong>10 credits</strong></td></tr> 
  </tbody>
</table>

{{< callout >}} **Opmerking**: In het algemeen kunt u ervan uitgaan dat een controleregeltype met een hoge basisprijs (credits per controleregel) zal leiden tot een hoog creditverbruik als u veel controlestations opneemt. {{< /callout >}}
